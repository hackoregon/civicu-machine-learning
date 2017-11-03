# Data Science for "Enterprise"

Big corps and universities often expect your familiarity with the tools useful for working with large data sets, spread out over many organizations.
You also need tools for interacting with teams and helping make your models repeatable.
You need to convince a boss that what you're doing is the right approach.
These exercises are often helpful in firming up your own thinking.
And brainstorming with peers is a great way to cross-pollenate across organizations and reset the seed in the random idea generator in your brain.

## [Predictive Model Markup Language](https://en.wikipedia.org/wiki/Predictive_Model_Markup_Language) (PMML)

Used mostly in large corporations and academics, PMML is an XML schema for sharing you design with other Data Scientists.
Python has a package for reading and writing this model file, the schema itself is limited in the types of models it can deal with.
So I have never used it, even when working for Intel and Sharp Labs.
Nonetheless, the standard may evolve to the point that it is useful for complex real-world models so here's how you can use it.

Let's think about a few things first:

1. How is PMML difference from `sklearn.Pipeline`?
2. What scenarious would PMML be useful for?
3. What are the pieces of a model?
4. Is data wranging, cleaning, and feature engineering part of a "model"?
5. Do PMML and Pipeline facilitate hyperparameter optimization?
6. Do PMML and Pipeline facilitate make it possible to fully automate the design, training, and testing of models?
7. What corporations or software libraries use PMML?
8. How popular is PMML?
9. How likely are others to use it?
10. Is it open source?

These last few are the sorts of questions you should ask about any platform, library, or language for doing machine learning or data science.
It's how I selected `python` and `scikitlearn` six years ago.
I used Ubuntu `apt` package installation trends to approximately model future popularity for tools like Ruby, C++, R, Python, Django, Flask, scipy, Pandas, and SciKit-Learn for web development and machine learning.

Let's train a decision tree model from the "iris" data set in `sklearn`:

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris_data = load_iris()
X, y = iris_data.data, iris_data.target
tree = DecisionTreeClassifier() 
tree = tree.fit(X, y)
```

The [sklearn2pmml](https://github.com/jpmml/sklearn2pmml) is a python package that can convert some simple sklearn models, like a `DecisionTree` to PMML.
It's just a wrapper for a command-line tool in a Java package called [`JPMML-sklearn`](https://github.com/jpmml/jpmml-sklearn), so you can always use that if you don't want to install `sklearn2pmml`.

```bash
pip install sklearn2pmml
```

We can use `sklearn2pmml` to export our trained (fitted) `DecisionTree` model in `tree` to PMML:


```python
from sklearn_pandas import DataFrameMapper
mapper = DataFrameMapper([(i, None) for i in iris.feature_names + ['Species']])

from sklearn2pmml import sklearn2pmml
sklearn2pmml(estimator=tree,
             mapper=mapper,
             pmml="sklearn-iris-decision-tree.pmml")
