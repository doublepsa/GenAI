# Lecture 1: Introduction to GenAI


<a id="org126c077"></a>

## Quick prompting tips

1.  Ask the llm to explain
    What implicit decisions were made, etc.
2.  Provide more context
    llm knows nothing - need to tell it
    add mental model/persective/assumptions


<a id="orgc97bc86"></a>

## What is GenAI


<a id="org6cfe234"></a>

### Symbolic AI

Aim to capture world in human-understandable symbols, give rules for manipulating the symbols
Logical models

-   Expert Systems
-   Search
-   knowledge representation


<a id="org5a698d3"></a>

### Subsymbolic AI

Is provided data, and uses math to define actions over the data

-   Statistical methods
-   Ensemble Techniques
-   Neural Nets

1.  Discriminative models

    p(Y|X)
    Y given features X - only need to know conditional probability

2.  Generative Models

    p(X,Y) or p(X) - X and Y, need to know the joint probability - captures more cases
    needs to know the whole dataset, not just one section
    
    1.  Sequence Modeling
    
        Discretize atomic - assign IDs
        Language Models strive to capture the true distribution of language
        V vocab
        n max sequence length
        X space of all possible token sequences
        p(x)=p(s\_1)p(s\_2|s\_1)p(s\_3|s\_2, s\_1)&#x2026;
        V\_1 is the random variable for a token at pos i
        p(V\_i|s\_1,&#x2026;, s\_i\_-1) is probability distribution over all possible tokens that will come next
        y\_i is the one-hot ground truth vector for the correct token
        L=-&Sigma;<sub>i</sub>y<sub>i</sub>log(p(V\_i|s<sub>1</sub>,&#x2026;,s\_i\_-1))=-&Sigma;<sub>i</sub>log(p(s\_i|s<sub>1</sub>,&#x2026;,s\_i\_-1))
        
        1.  Embeddings
        
            token -> token id -> higher dimension vector space
            Each dimension captures a subset of meaning of a word
            Allows us to do arithmetic on words
            Words with similar meaning are close together
            We can also capture the relations between words
            We can even perform translations. (King - Man + Woman ~= Queen)
            We can make anything into an embedding - text, image, audio
        
        2.  Diffusion
        
            Stochastic Denoising
            Diffusion is the gradual transformation that adds random noise to data until it is pure noise (forward diffusion)
            We can train a model to predict the noise added, and then go backwards, subtracting noise to gain a clearer image (backwards diffusion)
            Create normal distribution that centers around \sqrt{1-\beta_t}x\_t with variance &beta;<sub>t</sub>I
            can directly sample from x\_0 to any timestep t


<a id="org9e8b2b7"></a>

## The Transformer Architecture

[The Transformer Architecture, Cont.](#orga6ffd6e)


<a id="org4e0f7bb"></a>

### Encoder

Captures semantic meaning of sequence
can be used without a decoder to classify
Input, many encoder blocks, outputs embedding


<a id="orgc7a7928"></a>

### Decoder

Predicts next token
Can be used without an encoder autoregressively to generate
Input from Encoder, many decoder blocks, output probabilities


<a id="orgb645ef1"></a>

### Positional Encoding

Use sin/cos to to give a number to each position, give each embedding a unique number for each position


<a id="org23f4d28"></a>
