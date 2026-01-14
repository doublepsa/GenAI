# Lecture 4: Training LLMs & Applications

## Transformer Recap
- Encoder-only, Decoder-only, Encoder–Decoder
- Attention enables long-range dependencies
- Fully parallelizable

---

## LLM Training Pipeline
1. Pre-training
2. Post-training
3. Inference

---

## Pre-training
- Task: next-token prediction
- Input: sequence without last token
- Target: sequence shifted by one
- Output: vocab probability distribution

Loss:
- Cross-entropy / negative log likelihood

---

## Optimization
- Gradient descent (SGD, AdamW)
- Batch training

---

## Post-training
- Align model with human intent
- Methods:
  - SFT / Instruction tuning
  - Preference tuning
  - RL-based methods

---

## Encoder-only Models (BERT)
- Masked Language Modeling
- Next Sentence Prediction

---

## Why Transformers?
- Long-range context
- Parallel training
- Versatility

---

## LLM Behavior
- Weights = long-term memory
- Context = short-term memory

---

## Adapting Models
- Prompting (zero / one / few-shot)
- RAG (external knowledge)
- Fine-tuning (task specialization)

---

## Workflow Patterns
- Chains
- Structured outputs
- Tool calling
- Memory management

---

## LLM Capabilities
- Transform, extract, summarize
- Semantic search
- RAG
- Reasoning
- Agents
- Multi-modal models

---

## PKM Model
Collect → Surface → Connect → Synthesize → Reflect
