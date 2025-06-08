import useSWR from 'swr'

const fetcher = (url: string) => fetch(url).then(r => r.json())

export default function Dashboard() {
  const { data } = useSWR('/api/dashboard', fetcher)
  if (!data) return <div>Loading...</div>
  return (
    <div className="container">
      <h1>Teacher Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Student</th>
            <th>Grade</th>
          </tr>
        </thead>
        <tbody>
          {data.reports.map((r: any) => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.student}</td>
              <td>{r.grade}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
