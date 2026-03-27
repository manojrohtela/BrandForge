# BrandForge — Startup Branding Agent

Describe your startup and get a complete brand identity: name options, taglines, color palette, mission statement, value propositions, social bio, and elevator pitch. Refine with natural language feedback.

## Features
- 3 brand name options with domain hints and rationale
- 3 tagline options
- Full color palette (primary, secondary, accent, background, text) with hex codes
- Brand voice and mission statement
- Value propositions
- Font recommendations
- 150-char social media bio
- Elevator pitch
- Refinement chat for iterating on specific sections

## Stack
- **Frontend**: React 18, Vite, Tailwind CSS v4, Framer Motion
- **Backend**: FastAPI, Groq SDK

## Local Development

### Backend
```bash
cd backend && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend && npm install
echo "VITE_API_BASE_URL=http://localhost:8000" > .env
npm run dev
```
