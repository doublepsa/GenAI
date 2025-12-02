
# Lecture 2: Applied GenAI


<a id="org04f8d51"></a>

## Motivation

What are you doing right now?

-   Sitting in Lecture
-   Taking notes
    -   Why? To make this info retrievable
    -   To render the lecture into a system good for me
    -   To summarize the lecture


<a id="org0a9add3"></a>

## DIKW Pyramid

            Wisdom - Utilization of accumulated knowledge to make informed choices
        Knowledge - Information that has been culturally understood so that it provides insight and understanding
    Information - set of data that are linked/related within a context to be made useful
Data - discrete, objective facts. Symbols with no inherent meaning

nothing -> what -> how or why is -> why do or what is best
=
collecting -> connecting -> forming whole -> joining wholes

AI is at the top of information - we want it to create knowledge


<a id="orga209e31"></a>

## Model categories


<a id="org2040acc"></a>

### Frontier Model

Most advanced and powerful models


<a id="orgcf79f08"></a>

### Foundational Model

broadly trained model good for fine-tuning


<a id="org4d243ae"></a>

### Openness

-   closed source - proprietary
-   open-weight - weights and inference are released publicly
-   open-source models - everything is open

Open models even early are only lagging by 7 months
and they are catching up


<a id="org129cb06"></a>

### Benchmarks

lmarena - scores based on chess elo


<a id="org5baa439"></a>

## Problems


<a id="orgc34f8bf"></a>

### Energy Use

officials say don't worry about climate change, hope AI will fix everything


<a id="orgdb23c7c"></a>

### Will we run out of data

LLM scaling limited by amount of human-generated data
some discussed solutions like finding more data (either ai generated - problems, or otherwise - world models?)


<a id="org5b909e2"></a>

## Terms


<a id="org6e4fa25"></a>

### AI

System designed to do tasks that typically require human intelligence


<a id="org15d1ad2"></a>

### AGI - Artificial General Intelligence

System will general intelligence, learning, knowledge equal to humans - can perform a wide variety of tasks


<a id="org688954b"></a>

### ASI - Artificial Superintelligence

System with intelligence greater than humans


<a id="org2074e33"></a>

### Scaling Hypothesis

The secret of AGI is simply one of scale. Our current models are the 'right path', we just need to make them bigger/more data


<a id="org86f0959"></a>

## LLM


<a id="orgb815943"></a>

## Ecosystem


<a id="org9deab43"></a>

### Deployment

1.  AI-as-a-service
    openAI, google, anthropic
2.  Infrastructure-as-a-survice
    AWS, Runpod, Paperspace
3.  Bare-metal-as-a-service
    Hetzner, OVHcloud
4.  Self-hosting or On-premise
    Server setups in own rackspace/local computer


<a id="org39af42c"></a>

### Interaction

1.  Framework
    abstractions, etc.
    langchain, llamaindex (good for RAG), crewAI (best for multi-agent-sytems)
2.  APIs
    curl, python, or typescript - these really are the only way people interact with ai currently

1.  Parameters

    -   temperature - controls randomness, lower is more deterministic, hight has more creativity/variance
    -   max\_tokens limits context length


<a id="org76d7ebb"></a>

### Platforms

1.  HuggingFace

    hosts lots of free/open-weight models

2.  OpenRouter

    single place to find open models


<a id="orge22ce09"></a>

## Group Details

1-5 people groups
create a gen-ai project that makes working with digital data better

1.  Create project plan: domain, challenges, concept
2.  Review other group's plan
3.  Mid-term interview
4.  Build Prototype
5.  Submit code and report


<a id="org2e5460e"></a>

### Project Plan

single pdf with 2000 word max

1.  Structure

    -   Users
    -   Data (see TUWEL)
        you are responsible for obtaining or creating your own dataset
    -   The Problem
        Examples: retrieval, synthesis, stale knowledge
    -   Solution
        -   Concept
        -   Interface
        -   Technical Approach (see TUWEL)
            How it will work, include the 1-3 core technical challenges
    -   Evaluation
        measurable definition of success (don't go overboard)


<a id="orgffae94d"></a>

### Group Reviews

you will get 4 other project plans, you will earn up to 1.25p per review


<a id="orgeaafb97"></a>

### Mid-Term Interview

15min time slot
discuss proposal and peer reviews
NOT a test, but an opportunity to clarify project
No submission for interview (besides project plan)


<a id="org8c9b1a8"></a>

### Final Hand-in

Single zip containing

-   code necessary to run app
    if setup is complex, provide link to hosted version
-   technical report
    structure TBA
-   Screencast explaining application in case technical report is not sufficient to understand app
    optional
