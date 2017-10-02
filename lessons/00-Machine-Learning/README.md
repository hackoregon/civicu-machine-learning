# Today

## Example Machine Learning Problem

Your first machine learning problem.
Teach a machine to be a carnival magician that guesses your weight (based on your height)

Imagine our first example is 72 (6 ft) inches and 144 pounds.
We might guess that people generally have 2 lb of weight per inch of height

`predicted_weight = 2 * height`

But we have data!
We have examples from real people in `shared-resouces/heights_weights.csv`
_genders.csv`

So we can calculate a better height weight ratio than the 2 we guessed from only one example.
We can optimize our model with.


```python
weight_height_ratio = pd.np.mean(df['Weight'] / df['Height'])
```



But if we plot this we can see that our line of predictions starts below the "right answers" in our example data.
And it's above the right answers for taller people.
It overestimates the weight of tall people and underestimated the weights of shorter people.
How can we shift the whole line up a bit so that it intercepts the y (weight) axis above zero?
Well, instead of just a multiplier coefficient (ratio or slope) we also can **add** an offset or "intercept" to our model.

```python
intercept = pd.np.mean(df['Weight'])
coef = (pd.np.mean(df['Weight'] - intercept) / df['Height'])
predicted_weight = coef * height + intercept
```

But this isn't right either.
A linear regression should produce a line that goes through the middle of our data.
I couldn't remember the right way to do this either.
But sklearn has a LinearRegression machine learning model that can do this for us.
And if you really want to know how to do this manually...


```python
average_height = pd.np.mean(df['Height'])
average_weight = pd.np.mean[df['Weight'])

df['centered_weight'] = df['Weight'] - average_weight
df['centered_height'] = df['Height'] - average_height

coef = pd.np.mean(df['centered_weight'] * df['centered_height'])
coef = coef / (df['centered_weight'].mean() * df['centered_height'].mean())

```





* Manually programming a weight predictor
    * y = a * x 
    * y = a * x + b
    * y = coef * x + intercept
    

* Using data to manually improve the predictions
* Automating this manual process
    * LinearRegression 
   
 


# Homework

Think about the ethics of machine learning.
Check out these blogs and videos to get some ideas.

* [machine learning isn't the arbiter of truth and morality](https://www.ted.com/talks/cathy_o_neil_the_era_of_blind_faith_in_big_data_must_end)
* [moral decsions about the technology of self-driving cars](https://www.ted.com/talks/iyad_rahwan_what_moral_decisions_should_driverless_cars_make)
* [a realistic self-driving car ethical delimma](https://youtu.be/ixIoDYVfKA0)

# Machine Learning

Machine learning
