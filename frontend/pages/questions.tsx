import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'

export default function Questions() {
  const router = useRouter()
  const [report, setReport] = useState<any>(null)
  const [answers, setAnswers] = useState<string[]>([])
  const [time, setTime] = useState(300)

  useEffect(() => {
    const stored = localStorage.getItem('report')
    if (stored) {
      const r = JSON.parse(stored)
      setReport(r)
      setAnswers(new Array(r.questions.length).fill(''))
    }
    const t = setInterval(() => setTime(t => t-1), 1000)
    return () => clearInterval(t)
  }, [])

  const submit = async () => {
    const username = localStorage.getItem('username')
    const payload = {
      username,
      report_id: report.id,
      answers: report.questions.map((q:any, i:number) => ({ question_id: q.id, text: answers[i] }))
    }
    const res = await fetch('/api/submit_answers', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    localStorage.setItem('report', JSON.stringify(data))
    router.push('/result')
  }

  if (!report) return null
  return (
    <div className="container">
      <div>Time left: {time}s</div>
      {report.questions.map((q: any, i: number) => (
        <div key={q.id}>
          <p>{q.text}</p>
          <textarea
            value={answers[i]}
            onChange={e => {
              const copy = [...answers]
              copy[i] = e.target.value
              setAnswers(copy)
            }}
          />
        </div>
      ))}
      <button onClick={submit}>Submit Answers</button>
    </div>
  )
}
