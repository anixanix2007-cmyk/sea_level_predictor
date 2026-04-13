import unittest
import sea_level_predictor
import matplotlib as mpl
import numpy as np

class SeaLevelTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected plot title to be 'Rise in Sea Level'")

    def test_plot_labels(self):
        actual_x = self.ax.get_xlabel()
        actual_y = self.ax.get_ylabel()
        self.assertEqual(actual_x, "Year", "Expected x-label to be 'Year'")
        self.assertEqual(actual_y, "Sea Level (inches)", "Expected y-label to be 'Sea Level (inches)'")

    def test_plot_data_points(self):
        # Check if the number of lines of best fit is correct
        actual = len(self.ax.get_lines())
        expected = 2
        self.assertEqual(actual, expected, "Expected 2 lines of best fit.")