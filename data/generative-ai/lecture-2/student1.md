# Lecture 2 – Applied Generative AI

## Motivation
What are we doing right now?
- Sitting in a lecture
- Taking notes

Why take notes?
- Make information retrievable
- Transform lecture into a system that works for *me*
- Summarize and compress knowledge

---

## DIKW Pyramid

- **Data**  
  Raw symbols, no meaning on their own

- **Information**  
  Data placed into context

- **Knowledge**  
  Culturally understood information that enables insight

- **Wisdom**  
  Applying knowledge to make good decisions

Flow:
Data → Information → Knowledge → Wisdom

AI currently operates mostly at the **information** level  
Goal: use AI to help *create knowledge*

---

## AI Model Categories

### Frontier Models
- Most advanced models available
- Push the state of the art

### Foundation Models
- Broadly trained
- Adaptable via fine-tuning or prompting

### Openness Spectrum
- Closed-source (proprietary APIs)
- Open-weight (weights released, training hidden)
- Open-source (full transparency)

Observation:
- Open models lag frontier models by ~months, not years
- Gap is closing quickly

---

## Benchmarks
- **LM Arena**
  - Human preference-based evaluation
  - Chess ELO-style ranking

---

## Challenges & Open Problems

### Energy Use
- AI energy demand is rapidly increasing
- Some argue AI might solve climate issues instead of being constrained

### Data Limits
- LLMs depend on human-generated data
- Potential issues:
  - Running out of high-quality data
  - Training on AI-generated data causes degradation
- Possible direction: world models

---

## Terminology

### AI
Systems performing tasks that typically require human intelligence

### AGI
- Human-level general intelligence
- Can transfer knowledge across domains

### ASI
- Intelligence exceeding human capabilities

### Scaling Hypothesis
- Intelligence emerges from scale
- Bigger models + more data + more compute = smarter systems

---

## LLM Ecosystem Overview

### Deployment Options
1. AI-as-a-Service (OpenAI, Google, Anthropic)
2. Infrastructure-as-a-Service (AWS, RunPod)
3. Bare-Metal-as-a-Service (Hetzner, OVH)
4. Self-hosting / On-premise

---

## Interaction with LLMs

### Frameworks
- LangChain (general abstraction)
- LlamaIndex (RAG-focused)
- CrewAI (multi-agent systems)

### APIs
- Direct interaction via:
  - Python
  - TypeScript
  - cURL

### Key Parameters
- `temperature`: randomness vs determinism
- `max_tokens`: output/context limit

---

## Platforms
- HuggingFace: models, datasets, tooling
- OpenRouter: unified API for many models

---

## Group Project Overview

- Teams of 1–5
- Goal: GenAI project improving work with digital data

### Milestones
1. Project plan
2. Peer reviews
3. Mid-term interview
4. Prototype
5. Final submission

---

## Project Plan Requirements

Single PDF (≤ 2000 words)

Include:
- Users
- Data (self-collected or created)
- Problem definition
- Solution concept
- Interface
- Technical approach (1–3 core challenges)
- Evaluation metrics