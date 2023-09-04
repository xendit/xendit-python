"""
    The version of the XENDIT API: 1.4.2
"""


import sys
import unittest

import xendit
from xendit.invoice.model.notification_channel import NotificationChannel
globals()['NotificationChannel'] = NotificationChannel
from xendit.invoice.model.notification_preference import NotificationPreference


class TestNotificationPreference(unittest.TestCase):
    """NotificationPreference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotificationPreference(self):
        """Test NotificationPreference"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotificationPreference()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
