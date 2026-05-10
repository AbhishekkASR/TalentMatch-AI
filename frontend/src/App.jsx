import React, { useState } from "react";
import "./App.css";

export default function App() {
  const [resume, setResume] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeResume = async () => {
    if (!resume || !jobDesc) {
      alert("Upload resume and paste job description");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("resume_file", resume);
    formData.append("job_description", jobDesc);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/analyze_resume",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.log(error);
      alert("Backend connection failed");
    }

    setLoading(false);
  };

  return (
    <div className="main-container">
      {/* HERO SECTION */}
      <section className="hero-section">
        <div className="overlay"></div>

        <div className="hero-content">
          <div className="left-section">
            <span className="badge">AI Resume Analyzer</span>

            <h1>
              Check Whether
              <br />
              Your Resume
              <br />
              Will Get Shortlisted
            </h1>

            <p>
              Upload your resume and compare it against any real-world job
              description from Naukri, LinkedIn, Indeed, Microsoft Careers,
              Blinkit, Amazon, and more.
            </p>

            <div className="hero-stats">
              <div className="stat-card">
                <h2>ATS</h2>
                <span>Score Analysis</span>
              </div>

              <div className="stat-card">
                <h2>AI</h2>
                <span>Skill Matching</span>
              </div>

              <div className="stat-card">
                <h2>LIVE</h2>
                <span>Role Suggestion</span>
              </div>
            </div>
          </div>

          {/* RIGHT PANEL */}
          <div className="upload-panel">
            <h2>Upload Resume</h2>

            <input
              type="file"
              onChange={(e) => setResume(e.target.files[0])}
            />

            <textarea
              placeholder="Paste complete job description here..."
              value={jobDesc}
              onChange={(e) => setJobDesc(e.target.value)}
            />

            <button onClick={analyzeResume}>
              {loading ? "Analyzing..." : "Check Resume"}
            </button>
          </div>
        </div>
      </section>

      {/* RESULT SECTION */}
      {result && (
        <section className="result-section">
         <div className="score-wrapper">

  <div className="score-card">
    <h2>{result.match_percentage}%</h2>
    <p>Resume Match Score</p>
  </div>

  <div className="score-card">
    <h2>{result.ats_score}%</h2>
    <p>ATS Score</p>
  </div>

</div>
<div className="roles-section">

  <h2>Recommended Job Roles</h2>

  <div className="roles-grid">

    {result.recommended_roles?.map((role, index) => (
      <div className="role-card" key={index}>

        <h3>{role.title}</h3>

        <p className="role-score">
          Match: {role.score}%
        </p>

        <div className="skills">
          {role.matched_skills?.map((skill, i) => (
            <span key={i} className="green">
              {skill}
            </span>
          ))}
        </div>

        <div className="job-links">
          <a href={role.job_links.naukri} target="_blank">
            Naukri
          </a>

          <a href={role.job_links.linkedin} target="_blank">
            LinkedIn
          </a>

          <a href={role.job_links.indeed} target="_blank">
            Indeed
          </a>
        </div>

      </div>
    ))}

  </div>
</div>

          <div className="result-grid">
            <div className="result-box">
              <h3>Decision</h3>
              <p>{result.decision}</p>
            </div>

            <div className="result-box">
              <h3>Matched Skills</h3>

              <div className="skills">
                {result.matched_skills?.map((skill, index) => (
                  <span key={index} className="green">
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            <div className="result-box">
              <h3>Missing Skills</h3>

              <div className="skills">
                {result.missing_skills?.map((skill, index) => (
                  <span key={index} className="red">
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            <div className="result-box">
              <h3>Improvement Suggestions</h3>

              <ul>
                {result.improvement_suggestions?.map((tip, index) => (
                  <li key={index}>{tip}</li>
                ))}
              </ul>
            </div>
          </div>
        </section>
      )}

      {/* FEATURES */}
      <section className="features">
        <h2>Why TalentMatch AI?</h2>

        <div className="feature-grid">
          <div className="feature-card">
            <h3>ATS Checker</h3>
            <p>
              Analyze ATS compatibility and recruiter shortlist probability.
            </p>
          </div>

          <div className="feature-card">
            <h3>Skill Gap Analysis</h3>
            <p>
              Detect missing technologies and required professional skills.
            </p>
          </div>

          <div className="feature-card">
            <h3>Role Recommendation</h3>
            <p>
              Suggest suitable job profiles according to your resume.
            </p>
          </div>

          <div className="feature-card">
            <h3>Real Job Matching</h3>
            <p>
              Match resumes with real-world company job descriptions.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}