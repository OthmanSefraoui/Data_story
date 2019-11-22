import json
import pandas as pd
from networkx import DiGraph, topological_sort, NetworkXUnfeasible, find_cycle
from dotmap import DotMap
from pathlib import Path

_DEFAULT_PATHS = {
    "def_flags": "definitions_and_standards/flags.csv",
    "emission_intensity": "global-food-agriculture-statistics/raw_files/Environment_Emissions_intensities_E_All_Data_(Normalized).csv"
}

def load_def_flags(filepath, dfs):
    flags = pd.read_csv(
        filepath,
        keep_default_na=False,
        index_col="Flag"
    )
    return flags


def load_em_intensity(filepath, dfs):
    df = (
        pd.read_csv(filepath, encoding="latin1")
        .drop("Year Code", axis='columns')
    )
    #reload flags without NA to avoid conflict between "NA" and "" flag
    df["Flag"] = pd.read_csv(filepath, encoding="latin1", usecols=["Flag"], keep_default_na=False)
    df = df.merge(dfs.def_flags, on="Flag").drop(columns="Flag").rename(columns={"Flags": "Flag"})

    split_dfs = DotMap(_dynamic=False)
    for element in df["Element"].unique():
        split_dfs[element]



_DFS = {
    "def_flags": {"func": load_def_flags},
    "emission_intensity": {
        "func": load_em_intensity,
        "deps": ["def_flags"]
    }

}

def load_dfs(*df_names, data_dir="./data"):
    data_dir = Path(data_dir)

    # find missing df_name
    missing = set(df_names) - _DFS.keys()
    if missing:
        raise ValueError(f"Unknown table names {', '.join(missing)}")

    # solve dependencies
    deps = DiGraph()
    for df_name in df_names:
        deps.add_node(df_name)
        for dep in _DFS[df_name].get("deps", []):
            deps.add_edge(dep, df_name)
    try:
        load_order = list(topological_sort(deps))
    except NetworkXUnfeasible:
        raise ValueError(f"cylic dependencies in table loading: {' -> '.join(find_cycle(deps, orientation='reverse'))}")   

    # load paths
    path_file = data_dir / "df_paths.json"
    df_paths = _DEFAULT_PATHS.copy()
    if not path_file.exists():
        with path_file.open('w') as f:
            json.dump(_DEFAULT_PATHS, f, indent=4, sort_keys=True)
    else:
        with path_file.open() as f:
            df_paths.update(json.load(f))
    #find datFrames with missing paths
    missing = set(load_order) - df_paths.keys()
    if missing:
        raise ValueError(f"No path for tables {', '.join(missing)}")
    
    #load dfs
    dfs = DotMap(_dynamic=False)
    for df_name in load_order:
        func = _DFS[df_name].get('func')
        if func is None:
            raise ValueError(f'No loading function for table {df_name}')
        dfs[df_name] = func(data_dir / df_paths[df_name], dfs)
    
    return dfs
