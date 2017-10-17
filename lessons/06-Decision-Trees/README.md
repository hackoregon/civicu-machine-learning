# Entropy

## Review

* What is a Time Series
* A simple transformation for time-series modeling
* What kinds of models work

## Entropy

Entropy is the amount of information in an event, the knowledge we gain by knowing the results of an experiment.

Imagine playing a game of 20 questions.  
Depending on how good you are at asking questions, you may take many more than 20 questions or many fewer.  
It turns out, the more interesting your questions are the faster you'll "win."  
A measure of the interestingness in your questions is their entropy!  

And it turns out there's a way to precisely measure interestingness!

We just need to know the probabilities or frequencies of the answers to those questions.  

So we could really only measure it for a 20-Questions game if we watched the whole game and counted the yes and no answers.  

How interesting do you think our questions are in this game?  
If you had to give it a number, a score what would you give it?  

**Q:** Is it a white Toyota Prius?  
**A:** No  

**Q:** Is it an unladen African swallow?  
**A:** No 

**Q:** Is it the number 42?  
**A:** No  

**Q:** Is it OR-7?  
**A:** No  

**Q:** Is it Jeremy Bentham?  
**A:** No  

**Q:** Is it Joseph Priestly?  
**A:** No  

  




----

### Information Theory

Shannon's 20-questions game was, what is the next word or symbol or bit in a message between a transmitter and receiver.  
If he could guess the next word or bit perfectly, the receiver wouldn't even need to send it.  
This would be a compressed message.  
And if you measure the "entropy" of a compressed message it should be the same or greater for the uncompressed message even though it has more bits.  
It's constant, kind of like thermodynamic entropy (as long as you don't change the "information" in the message).  
You can only add more entropy to a message, you can't reduce it.  

```python
sum(-p * log2(p) for p in outcome_probabilities)
```

![Shannon entropy: sum(-p * log2(p) for p in outcome_probabilities)](../shared-resources/entropy_shannon.svg "Shannon Information Entropy")

### Theromdynamics Theory

Shannon information entropy is the same as Boltzmann's thermodynamic entropy, just multiplied by Boltzmann's constant to turn convert units of information (bits) into units of energy, like the charge in your battery (Joules or Watt-seconds).  

```python
sum(-p * log2(p) for p in outcome_probabilities)
```

![Shannon entropy: k * sum(-p * log2(p) for p in outcome_probabilities)](../shared-resources/entropy_boltzman.svg "Boltzman Theromdynamics Entropy")

This means if you have a measure of entropy for a message, you can know just how small you could ever make it without destroying any information in the original message.

Thiwas trying to figure out how much information there was in an encoded radio message.
compress (encode) messages as much as possible so they could be transmitted over radio or telegram.
He wanted to know how small he could make the compressed "file".


driven by an unpredictable system.

Entropy is the amount of "complexity" in a system