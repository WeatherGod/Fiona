# testing features, to be called by nosetests

import logging
import sys
import unittest

from fiona import collection
from fiona.ogrext import featureRT

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class PointTest(unittest.TestCase):
    def test_point(self):
        f = { 'id': '1', 
              'geometry': {'type': 'Point', 'coordinates': (0.0, 0.0)},
              'properties': {'title': u'foo'} }
        schema = {'geometry': 'Point', 'properties': {'title': 'str'}}
        with collection("/tmp/foo.shp", "w", "ESRI Shapefile", schema) as c:
            g = featureRT(f, c)
            self.failUnless(g.has_key('id'))
            self.failUnlessEqual(g['properties']['title'], 'foo')

