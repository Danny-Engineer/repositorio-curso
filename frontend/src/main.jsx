import React, { useEffect, useState } from 'react'
import { createRoot } from 'react-dom/client'
import {
  getSystemStatus,
  generateAI,
  createChapter,
  analyzePemexDocument,
  generatePemexResponse
} from './services/api'
import './styles/app.css'

function App() {
  const [page, setPage] = useState("Dashboard")
  const [status, setStatus] = useState(null)
  const [topic, setTopic] = useState("IA aplicada a Recursos Humanos")
  const [result, setResult] = useState("")
  const [chapterTitle, setChapterTitle] = useState("La revolución de la inteligencia artificial")
  const [chapter, setChapter] = useState("")
  const [oficioText, setOficioText] = useState("Se solicita remitir evidencia documental relacionada con el procedimiento de calidad y atención de auditoría.")
  const [analysis, setAnalysis] = useState("")
  const [draft, setDraft] = useState("")

  useEffect(() => { getSystemStatus().then(setStatus).catch(() => setStatus(null)) }, [])

  async function handleGenerate() {
    const data = await generateAI({ topic, audience: "RH y Calidad", tone: "profesional" })
    setResult(data.content)
  }

  async function handleChapter() {
    const data = await createChapter({
      title: chapterTitle,
      summary: "Capítulo generado desde API Publisher.",
      objectives: ["Comprender el tema", "Aplicarlo en procesos empresariales", "Diseñar un caso práctico"],
      competencies: ["Pensamiento crítico", "Uso de IA", "Automatización documental"]
    })
    setChapter(data.markdown)
  }

  async function handleAnalyzeOficio() {
    const data = await analyzePemexDocument({ raw_text: oficioText, area: "Servicios Logísticos", document_type: "Oficio" })
    setAnalysis(JSON.stringify(data, null, 2))
  }

  async function handleGenerateResponse() {
    const data = await generatePemexResponse({
      raw_text: oficioText,
      instruction: "Elabora una respuesta institucional clara, formal y orientada a acciones.",
      sender_area: "Área de Especialidad de Servicios Logísticos Terrestres",
      recipient: "Área solicitante",
      signer: "Daniel Melchor Pérez",
      tone: "institucional PEMEX"
    })
    setDraft(data.draft_markdown)
  }

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>Logística IA Lab</h2>
        {["Dashboard", "Publisher", "AI Studio", "Knowledge Hub", "PEMEX Suite"].map(item => (
          <button key={item} onClick={() => setPage(item)} className={page === item ? "active" : ""}>{item}</button>
        ))}
      </aside>

      <main className="main">
        <h1>Logística IA Lab Suite</h1>
        <p>Plataforma empresarial para IA, documentación, RAG y automatización.</p>

        {page === "Dashboard" && (
          <>
            <div className="cards">
              <div className="card"><h3>Backend</h3><p>{status ? "Activo" : "Sin conexión"}</p></div>
              <div className="card"><h3>Proveedor IA</h3><p>{status?.ai_provider || "N/D"}</p></div>
              <div className="card"><h3>OpenAI</h3><p>{status?.openai_configured ? "Configurado" : "Pendiente"}</p></div>
              <div className="card"><h3>Claude</h3><p>{status?.claude_configured ? "Configurado" : "Pendiente"}</p></div>
            </div>
            <section className="panel"><h2>Módulos</h2><p>{status?.modules?.join(" · ")}</p></section>
          </>
        )}

        {page === "AI Studio" && (
          <section className="panel">
            <h2>AI Studio</h2>
            <input value={topic} onChange={e => setTopic(e.target.value)} />
            <button onClick={handleGenerate}>Generar contenido</button>
            <pre>{result}</pre>
          </section>
        )}

        {page === "Publisher" && (
          <section className="panel">
            <h2>Publisher</h2>
            <input value={chapterTitle} onChange={e => setChapterTitle(e.target.value)} />
            <button onClick={handleChapter}>Generar capítulo</button>
            <pre>{chapter}</pre>
          </section>
        )}

        {page === "Knowledge Hub" && (
          <section className="panel">
            <h2>Knowledge Hub</h2>
            <p>Próximo módulo: RAG, OCR, vector DB y búsqueda semántica.</p>
          </section>
        )}

        {page === "PEMEX Suite" && (
          <section className="panel">
            <h2>Motor Documental PEMEX</h2>
            <textarea value={oficioText} onChange={e => setOficioText(e.target.value)} />
            <div>
              <button onClick={handleAnalyzeOficio}>Analizar oficio</button>
              <button onClick={handleGenerateResponse}>Generar respuesta</button>
            </div>
            <h3>Análisis</h3>
            <pre>{analysis}</pre>
            <h3>Borrador</h3>
            <pre>{draft}</pre>
          </section>
        )}
      </main>
    </div>
  )
}

createRoot(document.getElementById('root')).render(<App />)
