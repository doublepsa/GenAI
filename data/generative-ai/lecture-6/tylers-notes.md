
# Lecture 6: GPT II


<a id="org2be6a9f"></a>

## How to convert rankings to reward


<a id="org436421c"></a>

### Direct Assignment of Reward

ranking of multiple responses are converted to numerical rewards
Simplest method is fixed reword for order, like +1,0,-1
Another approach is normalized rewards, 0-1
A third approach is to use nonlinear scaling such as logarithmic or exponential. -ln(a) or e<sup>-&lambda; a</sup>


<a id="org739fbf0"></a>

### Supervised Learning

a starting point is Bradley-Terry Model (1952)
assigns probabilities to outcome of pairwise comparison between items
preference i > j of two items is assigned value s<sub>i</sub> / (s<sub>i</sub>+s<sub>j</sub>)
P(i>j)+P(j>i)=1
The original model used exponential scaling of scores

Plackett-Luce model - generalization for arbitrarily long lists
product of s1/sum(s1..sn) \* s2/sum(s2..sn) &#x2026;

output of reward model is r<sub>&theta;</sub>(x,y)
we want to maximize probability P(y1>y2) = exp r<sub>&theta;</sub>(x,y1) / (exp r<sub>&theta;</sub>(x,y1) + exp r<sub>&theta;</sub>(x,y2))
or argmax(&sigma;(r<sub>&theta;</sub>(x,y1)-r<sub>&theta;</sub>(x,y2)))
optimize this with supervised learning


<a id="orgf86eb59"></a>

## Proximal Policy Optimization

Actor-critic method (Policy-gradient for us)
loss J<sub>PG</sub>(&theta;)=Et<sub>nil</sub>[log&pi;<sub>&theta;</sub>(at|st)At]
where At(s,a) is Qt(s,a) - Vt(s,a)
J=E[v(S0)|S0~t] where S0 is starting state, v is sum of reward
Then gradient is L&Sigma;&mu;&Sigma; q \* gradient &pi;
&theta;=&theta;+&alpha;&Sigma; q gradient &pi; where q is an approximation of the action-value function


<a id="org8bc5db6"></a>

### REINFORCE

replace sum over all actions by sample At in &pi;
q(S,A) = the return of the sample G
(gradient f)/f = gradient ln f
so &theta;<sub>t+1</sub>=&theta;<sub>t</sub>+&alpha;&gamma;<sup>t</sup> G<sub>t</sub> gradient ln &pi;<sub>&theta;</sub>(A<sub>t</sub>|S<sub>t</sub>,&theta;<sub>t</sub>)
we can add a baseline b(S<sub>t</sub>) (because it will is always equal to 0 when gradient is summed over)
the best baseline is the state-value function v, because then we get the advantage, so how much better the new action is from before
&theta;<sub>t+1</sub>=&theta;<sub>t</sub>+&alpha;&gamma;<sup>t</sup> (G<sub>t</sub>-b(S<sub>t</sub>)) gradient ln &pi;<sub>&theta;</sub>(A<sub>t</sub>|S<sub>t</sub>,&theta;<sub>t</sub>)
this is the actor critic model, pi is the actor, the advantage function is the critic - judging the action


<a id="orgde9e7d9"></a>

### TRPO

trust region policy optimization
maximize expected value of advantage \* pi/pi-old
subject to expected value of KL(pi-old,pi)<=&delta;
    that is, Kullback-Leibler divergence should not be too large, we don't want our step size to be large
alternatively, instead of constraint (hard to solve) we can use a penalty to go to unconstrained optimization problem
max expected value of advantage \* pi/pi-old - &beta; KL(pi-old,pi) where &beta; is a positive constant
Next, define clipped surrogate objective - Hubar loss function - loss becomes linear far from minima, gradient becomes zero, equivalent to clipping gradient
Jclip = expected value of min between advantage \* ratio, clip(ratio, 1-e, 1+e)\*advantage
performance is the lower or pessimistic bound on the unclipped value - changes in r are included when they make the objective worse, but ignored when making it better
We adapt &beta; so that a prescribed target d of KL divergence is achieved
if divergence d < target / 1.5, &beta; is halved, if d > target \* 1.5, &beta; is doubled
   hyperparameters are chosen heuristically
KLPENALTY works worse than CLIP


<a id="org994f998"></a>

### PPO

J = expected value of JCLIP - c1 JVF + c2 S(&pi;<sub>&theta;</sub>)(s<sub>t</sub>) where c1,c2 are nonnegative coefficients
JVF is squared-error loss - makes it an actor-critic model (V<sub>&theta;</sub>(s<sub>t</sub>) - Vtarget)<sup>2</sup>
S is entropy - added as reward in order to ensure sufficient exploration of states (optimization is stochastic, so there is uncertainty)
A = &delta;<sub>t</sub> + (&gamma;&lambda;)&delta;<sub>t+1</sub>+(&gamma;&lambda;)<sup>2</sup>&delta;<sub>t+2</sub> + &#x2026;
&delta;=r+&gamma;\*V(s+1)-V(s)


<a id="orgbec48cb"></a>

### Group Relative Policy Optimization

removes JVF - no longer actor-critic model
instead use average reward of sampled outputs
