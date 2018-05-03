.. -*-restructuredtext-*-

russellcapping: Single level FTSE Russell Capping Methodology implementation
============================================================================

.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
    :target: https://www.python.org/

.. image:: https://img.shields.io/pypi/v/russellcapping.svg
    :target: https://pypi.org/project/russellcapping/

.. image:: https://img.shields.io/pypi/l/russellcapping.svg
    :target: https://pypi.org/project/russellcapping/

.. image:: https://img.shields.io/pypi/pyversions/russellcapping.svg
    :target: https://pypi.org/project/russellcapping/

Installation
------------

To install russellcapping, simply use pip:

.. code:: bash

    $ pip install russellcapping

or install directly from source to include latest changes:

.. code:: bash

    $ pip install git+https://github.com/saporitigianni/russellcapping.git

or clone and then install:

.. code:: bash

    $ git clone https://github.com/saporitigianni/russellcapping.git
    $ cd russellcapping
    $ python3 setup.py install

Usage
-----

.. code:: python

    import russellcapping as rc

    # Constructor takes in total market cap, data for the individual constituents and a capping percentage
    item = rc.RussellCapping(total_mc=sample_mc, raw_data=sample_data, capping_percent=10)

    # Run capping method which returns the data adjusted for the capping percent and the new market cap
    new_data, new_mc = item.russell_capping()


Acknowledgements
----------------

An original publication of the FTSE Russell capping methodology can be found `here <http://www.ftse.com/products/downloads/Capping_Methodology_Guide.pdf>`_.

Contributing
------------

Please read the `CONTRIBUTING <https://github.com/saporitigianni/russellcapping/blob/master/CONTRIBUTING.md>`_ document before making changes that you would like adopted in the code.

Code of Conduct
---------------

Everyone interacting in the ``russellcapping`` project's codebase, issue
trackers, chat rooms, and mailing lists is expected to follow the
`PyPA Code of Conduct <https://www.pypa.io/en/latest/code-of-conduct/>`_.

Buy me a coffee?
----------------

| ETH 0xaD1F09626b9B8e701D5f0F4a237193Df73d3C445
| BTC 199zsVqCusefv8yjdYQhUQZmLCyh75dqNV
| LTC LUBqs7VxC43ttPsQuM1jaZFmshKTAU1Rs9
