

function myFunction() {
    var greeting;
    var time = new Date().getHours();

    if (time < 10) {
        greeting = "Good Morning";
    }

    else if (time < 20) {
        greeting = "Good Day";
    }

    else {
        greeting = "Good Evening";
    }

    document.getElementById("hour").innerHTML = "The current hour is: " + time
    document.getElementById("greeting").innerHTML
        = greeting;
}