# Lecture 3: Transformers

## Core Idea
- Tokens attend to each other
- Context replaces recurrence

Pipeline:
token → embedding → positional encoding → attention

---

## Attention Formula
Attention(Q,K,V) = softmax(QKᵀ / √d_k) V

yaml
Copy code

- Q: what I want
- K: what I offer
- V: information content

---

## Q, K, V
- Computed via linear projections
- Learned parameters

---

## Masked Attention
- Prevents access to future tokens
- Required for autoregressive decoding

---

## Multi-Head Attention
- Multiple attention heads in parallel
- Each head learns different relationships
- Outputs concatenated

---

## Cross Attention
- Decoder queries encoder outputs
- Used in translation & seq2seq tasks

---

## Add & Norm
- Residual connection + layer norm
- Prevents vanishing signal

---

## Feed Forward Network
- Token-wise MLP
- Linear → ReLU → Linear

---

## Output Softmax
- Maps embeddings → vocab probabilities
- Temperature controls randomness

---

## Transformer Types
- Encoder-only: BERT
- Decoder-only: GPT
- Encoder–Decoder: Translation models
