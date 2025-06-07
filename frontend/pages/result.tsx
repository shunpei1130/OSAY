import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'

export default function Result() {
  const router = useRouter()
  const [report, setReport] = useState<any>(null)
  useEffect(() => {
    const stored = localStorage.getItem('report')
    if (stored) setReport(JSON.parse(stored))
  }, [])
  if (!report) return null
  return (
    <div style={{padding:20}}>
      <h1>Result: {report.grade || 'pending'}</h1>
      <button onClick={()=>router.push('/submit')}>New Report</button>
    </div>
  )
}
