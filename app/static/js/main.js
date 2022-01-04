const dateElement = document.getElementById("date");
const greeting = document.getElementById("greeting");
const userName = document.getElementById("name");

setInterval(() => {
    const date = new Date();

    const hours = date.getHours();
    const mins = date.getMinutes();
    dateElement.innerHTML = `${hours < 10 ? "0" + hours : hours}:${mins < 10 ? "0"+mins : mins}`;
    if (12 > hours && hours >= 5) {
        greeting.innerHTML = "Good morning, "+userName.innerHTML+"!";
    } else if (17 > hours && hours >= 12) {
        greeting.innerHTML = "Good afternoon, "+userName.innerHTML+"!";
    } else if (21 > hours && hours >= 17) {
        greeting.innerHTML = "Good evening, "+userName.innerHTML+"!";
    } else {
        greeting.innerHTML = "Good night, " + userName.innerHTML + "!";
    }
}, 1000);