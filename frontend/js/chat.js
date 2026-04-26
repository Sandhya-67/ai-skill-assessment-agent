// 🔥 GLOBAL VARIABLES
let missingSkillsGlobal = [];
let resumeSkillsGlobal = [];
let skillScores = {};
let currentSkillIndex = 0;

console.log("CHAT JS LOADED");

// 🚀 ANALYZE FUNCTION
async function analyzeResume() {
  if (window.isAnalyzing) return;
window.isAnalyzing = true;
  const chat = document.getElementById("chat");
  const fileInput = document.getElementById("resumeFile");
  const jd = document.getElementById("jd").value;
  const resultBox = document.getElementById("result");
  const btn = document.getElementById("analyzeBtn");

  const file = fileInput.files[0];

  if (!file || !jd) {
    alert("Upload resume and enter JD");
    return;
  }

  try {
    btn.innerText = "Analyzing...";
    btn.disabled = true;

    const formData = new FormData();
    formData.append("file", file);

    const uploadRes = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData
    });

    const uploadData = await uploadRes.json();

    const analyzeRes = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        resume_text: uploadData.resume_text,
        jd_text: jd
      })
    });

    const result = await analyzeRes.json();

    // const resume = result.resume_skills || [];
    // const jdSkills = result.jd_skills || [];
    const resume =
  result.analysis?.resume_skills ||
  result.resume_skills ||
  [];

const jdSkills =
  result.analysis?.jd_skills ||
  result.jd_skills ||
  [];
    // 🔥 NORMALIZE FUNCTION
    const normalize = (str) =>
      str.toLowerCase().replace(/[^a-z0-9]/g, "").trim();

    // 🔥 FIXED MISSING SKILLS
    const missing = jdSkills.filter(jdSkill =>
      !resume.some(r =>
        normalize(r) === normalize(jdSkill)
      )
    );

    // 🔥 STORE GLOBAL
    missingSkillsGlobal = missing;
    resumeSkillsGlobal = resume;

    // 🔥 RESULT UI
    resultBox.innerHTML = `
      <b>Resume Skills:</b><br>${resume.join(", ") || "None"}<br><br>
      <b>JD Skills:</b><br>${jdSkills.join(", ") || "None"}<br><br>
      <b>Missing Skills:</b><br>${missing.join(", ") || "None"}
    `;

    const msg = `
    I have analyzed your resume.

    Missing skills: ${missing.join(", ") || "None"}.

    Do you want:
    1. Mock interview on your skills
    2. Study plan for missing skills
    `;

    chat.innerHTML += `<p><b>AI:</b> ${msg}</p>`;
    speak(msg);

  } catch (err) {
    console.error(err);
  } finally {
    btn.innerText = "Analyze";
    btn.disabled = false;
     window.isAnalyzing = false;   // 🔥 ADD THIS
  btn.innerText = "Analyze";
  btn.disabled = false;
  }
}

// 🚀 FULL INTERVIEW LOOP
function startFullInterview() {
  currentSkillIndex = 0;
  skillScores = {};
  askNextSkill();
}

function askNextSkill() {
  if (currentSkillIndex >= resumeSkillsGlobal.length) {
    generateFinalReport();
    return;
  }

  const skill = resumeSkillsGlobal[currentSkillIndex];

  const chat = document.getElementById("chat");
  chat.innerHTML += `<p><b>AI:</b> Now let's test your skill in ${skill}</p>`;
  speak(`Now let's test your skill in ${skill}`);

  startInterview(skill);
}

// 🚀 START INTERVIEW
async function startInterview(skill) {
  const res = await fetch("http://127.0.0.1:8000/questions", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ skill })
  });

  const data = await res.json();

  const chat = document.getElementById("chat");
  chat.innerHTML += `<p><b>AI:</b> ${data.questions}</p>`;
  speak(data.questions);
}

// 🚀 SEND MESSAGE
async function sendMessage() {
  const input = document.getElementById("input");
  const chat = document.getElementById("chat");

  const msg = input.value.trim();
  if (!msg) return;

  chat.innerHTML += `<p><b>You:</b> ${msg}</p>`;
  input.value = "";

  const lower = msg.toLowerCase();

  // 👉 START INTERVIEW
  if (lower.includes("interview")) {
    speak("Starting your interview");
    startFullInterview();
    return;
  }

  // 👉 STUDY PLAN
  if (lower.includes("study")) {
    const res = await fetch("http://127.0.0.1:8000/study-plan", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        skills: missingSkillsGlobal.join(", ")
      })
    });

    const data = await res.json();

    const plan = data.plan || JSON.stringify(data);

    chat.innerHTML += `<p><b>AI:</b> ${plan}</p>`;
    speak(plan);
    return;
  }

  // 👉 EVALUATE ANSWER
  const skill = resumeSkillsGlobal[currentSkillIndex];

  const res = await fetch("http://127.0.0.1:8000/evaluate", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      skill: skill,
      answer: msg
    })
  });

  const data = await res.json();
  const feedback = data.evaluation || "Could not evaluate.";
  // 🔥 LIMIT TEXT FOR SPEECH
const shortFeedback = feedback.substring(0, 120);

chat.innerHTML += `<p><b>AI:</b> ${feedback}</p>`;

// 🔥 DELAY ADD
setTimeout(() => {
  speak(shortFeedbackfeedback);
}, 300);
  // chat.innerHTML += `<p><b>AI:</b> ${data.evaluation}</p>`;
  // speak(data.evaluation);

  // 🔥 EXTRACT SCORE
  const scoreMatch = data.evaluation.match(/\d+/);
  const score = scoreMatch ? parseInt(scoreMatch[0]) : 5;

  skillScores[skill] = score;

  currentSkillIndex++;
  setTimeout(askNextSkill, 1500);
}

// 🚀 FINAL REPORT
function generateFinalReport() {
  let strong = [];
  let weak = [];

  for (let skill in skillScores) {
    if (skillScores[skill] >= 7) strong.push(skill);
    else weak.push(skill);
  }

  const report = `
  FINAL REPORT:

  Strong Skills: ${strong.join(", ") || "None"}

  Weak Skills: ${weak.join(", ") || "None"}

  Missing Skills: ${missingSkillsGlobal.join(", ") || "None"}

  Recommendation:
  Focus on weak + missing skills.
  `;

  const chat = document.getElementById("chat");
  chat.innerHTML += `<p><b>AI:</b> ${report}</p>`;
  speak(report);
}

// 🚀 BUTTON CONNECT
// 
window.onload = () => {
  const btn = document.getElementById("analyzeBtn");

  if (btn) {
    btn.onclick = analyzeResume; // 🔥 only one binding
  }
};