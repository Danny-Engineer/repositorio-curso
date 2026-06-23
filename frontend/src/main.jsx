import React,{useEffect,useState}from'react'
import{createRoot}from'react-dom/client'
import{getSystemStatus,getSystemMetrics,getAIProviders,testAIProvider,generateAI,createChapter,analyzePemexDocument,generatePemexResponse}from'./services/api'
import'./styles/app.css'

function StatusPill({value}){const cls=value==="active"||value===true?"pill ok":value==="pending"||value===false?"pill warn":"pill";return <span className={cls}>{String(value)}</span>}

function App(){
 const[page,setPage]=useState("Dashboard"),[status,setStatus]=useState(null),[metrics,setMetrics]=useState(null),[providers,setProviders]=useState(null)
 const[provider,setProvider]=useState("local"),[model,setModel]=useState("local-simulated")
 const[topic,setTopic]=useState("IA aplicada a Recursos Humanos"),[audience,setAudience]=useState("RH y Calidad"),[tone,setTone]=useState("profesional"),[context,setContext]=useState(""),[result,setResult]=useState(""),[testResult,setTestResult]=useState("")
 const[chapterTitle,setChapterTitle]=useState("La revolución de la inteligencia artificial"),[chapter,setChapter]=useState("")
 const[oficioText,setOficioText]=useState("Se solicita remitir evidencia documental relacionada con el procedimiento de calidad y atención de auditoría."),[analysis,setAnalysis]=useState(""),[draft,setDraft]=useState("")
 useEffect(()=>{getSystemStatus().then(setStatus).catch(()=>setStatus(null));getSystemMetrics().then(setMetrics).catch(()=>setMetrics(null));getAIProviders().then(d=>{setProviders(d);setProvider(d.default_provider||"local")}).catch(()=>setProviders(null))},[])
 const selectedProvider=providers?.providers?.find(p=>p.id===provider)
 async function refreshMetrics(){setMetrics(await getSystemMetrics())}
 async function handleTestProvider(){const d=await testAIProvider({provider,model});setTestResult(JSON.stringify(d,null,2))}
 async function handleGenerate(){const d=await generateAI({topic,audience,tone,context,provider,model});setResult(d.content)}
 async function handleChapter(){const d=await createChapter({title:chapterTitle,summary:"Capítulo generado desde API Publisher."});setChapter(d.markdown)}
 async function handleAnalyzeOficio(){const d=await analyzePemexDocument({raw_text:oficioText,area:"Servicios Logísticos",document_type:"Oficio"});setAnalysis(JSON.stringify(d,null,2))}
 async function handleGenerateResponse(){const d=await generatePemexResponse({raw_text:oficioText,instruction:"Elabora respuesta institucional.",signer:"Daniel Melchor Pérez",tone:"institucional PEMEX"});setDraft(d.draft_markdown)}
 return <div className="app"><aside className="sidebar"><h2>Logística IA Lab</h2>{["Dashboard","Publisher","AI Studio","Knowledge Hub","PEMEX Suite"].map(i=><button key={i} onClick={()=>setPage(i)} className={page===i?"active":""}>{i}</button>)}</aside><main className="main"><h1>Logística IA Lab Suite</h1><p>Plataforma empresarial para IA, documentación, RAG y automatización.</p>
 {page==="Dashboard"&&<><div className="cards"><div className="card"><h3>Backend</h3><StatusPill value={status?"active":"offline"}/></div><div className="card"><h3>Proveedor IA</h3><p>{status?.ai_provider||"N/D"}</p></div><div className="card"><h3>OpenAI</h3><StatusPill value={status?.openai_configured||false}/></div><div className="card"><h3>Claude</h3><StatusPill value={status?.claude_configured||false}/></div></div><section className="panel"><h2>Recursos</h2><button onClick={refreshMetrics}>Actualizar métricas</button><div className="cards small"><div className="card"><h3>CPU</h3><p>{metrics?.resources?.cpu_percent??"N/D"}%</p></div><div className="card"><h3>RAM</h3><p>{metrics?.resources?.memory_percent??"N/D"}%</p></div><div className="card"><h3>Disco</h3><p>{metrics?.resources?.disk_percent??"N/D"}%</p></div><div className="card"><h3>Libre</h3><p>{metrics?.resources?.disk_free_gb??"N/D"} GB</p></div></div></section></>}
 {page==="AI Studio"&&<section className="panel"><h2>AI Studio</h2><div className="form-grid"><label>Proveedor<select value={provider} onChange={e=>{setProvider(e.target.value);setModel("")}}>{providers?.providers?.map(p=><option key={p.id} value={p.id}>{p.name} {p.configured?"✓":"⚠"}</option>)}</select></label><label>Modelo<select value={model} onChange={e=>setModel(e.target.value)}>{(selectedProvider?.models||["local-simulated"]).map(m=><option key={m} value={m}>{m}</option>)}</select></label><label>Tono<input value={tone} onChange={e=>setTone(e.target.value)}/></label><label>Audiencia<input value={audience} onChange={e=>setAudience(e.target.value)}/></label></div><input value={topic} onChange={e=>setTopic(e.target.value)} placeholder="Tema"/><textarea value={context} onChange={e=>setContext(e.target.value)} placeholder="Contexto opcional"/><button onClick={handleTestProvider}>Probar proveedor</button><button onClick={handleGenerate}>Generar contenido</button><h3>Prueba</h3><pre>{testResult}</pre><h3>Resultado</h3><pre>{result}</pre></section>}
 {page==="Publisher"&&<section className="panel"><h2>Publisher</h2><input value={chapterTitle} onChange={e=>setChapterTitle(e.target.value)}/><button onClick={handleChapter}>Generar capítulo</button><pre>{chapter}</pre></section>}
 {page==="Knowledge Hub"&&<section className="panel"><h2>Knowledge Hub</h2><p>Próximo módulo: RAG, OCR, vector DB y búsqueda semántica.</p></section>}
 {page==="PEMEX Suite"&&<section className="panel"><h2>Motor Documental PEMEX</h2><textarea value={oficioText} onChange={e=>setOficioText(e.target.value)}/><button onClick={handleAnalyzeOficio}>Analizar oficio</button><button onClick={handleGenerateResponse}>Generar respuesta</button><h3>Análisis</h3><pre>{analysis}</pre><h3>Borrador</h3><pre>{draft}</pre></section>}
 </main></div>
}
createRoot(document.getElementById('root')).render(<App/>)
