import { useState, useEffect, useRef } from "react";
import "./App.css";

type Message = {
  role: "user" | "oreon";
  text: string;
  time: string;
};

function App() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "oreon",
      text: "Sistema online. Olá, Thiago. Como posso ajudar?",
      time: new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" }),
    },
  ]);
  const [input, setInput] = useState("");
  const [listening, setListening] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

    async function sendMessage() {
    if (!input.trim()) return;
    const time = new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" });
    const texto = input;
    setMessages((prev) => [...prev, { role: "user", text: texto, time }]);
    setInput("");

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto }),
      });
      const data = await res.json();
      setMessages((prev) => [...prev, { role: "oreon", text: data.resposta, time }]);
    } catch {
      setMessages((prev) => [...prev, { role: "oreon", text: "Erro ao conectar com o backend.", time }]);
    }
    }

  return (
    <div className="app">
      <div className="sidebar">
        <div className="logo">
          <span className="logo-text">OREON</span>
          <span className="logo-badge">AI</span>
        </div>
        <nav className="nav">
          <button className="nav-item active">💬 Chat</button>
          <button className="nav-item">🖥️ Sistema</button>
          <button className="nav-item">📈 Binance</button>
          <button className="nav-item">🎵 Spotify</button>
          <button className="nav-item">⚙️ Config</button>
        </nav>
        <div className="status">
          <span className="dot-green" /> Online
        </div>
      </div>

      <div className="main">
        <div className="topbar">
          <span className="topbar-title">Assistente Pessoal</span>
          <span className="topbar-model">Groq · Llama 3</span>
        </div>

        <div className="messages">
          {messages.map((msg, i) => (
            <div key={i} className={`message ${msg.role}`}>
              <div className="bubble">
                {msg.role === "oreon" && <span className="sender">OREON</span>}
                <p>{msg.text}</p>
                <span className="time">{msg.time}</span>
              </div>
            </div>
          ))}
          <div ref={bottomRef} />
        </div>

        <div className="inputbar">
          <button
            className={`mic-btn ${listening ? "active" : ""}`}
            onClick={() => setListening(!listening)}
          >
            🎙️
          </button>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder="Digite ou fale algo..."
          />
          <button className="send-btn" onClick={sendMessage}>
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;