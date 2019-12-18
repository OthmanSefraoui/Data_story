# TESTS BELOW - DO NOT KEEP

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