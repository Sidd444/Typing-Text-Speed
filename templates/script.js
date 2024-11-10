let startTime, endTime;
let sentence;

async function startTest() {
    const sentenceElement = document.getElementById("sentence");
    const typingInput = document.getElementById("typingInput");
    const resultElement = document.getElementById("result");

    try {
        // Fetching a random sentence from the backend
        //const response = await fetch("http://127.0.0.1:5000/get-sentence");
        const response = await fetch("https://typing-text-speed.onrender.com/get-sentence");
        const data = await response.json();
        sentence = data.sentence;

        // Displaying the sentence and reset input
        sentenceElement.textContent = "''"+sentence+"''";
        typingInput.value = "";
        typingInput.disabled = false;
        typingInput.focus();

        // Starting the timer
        startTime = new Date().getTime();
        resultElement.textContent = "";
    } catch (error) {
        console.error("Error fetching the sentence:", error);
        resultElement.textContent = "Error fetching the sentence. Please try again.";
    }
}

document.getElementById("typingInput").addEventListener("input", () => {
    const typingInput = document.getElementById("typingInput");
    const resultElement = document.getElementById("result");

    if (typingInput.value === sentence) {
        // Stopping the timer when the sentence is typed correctly
        endTime = new Date().getTime();

        // Calculating typing speed in words per minute
        const timeTaken = (endTime - startTime) / 1000; // in seconds
        const wordsTyped = sentence.split(" ").length;
        const speed = (wordsTyped / timeTaken) * 60; // words per minute

        resultElement.textContent = `Typing Speed: ${speed.toFixed(2)} WPM`;
        typingInput.disabled = true;
    }
});
