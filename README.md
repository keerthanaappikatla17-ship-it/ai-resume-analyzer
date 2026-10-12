
# AI Resume Analyzer and Job Matcher

## Project Overview
The Resume Analyzer is a web application that compares a resume with a job description. It identifies matching skills, highlights missing skills, calculates a skill-match percentage, and provides basic improvement suggestions.

## Features
- Resume text input
- Job description input
- Resume and job skill matching
- Match percentage calculation
- Matching and missing skill identification
- Resume improvement suggestions
- Simple and user-friendly interface

## Technologies Used
- Python
- Flask
- HTML
- CSS

## How It Works
1. The user enters resume text.
2. The user enters a job description.
3. The application detects supported skills in both texts.
4. It calculates the percentage of job-description skills found in the resume.
5. It displays matching skills, missing skills, and suggestions.

## Installation and Setup

1. Install Python.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment.
4. Install Flask:

   pip install flask

5. Start the application:

   python app.py

6. Open http://127.0.0.1:5000 in your browser.

## Future Enhancements
- Upload PDF and DOCX resumes
- Add more job roles and skills
- Improve text analysis using NLP
- Save previous analysis results

## Disclaimer
The match percentage is a basic keyword-based estimate. It is not a measure of a candidate's actual suitability or a guarantee of employment.
