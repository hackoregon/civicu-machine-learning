# AI Morality

## Industry Trends

Poll by Andrew Ng at Spark Conf 2016 ignored many industries like law, construction, professional services, and blue collar services like hairdressing and fast food restaurant work.

Respondents: 574

Which industry is most likely to be transformed by AI in the near term (this is really just a poll of the industry mix of attendees at Spark Conf, industries using Spark.

1. Healthcare: 35%
2. Transportation: 21%
3. Media/Entertainment: 10%
4. Manufacturing: 10%
5. Retail: 7%
6. Agriculture: 6%
7. Education: 6%
8. Energy: 5%

## Autonomous Cars

Self-driving cars will have to differentiate between selfish self-driving cars and prosocial self-driving cars.
Auto manufacturers may differentiate themselves by being the prosocial one (low emission Prius, zero-emission Tesla) or selfish (gas-guzzling american SUV manufacturers).
Eventually the prosocial, forward-thinking, big-picture vision companies and engineers always win.
So regulation cannot solve this riddle is not the answer, big-thinking, altruistic design is!

Must make safety-critical predictions like predicting the gesture of a construction worker making eye contact and beconing forward toards him, vs holding a hand up to signal stop.[1]

## Slides

<!SLIDE>

.callout.quote The higher the buildings, the lower the morals. 

> The higher the buildings,
> the lower the morals. 
> -- Noel Coward

<!SLIDE bullets incremental transition=fade>

# Drone Crashing

* Amazon delivery mission
* Battery overheating
* 4 lb package

<!SLIDE transition=fade>

# You have 3 seconds... 

1. highway: slow moving cars
2. side street: parked cars, pedestrians
3. park: people and pets
4. private rooftop
5. private yard/garden

<!SLIDE transition=fade>

# Dynamic programming problem

- partial info
- weakly adversarial
- stochastic
- chaotic


<!SLIDE transition=fade>

# Naive Approach

- safe ditch location DB
  - continuous ditch planning
  - motion detection of ditch sites
- health monitor
  - range estimator
  - life estimator

e.g. Safe2Ditch

~~~SECTION:notes~~~

allowance for adaptive morals?
parking lots aren't stationary active 
flags on rooftops
trees have leaves and branches that sway
sunbathers?
cars don't move at intersection

~~~ENDSECTION~~~


~~~SECTION:references~~~

## References

### Inequality Arbitrage and AI Morality

- Quant Trading by Karen Rubin: [video](http://pyvideo.org/pycon-us-2016/karen-rubin-building-a-quantitative-trading-strategy-to-beat-the-sp500-pycon-2016.html), [slides](https://speakerdeck.com/pycon2016/karen-rubin-building-a-quantitative-trading-strategy-to-beat-the-s-and-p500)
- Bertrand and Mullainathan "...More Employable than Lakisha and Jamal": [NBER draft paper](http://www.nber.org/papers/w9873), [2004 Indiana State paper](http://www2.econ.iastate.edu/classes/econ321/Orazem/bertrand_emily.pdf)
- [Wang & Kosinski](https://osf.io/fk3xr/download)
- [machine learning isn't the arbiter of truth and morality](https://www.ted.com/talks/cathy_o_neil_the_era_of_blind_faith_in_big_data_must_end)
- [moral decsions about the technology of self-driving cars](https://www.ted.com/talks/iyad_rahwan_what_moral_decisions_should_driverless_cars_make)

### Amoral AI

- [hackers use machine learning to find soft points](http://gizmodo.com/hackers-have-already-started-to-weaponize-artificial-in-1797688425)
- [autonomous weapons](https://futureoflife.org/open-letter-autonomous-weapons/)

### AI Trends

- [Andrew Ng Poll Results](http://files.quizsnack.com/iframe/embed.html?hash=q715o9n1)

### Driverless Cars

- [Patrick Lin: Ethical dilemma of self-driving cars](https://www.youtube.com/watch?v=ixIoDYVfKA0): Moral, ethical decisions that machines must make, that humans don't have to.
- [Iyad Rahwan: Moral decisions driverless cars should make](https://www.ted.com/talks/iyad_rahwan_what_moral_decisions_should_driverless_cars_make): Webapp to build a moral framework for self-driving cars (great training set!) 
- [Edmond Awad, Sohan Dsouza, Iyad Rahwan, Azim Shariff, Jean-François Bonnefon: Moral Machine](https://www.media.mit.edu/research/groups/10005/moral-machine)
- [The Verge: Trolley Problem](https://www.theverge.com/2016/6/23/12010476/social-dilemma-autonomous-vehicles-car-moral-machine-trolley-problem)
- [moral machine for android](http://androidforfree1.download/games/who-would-you-kill-moral-machine)
- [Edmond Awad: Collective Intelligence, Group Argumentation, and logial ethics decisionmaking](http://web.media.mit.edu/~awad/)
- [a realistic self-driving car ethical delimma](https://youtu.be/ixIoDYVfKA0)

### Advertising

Advertising and Sales is inherently anti-social (capitalistic).
If machines are good at manipulating us and are motivated by survival instincts and self-interest, they will quickly learn to influence us to help them survive by replicating themselves and expanding their power/influence in the world.

- [Andrew Ng: AI is focused on predicting Ads we'll click on, selling us stuff](https://www.youtube.com/watch?v=21EiKfQYZXc)


### Non-virtuous Cycle of Hype

[Ng isn't worried about Superintelligence](https://youtu.be/21EiKfQYZXc?t=39m8s)

Ng feels it's a misallocation of resources (his friends are not involved in anti-evil AI research)?

Ng is more concerned about job displacement by AI

Andrew Ng's [lecture to Stanford MBA students](https://youtu.be/21EiKfQYZXc?t=41m36s) advises them to "sleep easy", worrying about evil AI is like worrying about overpopulation of Mars

Andrew Ng dismisses the Trolly Problem as irrelevant. But [that assessment](https://youtu.be/21EiKfQYZXc) ignores the fact that the trolly problem is an analogy for a whole class of real-world ethical dilemmas that we make decisions about every day. And every self-driving car decision is a balance between safety of the driver and others in the environment or among various environmental elements including both animals and people. For example the tailgating distance for a self-driving car behind a human car has several effects that must be balanced with more than purely rational self-interest "in mind."

* safety of the self-driving car occupants
* safety of the human-driven car
* safety of cars behind the self-driving car
* speed of travel for the self-driving car
* speed of travel for the cars nearby
* safety of animals and pedestrians that might be ahead
* fuel efficiency gain or loss from drafting
* environmental impact from emissions and noise

Of course these ethical dilemmas don't have as obvious or immediate effects as the alegory of the Trolley Problem, but because it will be a constant concern of every self-driving car in traffic, the decisions will have a huge impact.

[Andrew Ng "sleep easy", worrying about evil AI is like worrying about overpopulation of Mars

Ng seems to dismiss several reasonable arguments by smart people (see Surviving AI) without any analysis or thought.
Seems like a false analogy. A more appropriate analogy might be worrying about the seeding of Mars with viral/bacteria life from Earth that destroys existing life on Mars or makes it uninhabitable.

~~~ENDSECTION~~~