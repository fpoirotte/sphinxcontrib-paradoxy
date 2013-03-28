sphinxcontrib.doxylinks
=======================

Sphinx extension to save typing when linking to some information contained in
a Doxygen documentation.


Installation
------------

Download the latest version of the code from GitHub:
https://github.com/fpoirotte/sphinxcontrib-doxylinks/archive/master.tar.gz

Then, install the extension from the machine's root account::

    root@localhost:~# python setup.py install


How to use
----------

First, load the extension in your ``conf.py``::

    extensions = [
        'sphinxcontrib.doxylinks',
        # other extensions...
    ]

This extension adds two new config values.
The first one is called ``doxylinks`` and is created like this::

    doxylinks = {'exmpl': ('http://example.com/', '/path/to/tagfile'), ...}

The second one is called ``doxylinks_cache_limit`` and indicates
the number of days for which a remote tagfile will be kept in cache
before being considered invalid (and fetched again).
The default value is 1, meaning that remote tagfiles will only be
fetched once per day.

Now you can use e.g. :exmpl:`foo` in your documents.  This will create a
link to the page at ``http://example.com/`` containing the documentation
about the symbol named ``foo``.
The link caption will be the symbol's name, unless an explicit caption
is given, e.g. :exmpl:`Foo <foo>`.

The full path to the symbol is retrieved from the Doxygen tagfile located
at ``/path/to/tagfile``, which can be either a local file or an URL
to some online file.

If ``add_function_parentheses`` is set to ``True`` in your configuration
file and if no explicit caption was given, the symbol will be suffixed
with a set of parentheses whenever this is appropriate.

The following objects can currently be referenced:

-   Custom pages (pass the page's name).
-   Classes (pass the class' name).
-   Interfaces (pass the interface's name).
-   Class methods (pass something like :exmpl:`MyClass::MyMethod`).
-   Class constants (pass something like :exmpl:`MyClass::MY_CONSTANT`).
-   Class variables (pass something like :exmpl:`MyClass::MyVariable`).
    For languages that prefix variables (e.g. PHP), the prefix must be
    included (e.g. :exmpl:`MyClass::$_myVariable`).


Contributing
------------

-   `Fork the code on GitHub`__
-   Patch as necessary
-   Send a pull request

.. __: https://github.com/fpoirotte/sphinxcontrib-doxylinks/fork_select


Bug reports
-----------

Bugs should be reported through the project's issue tracker on GitHub:
https://github.com/fpoirotte/sphinxcontrib-doxylinks/issues.


License and credits
-------------------

This extension is licensed under the 2-clause BSD license.
See the `LICENSE`__ file for more information.

© 2013, François Poirotte <clicky@erebot.net>.

This extension is heavily based on the extlinks and intersphinx extensions
developped by the Sphinx community.

.. __: https://github.com/fpoirotte/sphinxcontrib-doxylinks/blob/master/LICENSE

