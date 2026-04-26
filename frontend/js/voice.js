let recognition;
let isSpeaking = false;
let currentSpeech = null;

// 🎤 START MIC
function startMic() {
  const status = document.getElementById("status");

  if (!('webkitSpeechRecognition' in window)) {
    alert("Speech Recognition not supported");
    return;
  }

  // 🔥 अगर AI बोल रहा है → पहले रोक दो
  stopSpeaking();

  recognition = new webkitSpeechRecognition();
  recognition.lang = "en-US";

  if (status) status.innerText = "Listening...";

  recognition.onresult = function(e) {
    const text = e.results[0][0].transcript;
    document.getElementById("input").value = text;

    setTimeout(() => sendMessage(), 500);
  };

  recognition.onerror = function(e) {
    console.error("Mic error:", e);
    if (status) status.innerText = "Idle";
  };

  recognition.onend = function() {
    if (status) status.innerText = "Idle";
  };

  recognition.start();
}

// 🔊 SPEAK FUNCTION (UPGRADED)
function speak(text) {
  const circle = document.getElementById("ai-circle");
  const status = document.getElementById("status");

  if (!window.speechSynthesis) {
    console.log("Speech not supported");
    return;
  }

  // 🔥 अगर पहले से बोल रहा है → रोक दो
  stopSpeaking();

  // 🔥 CLEAN TEXT
  const cleanText = text
    .replace(/[\u{1F600}-\u{1F6FF}]/gu, "")
    .replace(/[^\w\s,.]/g, "");

  const speech = new SpeechSynthesisUtterance(cleanText);

  currentSpeech = speech;
  isSpeaking = true;

  // 🔥 Voice tuning
  speech.rate = 0.9;
  speech.pitch = 1;

  // 🔥 UI update
  if (status) status.innerText = "Speaking...";
  if (circle) circle.classList.add("speaking");

  speech.onstart = () => {
    console.log("Voice started");
  };

  speech.onend = () => {
    isSpeaking = false;
    currentSpeech = null;

    if (status) status.innerText = "Idle";
    if (circle) circle.classList.remove("speaking");

    console.log("Voice ended");
  };

  speech.onerror = (e) => {
    console.error("Speech error:", e);

    isSpeaking = false;
    currentSpeech = null;

    if (status) status.innerText = "Idle";
    if (circle) circle.classList.remove("speaking");
  };

  speechSynthesis.speak(speech);
}

// 🛑 STOP / OVERRIDE FUNCTION (🔥 NEW)
function stopSpeaking() {
  if (isSpeaking) {
    speechSynthesis.cancel();

    isSpeaking = false;
    currentSpeech = null;

    const status = document.getElementById("status");
    const circle = document.getElementById("ai-circle");

    if (status) status.innerText = "Stopped";
    if (circle) circle.classList.remove("speaking");

    console.log("Voice stopped manually");
  }
}

// 🔥 Chrome voice unlock fix
document.addEventListener("click", () => {
  if (speechSynthesis) {
    speechSynthesis.resume();
  }
});