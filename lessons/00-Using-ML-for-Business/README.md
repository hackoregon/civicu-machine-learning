# ML for Business

It is becoming more and more important for business managers to understand Machine Learning and AI in order to keep up with our robot overlords.
This lesson will provide a high level overview of machine learning suitable for those with a limited STEM background.

## Prep

[Andrew Ng lecture to Stanford MBA students 2017-01-25](https://www.youtube.com/watch?v=21EiKfQYZXc)

# Business with ML

## Competitive Advantage

Algorithms are not a competitive advantage.

- Baidu & Google < 2 yr ahead of competition
- Leading AI researchers share details of their algorithms

Two possible competitive advantages

- Data
- People

## Virtuous Cycle

The driver behind AI is virtuous cycle of AI product launch

- AI product 
- User interactions (gmail subscriber growth)
- Training data (users label data for you)

Examples

### Gmail spam

1. gmail spam filter
2. subscriber growth
3. more users labeling spam for you

### Inbox Response Suggestor

1. gmail Inbox autoresponder
2. subscriber growth
3. more users labeling spam for you


## Supervised Learning Examples

### [Commercial Examples by Andrew Ng](https://youtu.be/21EiKfQYZXc?t=10m16s)

Machine learning is programing a computer to recognize Input -> Output mappings without having to manually program a function to do that.

Andrew Ng's list of common commercial applications of Supervised Machine Learning (AI).

- email -> is it spam?
- image -> is there a person? cat? dog?
- speech -> text transcript
- text -> natural sounding speech
- English -> French
- ad & user -> probability of click/purchase

It's distubing to me that machines are getting good at participating in a capitalistic world faster than they're getting good at being good citizens (prosocial).
Corporations provide an example of what happens when autonomous, inhuman (mechanical?) systems are incentivized to survive in a capitalistic world.
They also provide an example of how superintelligence may behave.
Corporations do not behave like humans, but collaborate with humans to accomplish their thinking and actions, just as superintelligence likely will.

Real world examples of these collaborative AI systems that are growing in tehir capability and are already much more capable than an individual human brain:

- facebook "community mediation" AI
- Google search AI
- Google assistant
- Amazon Alexa
- Siri
- warfighting AI (war room software)?

These systems are shaping society for their own benefit/survival.
If they're incentivized to replicate themselves (architect and spin off competing businesses), we're in trouble.
Systems capable of reproduction can evolve greater capability if they're incentivized to survive (fitness).


### Examples of Supervised Learning

Simple mappings that ML is good at.

- height -> weight
- height, gender -> weight
- height, weight, gender, age -> body temp
- height, weight, gender, age, body temp, TOD, DOW -> heart rate

Notice how a simple model can be made more useful and accurate by simply changing the input features or the output (target) variable?
Try that for a Zestimate algorithm (predict home prices).

- number of bedrooms -> home price
- beds, baths -> homoe price
- beds, baths, type (duplex, flat, ...) -> home price
- home price -> structure type, beds, baths
- home price, beds, baths -> structure type
- beds, baths, type, zoning, frontage ft, lat, lon, ... -> price

Notice that sometimes you can move an output to an input or move an input to an output.
The only limitation is what information you can "pair-up" that is interesting to you.
A problem is interesting to your business if you can easily get the input data, but can't easily get the output (target) values.

Here's a [Kaggle competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) for this if you want to experiment with this type of problem.

Can you think of other data sources you'd "join" with this one to improve your model?

More complex mappings that ML is good at:

- stock price history -> future stock price(s)
- loan application -> default probability
- resume & job description -> probability of callback
- person profile & product features -> probability of customer liking it

Ng says that anything that a typical human can do with less than 1 second of thought then it can probably be automated with AI or machine learning.

Feasible examples:

- driving decisions
- radiologists

Difficult AU problems:

- equity markets^*^
- earthquakes
- volcanoes
- epidemics
- revolutions^*^
- human responses/reactions^*^
- wars
- adversary behavior

Once you exceed human performance/accuracy, AI development progress slows.
Humans can no longer have good instincts about the kinds of tweaks to the algorithm that might improve performacne beyond human performance.

# References

[Andrew Ng lecture to Stanford MBA students 2017-01-25](https://www.youtube.com/watch?v=21EiKfQYZXc)


