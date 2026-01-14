# Lecture 4 – How LLMs Are Trained & Used

## Big Picture
LLMs:
- Learn language statistically
- Are trained first to *predict*
- Then trained again to *behave*

---

## How LLMs Learn Language

Training goal:
> Guess the next word as well as possible

Input:
"The cute green dragon trotted into the"

Target:
"cute green dragon trotted into the cave"

This happens for **every token**.

---

## Loss = Learning Signal
- Model guesses → compares to correct token
- Wrong guess = higher loss
- Optimizer nudges weights to improve

Repeat trillions of times.

---

## Base Models vs Aligned Models

Base models:
- Fluent
- Knowledgeable
- Not obedient

Post-training teaches:
- Following instructions
- Being helpful
- Avoiding harmful outputs

---

## BERT-style Training
- Hide words → predict them
- Learn meaning from context
- Great for understanding, not generation

---

## Why Transformers Won
- Can connect distant words instantly
- No sequential bottleneck
- Same architecture works everywhere

---

## Using LLMs in Practice

Two memories:
- Weights = what the model knows
- Context = what you tell it now

---

## Three Ways to Adapt a Model

### Prompting
- Show examples in the prompt
- Fast, cheap, flexible

### RAG
- Give the model documents
- Prevent hallucinations
- Best for new knowledge

### Fine-tuning
- Change the model itself
- Good for style
- Dangerous for facts

---

## Designing LLM Systems

Best systems:
- Break tasks into steps
- Keep structured outputs
- Manage memory explicitly
- Call tools when needed

---

## What LLMs Are Good At
- Summarizing
- Extracting
- Searching semantically
- Synthesizing ideas
- Reasoning step-by-step
- Acting as agents

---

## PKM Perspective
LLMs can:
- Collect information
- Surface it when needed
- Connect ideas
- Synthesize insights
- Help reflect on thinking

They are **thinking amplifiers**, not thinkers.
