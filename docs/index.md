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

Can data analysis provide us useful insight in that controversial topic ?

# About
The first challenge is to find the data. The [FAO](http://www.fao.org/faostat/en/#home) provides extensive agricultural data on production, trade etc. for most countries in the world, dating back to 1961, that we will use in our study. Since we only use that database, our conclusion are limited by the particular data we use.
{: .text-justify}

The second difficulty is to find a metric to quantify the notion of "environmental footprint", that is very vague and ill-defined. We will focus on *greenhouse gas emissions*, and for comparison purposes always express them in CO<sub>2</sub> equivalence. 





  {% include globem_display.html %}