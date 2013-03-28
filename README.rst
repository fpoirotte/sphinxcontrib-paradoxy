doxylinks
=========

Sphinx extension to save typing when linking to some information contained in
a Doxygen documentation.

This adds two new config values.
The first one is called ``doxylinks`` and is created like this::

   doxylinks = {'exmpl': ('http://example.com/', '/path/to/tagfile'), ...}

The second one is called ``doxylinks_cache_limit`` and indicates
the number of days for which a remote tagfile will be kept in cache
before being considered invalid (and fetched again).
The default value is 1, meaning that remote tagfiles will only be
fetched once per day.

Now you can use e.g. :exmpl:`foo` in your documents.  This will create a
link to a page hosted at ``http://example.com/`` and containing the
documentation about the symbol named ``foo``.  The link caption will be
the full URL, unless an explicit caption is given, e.g. :exmpl:`Foo <foo>`.

The full path to the symbol is retrieved from the Doxygen tagfile located
at ``/path/to/tagfile``, which can be either a local file or an URL
to some online file.

This extension is heavily based on the extlinks and intersphinx extensions.
