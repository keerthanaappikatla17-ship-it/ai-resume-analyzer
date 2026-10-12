
from flask import Flask, render_template, request

app = Flask(__name__)

SKILLS = [
    "python", "java", "c++", "sql", "mysql",
    "html", "css", "javascript", "flask",
    "communication", "teamwork", "leadership",
    "excel", "power bi", "tableau",
    "data analysis", "problem solving",
    "business analysis", "requirements gathering"
    "javascript", "tableau", "requirements gathering",
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.form.get("resume", "").lower()
    job = request.form.get("job", "").lower()

    required_skills = [skill for skill in SKILLS if skill in job]
    matched_skills = [skill for skill in required_skills if skill in resume]
    missing_skills = [skill for skill in required_skills if skill not in resume]

    if required_skills:
        score = round(len(matched_skills) / len(required_skills) * 100)
    else:
        score = 0

    suggestions = []

    if missing_skills:
        suggestions.append("Learn or highlight relevant missing skills.")
    if len(resume.split()) < 100:
        suggestions.append("Consider adding more relevant details to your resume.")
    if not suggestions:
        suggestions.append("Good start! Tailor your experience and achievements to the job.")

    return render_template(
        "result.html",
        score=score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)
