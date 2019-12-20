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

The second difficulty is to find a metric to quantify the notion of "environmental footprint", that is a very vague and ill-defined notion, unsutable for analysis. We will focus on *greenhouse gas emissions*, and for comparison purposes always express them in CO<sub>2</sub> equivalence.

We would like to focus on animal products. For simplicity, we will only look at *cattle*, *chickens* and *swine*: those are the three main group of animals. Goods produced by those animals, namely *milk* and *eggs*, will also retain our attention, so we need to do an important distinction: cattle and chicken can be breed for meat or for production. This gives five categories total.

# World trend

{% include display_world_prod.html %}

# Production

{% include display_map_prod.html %}

# Emissions

{% include display_globem.html %}

{% include display_map_emission.html %}

# Consumption

{% include display_trade_frac.html %}

{% include display_map_conso.html %}


# World emission trends

{% include display_world_em.html %}

{% include display_world_em_norm.html %}