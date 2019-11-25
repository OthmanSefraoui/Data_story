Environmental impact of Agriculture
===================================

## Abstract

Enviromental concerns have drastically increased in the past years and agriculture's role in polluting the soils, air and water is a topic of choice. The *Global Food & Agriculture Statistics* provides global data on several aggricultural indicators, from production of certains goods to global trade data. Leveraging this dataset, we would like to find out if countries around the world have grasped the full extent of situation: are behaviors changing for the better ? On the other hand, we want to find countries that have a worse impact.

As the question is very broad in its previous form, we need to narrow the focus of our study as well as to define quantitative indicators of environmental 'impact'. The most obvious indicator are Greenhouse-gas emissions, mesured as an equivalence in CO2 emissions. As this indicator is available to us given our data, it constitutes our choice of 'enviromental impact' indicator.

Meat has been a focus of recent debates on environmental impact and climate change and has raised numerous concerns about its resources use. We would therefore like to focus on the impact of meat production. This choice is also motivated by the data available, as there are some missing corners concerning crops in the database (see notes).

While the dataset does provide a rough estimates of the CO2 equivalent emissions for meat production, we would like to refine this estimates through two ways. First by including the food eaten by the animals, which we expect to account for a non-negligible part of their footprint. Then, we would like to include trading data to take into account the globalised nature of nowadays' world. The producer and the consumer rarely are the same, so imputing the emissions to  the actual consumming country might be a fairer comparison between them, as well as yield insight in terms of consumption behavior accross the world.

Data visualization would greatly benefit from dynamic maps, where impact per year, category and/or countries can be tuned and selected.

## Research questions

+ What is the environmental impact of agriculture in each country in the past year, in terms of equivalent CO2 emissions 
+ How did agricultural habits change over the year: are heavily emitting practices in decline ?
+ Are some countries less emissive than others ? Can we find a reason for that in the data
+ When imputing the emissions to the actual consumer using trade data, what changes in terms of equivalent CO2 emissions per country ?

## Dataset and resources

+ [Global Food & Agriculture Statistics](https://www.kaggle.com/unitednations/global-food-agriculture-statistics)
+ [Detailed trade matrix](http://www.fao.org/faostat/en/#data/TM)
+ [Manure production and caracteristics](http://www.agronext.iastate.edu/immag/pubs/manure-prod-char-d384-2.pdf) for estimating food consumption of animals

## Notes

Concerning crops, there is a missing piece of info in the dataset. The crops production are given, and the emissions from fertilizer use are also given. However, we miss the amount of fertilizer used by crops type and fertilizer type, by year and by country. This prevents use from estimating emissions from crops due to fertilizer uses.

The dataset does contains estimates for the emissions per kg of product for agricultural goods, but provide those estimated aggregated over all types of crops but rice. The coefficients used for the amount of fertilizer used per crop are not given, and the documentation reports using data that was not made available.

We looked at [Fertilizer Use and Price](https://www.ers.usda.gov/data-products/fertilizer-use-and-price.aspx) from the United State Department of Agriculture, to try to estimate those coefficient. However, even within the different states of the USA, fertilizer use habits varies quite alot between states, as can be seen in the final plot of `notes.ipynd`.
If variability is so high even in a single country, we do not believe that calculating fertilizer use by crops type by fertilizer type from USA's data and then apply those coefficients to the rest of the world will yield meaningful results. Differences in wealth, habits etc. induce too high a variation.