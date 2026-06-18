"""from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)

# ✅ FIXED CORS (more reliable)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# ⚠️ API KEY (DON'T SHARE IN REAL PROJECTS)
genai.configure(api_key="AQ.Ab8RN6KbN07Lra8MbLW2JIMf8vOGq3VcVn7I93z_zKPdS_HylQ")


@app.route("/")
def home():
    return "Backend Connected Successfully!"


@app.route("/explain", methods=["POST"])
def explain():
    try:
        print("🔥 /explain HIT")

        data = request.get_json()
        print("DATA:", data)

        # ✅ safer way (avoids crash)
        topic = data.get("topic", "")

        if topic == "":
            return jsonify({"error": "No topic provided"}), 400

        model = genai.GenerativeModel("gemini-2.5-flash")


        response = model.generate_content(
            f"Explain {topic} in simple language with example and key points"
        )

        print("✅ RESPONSE GENERATED")

        return jsonify({
            "answer": response.text
        })

    except Exception as e:
        print("❌ ERROR:", str(e))
        return jsonify({
            "error": str(e)
        }), 500
@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        print("🔥 /summarize HIT")

        data = request.get_json()
        print("DATA:", data)

        notes = data.get("notes", "")

        if notes == "":
            return jsonify({"error": "No notes provided"}), 400

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            
            Summarize the following notes in simple language.

            Give:
            1. Short Summary
            2. Important Points
            3. Exam Tips

            Notes:
            {notes}
            
        )

        print("✅ SUMMARY GENERATED")

        return jsonify({
            "summary": response.text
        })
    except Exception as e:
        error_msg = str(e)

    if "429" in error_msg:
        return jsonify({
            "answer": "Gemini rate limit reached. Please wait 1 minute and try again."
        })

    return jsonify({
        "answer": f"Error: {error_msg}"
    })
    

if __name__ == "__main__":
    app.run(debug=True)"""
    
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)

# Allow React frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Paste your Gemini API key below
genai.configure(api_key="AQ.Ab8RN6Jr3PAjK3LdmzktlDN_7zEAzDpf3T6vu663P1knR1inLQ")


@app.route("/")
def home():
    return "Backend Connected Successfully!"


# ==========================
# EXPLAIN TOPIC
# ==========================
@app.route("/explain", methods=["POST"])
def explain():
    try:
        print("🔥 /explain HIT")

        data = request.get_json()
        print("DATA:", data)

        topic = data.get("topic", "")

        if topic == "":
            return jsonify({
                "answer": "Please enter a topic."
            })

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            f"Explain {topic} in simple language with example and key points."
        )

        print("✅ RESPONSE GENERATED")

        return jsonify({
            "answer": response.text
        })

    except Exception as e:
        error_msg = str(e)
        print("❌ ERROR:", error_msg)

        if "429" in error_msg:
            return jsonify({
                "answer": "⚠️ Gemini API rate limit reached. Please wait 1 minute and try again."
            })

        return jsonify({
            "answer": f"Error: {error_msg}"
        })


# ==========================
# NOTES SUMMARIZER
# ==========================
@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        print("🔥 /summarize HIT")

        data = request.get_json()
        print("DATA:", data)

        notes = data.get("notes", "")

        if notes == "":
            return jsonify({
                "summary": "Please enter some notes."
            })

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            f"""
            Summarize the following notes in simple language.

            Give:
            1. Short Summary
            2. Important Points
            3. Exam Tips

            Notes:
            {notes}
            """
        )

        print("✅ SUMMARY GENERATED")

        return jsonify({
            "summary": response.text
        })

    except Exception as e:
        error_msg = str(e)
        print("❌ ERROR:", error_msg)

        if "429" in error_msg:
            return jsonify({
                "summary": "⚠️ Gemini API rate limit reached. Please wait 1 minute and try again."
            })

        return jsonify({
            "summary": f"Error: {error_msg}"
        })
@app.route("/quiz", methods=["POST"])
def quiz():
    try:
        print("🔥 /quiz HIT")

        data = request.get_json()
        print("DATA:", data)

        topic = data.get("topic", "")

        if topic == "":
            return jsonify({
                "quiz": "Please enter a topic."
            })

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            f"""
            Generate 5 multiple-choice questions (MCQs) on {topic}.

            Format:

            Q1.
            A)
            B)
            C)
            D)

            Answer:

            Repeat for 5 questions.
            """
        )

        return jsonify({
            "quiz": response.text
        })

    except Exception as e:
        error_msg = str(e)

        if "429" in error_msg:
            return jsonify({
                "quiz": "⚠️ Gemini API limit reached. Please wait and try again."
            })

        return jsonify({
            "quiz": f"Error: {error_msg}"
        })
@app.route("/flashcards", methods=["POST"])
def flashcards():

    try:

        data = request.get_json()

        topic = data.get("topic", "")

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            f"""
            Generate 5 study flashcards for {topic}.

            Format:

            Flashcard 1
            Question:
            Answer:

            Flashcard 2
            Question:
            Answer:
            """
        )

        return jsonify({
            "flashcards": response.text
        })

    except Exception as e:

        return jsonify({
            "flashcards": f"Error: {str(e)}"
        })
if __name__ == "__main__":
    app.run(debug=True)