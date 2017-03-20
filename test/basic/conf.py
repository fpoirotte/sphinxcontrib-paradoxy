from os import path

extensions = ['sphinxcontrib.paradoxy']
exclude_patterns = ['_build']
version = '1.2.3'

paradoxy = {
    'example': (
        'http://example.com/doc/',
        path.join(path.dirname(path.abspath('.')), 'doxygen', 'Example.xml')
    ),
}
