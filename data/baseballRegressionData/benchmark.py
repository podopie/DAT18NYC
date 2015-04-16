#! /usr/bin/env python

def main():
    import pandas as pd
    from sklearn import linear_model, metrics
    b2011 = pd.read_csv('baseball_training_2011.csv')
    b2012 = pd.read_csv('baseball_test_2012.csv')
    #
    train_X = b2011[['G', 'AB', 'R', 'H', 'X2B', 'X3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF']].values
    train_y = b2011['salary'].values
    #
    test_X = b2012[['G', 'AB', 'R', 'H', 'X2B', 'X3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF']].values
    b2012_csv = b2012[['playerID','yearID', 'salary']]
    #
    lm = linear_model.Ridge()
    lm.fit(train_X, train_y)
    #
    # Checking performance, roughly .19
    print 'R-Squared:',lm.score(train_X, train_y)
    # Checking MSE, roughly terrible
    print 'MSE:',metrics.mean_squared_error(lm.predict(train_X), train_y)
    #
    # Outputting to a csv file
    print "Outputting submission file as 'submission.csv'"
    b2012_csv['predicted'] = lm.predict(test_X)
    b2012_csv.to_csv('submission.csv')

if __name__ == "__main__":
    main()
