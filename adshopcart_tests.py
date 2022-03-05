import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdshopcartPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_adshopcarttest():
        methods.setUp()
        methods.createnewaccount()
        methods.myaccount()
        methods.shoppingcart()
        methods.signout()
        methods.signin()
        methods.deleteuser()
        methods.checkifuserisdeleted()
        methods.displays()
        methods.tabs()
        methods.contactus()
        methods.tearDown()
