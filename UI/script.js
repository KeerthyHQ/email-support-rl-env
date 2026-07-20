const BASE_URL = "";

// ----------------------------
// Reset Environment
// ----------------------------

async function resetEnvironment() {

    try {

        const response = await fetch(BASE_URL + "/reset", {
            method: "POST"
        });

        const data = await response.json();
        const obs = data.observation;

        document.getElementById("status").innerText =
            "🟢 Environment Running";
        document.getElementById("status").className =
            "status running";

        document.getElementById("email").innerText =
            obs.email;

        document.getElementById("reward").innerText =
            Number(data.reward).toFixed(2);

        document.getElementById("reward-progress").style.width =
            Math.max(0, Math.min(100, data.reward * 100)) + "%";

        document.getElementById("category").innerText =
            obs.category;

        document.getElementById("priority").innerText =
            obs.priority;

        document.getElementById("sentiment").innerText =
            obs.sentiment;

        document.getElementById("task").innerText =
            formatLabel(obs.task);

        document.getElementById("task_score").innerText =
            Number(obs.task_score).toFixed(2);

        document.getElementById("matches").innerText =
            obs.keyword_matches;

        document.getElementById("step_count").innerText =
            obs.step_count;

        document.getElementById("difficulty").innerText =
            obs.difficulty;

        document.getElementById("history").innerHTML = `
            <div class="message customer">
                <div class="bubble">
                    <span class="sender">📩 Customer</span>
                    ${obs.email}
                </div>
            </div>
        `;

       

        document.getElementById("reply").value = "";
        document.getElementById("reply").disabled = false;
        document.getElementById("send-btn").disabled = false;

        document
            .getElementById("evaluation-section")
            .classList.add("hidden");

    } catch (error) {

        document.getElementById("status").innerText =
            "🔴 Environment Offline";

        document.getElementById("status").className =
            "status offline";

        console.error(error);
    }
}

// ----------------------------
// Send Reply
// ----------------------------

async function sendReply() {

    const replyBox = document.getElementById("reply");
    const reply = replyBox.value.trim();

    if (!reply)
        return;

    replyBox.value = "";

    const history = document.getElementById("history");
    history.innerHTML += `
        <div class="message agent">
            <div class="bubble">
                <span class="sender">🤖 Agent</span>
                ${reply}
            </div>
        </div>
    `;
   
    try {

        const response = await fetch(BASE_URL + "/step", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                action: {
                    reply: reply
                }
            })

        });

        const data = await response.json();
        const obs = data.observation;

        document.getElementById("reward").innerText =
            Number(data.reward).toFixed(2);

        document.getElementById("reward-progress").style.width =
            Math.max(0, Math.min(100, data.reward * 100)) + "%";

        document.getElementById("email").innerText =
            obs.email;

        document.getElementById("category").innerText =
            obs.category;

        document.getElementById("priority").innerText =
            obs.priority;

        document.getElementById("sentiment").innerText =
            obs.sentiment;

        document.getElementById("task").innerText =
            formatLabel(obs.task);

        document.getElementById("task_score").innerText =
            Number(obs.task_score).toFixed(2);

        document.getElementById("matches").innerText =
            obs.keyword_matches;

        document.getElementById("step_count").innerText =
            obs.step_count;

        document.getElementById("difficulty").innerText =
            obs.difficulty;

        if (!data.done) {
            history.innerHTML += `
                <div class="message customer">
                    <div class="bubble">
                        <span class="sender">📩 Customer</span>
                        ${obs.email}
                    </div>
                </div>
            `;
           

        } else {

            history.innerHTML += `
                <div class="message system">

                    <div class="system-message">
                        ✅ Conversation Completed
                    </div>

                </div>
            `;

            replyBox.disabled = true;
            document.getElementById("send-btn").disabled = true;

            if (data.evaluation) {
                showEvaluation(data.evaluation);
            }

        }

        history.scrollTop = history.scrollHeight;

    } catch (error) {

        document.getElementById("status").innerText =
            "🔴 Environment Offline";

        document.getElementById("status").className =
            "status offline";

        console.error(error);
    }
}

// ----------------------------
// Final Evaluation
// ----------------------------

function showEvaluation(report) {

    document
        .getElementById("evaluation-section")
        .classList.remove("hidden");

    document.getElementById("overall_score").innerText =
        report.overall_score;

    document.getElementById("grade").innerText =
        report.grade;

    document.getElementById("evaluation_status").innerText =
        report.status;

    // Metrics

    const metricsDiv =
        document.getElementById("evaluation_metrics");

    metricsDiv.innerHTML = "";

    for (const key in report.metrics) {

        const value = report.metrics[key];

        metricsDiv.innerHTML += `
            <div class="metric-row">

                <p>
                    <strong>
                        ${formatLabel(key)}
                    </strong>

                    (${value}%)
                </p>

                <div class="metric-progress">
                    <div style="width:${value}%"></div>
                </div>

            </div>
        `;
    }

    // Strengths

    const strengths =
        document.getElementById("strengths");

    strengths.innerHTML = "";

    report.strengths.forEach(item => {

        strengths.innerHTML +=
            `<li>${item}</li>`;

    });

    // Suggestions

    const suggestions =
        document.getElementById("suggestions");

    suggestions.innerHTML = "";

    report.suggestions.forEach(item => {

        suggestions.innerHTML +=
            `<li>${item}</li>`;

    });

    document
        .getElementById("evaluation-section")
        .scrollIntoView({
            behavior: "smooth"
        });

}

// ----------------------------
// Utility
// ----------------------------

function formatLabel(text) {

    return text
        .replaceAll("_", " ")
        .replace(/\b\w/g, c => c.toUpperCase());

}

// ----------------------------

resetEnvironment();