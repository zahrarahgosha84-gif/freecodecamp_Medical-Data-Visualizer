import unittest
import medical_data_visualizer


class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "variable")
        self.assertEqual(self.ax.get_ylabel(), "total")


class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heat_map_labels(self):
        actual = [label.get_text() for label in self.ax.get_xticklabels()]
        expected = [
            "id",
            "age",
            "sex",
            "height",
            "weight",
            "ap_hi",
            "ap_lo",
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "cardio",
            "overweight",
        ]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
