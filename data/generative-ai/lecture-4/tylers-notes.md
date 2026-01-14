
# Lecture 4: Transformers II

start with pure randomness
pre-train to get base model
post-train to get final model
then training is done, and you can start inference

## Decoder-only models

### Pretraining

start with a model that has randomly initialized weights
method is self-supervised training
has ground truth, but it is not labeled (because the data is the label)
end result is base (or pretrained) model. Able to generate syntactic and semantically meaningful text, recall knowledge
but has no external values

1.  Details

    Input is sequence without last token
    Target is sequence shifted right by one token
    output is probability distributions of each next token, given previous (set) tokens
    one-hot encode the target data
    Then can define a loss function as the negative log-likelihood of the correct tokens across all positions given previous tokens
    Then we can use an optimizer (like stochastic gradient descent) to adapt weights based on gradient of the loss function

2.  Batching

    Push multiple sequences to the model at once (list of matrices, or tensor)

### Posttraining

Supervided finetuning, preference finetuning, reinforcement learning with verifiable results

## Encoder-only models

Act of training (optimizer) stays the same, but input and out are different
Input is still token sequence (with special tokens)
Gets turned into embeddings
But has more layers, token, segment and positional embeddings (all learned)

### Masked Token Prediction

Instead of predicting next token, mask a random token from sequence, and predict that
80% replace with special mask token
10% replace with random token
10% unchanged
This avoids putting emphasis on a special token and does not bias the model to the specific task

### Next sentence prediction

binary classifier, does one sentence come after the next
Splits the sentences by a special [SEP] token

### There are many more types of training

-   Sentence pair classification
-   single sentence classification
-   question answering
-   single token tagging

## What is so special about the Transformer

Amazing at long-range dependencies in sequences - can accurately judge how first token impacts last, even for very long sequences
Fully parallelizable training paradigm - much more rich impact from each input
Versatility - can implement almost any modality - text, audio, 
