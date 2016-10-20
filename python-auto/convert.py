# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines utility functions to enable easy conversion between colour models.
"""

from __future__ import division, unicode_literals

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2016 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['convert']


def convert(input_colour, from_model_name, target_model_name, **path_options):
    """
    Return colour in target representation.

    Parameters
    ----------
    input_colour : array_like
        Input colour value that will be converted to target model.
    from_model_name : array_like
        Name of input colour model.
    target_model_name : array_like
        Name of target colour model.
    path_options : dict
        Additional options that might be required to for a successful
        conversion, or to modify the conversion path.

    Returns
    -------
    ndarray
        Colour in target colour model.
    """
    raise NotImplementedError()
