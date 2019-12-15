---
layout: default
title: test Title
---
# Welcome to the test site !
The above title is H1

## This is an H2 !
### And an H3

Can we add lists ?
+ test item
+ test item

# LIQUID TEST
{{ page.title }}


# Map test

{% capture includeTime %}
{% include time.html %}
{% endcapture %}
{{ includeTime | replace: '  ', ''}}

Second test

<br/>

<div>
  <iframe src="img/TimeSliderChoropleth.html" height="700" width="1000" frameborder="0" scrolling="no"></iframe>
</div>