
# Lecture 3: Transformers


<a id="orga6ffd6e"></a>

## The Transformer Architecture, Cont.

[The Transformer Architecture](#org9e8b2b7)
token->id->embedding->positional encoding


<a id="org2752201"></a>

### The attention mechanism

how does the context around a word change it's meaning?
Attention(Q,K,V) = softmax(QK<sup>T</sup>/sqrt(d<sub>k</sub>))V

-   Query - description of knowledge you want to gather
-   Key - a description of what each can teach
-   Value - the actual knowledge
-   d<sub>k</sub> is arbitrary

Attention measures how much Query and Key align
influence is value scaled by attention

X is the input - a sequence of embeddings
Ws are learned weight matrix
XW<sup>Q</sup>=Q

XW<sup>V</sup>=V

XW<sup>K</sup>=K

QK<sup>T</sup>=alignment

softmax(alignment/sqrt(d<sub>k</sub>)V = attention

1.  Masked Attention

    The above means a word can be influenced by words after it
    This makes sense linguistically, but breaks prediction (we want the next token to be conditional only on all previous tokens)
    
    To solve, add a mask that adds negative infinity attention for every token after the current
    Then the softmax makes all these future token weights 0

2.  Multi-Head Attention

    Use multiple attention matrices to learn different semantic properties of tokens
    
    Split Q into multiple smaller matrices that are d<sub>model</sub>/heads in width, instead of d<sub>model</sub>

3.  Cross attention

    bridge between encoder and decoder
    combine source language with target language in one shared space
    How well does the query of the decoder align with the key,value of the encoder, (softmax) then times value of the source


<a id="org4a61d69"></a>

### Add and Norm

normalization across embedding space
takes norm of sum of input + output of feed forward network
done because original input signal is lost overtime without
This is where mixture of expert magic happens

1.  Feed Forward

    mini MultiLayer Perceptron
    linear+ReLU+Linear


<a id="orgbe0c64a"></a>

### Linear+Softmax output

Projects output onto token dictionary
Softmax gives most likely tokens

-   uses temperature
    e<sup>x<sub>i</sub>/T</sup>/ &Sigma; e<sup>x<sub>j</sub>/T</sup>
