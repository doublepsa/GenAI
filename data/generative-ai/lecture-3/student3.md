# Lecture 3 – Transformers

## Big Picture
Transformers understand language by letting words
**pay attention to each other** instead of reading sequentially.

---

## From Words to Meaning
1. Text → tokens
2. Tokens → embeddings
3. Add position info
4. Let tokens interact via attention

---

## What Is Attention?
Question:
> How does “dragon” change meaning in different contexts?

Answer:
- By looking at surrounding words
- Attention assigns importance weights

---

## Query, Key, Value (Human Analogy)

- Query: what I want to learn
- Key: what others can teach
- Value: what they actually know

If my query matches your key → I listen more to your value

---

## The Attention Formula (Intuition)
- Dot product → similarity
- Softmax → normalized importance
- Multiply by values → new meaning

Scaling by √dₖ keeps training stable

---

## Masked Attention
- During text generation:
  - You can’t peek at future words
- Mask blocks future tokens
- Ensures proper next-token prediction

---

## Multi-Head Attention
Why multiple heads?
- One head focuses on grammar
- Another on meaning
- Another on long-distance dependencies

Parallel perspectives → richer understanding

---

## Cross Attention
- Used when translating
- Decoder looks back at encoded source sentence
- Aligns target words with source words

---

## Add & Norm (Why It Matters)
- Residuals keep original info alive
- Layer norm keeps values stable
- Makes deep models trainable

---

## Feed Forward Layers
- Small neural network per token
- Adds non-linearity
- Same operation for every position

---

## Output & Generation
- Final vector → vocabulary
- Softmax gives probabilities
- Temperature controls creativity

---

## Transformer Families
- BERT: understands text
- GPT: generates text
- Encoder–Decoder: transforms text

---

## Key Insight
Attention is the mechanism that gives
transformers *contextual understanding*