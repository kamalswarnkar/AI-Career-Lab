import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

// Initialise theme before first paint to avoid flash
;(function () {
  const root = document.documentElement
  const saved = localStorage.getItem('ai-career-lab-theme')
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
  root.dataset.theme = saved || (prefersDark ? 'dark' : 'light')
})()

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
