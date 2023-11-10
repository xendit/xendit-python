
import unittest
import os
import sys
from xendit import Configuration, ApiClient, XenditSdkException
from xendit.apis import InvoiceApi
from test.utils.test_utils import TestUtil
from dotenv import load_dotenv

class TestInvoiceAPI(unittest.TestCase):

    def setUp(self):
        test_folder_path = os.path.join(os.getcwd(), 'test')
        load_dotenv(os.path.join(test_folder_path, '.env.test'))

        if os.getenv('DEVELOPMENT_API_KEY') == None:
            print("DEVELOPMENT_API_KEY doesn't exists")

        configuration = Configuration(
            api_key=os.getenv('DEVELOPMENT_API_KEY')
        )
        api_client = ApiClient(configuration)
        self.invoice_api_instance = InvoiceApi(api_client)
        self.ignore_error_codes = os.getenv("IGNORED_ERRORCODE")

    def test_create_invoice(self):
        try:
            external_id = TestUtil.generate_unique_id_for_business(os.getenv("BUSINESS_ID"))
            response = self.invoice_api_instance.create_invoice({
                'external_id': external_id,
                'amount': 1000,
            })

            print("test_create_invoice Resp", response)
            self.assertIsNotNone(response)
            self.assertEqual(response['amount'], 1000)
            self.assertEqual(response['external_id'], external_id)
            self.assertEqual(str(response['status']), "PENDING")
        except XenditSdkException as error:
            print("test_create_invoice", error)

            if error.errorCode not in self.ignore_error_codes:
                raise error

    def test_get_invoice_by_id(self):
        try:
            response = self.invoice_api_instance.get_invoice_by_id("654a103b5e6dfa587b6025c3")

            print("test_get_invoice_by_id Resp", response)
            self.assertIsNotNone(response)
        except XenditSdkException as error:
            print("test_get_invoice_by_id", error)

            if error.errorCode not in self.ignore_error_codes:
                raise error


if __name__ == '__main__':
    unittest.main()
