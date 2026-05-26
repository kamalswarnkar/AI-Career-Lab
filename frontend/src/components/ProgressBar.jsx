import { useEffect, useRef } from 'react'

export default function ProgressBar({ value }) {
  const fillRef = useRef(null)

  useEffect(() => {
    const raf = requestAnimationFrame(() => {
      if (fillRef.current) {
        fillRef.current.style.width = `${value}%`
      }
    })
    return () => cancelAnimationFrame(raf)
  }, [value])

  return (
    <div className="progress-bar" role="progressbar" aria-valuenow={value} aria-valuemin={0} aria-valuemax={100}>
      <div ref={fillRef} className="progress-fill" style={{ width: '0%' }} />
    </div>
  )
}
