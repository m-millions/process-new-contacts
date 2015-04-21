from __future__ import print_function

import unittest
from process_new_contacts import get_new_contacts, get_clean_data, \
                                 process_contacts


class TestProcessNewContactData(unittest.TestCase):
    def setUp(self):
        self.r0 = ['George Won', 'aqua marine', '97148', ' 488 084 5794 ']
        self.r1 = [' Mario G. Humperdink', 'red', '36410', '(839) 014-8051']
        self.r2 = ['Shanika', 'Dodd', '82733', ' 940 - 761-0886 ', 'pink']

        self.name1 = ['Mario', 'G.', 'Humperdink']

        self.clean_r0 = ['GeorgeWon', 'aquamarine', '97148', '4880845794']
        self.name0 = ['George', 'Won']
        self._RNUM0 = 0

        self.clean_r1 = ['MarioG.Humperdink', 'red', '36410', '8390148051']
        self.name1 = ['Mario', 'G.', 'Humperdink']
        self._RNUM1 = 1

        self.clean_r2 = ['Shanika', 'Dodd', '82733', '9407610886', 'pink']
        self.name2 = ['Shanika', 'Dodd']
        self._RNUM2 = 2

        self.colors = ['yellow', 'aquamarine', 'blue', 'gray', 'pink', 'red',
                       'green']

        print ("setUp was successfully executed!")

    def test_get_new_contacts(self):
    	pass

    '''
    Tests of all successful data transformations
    Todo: Make an iterative approach
    '''
    def	test_get_clean_data(self):
        #Len 4 record with name split resulting in first_name, and
        #last_name
        self.assertEqual(get_clean_data(self.r0),
                         ['GeorgeWon', 'aquamarine', '97148', '4880845794'])

        #Len 4 record with name split resulting in first_name, middle, and
        #last_name
        self.assertEqual(get_clean_data(self.r1),
                         ['MarioG.Humperdink', 'red', '36410', '8390148051'])

        #Len 5 record with no name split, resulting in first_name and last_name
        self.assertEqual(get_clean_data(self.r2),
                         ['Shanika', 'Dodd', '82733', '9407610886', 'pink'])

    def test_process_contacts(self):
    	#Len 4 record with name split resulting in first_name, and
        #last_name - full name populated from self.name0
        self.assertEqual(process_contacts(self.clean_r0, self.name0,
                                          self._RNUM0),
                         {"middle": " ", "firstname": "George",
                          "color": "aquamarine", "lastname": "Won",
                          "zipcode": "97148", "telephone": "4880845794"})

        #Len 4 record with name split resulting in first_name, middle, and
        #last_name - full name populated from self.name1
        self.assertEqual(process_contacts(self.clean_r1, self.name1,
                                          self._RNUM1),
                         {"middle": "G.", "firstname": "Mario",
                          "color": "red", "lastname": "Humperdink",
                          "zipcode": "36410", "telephone": "8390148051"})

        #Len 5 record with no name split, resulting in first_name and last_name
        # - full name populated from self.clean_r2
        self.assertEqual(process_contacts(self.clean_r2, self.name2,
                                          self._RNUM2),
                         {"middle": " ", "firstname": "Shanika",
                          "color": "pink", "lastname": "Dodd",
                          "zipcode": "82733", "telephone": "9407610886"})

        #Test to makes sure the value returned for color is indeed one of the
        #colors expected - If color is two or more words all spaces between
        #letters would have been removed
        return_value = process_contacts(self.clean_r0, self.name0, self._RNUM0)
        self.assertIn(return_value['color'], self.colors, 'incorrect color \
                                                           passed.')

    def tearDown(self):
        self.r0 = None
        self.r1 = None
        self.r2 = None

        self.clean_r0 = None
        self.clean_r1 = None
        self.clean_r2 = None

        self.name0 = None
        self.name1 = None
        self.name2 = None

        self._RNUM0 = 0
        self._RNUM1 = 0
        self._RNUM2 = 0

        self.colors = None

        print ("tearDown was successfully executed!")

suite = unittest.TestLoader().loadTestsFromTestCase(TestProcessNewContactData)
unittest.TextTestRunner(verbosity=2).run(suite)
