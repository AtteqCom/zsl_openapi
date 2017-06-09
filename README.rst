========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/zsl_openapi/badge/?style=flat
    :target: https://readthedocs.org/projects/zsl_openapi
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/AtteqCom/zsl_openapi.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/AtteqCom/zsl_openapi

.. |coveralls| image:: https://coveralls.io/repos/AtteqCom/zsl_openapi/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/AtteqCom/zsl_openapi

.. |codecov| image:: https://codecov.io/github/AtteqCom/zsl_openapi/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/AtteqCom/zsl_openapi

.. |version| image:: https://img.shields.io/pypi/v/zsl-openapi.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/zsl-openapi

.. |commits-since| image:: https://img.shields.io/github/commits-since/AtteqCom/zsl_openapi/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/AtteqCom/zsl_openapi/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/zsl-openapi.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/zsl-openapi

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/zsl-openapi.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/zsl-openapi

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/zsl-openapi.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/zsl-openapi


.. end-badges

Generate OpenAPI specification out of your ZSL service.

* Free software: BSD license

Installation
============

::

    pip install zsl-openapi

Documentation
=============

https://zsl_openapi.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
