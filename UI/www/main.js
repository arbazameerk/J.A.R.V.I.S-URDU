// Execute when the document is ready
$(document).ready(function () {
    
    // Set the window size and position on page load
    window.onload = function() {
        window.resizeTo(screen.availWidth, screen.availHeight);
        window.moveTo(0, 0);
    }
    
    // Siri configuration using SiriWave library
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.1",
        autostart: true
    });

    function updateCommandDisplay(command) {
        // Create a new dialog box element
        const dialogBox = document.createElement('div');
        dialogBox.classList.add('dialog-box', 'text-light', 'text-center');
        dialogBox.textContent = `Executed command: ${command}`;
    
        // Append the dialog box to the body
        document.body.appendChild(dialogBox);
    
        // Show the dialog box for 3 seconds (3000 milliseconds)
        setTimeout(() => {
            dialogBox.remove();
        }, 3000);
    }
    
    // Expose the updateCommandDisplay function to Python
    eel.expose(updateCommandDisplay, 'senderText');
    // Enable Bootstrap tooltips for elements with 'data-toggle="tooltip"'
    $('[data-toggle="tooltip"]').tooltip();

    // Mic button click event
    $("#MicBtn").click(function () {
        // Show SiriWave section and hide Oval section
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        // Call Python function using Eel
        eel.takecommand();
    });

    // Cancel button click event
    $("#cancelButton").click(function () {
        // Show Oval section and hide SiriWave section
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
        // Add any additional functionality for cancellation if needed
    });

    // Function to get the current date and time
    function updateDateTime() {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        // Update date and time elements in the HTML
        document.getElementById('currentDate').innerText = now.toLocaleDateString('en-US', options);
        document.getElementById('currentTime').innerText = now.toLocaleTimeString('en-US');
    }

    // Function to get weather information from OpenWeatherMap API
    function getWeather() {
        const apiKey = 'c206f9505888ccfc79890dd81f524f42'; 
        const city = 'Faisalabad';
        const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

        // Make an asynchronous GET request to OpenWeatherMap API
        $.get(apiUrl, function (data) {
            const temperature = data.main.temp;
            const description = data.weather[0].description;
            // Update weather element in the HTML
            document.getElementById('currentWeather').innerText = `Weather: ${description}, Temperature: ${temperature}°C`;
        });
    }

    // Call the functions on page load
    updateDateTime();
    getWeather();

    // Update date and time every second
    setInterval(updateDateTime, 1000);

    // Update weather every 30 minutes
    setInterval(getWeather, 1800000);
});
