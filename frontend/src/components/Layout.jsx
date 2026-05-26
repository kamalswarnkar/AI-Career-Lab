import { Link, NavLink, Outlet } from 'react-router-dom'
import { useCallback, useEffect, useState } from 'react'

export default function Layout() {
  const [theme, setTheme] = useState(() => {
    return document.documentElement.dataset.theme || 'light'
  })

  useEffect(() => {
    document.documentElement.dataset.theme = theme
    localStorage.setItem('ai-career-lab-theme', theme)
  }, [theme])

  const toggleTheme = useCallback(() => {
    setTheme((t) => (t === 'dark' ? 'light' : 'dark'))
  }, [])

  return (
    <>
      {/* Background decoration */}
      <div className="bg-mesh" />
      <div className="bg-orb orb-left" />
      <div className="bg-orb orb-right" />

      {/* Header */}
      <header className="site-header">
        <div className="shell">
          <Link to="/" className="brand">
            <span className="brand-mark">AL</span>
            <span className="brand-copy">
              <strong>AI Career Lab</strong>
              <small>Career direction, distilled</small>
            </span>
          </Link>

          <nav className="site-nav">
            <NavLink to="/" end>Home</NavLink>
            <NavLink to="/analyze">Analyze</NavLink>
          </nav>

          <button
            type="button"
            className="theme-toggle"
            aria-label="Toggle dark mode"
            aria-pressed={theme === 'dark'}
            onClick={toggleTheme}
          >
            <span className="theme-toggle-track">
              <span className="theme-toggle-label theme-toggle-light">Light</span>
              <span className="theme-toggle-label theme-toggle-dark">Dark</span>
            </span>
          </button>
        </div>
      </header>

      {/* Page content */}
      <main className="shell page-content">
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="site-footer">
        <div className="shell">
          <p>Built for smarter career decisions.</p>
        </div>
      </footer>
    </>
  )
}
