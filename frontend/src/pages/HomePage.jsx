import { Link } from 'react-router-dom'

export default function HomePage() {
  return (
    <section className="hero-panel">
      {/* Left — main copy */}
      <div className="hero-copy card">
        <p className="eyebrow">Minimal AI Guidance</p>
        <h1>See where your current strengths can take you next.</h1>
        <p>
          AI Career Lab turns your skills, interests, and work preferences into a focused
          recommendation flow with role matches, missing skills, and a practical roadmap.
        </p>

        <div className="pill-row">
          <span className="pill">Career fit</span>
          <span className="pill">Skill gaps</span>
          <span className="pill">Learning path</span>
        </div>

        <div className="cta-row">
          <Link to="/analyze" className="btn btn-primary">Start analysis</Link>
          <Link to="/analyze" className="btn btn-ghost">Try the planner</Link>
        </div>
      </div>

      {/* Right — feature list */}
      <aside className="hero-sidebar card">
        <p className="eyebrow">What you get</p>
        <div className="feature-stack">
          <div className="feature-item">
            <span className="feature-kicker">01</span>
            <div>
              <h3>Clear role ranking</h3>
              <p>Compare strong-fit career directions instead of guessing from scratch.</p>
            </div>
          </div>
          <div className="feature-item">
            <span className="feature-kicker">02</span>
            <div>
              <h3>Focused skill advice</h3>
              <p>Spot the most useful gaps so your next steps stay small and realistic.</p>
            </div>
          </div>
          <div className="feature-item">
            <span className="feature-kicker">03</span>
            <div>
              <h3>Useful in dark mode too</h3>
              <p>A dedicated low-glare theme keeps the interface calm without losing contrast.</p>
            </div>
          </div>
        </div>
      </aside>
    </section>
  )
}
