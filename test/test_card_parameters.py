"""
    The version of the XENDIT API: 2.86.1
"""


import sys
import unittest

import xendit
from xendit.payment_method.model.card_channel_properties import CardChannelProperties
from xendit.payment_method.model.card_parameters_card_information import CardParametersCardInformation
globals()['CardChannelProperties'] = CardChannelProperties
globals()['CardParametersCardInformation'] = CardParametersCardInformation
from xendit.payment_method.model.card_parameters import CardParameters


class TestCardParameters(unittest.TestCase):
    """CardParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCardParameters(self):
        """Test CardParameters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CardParameters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
