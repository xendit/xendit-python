
import unittest
from dotenv import load_dotenv
import os
import xendit
from xendit.apis import InvoiceApi

from utils.test_utils import TestUtil

class TestInvoiceAPI(unittest.TestCase):

    def setUp(self):
        test_folder_path = os.path.join(os.getcwd(), 'test')
        load_dotenv(os.path.join(test_folder_path, '.env.test'))

        configuration = xendit.Configuration(
            api_key=os.getenv('DEVELOPMENT_API_KEY')
        )
        api_client = xendit.ApiClient(configuration)
        self.invoice_api_instance = InvoiceApi(api_client)
        self.ignore_error_codes = os.getenv("IGNORED_ERRORCODE")

    def test_create_invoice(self):
        try:
            external_id = TestUtil.generate_unique_id_for_business(os.getenv("BUSINESS_ID"))
            response = self.invoice_api_instance.create_invoice({
                'external_id': external_id,
                'amount': 1000,
            })

            self.assertIsNotNone(response)
            self.assertEqual(response['amount'], 1000)
            self.assertEqual(response['externalId'], external_id)
        except Exception as error:
            print("test_create_invoice", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

    def test_get_invoice_by_id(self):
        try:
            response = self.invoice_api_instance.get_invoice_by_id("654a103b5e6dfa587b6025c3")

            self.assertIsNotNone(response)
        except Exception as error:
            print("test_get_invoice_by_id", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error


if __name__ == '__main__':
    unittest.main()
