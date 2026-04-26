import requests
import json

API_KEY = "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"

def generate_questions(skill):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""You are a strict technical interviewer.Conduct a real interview on {skill}.Rules:- Ask ONLY ONE question- Do NOT ask multiple questions- Do NOT give a list- Do NOT explain anything- Keep it short- Stop after asking one questionStart with a basic level question."""



    data = {
        "model":"meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    print("RAW QUESTIONS RESPONSE:", response.text)

    try:
        res_json = response.json()

        if "choices" in res_json:
            return res_json["choices"][0]["message"]["content"]

        else:
            return f"Error: {res_json}"

    except:
        return "Error generating questions"

def evaluate_answer(skill, answer):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Evaluate this answer for {skill}.

    Answer: {answer}

    Give feedback and score out of 10.
    """

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    print("RAW EVALUATION RESPONSE:", response.text)

    try:
        res_json = response.json()
        return res_json.get("choices", [{}])[0].get("message", {}).get("content", "Error")
    except:
        return "Error evaluating answer"
