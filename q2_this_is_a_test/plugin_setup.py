# ----------------------------------------------------------------------------
# Copyright (c) 2022, <Greg Caporaso>.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Citations, Plugin
from q2_types.feature_table import FeatureTable, Frequency

from q2_this_is_a_test import __version__
import biom

citations = Citations.load("citations.bib", package="q2_this_is_a_test")

plugin = Plugin(
    name="this-is-a-test",
    version=__version__,
    website="https://github.com",
    package="q2_this_is_a_test",
    description="This is a template for building a new QIIME 2 plugin.",
    short_description="",
)


def duplicate_table(table: biom.Table) -> biom.Table:
    return table


plugin.methods.register_function(
    function=duplicate_table,
    inputs={'table': FeatureTable[Frequency]},
    parameters={},
    outputs=[('new_table', FeatureTable[Frequency])],
    input_descriptions={'table': 'The feature table to be duplicated.'},
    parameter_descriptions={},
    output_descriptions={
        'new_table': 'The duplicated feature table.'
    },
    name='Duplicate table',
    description=("Create a copy of a feature table with a new uuid. "
                 "This is for demonstration purposes only."),
    citations=[]
)
