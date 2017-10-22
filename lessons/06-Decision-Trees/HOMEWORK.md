# HOMEWOK

* load a financial time series dataframe
* transform the data to create a vector of features for each day (you know this)
  * y = shifted forward by a day
  * X = df.diff() for today, yesterday, and day before yesterday (3-day rolling window)
* predict whether tomorrow's change in price will be above some threshold (zero is fine) using:
  * logistic regression
  * random forest
  * gradient boosting

## BONUS:

Create your own ensemble method by combining the answers from all 3 models.
