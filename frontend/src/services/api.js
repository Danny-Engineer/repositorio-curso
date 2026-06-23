const API_BASE = "http://localhost:8000/api"

export async function getSystemStatus() {
  const res = await fetch(`${API_BASE}/system/status`)
  return await res.json()
}

export async function generateAI(payload) {
  const res = await fetch(`${API_BASE}/ai/generate`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
  })
  return await res.json()
}

export async function createChapter(payload) {
  const res = await fetch(`${API_BASE}/publisher/chapter`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
  })
  return await res.json()
}

export async function analyzePemexDocument(payload) {
  const res = await fetch(`${API_BASE}/pemex/documents/analyze`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
  })
  return await res.json()
}

export async function generatePemexResponse(payload) {
  const res = await fetch(`${API_BASE}/pemex/documents/generate-response`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
  })
  return await res.json()
}
