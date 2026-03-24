from flask import Flask, render_template, request, jsonify
from groq import Groq
app = Flask(__name__)
GROQ_API_KEY = "ENTER_YOUR_GROQ_API_KEY_HERE"
client = Groq(api_key=GROQ_API_KEY)
with open("knowledge.txt", "r", encoding="utf-8") as f:
    knowledge = f.read()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if user_input.lower() in ["hi", "hello", "hey", "hey there"]:
        return jsonify({"reply": "Hello!"
        " How can I help you with Python and machine learning concepts"})
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"user","content": f"Answer from this data: \n{knowledge}\n\nQuestion: {user_input}"
            }
        ]

    )
    reply = completion.choices[0].message.content
    return jsonify({"reply": reply})
if __name__ == "__main__":
    app.run(debug=True)
