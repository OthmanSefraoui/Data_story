---
layout: default
width: 1030
width_half: 512
height_half: 384
---
# TESTS BELOW - DO NOT KEEP

# CONFIG FOR TECH
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
  </style>
</head>

{% include globem_display.html %}

# Underscript
CO<sub>2</sub>

# Include Image

<img src=""></img>

# Include an IFRAME
<div>
  <iframe
    src="img/TimeSliderChoropleth.html"
    height="700"
    width="{{page.width}}"
    frameborder="0"
    scrolling="no"
  ></iframe>
</div>


# CREATE A DROP-DOWN MENU

<div class="dropdown-wrapper">
    <select class="dropdown-wrapper-child" id="TestDropdown">
        <option value="img/TimeSliderChoropleth.html">France</option>
        <option value="">Swiss</option>
    </select>
    <iframe id="diplay_drop" src="img/TimeSliderChoropleth.html" height="700" width="{{page.width}}" frameborder="0" scrolling="no"></iframe>
</div>
<script>
    function loadProjectImage() {
        var img = document.getElementById("diplay_drop");
        img.src = this.value;
        return false;
    }
document.getElementById("TestDropdown").onchange = loadProjectImage;
</script>

# SIDE BY SIDE ELEM

<div class="box2">
    <iframe src="img/TimeSliderChoropleth.html"
    frameborder="0" scrolling="no"
    width="{{page.width_half}}" height="{{page.height_half}}"
    align="left">
    </iframe>
</div>
<div class="box2">
    <iframe src="img/TimeSliderChoropleth.html"
    frameborder="0" scrolling="no"
    width="{{page.width_half}}"
    height="{{page.height_half}}" 
    align="left">
    </iframe>
</div>