```


This is what a PMML file looks like for that trained `sklearn` model:

```XML
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<PMML xmlns="http://www.dmg.org/PMML-4_3" version="4.3">
    <Header>
        <Application name="JPMML-SkLearn" version="1.1.1"/>
        <Timestamp>2016-09-26T19:21:43Z</Timestamp>
    </Header>
    <DataDictionary>
        <DataField name="sepal length (cm)" optype="continuous" dataType="float"/>
        <DataField name="sepal width (cm)" optype="continuous" dataType="float"/>
        <DataField name="petal length (cm)" optype="continuous" dataType="float"/>
        <DataField name="petal width (cm)" optype="continuous" dataType="float"/>
        <DataField name="Species" optype="categorical" dataType="string">
            <Value value="setosa"/>
            <Value value="versicolor"/>
            <Value value="virginica"/>
        </DataField>
    </DataDictionary>
    <TreeModel functionName="classification" splitCharacteristic="binarySplit">
        <MiningSchema>
            <MiningField name="Species" usageType="target"/>
            <MiningField name="sepal length (cm)"/>
            <MiningField name="sepal width (cm)"/>
            <MiningField name="petal length (cm)"/>
            <MiningField name="petal width (cm)"/>
        </MiningSchema>
        <Output>
            <OutputField name="probability_setosa" dataType="double" feature="probability" value="setosa"/>
            <OutputField name="probability_versicolor" dataType="double" feature="probability" value="versicolor"/>
            <OutputField name="probability_virginica" dataType="double" feature="probability" value="virginica"/>
        </Output>
        <Node id="1">
            <True/>
            <Node id="2" score="setosa" recordCount="50.0">
                <SimplePredicate field="petal width (cm)" operator="lessOrEqual" value="0.8"/>
                <ScoreDistribution value="setosa" recordCount="50.0"/>
                <ScoreDistribution value="versicolor" recordCount="0.0"/>
                <ScoreDistribution value="virginica" recordCount="0.0"/>
            </Node>
            <Node id="3">
                <SimplePredicate field="petal width (cm)" operator="greaterThan" value="0.8"/>
                <Node id="4">
                    <SimplePredicate field="petal width (cm)" operator="lessOrEqual" value="1.75"/>
                    <Node id="5">
                        <SimplePredicate field="petal length (cm)" operator="lessOrEqual" value="4.95"/>
                        <Node id="6" score="versicolor" recordCount="47.0">
                            <SimplePredicate field="petal width (cm)" operator="lessOrEqual" value="1.6500001"/>
                            <ScoreDistribution value="setosa" recordCount="0.0"/>
                            <ScoreDistribution value="versicolor" recordCount="47.0"/>
                            <ScoreDistribution value="virginica" recordCount="0.0"/>
                        </Node>
                        <Node id="7" score="virginica" recordCount="1.0">
                            <SimplePredicate field="petal width (cm)" operator="greaterThan" value="1.6500001"/>
                            <ScoreDistribution value="setosa" recordCount="0.0"/>
                            <ScoreDistribution value="versicolor" recordCount="0.0"/>
                            <ScoreDistribution value="virginica" recordCount="1.0"/>
                        </Node>
                    </Node>
                    <Node id="8">
                        <SimplePredicate field="petal length (cm)" operator="greaterThan" value="4.95"/>
                        <Node id="9" score="virginica" recordCount="3.0">
                            <SimplePredicate field="petal width (cm)" operator="lessOrEqual" value="1.55"/>
                            <ScoreDistribution value="setosa" recordCount="0.0"/>
                            <ScoreDistribution value="versicolor" recordCount="0.0"/>
                            <ScoreDistribution value="virginica" recordCount="3.0"/>
                        </Node>
                        <Node id="10">
                            <SimplePredicate field="petal width (cm)" operator="greaterThan" value="1.55"/>
                            <Node id="11" score="versicolor" recordCount="2.0">
                                <SimplePredicate field="sepal length (cm)" operator="lessOrEqual" value="6.95"/>
                                <ScoreDistribution value="setosa" recordCount="0.0"/>
                                <ScoreDistribution value="versicolor" recordCount="2.0"/>
                                <ScoreDistribution value="virginica" recordCount="0.0"/>
                            </Node>
                            <Node id="12" score="virginica" recordCount="1.0">
                                <SimplePredicate field="sepal length (cm)" operator="greaterThan" value="6.95"/>
                                <ScoreDistribution value="setosa" recordCount="0.0"/>
                                <ScoreDistribution value="versicolor" recordCount="0.0"/>
                                <ScoreDistribution value="virginica" recordCount="1.0"/>
                            </Node>
                        </Node>
                    </Node>
                </Node>
                <Node id="13">
                    <SimplePredicate field="petal width (cm)" operator="greaterThan" value="1.75"/>
                    <Node id="14">
                        <SimplePredicate field="petal length (cm)" operator="lessOrEqual" value="4.8500004"/>
                        <Node id="15" score="virginica" recordCount="2.0">
                            <SimplePredicate field="sepal width (cm)" operator="lessOrEqual" value="3.1"/>
                            <ScoreDistribution value="setosa" recordCount="0.0"/>
                            <ScoreDistribution value="versicolor" recordCount="0.0"/>
                            <ScoreDistribution value="virginica" recordCount="2.0"/>
                        </Node>
                        <Node id="16" score="versicolor" recordCount="1.0">
                            <SimplePredicate field="sepal width (cm)" operator="greaterThan" value="3.1"/>
                            <ScoreDistribution value="setosa" recordCount="0.0"/>
                            <ScoreDistribution value="versicolor" recordCount="1.0"/>
                            <ScoreDistribution value="virginica" recordCount="0.0"/>
                        </Node>
                    </Node>
                    <Node id="17" score="virginica" recordCount="43.0">
                        <SimplePredicate field="petal length (cm)" operator="greaterThan" value="4.8500004"/>
                        <ScoreDistribution value="setosa" recordCount="0.0"/>
                        <ScoreDistribution value="versicolor" recordCount="0.0"/>
                        <ScoreDistribution value="virginica" recordCount="43.0"/>
                    </Node>
                </Node>
            </Node>
        </Node>
    </TreeModel>
</PMML>
```

You can see that this file contains not only the structure (logic) of the decision tree model, but also the thresholds for each branch in the decision tree.

