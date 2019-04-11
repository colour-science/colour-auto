# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines initial unit tests to explore API design and specify functionality.
"""

from __future__ import division, unicode_literals

import numpy as np

from colour_auto import convert_colour

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['test_CIEXYZ_to_CIELab_conversion',
           ]


def test_CIEXYZ_to_CIELab_conversion():
    def XYZ_to_Lab(XYZ):
        return convert_colour(XYZ, 'CIE XYZ', "CIE Lab")

    np.testing.assert_almost_equal(
        XYZ_to_Lab(np.array([0.07049534, 0.10080000, 0.09558313])),
        np.array([37.98562910, -23.62907688, -4.41746615]),
        decimal=7)

    np.testing.assert_almost_equal(
        XYZ_to_Lab(np.array([0.47097710, 0.34950000, 0.11301649])),
        np.array([65.70971880, 41.56438554, 37.78303554]),
        decimal=7)

    np.testing.assert_almost_equal(
        XYZ_to_Lab(np.array([0.25506814, 0.19150000, 0.08849752])),
        np.array([50.86223896, 32.76150086, 20.25483590]),
        decimal=7)
