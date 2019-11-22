# -*- coding: utf-8 -*-
def select_on(df, columns, dict_elements):
    ''' Filter columns of df by elements in the dict dict_elements where the keys are the columns'''
    for column in columns:
        elements = dict_elements[column]
        df = df[df[column].isin(elements)]
    return df

