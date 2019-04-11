#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Colour Auto
"""

from __future__ import absolute_import

import networkx as nx

from colour.metadata import models
from colour.metadata.common import Metadata

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Developement'

__application_name__ = 'Colour-auto'


def get_all_colour_model_functions():
    """
    Yields all model functions from the family 'Colour Model Functions'.
    """
    metadata_instances = Metadata._INSTANCES
    for metadata_instance_key, metadata_instance in \
            metadata_instances.items():
        if metadata_instance._FAMILY == 'Colour Model Function':
            yield metadata_instance


def build_conversion_graph():
    """
    Return conversion graph that contains all colour model functions as edges.

    Returns
    -------
    networkx.MultiDiGraph
        Directed Graph of all colour model conversion fucntions.
    """

    # TODO: Check for multiple edges between the same nodes.
    conversion_graph = nx.DiGraph()
    for model_function in get_all_colour_model_functions():
        conversion_graph.add_edge(model_function.input_entity.name,
                                  model_function.output_entity.name,
                                  attr_dict={
                                      'conversion_function': model_function})
    return conversion_graph


CONVERSION_GRAPH = build_conversion_graph()


def get_conversion_functions(start_model, target_model):
    """
    Return list of conversion functions that can be applied subsequently to
    reach the target model from the start model.

    Returns
    -------
    list
        List of conversion functions.
    """
    conversion_path = nx.shortest_path(CONVERSION_GRAPH,
                                       start_model,
                                       target_model)
    conversion_functions = []
    for n1, n2 in zip(conversion_path[:-1], conversion_path[1:]):
        conversion_functions.append(
            CONVERSION_GRAPH[n1][n2]["conversion_function"].callable)

    return conversion_functions


if __name__ == '__main__':
    from pprint import pprint

    print(models)

    print("#" * 69)
    print("Conversion graph nodes:")
    print("-" * 69)
    pprint(list(CONVERSION_GRAPH.nodes()))
    print("#" * 69)
    print("Conversion graph edges:")
    print("-" * 69)
    pprint(list(CONVERSION_GRAPH.edges()))
    print("#" * 69)

    print(get_conversion_functions('CIE XYZ', "CIE LCHab"))
