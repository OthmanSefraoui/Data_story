---
layout: default
width: 1036
width_half: 516
height_half: 384
---
<head>
  <style>
  .dropdown-wrapper > div {
    border: 1px solid;
  }
  .dropdown-wrapper-child {
    margin: auto;
    display: flex;
  }
  .dropdown-wrapper-child div {
    flex-grow: 1;
    width: 0;
  }
  .dropdown-wrapper {
    display: inline-block;
  }
  .box2 {
    display:inline-block;
  }
  .text-justify {
    text-align: justify;
  }
  </style>
</head>


Environmental issues are a hot topic today, as we are facing new challenges such as global warming and natural catastrophes. Concerns about our footprint on earth and especially about our evergrowing population, and the need to feed ourselves, raises questions about the sustainability of our agricultural and breeding methods. Animal product and especially meat are under specific scrutiny: while some have forgone them altogether, others advocate for more sustainable consumption habits.
{: .text-justify}

Can data analysis provide us useful insights on that controversial topic ?

# Getting the data
The first challenge is to find the data. The [FAO](http://www.fao.org/faostat/en/#home) provides extensive agricultural data on production, trade etc. for most countries in the world, dating back to 1961, that we will use in our study. Since we only use that database, our conclusion are limited by the particular data we use.
{: .text-justify}

We would like to focus on animal products. For simplicity, we will only look at *cattle*, *chickens* and *swine*: those are the three main group of animals. Goods produced by those animals, namely *milk* and *eggs*, will also retain our attention, so we need to do an important distinction: cattle and chicken can be breed for meat or for production. This gives five categories total.
{: .text-justify}


# Overview of the world
## Global trends in production
The first insight we can get from the data is an overview of the situation. Let us be basic first, and simply look at how the production of the goods evolved over the years. To better compare our data, we will use the first year, 1961, as a baseline, arbitrarily set to 1, and look at the ratios. The initial productions were in tonnes.
{: .text-justify}

{% include display_world_prod.html %}

We can see that the global trend is on the increase, with a 2x factor for beef and milk, and up to a 14x factor for chicken meat production ! However, this visualization is a bit spurious: the world population has changed since 1961, and the food production is expected to increase in response. Let us normalize by the world population:
{: .text-justify}

{% include display_world_prod_norm.html %}

The plot above better reflect the production trends. And it comes with an unexpected result: overall, the production of beef and milk per person hasn't changed since 1961 ! This is very unexepected, considering the development of lifestyles since 1961. However, porc and milk normalised production have increased 2.5-fold, and chicken meat production has the bigger increase, six-fold.
{: .text-justify}

From that, we can say that the increased meat consumption per person since 1961, globally, relies on porc meat and heavily on chicken, while beef consumptions have been steady. As we are for now working on aggregated data for the world, this obsiously hides the differences between countries, but the conclusion is nethertheless a surprising one in the context.
{: .text-justify}

It is also interesting to note that there seems to be three groups of related goods: beef and milk, eggs and porc, and chicken.
{: .text-justify}

## Detailed production
Since the above study was global, we missed the differences between countries. We expect some very general groups to emerge, such as developped, developping and third-world countries. However, we face the same problem above as with the raw world production: countries have different sizes, and to better compare them we have to take that into account. We need to look at the production per inhabitant to compare, say, the US and Switzerland. We therefore normalise by the number of inhabitants, and the unit becomes *tonnes per inhabitant*.
{: .text-justify}

As even normalization by countries doesn't smooth the difference enough, two scales are available: linear scale and log scale.
{: .text-justify}

> Use the slide above the map to advance through time and watch the countries' normalized production change ! You can also zoom in and out, and move around in the map. Countries in white are countries for which there is missing data.
{: .text-justify}

{% include display_map_prod.html %}

Using the above visualization, you can identify the big producers (compared to their population) for each good. Try "Porc": you will see that an unusual country has a very high ratio. But it is not due to a high production !

After this overview of the production trends to get accustomed to the kind of data and problems we face (normalisation will comme back at us often), we would like to focus on the "environmental impact" of animal breeding. But the term is extremely vague: how do we mesure it ?
{: .text-justify}

# Looking at the environment
The notion of "environmental footprint" is too vague and ill-defined to use it with data. We need something we can mesure, analyse and visualize. We will therefore use *greenhouse gas emissions*, and express them in CO<sub>2</sub> equivalent quantities: that is the amount of CO<sub>2</sub> needed to have the same greenhouse effect as the original emission. As we are not interested in the specific gas being studied, every number will just be expressed in equivalent CO<sub>2</sub>.
{: .text-justify}

One can be a bit disapointed that we use such a metric for the study. It is however extremely difficult to find number that do represent "environmental footprint" in some sense, can be measure and for which we actually have data. As a matter of fact, the dataset from FAO we are used only reports things related to environmental impact as equivalent CO<sub>2</sub>, because it's the only accessible metrics that can compare widely differing causes. Since this is the dataset we use, there isn't much of a choice there.
{: .text-justify}

We must precisely describe the emissions we take into account. We sum the emission from four sources:
+ emissions from manure that as been left as is in the field
+ emissions from manure that have been handled: reused as fertilizer or over
+ enteric fermentation, that cow ruminating and digesting (cattle only)
+ emissions from the production of food
{: .text-justify}

For the last point, we estimated the food needs of animals in eahc categories, considered they were eating a mixture of cereals and used the FAO data for the equivalent CO<sub>2</sub> emission per food mass. This is less than ideal, but we miss precise data there, so we estimated as we could.
{: .text-justify}

Overall, the only emissions we take into account are *direct*: emissions coming from electricity use, for instance, are ignored (becaus not in the dataset). The emissions we compute are therefore an *underestimate* of the total emissions.
{: .text-justify}

## Global emissions
First, let us look at the global emisions for our five goods. As usual, we need to adjust for a growing population, so we plot the "raw" data as well as the "per capita" data, normalized by the (human) population. Mind the axis: there is no baseline so that you are able to compare the emissions between products, and the vertical axis *doesn't start at 0*. We vizualize variations, but be careful about the starting point.
{: .text-justify}

{% include display_globem.html %}

If you look at the raw emission for cattle, between 1986 and about 2000, there is a huge drop in emissions. This is expected, because it corresponds to the mad cow disease epidemic. Other emissions have seen a somewhat steady rise.
{: .text-justify}

Per capita emission are very revealing: we can see that dairy cattle, meat cattle and swine emission per animal decreases over time! (dairy cattle: x0.5, meat cattle x0.64, swine x0.75): This reveals either a decreased global consumption per capita, or improving techniques.
{: .text-justify}

Chickens, however, are another story. While the emissions per animal haven't changed much for laying chickens between 1961 and 2014, it should be noted that they first decreased by 25% (mind the y-axis) before going back to the original value - whatever progress was made in that area was lost. Chicken bred for meat have seen a 2-fold increase in the emission per capita, which is hardly beneficial.
An explanation for that is the growing production of chickens (see production above) in crowded spaces and in high volume: it correlates with the increased production per capita. It is also possibale that manure is left to rot. This is the only expandable emission source in the emissions we consider (chicken eat the same to reach maturity).
{: .text-justify}

## Detailed emissions
As usual when using global data, we miss differences between countries. Let us look at a map of the emissions (in gigagrams), with time evolution.
{: .text-justify}

As the map show different trends, you can chose the scale at which to look at: log scale or classic linear scale. Linear scale will highligh dominating producers, will log will show the difference in magnitudes.
{: .text-justify}

{% include display_map_emission.html %}

The evolution there is particularly interesting: will the USA, Russi and China used to be the main sources of emissions back in 1961, new countries have come around. We can clearly identify Brazil as the world's biggest producer of beef throught its emission, and China as the world's first producer of porc, by several magnitudes ! India also stands out as nowadays biggest cattle breeder for milk according to their emissions. But it might be that they are really inefficient.
{: .text-justify}



# Consumption
While visualizing the emission due to animal breeding in their origin countries, we ignore the fact that the world is globalized and that there are trades everywhere. Is that important in our case ? Let us take a look: we plot the ratio between the volume of traded goods and the production of that good.
{: .text-justify}

{% include display_trade_frac.html %}

We see that up to 15% of the world's production of goods are exchanged ! This is a lot, so we better take trades into account in our analysis. There is one big caveat, though: given our data, if a good transit throught a country (that is, country A buys it from country B which bought it from country C), it is counted twice, since we cannot distinguish between the origins of exports. It is likely we overestimate the fraction of trades - however, we do not expect the goods to transit through many countries, so the ratio is at most something like 5, being pessimistic.
{: .text-justify}

However, adjusting our emissions visualization for trades allows to distinguish between producers countries and consumers countries, which is interessting - it is worth a shot
{: .text-justify}
<!--
Now, how do we adjust for trade ? We can't determine if exported goods have already been imported or comes from local production, 
-->

## Trade adjusted
Let us vizualize the emissions, but this time imputed to the consuming country:

{% include display_map_conso.html %}

Let us focus on a particular example: Meat cattle, brazil and the USA. From the previous emission visualization, we saw that brazil was a heavy emitter. However, when we account for trade, it significantly drops, while USA gets more emissive ! So some countries do import a lot, so that their emissions appears abroad if we do not adjust for trade.
{: .text-justify}

# World emission trends


{% include display_world_em.html %}

{% include display_world_em_norm.html %}