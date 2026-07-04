var tasks = ["Homework", "Breakfast", "Exersise", "Reading", "Packing Bag"];

var minutes = [30, 15, 20, 25, 10];

document.getElementById("taskResult").innerHTML = "Tasks: " + tasks;

document.getElementById("timeResult").innerHTML = "Minutes needed: " + minutes;

document.getElementById("labelResult").innerHTML = "Press the Button above!";

function sortAZ() {
    var sortTasks = tasks.sort();
    document.getElementById("taskResult").innerHTML = "A to Z: " + sortTasks;
}

function sortZA() {

    var reversedTasks = [...tasks].sort().reverse();

    document.getElementById("taskResult").innerHTML = "Z to A: " + reversedTasks;
}

function sortShortest() {
    minutes.sort(function (a, b) { return a - b; });

    document.getElementById("timeResult").innerHTML = "Shortest tasks first: " + minutes;
}

function sortLongest() {
    minutes.sort(function (a, b) { return b - a; })

    document.getElementById("timeResult").innerHTML = "Longest tasks first: " + minutes;
}

function addLabel() {
    var labelledMinutues = minutes.map(function (time) { return time + " mintues"; });

    document.getElementById("labelResult").innerHTML = "Labelled times: " + labelledMinutues
}

