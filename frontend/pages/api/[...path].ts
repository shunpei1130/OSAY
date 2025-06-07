import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { path = [] } = req.query
  const backendUrl = process.env.BACKEND_URL || 'http://localhost:8000'
  const url = `${backendUrl}/${(path as string[]).join('/')}`
  const r = await fetch(url, {
    method: req.method,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(req.body)
  })
  const data = await r.json()
  res.status(r.status).json(data)
}
