sphinxcontrib.paradoxy
=======================

`Sphinx`__ extension to save typing when linking to some information
contained in a `Doxygen`__ documentation.

.. __: http://sphinx-doc.org/
.. __: http://www.doxygen.org/


Installation
------------

Installing this extension is done in just a few steps:

-   Download the latest version of the code from GitHub:
    https://github.com/fpoirotte/sphinxcontrib-paradoxy/archive/master.tar.gz

-   Extract the contents of the archive and go into the newly created directory.

-   Then, install the extension from the machine's root account::

        root@localhost:~# python setup.py install

Please note that it is also possible to build a Debian package
for the extension (see below), which makes it easier to uninstall
the extension afterwards.


Debian package
--------------

If like me you prefer installing softwares from packages instead of sources
to ease maintenance, here's a quick guide on how to build a package for
this extension on Debian testing:

-   Make sure the following packages are installed beforehand:

    -   debhelper
    -   python-all
    -   python-setuptools

-   Download the latest version of the code from GitHub:
    https://github.com/fpoirotte/sphinxcontrib-paradoxy/archive/master.tar.gz

-   Rename the tarball into: ``sphinxcontrib-paradoxy_<version>.orig.tar.gz``,
    where ``<version>`` matches the version string defined in `setup.py`__.

-   Extract the tarball and go to the newly created directory.

-   Build the package by running ``dpkg-buildpackage``.

-   Install the newly created package with
    ``sudo dpkg -i ../python-sphinxcontrib.paradoxy_*_all.deb``

Other .deb-based distributions and older Debian releases may require some
tweaking in the `packaging directory`__ for a package to be built correctly.

.. __: https://github.com/fpoirotte/sphinxcontrib-paradoxy/blob/master/setup.py
.. __: https://github.com/fpoirotte/sphinxcontrib-paradoxy/blob/master/debian/


Prerequisites
-------------

The following packages must be installed on your machine for this extension
to work:

-   python (2.6.x or 2.7.x).
    The code has not been tested under Python 3.x.y yet.
-   python-sphinx (1.0.7 or later)
-   python-lxml (2.3.2 is known to work, others probably work too)

You will also need a Doxygen tagfile for the project you want to link to.
Such a tagfile can be generated by setting the option ``GENERATE_TAGFILE``
in your Doxyfile to the path where you want the file to be generated
and then running doxygen.


How to use
----------

First, load the extension in your ``conf.py``::

    extensions = [
        'sphinxcontrib.paradoxy',
        # other extensions...
    ]

This extension adds two new config values.
The first one is called ``paradoxy`` and is created like this::

    paradoxy = {'exmpl': ('http://example.com/', '/path/to/tagfile'), ...}

The second one is called ``paradoxy_cache_limit`` and indicates
the number of days a remote tagfile will be kept in cache before
being considered invalid (which will cause it to be fetched again
the next time ``sphinx-build`` is run).
The default value is 1, meaning that remote tagfiles will only be
fetched once per day. Set the value to 0 to disable caching entirely.

Now you can use e.g. :exmpl:`foo` in your documents.  This will create a
link to the page at ``http://example.com/`` containing the documentation
about the symbol named ``foo``.
The link caption will be the symbol's name, unless an explicit caption
is given, e.g. :exmpl:`Foo <foo>`.

The full path to the symbol is retrieved from the Doxygen tagfile located
at ``/path/to/tagfile``, which can be either a local file or an URL
to some online file.

If `add_function_parentheses`__ is set to ``True`` in your ``conf.py``
and if no explicit caption was given, the symbol will be suffixed
with a set of parentheses whenever this is appropriate.

.. __: http://sphinx-doc.org/config.html#confval-add_function_parentheses

The following objects can currently be referenced:

-   Custom pages (e.g. :exmpl:`My_custom_page`).
-   Classes (e.g. :exmpl:`MyClass`).
-   Interfaces (e.g. :exmpl:`MyInterface`).
-   Class methods (e.g. :exmpl:`MyClass::MyMethod`).
-   Class constants (e.g. :exmpl:`MyClass::MY_CONSTANT`).
-   Class variables (e.g. :exmpl:`MyClass::MyVariable`).
    For languages that prefix variables (e.g. PHP), the prefix must also
    be included (e.g. :exmpl:`MyClass::$_myVariable`).


Contributing
------------

-   `Fork the code on GitHub`__
-   Patch as necessary
-   Send a pull request

.. __: https://github.com/fpoirotte/sphinxcontrib-paradoxy/fork_select


Bug reports
-----------

Bugs should be reported through the project's issue tracker on GitHub:
https://github.com/fpoirotte/sphinxcontrib-paradoxy/issues.


License and credits
-------------------

This extension is licensed under the 2-clause BSD license.
See the `LICENSE`__ file for more information.

© 2013, François Poirotte <clicky@erebot.net>.

This extension is heavily based on the extlinks and intersphinx extensions
developped by the Sphinx community.

.. __: https://github.com/fpoirotte/sphinxcontrib-paradoxy/blob/master/LICENSE

