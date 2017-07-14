# Decision Trees

*Decision Trees* are a favorite tool for classification problems with large numbers of features or nonlinear, interdependent decision boundaries. They are used a lot in business and finance because they can be explained to managers without any background in statistics or math or machine learning. Decision trees define a "process" that either humans or machines can implement. And managers understand how to define processes ;) Decision Trees are sometimes the first classifier that Data Science students learn about, for this same reason.

Despite being relatively easy to explain and understand, they can be quite powerful, making quite complicated classification decisions that humans might not ever think of. This is especially true when multiple decision trees are trained and they are combined together to create a Random Forest model--a collection of decision trees that each "vote" on the right answer.

A *decision tree* is a sequence of nested (interdependent) yes/no answers about the data. That nesting (interdependence) is what makes it a tree. Each question depends on the answer to the previous question. Once you have trained a decision tree model, you can explain examples to your management, collaborators, or students by going through the sequence of decisions one by one. This makes it familiar to most people because it's like a sequence of roll playing game decisions to navigate through a dungeon, or a choose your own adventure book, or set of rules for how to play a game of 20 questions. The decision tree for a game of 20 questions will typically define many more than just 20 questions, because each answer generates a new fork in the tree and a new question to be answered, until you work your way all the way to the "leaf" where the answer is known. But you will have always answered fewer than 20 questions by the time you reach the leaf (if your decision tree algorithm or model is a winning one ;).

Decision trees define a procedure or process for asking logical questions about each feature that help you narrow down the answer to the question "Which class is this example in?"   Decision trees are an attempt at having the computer learn what the sequence of if/then statements should be to identify which category label to give each example (table row in a list of example feature vectors). In a way it's like teaching a computer to ask the right questions in a game of 20 questions, where each question depends on the last one (that's why it's called a tree and not just a linear classifier based on a single threshold on each feature). Only you don't have to program the thousands of if/then statements manually, the machine can find them automatically, by just looking at a set of examples.

## Random Forest

A random forest model just combines decision trees by allowing each one to "vote" on the right answer--"wisdom of the tree crowd". A decision tree learns the thresholds on each of your features that can be used to distinguish between classes, the boundaries between classes in your "feature space." 


## Resources

1. (Using Random Forests to classify images (MNIST digits)](https://github.com/TheGrimmScientist/SlidesFromTalks/blob/master/2016_03_17_HUML_Guest_Lecture/2_EnsembleLearningWorkbook.ipynb) by Alan Grimm (last Fall's machine learning class)