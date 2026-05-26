import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'

const INITIAL = { skills: '', interests: '', subjects: '', work_style: '' }

export default function AnalyzePage() {
  const [form, setForm] = useState(INITIAL)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const navigate = useNavigate()

  const handleChange = (e) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)

    const { skills, interests, subjects, work_style } = form
    if (!skills.trim() || !interests.trim() || !subjects.trim() || !work_style.trim()) {
      setError('All fields are required.')
      return
    }

    setLoading(true)
    try {
      const res = await fetch('/api/analyze/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      })

      const data = await res.json()

      if (!res.ok) {
        throw new Error(data.error || 'Something went wrong. Please try again.')
      }

      // Pass result data to the result page via navigation state
      navigate('/result', { state: { result: data } })
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <section className="split-layout">
      {/* Left — form */}
      <div className="card form-shell">
        <p className="eyebrow">Profile Input</p>
        <h2>Build your career snapshot</h2>
        <p className="section-note">Keep each answer short and comma-separated for the most accurate match suggestions.</p>

        {error && (
          <div style={{
            padding: '0.75rem 1rem',
            borderRadius: '14px',
            background: 'rgba(220, 38, 38, 0.1)',
            border: '1px solid rgba(220, 38, 38, 0.2)',
            color: '#dc2626',
            fontSize: '0.9rem',
            marginTop: '0.75rem',
          }}>
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            <div className="field-wrap">
              <label htmlFor="skills">Skills</label>
              <input
                id="skills"
                name="skills"
                type="text"
                placeholder="e.g. python, sql, machine learning"
                value={form.skills}
                onChange={handleChange}
                disabled={loading}
              />
              <small>Example: python, sql, machine learning</small>
            </div>

            <div className="field-wrap">
              <label htmlFor="interests">Interests</label>
              <input
                id="interests"
                name="interests"
                type="text"
                placeholder="e.g. AI products, research"
                value={form.interests}
                onChange={handleChange}
                disabled={loading}
              />
              <small>Example: AI products, research, data storytelling</small>
            </div>

            <div className="field-wrap">
              <label htmlFor="subjects">Favorite subjects</label>
              <input
                id="subjects"
                name="subjects"
                type="text"
                placeholder="e.g. mathematics, statistics"
                value={form.subjects}
                onChange={handleChange}
                disabled={loading}
              />
              <small>Example: mathematics, statistics, computer science</small>
            </div>

            <div className="field-wrap">
              <label htmlFor="work_style">Preferred work style</label>
              <input
                id="work_style"
                name="work_style"
                type="text"
                placeholder="e.g. analytical, collaborative"
                value={form.work_style}
                onChange={handleChange}
                disabled={loading}
              />
              <small>Example: analytical, collaborative, independent</small>
            </div>
          </div>

          <div className="cta-row">
            <button type="submit" className="btn btn-primary" disabled={loading}>
              {loading && <span className="spinner" aria-hidden="true" />}
              {loading ? 'Analysing…' : 'Analyze career'}
            </button>
            <Link to="/" className="btn btn-ghost">Back home</Link>
          </div>
        </form>
      </div>

      {/* Right — tips */}
      <aside className="card info-panel">
        <p className="eyebrow">Before you submit</p>
        <h3>How to get cleaner results</h3>
        <ul className="clean-list compact-list">
          <li>List tools and technologies you can actually use today.</li>
          <li>Mention interests that reflect the kind of work you enjoy, not just trending fields.</li>
          <li>Use work style to describe how you prefer solving problems and collaborating.</li>
        </ul>
        <div className="soft-callout">
          <strong>Tip</strong>
          <p>Short, specific inputs usually produce better role matches than long descriptive paragraphs.</p>
        </div>
      </aside>
    </section>
  )
}
