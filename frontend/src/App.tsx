import { useState, useRef, useEffect, FormEvent } from "react";
import './App.css'

interface Message {
  role: "user" | "oreon";
  content: string;
}

const API_URL = "http://localhost:8000/chat/text";

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [isThinking, setIsThinking] = useState(false);

  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({
      top: scrollRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages, isThinking]);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const text = input.trim();
    if (!text || isThinking) return;

    setMessages((prev) => [...prev, { role: "user", content: text }]);
    setInput("");
    setIsThinking(true);

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      if (!res.ok) throw new Error(`Falha na resposta: ${res.status}`);

      const data = await res.json();
      setMessages((prev) => [...prev, { role: "oreon", content: data.reply }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "oreon",
          content: "Não consegui me conectar ao servidor. Verifique se o backend está rodando.",
        },
      ]);
    } finally {
      setIsThinking(false);
    }
  };

  return (
    <div className="flex h-screen w-screen flex-col bg-[#0B0D10] text-[#E4E4E4]">
      {/* Cabeçalho */}
      <header className="flex items-center justify-between border-b border-[#1F2329] px-6 py-4">
        <span className="text-sm font-medium tracking-wide">OREON</span>
        <span className="flex items-center gap-2 text-xs text-[#6B7280]">
          <span className="h-1.5 w-1.5 rounded-full bg-[#E8A33D]" />
          online
        </span>
      </header>

      {/* Área de chat */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto px-6 py-6">
        <div className="mx-auto flex max-w-2xl flex-col gap-4">
          {messages.length === 0 && (
            <p className="mt-16 text-center text-sm text-[#4B5158]">
              Envie uma mensagem para começar.
            </p>
          )}

          {messages.map((msg, i) =>
            msg.role === "user" ? (
              <div key={i} className="flex justify-end">
                <div className="max-w-[75%] rounded-lg border border-[#E8A33D]/40 bg-[#14171B] px-4 py-3 text-sm leading-relaxed text-[#E4E4E4]">
                  {msg.content}
                </div>
              </div>
            ) : (
              <div key={i} className="flex justify-start">
                <div className="max-w-[75%] rounded-lg bg-[#1B1F24] px-4 py-3 text-sm leading-relaxed text-[#E4E4E4]">
                  {msg.content}
                </div>
              </div>
            )
          )}

          {isThinking && (
            <div className="flex justify-start">
              <div className="flex items-center gap-2 rounded-lg bg-[#1B1F24] px-4 py-3 text-sm text-[#8A8F98]">
                <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-[#E8A33D]" />
                Pensando...
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Input fixo */}
      <form
        onSubmit={handleSubmit}
        className="border-t border-[#1F2329] bg-[#0B0D10] px-6 py-4"
      >
        <div className="mx-auto flex max-w-2xl items-center gap-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Fale com o OREON..."
            className="flex-1 rounded-lg border border-[#1F2329] bg-[#14171B] px-4 py-2.5 text-sm text-[#E4E4E4] placeholder:text-[#4B5158] focus:outline-none focus:ring-1 focus:ring-[#E8A33D]"
          />

          <button
            type="submit"
            disabled={!input.trim() || isThinking}
            className="shrink-0 rounded-lg bg-[#E8A33D] px-5 py-2.5 text-sm font-medium text-[#14171B] transition-opacity disabled:cursor-not-allowed disabled:opacity-40"
          >
            Enviar
          </button>
        </div>
      </form>
    </div>
  );
}

export default App;