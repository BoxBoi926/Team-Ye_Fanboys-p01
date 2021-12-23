const dateElement = document.getElementById("date");

setInterval(() => {
    const date = new Date();

    const hours = date.getHours();
    const mins = date.getMinutes();
    dateElement.innerHTML = `${hours < 10 ? "0" + hours : hours}:${mins}`;
}, 1000);