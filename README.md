# TalentMatch AI

AI-powered Resume Analysis, ATS Scoring, and Semantic Job Matching Platform.

## Overview

TalentMatch AI is a major project developed to help users analyze resumes against job descriptions using Artificial Intelligence, semantic similarity, ATS scoring, and skill-gap analysis.

The platform allows users to:

* Upload resumes in PDF/Image format
* Paste job descriptions from platforms like Naukri, LinkedIn, Indeed, etc.
* Get AI-powered match percentage
* Analyze ATS compatibility
* Detect missing skills
* Receive improvement suggestions
* Get suitable job role recommendations
* Explore external job links

The system combines Natural Language Processing (NLP), Sentence Transformers, semantic embeddings, and skill extraction techniques to simulate real-world ATS and recruiter evaluation systems.

---

# Features

## Resume Upload

Users can upload resumes in:

* PDF
* Image formats

The backend extracts readable text automatically.

---

## Semantic Resume Matching

The system uses Sentence Transformers to:

* Convert resume text into embeddings
* Convert job descriptions into embeddings
* Perform cosine similarity matching
* Generate semantic match percentage

---

## ATS Score Analysis

The ATS engine evaluates:

* Resume structure
* Required sections
* Job-description relevance
* Skill alignment
* Resume readability

---

## Skill Gap Analysis

The platform identifies:

* Matched skills
* Missing skills
* Suggested improvements

---

## Job Recommendation System

The system uses the Naukri dataset to:

* Recommend suitable job roles
* Match resume skills with real job postings
* Suggest external job platforms

---

## Modern UI

Frontend inspired by modern ATS checker platforms.

Includes:

* Interactive dashboard
* Score cards
* Skill badges
* Recommendation cards
* Responsive design

---

# Tech Stack

## Frontend

* React.js
* Vite
* CSS
* JavaScript

## Backend

* FastAPI
* Python
* Uvicorn

## AI / NLP

* Sentence Transformers
* Scikit-learn
* Cosine Similarity
* NLP Skill Extraction

## Dataset

* Naukri Job Dataset

## Tools

* Git
* GitHub
* VS Code

---

# Project Architecture

```text
Resume Upload
      ↓
Resume Parser
      ↓
Text Extraction
      ↓
Skill Extraction
      ↓
Semantic Embedding
      ↓
Cosine Similarity Matching
      ↓
ATS Evaluation
      ↓
Skill Gap Analysis
      ↓
Job Recommendation Engine
      ↓
Frontend Dashboard
```

---

# Folder Structure

```text
TalentMatch-AI/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   └── analyze.py
│   │   │
│   │   ├── services/
│   │   │   ├── ats.py
│   │   │   ├── links.py
│   │   │   ├── matcher.py
│   │   │   ├── parser.py
│   │   │   └── skills.py
│   │   │
│   │   ├── data/
│   │   │   └── naukri_jobs.csv
│   │   │
│   │   └── __init__.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── public/
│   └── package.json
│
├── README.md
└── .gitignore
```

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/AbhishekkASR/TalentMatch-AI.git
```

---

# Backend Setup

## Navigate to backend

```bash
cd backend
```

## Create virtual environment

```bash
python -m venv venv
```

## Activate environment

### Windows

```bash
..\venv\Scripts\Activate.ps1
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run backend

```bash
python -m uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

## Navigate to frontend

```bash
cd frontend
```

## Install dependencies

```bash
npm install
```

## Run frontend

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# API Endpoint

## Analyze Resume

### POST

```text
/analyze_resume
```

### Form Data

| Parameter       | Type   |
| --------------- | ------ |
| resume_file     | File   |
| job_description | String |

---

# AI Matching Logic

The final resume score is calculated using:

```text
Final Score =
0.60 × Semantic Similarity
+ 0.30 × Skill Match
+ 0.10 × ATS Score
```

---

# ATS Scoring Factors

The ATS score considers:

* Resume structure
* Presence of sections
* Skills relevance
* Keyword matching
* Readability

---

# Dataset Information

The project uses a processed Naukri dataset containing:

* Job titles
* Skills
* Companies
* Locations
* Industry domains
* Experience levels
* Job descriptions

The dataset is used for:

* Role recommendations
* Skill matching
* External job redirection

---

# Future Improvements

Possible future enhancements:

* Authentication system
* Resume history
* Recruiter dashboard
* MongoDB/PostgreSQL integration
* Vector database optimization
* Real-time job APIs
* AI chatbot assistant
* Resume ranking system
* Cloud deployment

---

# Challenges Faced

* Large dataset processing
* Transformer model optimization
* ATS score balancing
* Semantic matching optimization
* Deployment limitations on free hosting

---

# Author

## Abhishek Singh

B.Tech Computer and Communication Engineering

Manipal University Jaipur

### Links

* GitHub: [https://github.com/AbhishekkASR](https://github.com/AbhishekkASR)
* LinkedIn: [https://www.linkedin.com/in/abhishek-singh-739102253/](https://www.linkedin.com/in/abhishek-singh-739102253/)
* Portfolio: [https://abhishekkasr.github.io/](https://abhishekkasr.github.io/)

---

# License

This project is developed for educational and academic purposes.

---

# Screenshots

<img width="1905" height="915" alt="Screenshot 2026-05-12 004702" src="https://github.com/user-attachments/assets/f122f967-a972-4d3c-a3ce-d6dc18f7a430" />
<img width="1919" height="996" alt="Screenshot 2026-05-12 004352" src="https://github.com/user-attachments/assets/f9859704-c135-4f9f-a7bd-a4a0d744be70" />
<img width="1905" height="857" alt="Screenshot 2026-05-11 061608" src="https://github.com/user-attachments/assets/72b987fb-d0a8-4d4d-bba5-82f54a166c8f" />


---

# Conclusion

TalentMatch AI provides an intelligent solution for resume evaluation and job-role recommendation using modern AI and NLP technologies. The project demonstrates practical implementation of semantic similarity, ATS analysis, and machine learning concepts in real-world recruitment systems.
