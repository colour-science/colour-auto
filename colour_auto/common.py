#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Colour Auto
"""

from __future__ import absolute_import

import networkx as nx

from colour.metadata.common import Metadata
import colour.metadata.models

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2016 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__application_name__ = 'Colour-auto'


def get_all_model_functions():
    """
    Return all models from the family 'Colour Model'.
    """
    metadata_instances = Metadata._INSTANCES
    for metadata_instance_key, metadata_instance in \
            metadata_instances.items():
        if metadata_instance._FAMILY == 'Colour Model Function':
            yield metadata_instance


def build_conversion_graph():
    conversion_graph = nx.MultiDiGraph()
    for model_function in get_all_model_functions():
        conversion_graph.add_edge(model_function.input_entity,
                                  model_function.output_entity)
    return conversion_graph


CONVERSION_GRAPH = build_conversion_graph()

if __name__ == '__main__':
    from pprint import pprint

    print("#" * 69)
    print("Conversion graph nodes:")
    print("-" * 69)
    pprint(list(CONVERSION_GRAPH.nodes()))
    print("#" * 69)
    print("Conversion graph edges:")
    print("-" * 69)
    pprint(list(CONVERSION_GRAPH.edges()))
    print("#" * 69)
