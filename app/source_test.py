import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('ABC','ABC News','The accurate one','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
    def test_init(self):
       '''
       set up a method that tests if the source object is correctly initiated
       '''
       self.assertEqual(self.new_source.id,"ABC")
       self.assertEqual(self.new_source.name,"ABC News")
       self.assertEqual(self.new_source.description,"The accurate one")
       self.assertEqual(self.new_source.category,"general")

if __name__ == '__main__':
    unittest.main()