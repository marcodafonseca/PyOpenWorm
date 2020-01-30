from __future__ import absolute_import
from .DataTestTemplate import _DataTest

from PyOpenWorm.plot import Plot


class PlotTest(_DataTest):
    ctx_classes = (Plot,)

    def test_no_data_error(self):
        """
        Is the correct error raised when we try to
        do get_data with no data?
        """
        pl = self.ctx.Plot()
        self.assertIsNone(pl.get_data())

    def test_incorrect_input_error(self):
        """
        Is the correct error raised when we try to instantiate
        with non-2D-list data?
        """
        with self.assertRaises(ValueError):
            self.ctx.Plot(data=['a', 'b'])

    def test_successful_get_data(self):
        """
        Can we retrieve the data we input?
        """
        ary = [[1, 2], [3, 4]]
        pl = self.ctx.Plot(data=ary)
        assert pl.get_data() == ary
