import { useRouter } from 'next/router'
import { useState } from 'react'

export default function Home() {
  const router = useRouter()
  const [username, setUsername] = useState('')
  const login = () => {
    localStorage.setItem('username', username)
    router.push('/submit')
  }
  return (
    <div className="container">
      <h1>AuthEssay Login</h1>
      <input
        value={username}
        onChange={e => setUsername(e.target.value)}
        placeholder="Username"
      />
      <button onClick={login}>Login</button>
    </div>
  )
}
