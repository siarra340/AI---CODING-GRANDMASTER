var seconds = 0;
setInterval(function () {
    seconds = seconds + 1;
    document.getElementById("timer").textContent = "You have been here for " + seconds + " seconds!"
}, 1000);

function checkForm() {
    var name = document.getElementById("name").value;
    var guess = document.getElementById("guess").value;
    var ok = true;

    if (name == "") {
        document.getElementById("msg-name").textContent = "Please enter your name!";
        document.getElementById("msg-name").style.color = "red";
        ok = false;

    } else {
        document.getElementById("msg-name").textContent = "Great name!";
        document.getElementById("msg-name").style.color = "Green";
    }

    if (guess == "") {
        document.getElementById("msg-guess").textContent = "Please enter a guess!";

        document.getElementById("msg-guess").style.color = "Red";
        ok = false;
    } else {
        document.getElementById("msg-guess").textContent = "Guess saved!";
        document.getElementById("msg-guess").style.color = "Green";
    }

    if (ok == true) {
        var lucky = Math.floor(Math.random() * 5) + 1;
        if (guess == lucky) {
            document.getElementById("result").textContent = "You win, " + "name" + "! The lucky number was " + lucky + "!";
            document.getElementById("result").style.color = "Green";
        } else {
            document.getElementById("result").textContent = "So close, " + name + "! The lucky number was " + lucky + ". Try again!";
            document.getElementById("result").style.color = "navy";
        }
    }

}