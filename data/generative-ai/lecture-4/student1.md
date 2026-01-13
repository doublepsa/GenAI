# Lecture 4 – Training Large Language Models & Applying LLM Capabilities

## Recap: Transformer Architecture

Transformers consist of:
- Tokenization → Embeddings → Positional Encoding
- Stacked attention + feed-forward blocks
- Linear + softmax output

Variants:
- Encoder-only (BERT, ViT)
- Decoder-only (GPT-style LLMs)
- Encoder–Decoder (Machine Translation)

Key advantages:
- Long-range dependency modeling
- Fully parallelizable training
- High versatility across tasks

---

## Training Large Language Models

### Three Phases
1. **Pre-training**
2. **Post-training**
3. **Inference**

---

## Pre-training (Base Model)

### Objective
Learn the true distribution of language:
p(x) = ∏ p(sᵢ | s₁, …, sᵢ₋₁)

yaml
Copy code

This is **next-token prediction**.

---

### Training Data
- Massive text corpora
- Example scale: LLaMA ~ 15 trillion tokens

---

### Input / Target Construction

Input:
- Sequence without last token

Target:
- Same sequence shifted by one token

Each target token is **one-hot encoded**.

---

### Model Output
- Probability distribution over vocabulary
- One distribution per token position

---

### Loss Function

Negative Log Likelihood (Cross-Entropy):
L = - Σᵢ log p(sᵢ | s₁, …, sᵢ₋₁)

yaml
Copy code

Purpose:
- Penalize incorrect predictions
- Encourage high probability on correct token

---

### Optimization
- Compute gradients ∇L(θ)
- Update parameters using optimizers:
  - SGD
  - AdamW

Batching:
- Multiple samples processed simultaneously

---

## Post-training (Alignment)

Base models:
- Can generate fluent text
- Cannot follow instructions reliably
- Are not aligned with human intent

### Post-training Methods
- Supervised Fine-Tuning (SFT)
- Instruction Tuning (IT)
- Preference Fine-Tuning
- RL with verifiable rewards (RLVR)

Goal:
- Make models helpful, safe, controllable

---

## Encoder-only Training (BERT)

### Masked Language Modeling
- 80% replace token with [MASK]
- 10% random token
- 10% unchanged token

Purpose:
- Learn contextual word representations

---

### Next Sentence Prediction
- Binary classification task
- Uses [CLS] token
- Learns sentence relationships

---

## Why Transformers Work So Well

1. Long-range dependencies
2. Parallel computation
3. General-purpose architecture

---

## Applying LLM Capabilities to Projects

### Foundation of LLM Behavior
- **Weights** → long-term memory
- **Context** → short-term memory (prompts, history, RAG)

Large contexts:
- Increase capacity
- Risk forgetting the middle

---

## Adapting Pre-trained Models

### Three Approaches
1. Prompting (In-context adaptation)
2. Retrieval-Augmented Generation (RAG)
3. Fine-tuning

---

## Prompting Strategies

- Zero-shot
- One-shot
- Few-shot

No parameters updated — only context changes.

---

## Fine-tuning
- Modifies model weights
- Good for:
  - Style
  - Formatting
- Bad for:
  - Adding new knowledge
  - Risk of catastrophic forgetting

---

## LLM Workflow Design

### Chains
- Break complex tasks into steps
- Example: summarize → extract → format

### Common Patterns
- Context & history handling
- Structured output (JSON/XML)
- Multi-step workflows
- Tool / function calling

---

## LLM Capabilities Overview

### Information Processing
- Transformation
- Extraction
- Summarization
- Classification

### Search & Retrieval
- Semantic search (embeddings)
- RAG pipelines

### Knowledge Generation
- Synthesis
- Reasoning
- Connection discovery

### Advanced Capabilities
- Agents
- Multi-modal reasoning
- Code generation
- Perspective shifting

---

## PKM (Personal Knowledge Management) Modes

1. Collect
2. Surface
3. Connect
4. Synthesize
5. Reflect

LLMs can support **all modes** when designed correctly.