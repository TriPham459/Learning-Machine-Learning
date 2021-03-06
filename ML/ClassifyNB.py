def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    
    clf = GaussianNB()
    clf.fit(features_train, labels_train) 
    
    return clf

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)    

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    cnt = 0;
    for i in range(len(pred)):
        if (pred[i] == labels_test[i]):
            cnt = cnt + 1
        
    accuracy = cnt/len(pred)
    
    
    
    return accuracy








