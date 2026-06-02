# 🤖 OREON — Your Personal AI Assistant

> An intelligent desktop assistant with voice, computer vision, automation, and financial integration. Built from scratch by a 16-year-old developer.

---

## 🧠 What is OREON?

OREON is a personal desktop assistant that combines multiple AI models to deliver a complete automation experience. It listens to your voice, sees your screen, controls your computer, analyzes the crypto market, and much more — all running locally on your PC.

---

## ⚡ Features

### v1 — Core
- 💬 Real-time text and voice chat
- 🧠 Persistent memory (remembers you across sessions)
- 👨‍💻 Coding assistant — writes, explains, and debugs code

### v2 — PC Control
- 🖥️ Computer vision — analyzes your screen in real time
- 📂 Opens, closes, and organizes programs and files
- 📊 Monitors CPU, RAM, and temperature

### v3 — Integrations
- 🎵 Voice-controlled Spotify
- 📈 Binance API — real-time prices and AI-powered market prediction
- 🔔 Custom crypto alerts

### v4 — Polish
- 🌅 Daily briefing on PC startup
- 🎯 Focus mode — blocks distractions
- 🔗 GitHub integration
- 🎮 Streamer mode (OBS)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Interface | Tauri + React + TypeScript |
| Backend | Python |
| Main AI | Groq API |
| Computer Vision | Google Gemini |
| Speech Recognition | Whisper |
| Voice Synthesis | ElevenLabs |
| Local Model (optional) | Ollama |
| Crypto | Binance API |

---

## 🗂️ Project Structure

```
oreon/
├── frontend/          # Tauri + React interface
│   ├── src/
│   │   ├── components/
│   │   └── App.tsx
├── backend/           # Python
│   ├── core/          # Main AI logic
│   ├── memory/        # Persistent memory system
│   ├── voice/         # Voice input and output
│   ├── vision/        # Computer vision
│   ├── integrations/  # Spotify, Binance, GitHub
│   └── main.py
├── memory/            # Local memory files
└── README.md
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/Thiagofeje54/oreon.git
cd oreon

# Backend
pip install -r requirements.txt
python backend/main.py

# Frontend (another terminal)
cd frontend
npm install
npm run tauri dev
```

---

## 🔑 Environment Variables

Create a `.env` file at the root:

```env
GROQ_API_KEY=your_key
GEMINI_API_KEY=your_key
ELEVENLABS_API_KEY=your_key
BINANCE_API_KEY=your_key
BINANCE_SECRET_KEY=your_key
```

---

## 🗺️ Roadmap

- [x] Planning and architecture
- [ ] v1 — Chat + voice + memory
- [ ] v2 — Vision + PC control
- [ ] v3 — Spotify + Binance
- [ ] v4 — Final polish

---

## 👤 Author

**Thiago — DevFeijó**
Full-Stack + AI Developer | 16 y/o | São Paulo, Brazil

[![LinkedIn](https://img.shields.io/badge/LinkedIn-DevFeijó-blue)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-Thiagofeje54-black)](https://github.com/Thiagofeje54)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
