# Lecture 1 – Generative AI Overview

## Prompting as Interaction
- LLMs don’t “know” context unless told
- Prompt = navigation through possibilities
- Better prompts = better outputs

---

## What Makes AI “Generative”?
- Generative models can create *new* data
- They learn the structure of the data itself

---

## Symbolic vs Subsymbolic AI

### Symbolic
- Logic statements (e.g. ∀x, ∃y)
- Explicit reasoning steps
- Brittle but interpretable

### Subsymbolic
- Learned representations
- Robust but harder to interpret
- Dominant in modern AI

---

## Discriminative vs Generative

| Type | Learns | Can Generate? |
|----|----|----|
| Discriminative | p(Y\|X) | ❌ |
| Generative | p(X), p(X,Y) | ✅ |

---

## Language as a Sequence Problem

- Text → tokens → IDs
- Model predicts next token probabilities
- Autoregressive generation

---

## Embeddings
- Words mapped to vectors
- Geometry = meaning
- Relationships preserved in vector space

Example:
- Germany - German + Austrian ≈ Austria

---

## Diffusion Models
- Start with real data
- Add noise gradually
- Learn to reverse noise
- Sampling = denoising from randomness

---

## Transformers

### Encoder
- Understands the input

### Decoder
- Generates output token by token

### Positional Encoding
- Necessary because transformers ignore order
