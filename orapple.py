#!/usr/bin/python3
                                           #svm=support vector machine(spam mails detection)
                                           #random forest KNN #Lion #decision tree


from sklearn import tree

features=[[110,"0"],[120,"0"],[130,"1"],[140,"1"]]

output=["Apple","Apple","Orange","Orange"]

# now loading decisiontree classifier

algo=tree.DecisionTreeClassifier()

#training the features and output

trained = algo.fit(features,output) #generally looking for one core CPU

output1 = trained.predict([[110,"0"]])

print(output1)
