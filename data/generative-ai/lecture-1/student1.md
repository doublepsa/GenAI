# Lecture 1 – Introduction to Generative AI

## Prompting Basics
- Prompting is collaborative: user + LLM
- What you include explicitly shapes the output
- What you omit becomes an implicit assumption

### Quick Prompting Tips
- Ask the model to explain *its reasoning*
- Ask about implicit decisions
- Provide:
  - Your mental model
  - Constraints
  - What you already tried

---

## What is Generative AI?

Generative AI refers to models that **learn the data distribution** and can **generate new samples** similar to the training data.

---

## Symbolic vs Subsymbolic AI

### Symbolic AI
- Uses human-readable symbols and explicit rules
- Logic-based reasoning
- Examples:
  - Expert systems
  - Search & planning
  - Knowledge representation

### Subsymbolic AI
- Learns patterns from data using mathematics
- No explicit rules
- Examples:
  - Statistical methods
  - Neural networks
  - Ensemble models

---

## Discriminative vs Generative Models

### Discriminative Models
- Learn: `p(Y | X)`
- Focus on decision boundaries
- Used for classification and prediction

### Generative Models
- Learn: `p(X)` or `p(X, Y)`
- Capture the full data distribution
- Can generate new data samples

---

## Sequence Modeling

### Tokens
- Text is split into atomic units (tokens)
- Tokens are mapped to token IDs

### Language Modeling Goal
- Learn the true distribution of language `p(X)`
- Probability of a sequence:
p(x) = ∏ p(s_i | s_1 ... s_{i-1})

### Training Objective
- Minimize negative log-likelihood
- Cross-entropy loss over tokens

---

## Embeddings
- Token IDs → dense vectors
- Capture semantic meaning
- Similar meanings → closer vectors
- Enable vector arithmetic:
- King - Man + Woman ≈ Queen

---

## Diffusion Models

- Learn data distribution via **stochastic denoising**
- Forward process: add noise gradually
- Backward process: remove noise step-by-step
- Allows sampling from noise to data

---

## Transformer Architecture

### Encoder
- Builds contextual representations
- Used for understanding tasks

### Decoder
- Autoregressive generation
- Predicts next token

### Positional Encoding
- Injects order information
- Uses sine and cosine functions