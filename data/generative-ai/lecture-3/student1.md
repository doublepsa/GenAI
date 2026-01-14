# Lecture 3 – Transformers

## Transformer Architecture (Overview)

Pipeline:
token → token ID → embedding → positional encoding → transformer blocks


Transformers replace recurrence with **attention**, allowing parallel processing of sequences.

---

## The Attention Mechanism

Goal:
- Capture how context changes the meaning of a token
- Let tokens influence each other based on relevance

### Scaled Dot-Product Attention

Formula:
Attention(Q, K, V) = softmax(QKᵀ / √d_k) V


Components:
- **Query (Q)**: what information a token is looking for
- **Key (K)**: what information a token offers
- **Value (V)**: the actual content passed on
- **d_k**: key dimension (used for scaling)

Interpretation:
- Q · Kᵀ → alignment score
- softmax → attention weights
- weights × V → contextualized representation

---

## From Input to Q, K, V

Given input sequence embeddings `X`:
Q = XW_Q
K = XW_K
V = XW_V


Where `W_Q`, `W_K`, `W_V` are learned matrices.

---

## Masked Attention

Problem:
- Standard attention allows a token to attend to *future* tokens
- This breaks autoregressive generation

Solution:
- Apply a **causal mask**
- Future token scores → −∞
- Softmax → probability 0 for future tokens

Effect:
- Token at position *i* only attends to positions `< i`

---

## Multi-Head Attention

Idea:
- Attend to different semantic relationships in parallel

Mechanism:
- Split Q, K, V into `h` smaller heads
- Each head attends independently
- Results concatenated and projected

Formula:
MultiHead(Q,K,V) = Concat(head₁,...,headₕ) W_O

Benefit:
- Different heads learn different patterns
  - syntax
  - semantics
  - long-range dependencies

---

## Cross Attention

Purpose:
- Connect encoder and decoder

Mechanism:
- Query from decoder
- Key & Value from encoder output

Use case:
- Machine translation
- Decoder queries source sentence representations

---

## Add & Norm

Structure:
output = LayerNorm(x + Sublayer(x))

yaml
Copy code

Why:
- Prevent signal degradation
- Stabilize training
- Preserve original input information

---

## Feed Forward Network

- Position-wise MLP
- Same network applied to every token

Structure:
Linear → ReLU → Linear

yaml
Copy code

Acts as:
- Nonlinear feature transformation

---

## Output Layer (Linear + Softmax)

- Project final embeddings to vocabulary size
- Softmax converts logits to probabilities

Temperature scaling:
softmax(x_i / T)

yaml
Copy code

- Low T → more deterministic
- High T → more diverse outputs

---

## Transformer Variants

- **Encoder-only**: BERT, ViT
- **Decoder-only**: GPT-style LLMs
- **Encoder–Decoder**: Translation models

---

## Key Takeaway

Transformers:
- Replace recurrence with attention
- Scale efficiently
- Form backbone of modern LLMs