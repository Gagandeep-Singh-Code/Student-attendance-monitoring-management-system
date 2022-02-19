function myFunction() {
    var x = document.getElementById("mytopnave");
    if (x.className === "topnav") {
        x.className += " responsive";
    }
    else{
        x.className = "topnav";
    }
}