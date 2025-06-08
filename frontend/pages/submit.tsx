import { useRouter } from 'next/router'
import { useState } from 'react'

export default function Submit() {
  const router = useRouter()
  const [text, setText] = useState('')
  const submit = async () => {
    const username = localStorage.getItem('username')
    const res = await fetch('/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, report_text: text })
    })
    const data = await res.json()
    localStorage.setItem('report', JSON.stringify(data))
    router.push('/questions')
  }
  return (
    <div className="container">
      <h1>Submit Report</h1>
      <textarea
        value={text}
        onChange={e => setText(e.target.value)}
      />
      <button onClick={submit}>Submit</button>
    </div>
  )
}
