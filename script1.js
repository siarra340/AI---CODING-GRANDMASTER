function showLoadingMessage(message) {
    document.getElementById("status").innerHTML = message;
}

function fetchSchoolEventData(callback) {
    callback("Loading school event data... Please wait")

    return new Promise(function (resolve) {

        setTimeout(function () {

            let schoolEvent = {
                eventName: "Annual Science Fair",
                date: "August 25, 2026",
                time: "10:00AM - 5:30PM",
                venue: "School Gymnasium",
                coordinator: "Mr. Enver",
                participants: 120,
                isRegistrationOpen: false
            };

            resolve(schoolEvent);
        }, 2000);

    })
}

async function showSchoolEvent() {
    let eventData = await fetchSchoolEventData(showLoadingMessage);

    document.getElementById("status").innerHTML = "Event data successfully loaded! 📋";

    let jsonText = JSON.stringify(eventData);

    let parsedEvent = JSON.parse(jsonText);

    let eventMessage = "";

    eventMessage = eventMessage + "Event Name: " + parsedEvent.eventName + "<br>";
    eventMessage = eventMessage + "Date: " + parsedEvent.date + "<br>";
    eventMessage = eventMessage + "Time: " + parsedEvent.time + "<br>";
    eventMessage = eventMessage + "Venue: " + parsedEvent.venue + "<br>";
    eventMessage = eventMessage + "Coordinator: " + parsedEvent.coordinator + "<br>";
    eventMessage = eventMessage + "Participants: " + parsedEvent.participants + "<br>";

    if (parsedEvent.isRegistrationOpen === true) {
        eventMessage = eventMessage + "Registration Status: Open";
    } else {
        eventMessage = eventMessage + "Registration Status: Closed";

    }

    document.getElementById("eventDetails").innerHTML = eventMessage;
    document.getElementById("jsonOutput").innerHTML = jsonText;

}

