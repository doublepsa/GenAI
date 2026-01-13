# Lecture 1: Intro to GenAI

## Prompting
- Prompt = control mechanism
- Missing info → implicit assumptions
- Ask:
  - Why did you choose this?
  - What should I change?

---

## AI Categories

### Symbolic AI
- Rules + logic
- Human-readable
- Expert systems, search

### Subsymbolic AI
- Data-driven
- Neural networks, statistics

---

## Model Types

### Discriminative
- p(Y|X)
- Learns decision boundary

### Generative
- p(X) or p(X,Y)
- Can synthesize new data

---

## Sequence Models

- Tokens = smallest language units
- Vocabulary size = V
- Sequence probability:

p(s1) · p(s2|s1) · ... · p(sk|s1..s(k-1))


### Loss
- Negative log-likelihood
- Sum over token positions

---

## Embeddings
- Map tokens → vectors
- Capture semantic similarity
- Used for text, images, audio

---

## Diffusion Models
- Forward: add Gaussian noise
- Backward: denoise step-by-step
- Learn p(X) through denoising

---

## Transformers

### Encoder
- Contextual understanding

### Decoder
- Autoregressive generation

### Positional Encoding
- Adds sequence order info
- Uses sin/cos functions
