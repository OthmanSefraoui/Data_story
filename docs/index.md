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
Since the above study was global, we missed the differences between countries. We expect some very general groups to emerge, such as developped, developping and third-world countries.
{: .text-justify}

{% include display_map_prod.html %}

> Analysis: TODO

However, we face the same problem above as with the raw world production: countries have different sizes, and to be able to better compare them we have to take that into account. We need to look at the production per inhabitant to be able to compare, say, the US and Switzerland:
{: .text-justify}

{% include display_map_prod_norm.html %}

> Analysis: TODO

After this overview of the production trends to get accustomed to the kind of data and problems we face (normalisation will comme back at us often), we would like to focus on the "environmental impact" of animal breeding. But the term is extremely vague: how do we mesure it ?
{: .text-justify}

# Looking at the environment

The notion of "environmental footprint" is too vague and ill-defined to use it with data. We need something we can mesure, analyse and visualize. We will therefore use *greenhouse gas emissions*, and express them in CO<sub>2</sub> equivalent quantities: that is the amount of CO<sub>2</sub> needed to have the same greenhouse effect as the original emission. As we are not interested in the specific gas being studied, every number will just be expressed in equivalent CO<sub>2</sub>.
{: .text-justify}

One can be a bit disapointed that we use that metric for the study. It is however extremely difficult to find number that do represent "environmental footprint" in some sense, can be measure and for which we actually have data. As a matter of fact, the dataset from FAO we are used only reports things related to environmental impact as equivalent CO<sub>2</sub>, because it's the only accessible metrics that can compare widely differing causes. Since this is the dataset we use, there isn't much of a choice there.
{: .text-justify}


{% include display_globem.html %}

{% include display_map_emission.html %}

# Consumption

{% include display_trade_frac.html %}

{% include display_map_conso.html %}


# World emission trends

{% include display_world_em.html %}

{% include display_world_em_norm.html %}