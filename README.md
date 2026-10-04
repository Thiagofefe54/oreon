# OREON

Protótipo de assistente de desktop com inteligência artificial.

![Status](https://img.shields.io/badge/status-n%C3%A3o%20finalizado-orange?style=flat-square)

**Tecnologias:** React · TypeScript · Tauri · Python · FastAPI · Groq

## Proposta e estado atual

A proposta é evoluir para um assistente com conversa, voz, memória e automações. **O projeto ainda não está finalizado.** Hoje há chat por texto, integração Groq e histórico local em JSON. Voz, visão, controle do computador e integrações externas são planos futuros. O endpoint de voz ainda não implementa reconhecimento de áudio.

## Estrutura

- `frontend/`: interface React e estrutura do aplicativo Tauri.
- `backend/main.py`: API de chat.
- `backend/core/`: cliente de IA.
- `backend/memory/`: histórico da conversa.
- `backend/voice/`: espaço reservado para voz.

## Backend

Use Python 3.10 ou superior.

```sh
git clone https://github.com/Thiagofefe54/oreon.git
cd oreon
python -m venv .venv
```

Ative o ambiente: no PowerShell use `.\.venv\Scripts\Activate.ps1`; no Linux/macOS, `source .venv/bin/activate`.

```sh
pip install -r backend/requirements.txt
```

Copie `.env.example` para `.env` na raiz e preencha `GROQ_API_KEY`. Depois, a partir da raiz:

```sh
python backend/main.py
```

A API local fica em http://localhost:8000 e sua documentação em http://localhost:8000/docs. O processamento de IA depende da API externa Groq.

## Interface

Em outro terminal, use Node.js compatível com Vite 8 (20.19+ ou 22.12+) e npm:

```sh
cd frontend
npm ci
npm run dev
```

O endereço de desenvolvimento é http://localhost:1420. Para desktop, instale também os pré-requisitos de Rust/Tauri da sua plataforma e execute `npm run tauri dev`. A interface não inicia o backend automaticamente.

## Memória e limitações

O histórico é salvo em `backend/memory/memory.json` e não deve ser publicado. É compartilhado pelo processo local; ainda falta isolamento de usuários e controle de concorrência. A API não implementa autenticação.

## Próximos passos

- [ ] Implementar voz e resposta em áudio.
- [ ] Melhorar recuperação de falhas e indicação de conexão.
- [ ] Proteger e organizar a memória.
- [ ] Integrar inicialização do backend ao aplicativo desktop.
- [ ] Implementar visão, automações e demais integrações planejadas.
- [ ] Validar instalação e empacotamento em cada plataforma.

---

Projeto de [Thiago Feijó](https://github.com/Thiagofefe54).
