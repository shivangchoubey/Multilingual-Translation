async function translateText() {
    let text = document.getElementById("inputText").value.trim();
    let lang = document.getElementById("language").value;
    let outputText = document.getElementById("outputText");

    if (text === "") {
        alert("Please enter some text to translate.");
        return;
    }

    outputText.innerText = "Translating...";

    try {
        let response = await fetch("/translate", {  // Use relative path (not full URL)
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text, lang: lang })
        });

        let result = await response.json();

        if (result.translated_text) {
            outputText.innerText = result.translated_text;
        } else {
            outputText.innerText = "Translation failed!";
        }

    } catch (error) {
        outputText.innerText = "Error: Unable to translate.";
        console.error("Translation Error:", error);
    }
}

async function speakText() {
    let text = document.getElementById("outputText").innerText;
    
    if (!text) {
        alert("No text to speak!");
        return;
    }

    try {
        let response = await fetch("http://127.0.0.1:5000/speak", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text })
        });

        let result = await response.json();
        console.log(result);
    } catch (error) {
        console.error("Speech Error:", error);
    }
}
