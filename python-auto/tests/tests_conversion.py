# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines initial unit tests to explore API design and specify functionality.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest
from ..convert import convert

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2016 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['test_conversion_spectral_to_YCbCR',
           'test_conversion_YCbCR_to_CIECAM02']


SAMPLE_SPD_DATA = {
    340: 0.0000,
    360: 0.0000,
    380: 0.0000,
    400: 0.0641,
    420: 0.0645,
    440: 0.0562,
    460: 0.0537,
    480: 0.0559,
    500: 0.0651,
    520: 0.0705,
    540: 0.0772,
    560: 0.0870,
    580: 0.1128,
    600: 0.1360,
    620: 0.1511,
    640: 0.1688,
    660: 0.1996,
    680: 0.2397,
    700: 0.2852,
    720: 0.0000,
    740: 0.0000,
    760: 0.0000,
    780: 0.0000,
    800: 0.0000,
    820: 0.0000}


def test_conversion_spectral_to_YCbCR():
    input_spectrum = SAMPLE_SPD_DATA
    convert(input_spectrum, 'spectral', 'YCbCR')


def test_conversion_YCbCR_to_CIECAM02():
    input_colour = np.aray([0, 0, 0])
    convert(input_colour, 'YCbCR', 'CIECAM02')
