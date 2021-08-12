$(document).ready(function(){

    //Generate random hue
    var hue = Math.floor(Math.random() * 360);
    console.log("Hue: " + hue);

    //Remove bright yellows which are hard to read
    if(hue >= 70 && hue < 80){
        hue = 80;
        console.log("Hue changed to 80");
    }
    else if(hue > 50 && hue < 70){
        hue = 50;
        console.log("Hue changed to 50");
    }

    //Change coloured items to the correct hue
    $(".light_hue").css({"background-color": "hsl(" + hue + ", 100%, 77%)"});
    $(".dark_hue").css({"color": "hsl(" + hue + ", 100%, 50%)"});
    $(".dark_hue_bg").css({"background-color": "hsl(" + hue + ", 100%, 50%)"});
    $(".dark_hue_border").css({"border-color": "hsl(" + hue + ", 100%, 50%)"});

    //Change text highlighting colour
    $("<style>")
    .prop("type", "text/css")
    .html("\
    ::selection {\
        background: hsl(" + hue + ", 100%, 50%);\
        color: #f7f7f7;\
    }\
    ::-moz-selection {\
        background: hsl(" + hue + ", 100%, 50%);\
        color: #f7f7f7;\
    }")
    .appendTo("head");

});

