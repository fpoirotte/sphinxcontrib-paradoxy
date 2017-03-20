"""
    test_embedded
    ~~~~~~~~~~~~~

    Test that embedded URIs work.
"""

import sys
import xml.etree.ElementTree as ET
from sphinx_testing.util import path, with_app
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestExtension(unittest.TestCase):
    def _iter_objects(self, root):
        for compound in root:
            name = compound.find('name').text
            filename = compound.find('filename').text
            yield name, filename

            for member in compound.findall('member'):
                mname = member.find('name').text
                mfilename = member.find('anchorfile').text
                manchor = member.find('anchor').text
                yield (
                    "%s::%s" % (name.replace('::', '\\'), mname),
                    "%s#%s" % (mfilename, manchor)
                )

    def test_basic(self):
        srcdir = path(__file__).dirname() / 'basic'
        tree = ET.parse(path(__file__).dirname() / 'doxygen' / 'Example.xml')
        root = tree.getroot()
        link = '<a class="reference external" ' \
               'href="http://example.com/doc/%s">%s</a>'

        @with_app(buildername='html', srcdir=srcdir, warningiserror=True)
        def execute(app, status, warning):
            app.build()
            contents = (app.outdir / 'contents.html').read_text()
            symbols = {
                'Example':
                    'Regular class',
                'Example::ANSWER':
                    'Regular class constant',
                'Example::$publicMember':
                    'Regular class member',
                'Example::$publicStaticMember':
                    'Regular static class member',
                'Example::publicMethod':
                    'Regular class method',
                'Example::publicStaticMethod':
                    'Regular static class method',
                'Namespaced':
                    'Namespace',
                'Namespaced\\Example':
                    'Namespaced class',
                'Namespaced\\Example::ANSWER':
                    'Namespaced class constant',
                'Namespaced\\Example::$publicMember':
                    'Namespaced class member',
                'Namespaced\\Example::$publicStaticMember':
                    'Namespaced static class member',
                'Namespaced\\Example::publicMethod':
                    'Namespaced class method',
                'Namespaced\\Example::publicStaticMethod':
                    'Namespaced static class method',
            }

            for (name, url) in self._iter_objects(root):
                if name not in symbols:
                    continue
                self.assertIn(link % (url, symbols[name]), contents)

        execute()
