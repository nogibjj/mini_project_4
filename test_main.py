"""
Test goes here

"""
from main import desripStats
import pandas as pd


def findMin(data):
    min_ind = 0
    for i in range(len(data)):
        if data[i] < data[min_ind]:
            min_ind = i
    return data[min_ind]


def findMax(data):
    max_ind = 0
    for i in range(len(data)):
        if data[i] > data[max_ind]:
            max_ind = i
    return data[max_ind]


def calcMean(data):
    total = 0
    for ele in data:
        total += ele
    return round(total / len(data), 3)


def test_pd_descriptive():
    # dataset file
    file = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"

    print("this code reads csv data from: ", file)

    data_summary = desripStats(file)
    print("==" * 30)
    print("descriptive statistic summary of the data is given as:")
    print(data_summary)
    print("==" * 30)

    data = pd.read_csv(file)["mpg"]

    # run some test cases: mean, min and max of the 'mpg'
    # minimum
    try:
        min_mpg = findMin(data)
        assert data_summary["mpg"]["min"] == min_mpg
    except AssertionError as msg:
        raise msg + "minimum result unmatch"

    # maximum
    try:
        max_mpg = findMax(data)
        assert data_summary["mpg"]["max"] == max_mpg
    except AssertionError as msg:
        raise msg + "maximum result unmatch"

    # mean
    try:
        mean_mpg = calcMean(data)
        assert round(data_summary["mpg"]["mean"], 3) == mean_mpg
    except AssertionError as msg:
        raise msg + "mean result unmatch"


if __name__ == "__main__":
    test_pd_descriptive()
