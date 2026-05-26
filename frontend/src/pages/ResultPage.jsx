import { Link, useLocation, useNavigate } from 'react-router-dom'
import { useEffect } from 'react'
import ProgressBar from '../components/ProgressBar.jsx'

export default function ResultPage() {
  const { state } = useLocation()
  const navigate = useNavigate()

  // If someone navigates here directly without result data, send them to analyze
  useEffect(() => {
    if (!state?.result) {
      navigate('/analyze', { replace: true })
    }
  }, [state, navigate])

  if (!state?.result) return null

  const {
    top_career,
    match_score,
    predictions,
    final_skills,
    ai_missing,
    ai_roadmap,
    ai_suggestions,
    data,
  } = state.result

  return (
    <>
      {/* Results hero banner */}
      <section className="card results-hero">
        <div>
          <p className="eyebrow">Results Dashboard</p>
          <h2>Career analysis result</h2>
          <p className="section-note">
            Top suggested path: <strong>{top_career}</strong>
          </p>
        </div>
        <div className="metric-chip">
          <span>Match score</span>
          <strong>{match_score}%</strong>
        </div>
      </section>

      {/* Profile + Skill match */}
      <section className="grid-layout">
        <div className="card">
          <h3>Your Profile</h3>
          <ul className="clean-list">
            <li><strong>Skills:</strong> {data.skills}</li>
            <li><strong>Interests:</strong> {data.interests}</li>
            <li><strong>Subjects:</strong> {data.subjects}</li>
            <li><strong>Work Style:</strong> {data.work_style}</li>
          </ul>
        </div>

        <div className="card">
          <h3>Skill Match Score</h3>
          <p><strong>{match_score}%</strong> alignment with required skills</p>
          <ProgressBar value={match_score} />
        </div>
      </section>

      {/* Top careers + Required skills */}
      <section className="grid-layout">
        <div className="card">
          <h3>
            Top Career Matches&nbsp;
            <span className="badge">AI Powered</span>
          </h3>
          <ul className="ranked-list">
            {predictions.map(([career, prob]) => (
              <li key={career}>
                <span>{career}</span>
                <strong>{prob.toFixed(2)}</strong>
              </li>
            ))}
          </ul>
        </div>

        <div className="card">
          <h3>Required Skills</h3>
          {final_skills.length > 0 ? (
            <ul className="chip-list">
              {final_skills.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>
          ) : (
            <p>No data</p>
          )}
        </div>
      </section>

      {/* Skill gaps + Roadmap */}
      <section className="grid-layout">
        <div className="card">
          <h3>Skill Gap for {top_career}</h3>
          {ai_missing.length > 0 ? (
            <ul className="clean-list">
              {ai_missing.map((skill, i) => (
                <li key={i}>{skill}</li>
              ))}
            </ul>
          ) : (
            <ul className="clean-list">
              <li>No missing skills. Nice work.</li>
            </ul>
          )}
        </div>

        <div className="card">
          <h3>Learning Roadmap for {top_career}</h3>
          {ai_roadmap.length > 0 ? (
            <ol className="roadmap-list">
              {ai_roadmap.map((step, i) => (
                <li key={i}>{step}</li>
              ))}
            </ol>
          ) : (
            <ol className="roadmap-list">
              <li>No roadmap available</li>
            </ol>
          )}
        </div>
      </section>

      {/* AI suggestions + CTAs */}
      <section className="card">
        <h3>AI Suggestions</h3>
        {ai_suggestions.length > 0 ? (
          <ul className="clean-list compact-list">
            {ai_suggestions.map((tip, i) => (
              <li key={i}>{tip}</li>
            ))}
          </ul>
        ) : (
          <ul className="clean-list">
            <li>No suggestions available</li>
          </ul>
        )}

        <div className="cta-row">
          <Link to="/analyze" className="btn btn-primary">Analyze Again</Link>
          <Link to="/" className="btn btn-ghost">Go Home</Link>
        </div>
      </section>
    </>
  )
}
