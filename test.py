import unittest
import numpy as np
import pandas as pd
from MLmodels import array, weather_y, weather_X, train_y, train_X, test_y, test_X, test_size

class TestDataSets(unittest.TestCase):

    def test_array_type(self):
        """
        Test that read data is stored as an array
        """
        random_array = np.arange(1,2)           # arbitrary array range
        self.assertEqual(type(array), type(random_array))

    def test_array_length(self):
        """
        Test that all original csv file data has been collected
        """
        self.assertEqual(len(array), 359448)

    def test_validation_set(self):
        """
        Test that validation set is of appropriate type ('numpy.float64')
        """
        x = np.float_(1.01)     # arbitrary choice of float value
        self.assertEqual(type(weather_y[0]), type(x))

    def test_training_set(self):
        """
        Test that training set is of appropriate type ('pandas.core.frame.DataFrame')
        """
        x = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        self.assertEqual(type(weather_X), type(x)), "weather_X values are not 'pandas.core.frame.DataFrame'"

    def test_correct_split_X(self):
        """
        Test that the test size chosen in train_test_split creates the correct training and test set sizes
        for weather_X
        """
        a = len(train_X[:])     # number of data entries in training set
        b = len(test_X[:])      # same for test set
        total_sum = a + b
        test_fraction = b / total_sum
        self.assertEqual(test_size, round(test_fraction, 2))

    def test_correct_split_y(self):
        """
        Test that the test size chosen in train_test_split creates the correct training and test set sizes
        for weather_y
        """
        a = len(train_y[:])     # number of data entries in training set
        b = len(test_y[:])      # same for test set
        total_sum = a + b
        test_fraction = b / total_sum
        self.assertEqual(test_size, round(test_fraction, 2))


if __name__ == '__main__':
    unittest.main()
