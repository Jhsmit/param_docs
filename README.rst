==========
param_docs
==========


.. image:: https://img.shields.io/pypi/v/param_docs.svg
        :target: https://pypi.python.org/pypi/param_docs

.. image:: https://img.shields.io/travis/Jhsmit/param_docs.svg
        :target: https://travis-ci.com/Jhsmit/param_docs

.. image:: https://readthedocs.org/projects/param-docs/badge/?version=latest
        :target: https://param-docs.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Test package for generating docs from param.Parameterized classes


* Free software: MIT license
* Documentation: https://param-docs.readthedocs.io.


Features
--------

This an example project of how to customize sphinx autodoc generation from param.Parameterized classes. The aim is to generate docs which are informative for users of the web application, where components are by ``param.Parameterized subclass`` 'controllers'. 
Numpydoc style docstrings are assumed for normal (non ``Parameterized``) classes, which is supressed for ``Parameterized`` classes.




Credits
-------
The code for formatting docstrings is based on Pyviz' nbsite paramdoc_ 

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _paramdoc: https://github.com/pyviz-dev/nbsite/blob/master/nbsite/paramdoc.py
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
 
