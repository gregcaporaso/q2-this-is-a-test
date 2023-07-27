# ----------------------------------------------------------------------------
# Copyright (c) 2022, <Greg Caporaso>.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

setup(
    name="q2-this-is-a-test",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="Greg Caporaso",
    author_email="greg.caporaso@nau.edu",
    description="This is a test.",
    url="https://github.com/",
    entry_points={
        "qiime2.plugins": ["q2-this-is-a-test=q2_this_is_a_test.plugin_setup:plugin"]
    },
    package_data={
        "q2_this_is_a_test": ["citations.bib"],
    },
    zip_safe=False,
)
