#!/usr/local/bin/python

"""
pip install csc-pysparse networkx divisi2
cd python-recsys-master
python setup.py install

"""

import pdb

import recsys.algorithm
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
from recsys.evaluation.prediction import RMSE, MAE
from recsys.utils.svdlibc import SVDLIBC

# enable verbose output
recsys.algorithm.VERBOSE = True

# ref: http://ocelma.net/software/python-recsys/build/html/quickstart.html
def quickstart():
    svd = SVD()
    recsys.algorithm.VERBOSE = True

    # load movielens data
    dat_file = 'ml-1m/ratings.dat'
    svd.load_data(filename=dat_file, sep='::', format={'col':0, 'row':1, 'value':2, 'ids': int})

    # compute svd
    k = 100
    svd.compute(k=k, min_values=10, pre_normalize=None, mean_center=True,
        post_normalize=True)

    pdb.set_trace()

    # movie id's
    ITEMID1 = 1      # toy story
    ITEMID2 = 1221   # godfather II

    # get movies similar to toy story
    svd.similar(ITEMID1)

    # get predicted rating for given user & movie
    MIN_RATING = 0.0
    MAX_RATING = 5.0
    USERID = 1
    ITEMID = 1

    # get predicted rating
    pred = svd.predict(ITEMID, USERID, MIN_RATING, MAX_RATING)
    actual = svd.get_matrix().value(ITEMID, USERID)
    print 'predicted rating = {0}'.format(pred)
    print 'actual rating = {0}'.format(actual)

    # which users should see Toy Story?
    svd.recommend(ITEMID)
    # [(283,  5.716264440514446),
    #  (3604, 5.6471765418323141),
    #  (5056, 5.6218800339214496),
    #  (446,  5.5707524860615738),
    #  (3902, 5.5494529168484652),
    #  (4634, 5.51643364021289),
    #  (3324, 5.5138903299082802),
    #  (4801, 5.4947999354188548),
    #  (1131, 5.4941438045650068),
    #  (2339, 5.4916048051511659)]

# ref: http://ocelma.net/software/python-recsys/build/html/examples.html
def ex1(dat_file='ml-1m/ratings.dat',
        pct_train=0.5):

    data = Data()
    data.load(dat_file, sep='::', format={'col':0, 'row':1, 'value':2,
    'ids':int})
        # About format parameter:
        #   'row': 1 -> Rows in matrix come from column 1 in ratings.dat file
        #   'col': 0 -> Cols in matrix come from column 0 in ratings.dat file
        #   'value': 2 -> Values (Mij) in matrix come from column 2 in ratings.dat
        #   file
        #   'ids': int -> Ids (row and col ids) are integers (not strings)

    # create train/test split
    train, test = data.split_train_test(percent=pct_train)

    # create svd
    K = 100
    svd = SVD()
    svd.set_data(train)
    svd.compute(
        k=K, min_values=5, pre_normalize=None, mean_center=True, post_normalize=True)

    # evaluate performance
    rmse = RMSE()
    mae = MAE()
    for rating, item_id, user_id in test.get():
        try:
            pred_rating = svd.predict(item_id, user_id)
            rmse.add(rating, pred_rating)
            mae.add(rating, pred_rating)
        except KeyError:
            continue

    print 'RMSE=%s' % rmse.compute()
    print 'MAE=%s' % mae.compute()

if __name__ == '__main__':
    quickstart()
    # ex1()
