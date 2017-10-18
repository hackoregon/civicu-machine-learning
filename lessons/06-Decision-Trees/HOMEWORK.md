# HOMEWOK

1. load a financial time series dataframe
2. transform the data to create a vector of features for each day (you know this)
    2.1. y = shifted forward by a day
    2.2. X = df.diff() for today, yesterday, and day before yesterday (3-day rolling window)
3. predict whether tomorrow's change in price will be above some threshold (zero is fine) using:
    3.1 logistic regression
    3.2 random forest
    3.3 gradient boosting

## BONUS:

Create your own ensemble method by combining the answers from all 3 models.
