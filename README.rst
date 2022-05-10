BISKOTAKI

Project generated from the https://github.com/boromir674/cookiecutter-python-package/tree/master/src/cookiecutter_python cookiecutter

.. start-badges

| |build| |release_version| |wheel| |supported_versions| |gh-lic| |commits_since_specific_tag_on_master| |commits_since_latest_github_release|


|
| **Source Code:** https://github.com/boromir674/biskotaki
| **Pypi Package:** https://pypi.org/project/biskotaki/
|


Features
========


1. **biskotaki** `python package`

   a. TODO **Great Feature**
   b. TODO **Nice Feature**

2. **Test Suite** using `Pytest`
3. **Parallel Execution** of Unit Tests, on multiple cpu's
4. **Automation**, using `tox`

   a. **Code Coverage** measuring
   b. **Build Command**, using the `build` python package
   c. **Pypi Deploy Command**, supporting upload to both `pypi.org` and `test.pypi.org` servers
   d. **Type Check Command**, using `mypy`
   e. **Lint** *Check* and `Apply` commands, using `isort`_ and `black`_
5. **CI Pipeline**, running on `Github Actions`

   a. **Job Matrix**, spanning different `platform`'s and `python version`'s

      1. Platforms: `ubuntu-latest`, `macos-latest`
      2. Python Iterpreters: `3.6`, `3.7`, `3.8`, `3.9`, `3.10`
   b. **Parallel Job** execution, generated from the `matrix`, that runs the `Test Suite`


Prerequisites
=============

You need to have `Python` installed.

Quickstart
==========

Using `pip` is the approved way for installing `biskotaki`.

.. code-block:: sh

    python3 -m pip install biskotaki


TODO demonstrate a use case


License
=======

|gh-lic|

* `GNU Affero General Public License v3.0`_


License
=======

* Free software: GNU Affero General Public License v3.0


.. MACROS/ALIASES

.. start-badges

.. Test Workflow Status on Github Actions for specific branch <branch>

.. |build| image:: https://img.shields.io/github/workflow/status/boromir674/biskotaki/Test%20Python%20Package/master?label=build&logo=github-actions&logoColor=%233392FF
    :alt: GitHub Workflow Status (branch)
    :target: https://github.com/boromir674/biskotaki/actions/workflows/test.yaml?query=branch%3Amaster

.. above url to workflow runs, filtered by the specified branch

.. |release_version| image:: https://img.shields.io/pypi/v/biskotaki
    :alt: Production Version
    :target: https://pypi.org/project/biskotaki/

.. |wheel| image:: https://img.shields.io/pypi/wheel/biskotaki?color=green&label=wheel
    :alt: PyPI - Wheel
    :target: https://pypi.org/project/biskotaki

.. |supported_versions| image:: https://img.shields.io/pypi/pyversions/biskotaki?color=blue&label=python&logo=python&logoColor=%23ccccff
    :alt: Supported Python versions
    :target: https://pypi.org/project/biskotaki

.. |commits_since_specific_tag_on_master| image:: https://img.shields.io/github/commits-since/boromir674/biskotaki/v0.0.3/master?color=blue&logo=github
    :alt: GitHub commits since tagged version (branch)
    :target: https://github.com/boromir674/biskotaki/compare/v0.0.3..master

.. |commits_since_latest_github_release| image:: https://img.shields.io/github/commits-since/boromir674/biskotaki/latest?color=blue&logo=semver&sort=semver
    :alt: GitHub commits since latest release (by SemVer)

.. Github License (eg AGPL, MIT)
.. |gh-lic| image:: https://img.shields.io/github/license/boromir674/biskotaki
    :alt: GitHub
    :target: https://github.com/boromir674/biskotaki/blob/master/LICENSE


.. LINKS

.. _GNU Affero General Public License v3.0: https://github.com/boromir674/biskotaki/blob/master/LICENSE

.. _isort: https://pycqa.github.io/isort/

.. _black: https://black.readthedocs.io/en/stable/
