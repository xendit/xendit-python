import unittest
from dotenv import load_dotenv
import os
from utils.test_utils import TestUtil
import xendit
from xendit.apis import PaymentMethodApi, PaymentRequestApi

class TestPaymentAPI(unittest.TestCase):

    def setUp(self):
        test_folder_path = os.path.join(os.getcwd(), 'test')
        load_dotenv(os.path.join(test_folder_path, '.env.test'))

        configuration = xendit.Configuration(
            api_key=os.getenv('DEVELOPMENT_API_KEY')
        )
        api_client = xendit.ApiClient(configuration)
        self.payment_method_instance = PaymentMethodApi(api_client)
        self.payment_request_instance = PaymentRequestApi(api_client)
        self.ignore_error_codes = os.getenv("IGNORED_ERRORCODE")

    def test_create_card_payment(self):
        try:
            # Create payment method
            pm_response = self.payment_method_instance.create_payment_method(
                payment_method_parameters={
                    'type': "CARD",
                    'reusability': "ONE_TIME_USE",
                    'reference_id': TestUtil.generate_unique_id_for_business(os.getenv("BUSINESS_ID")),
                    'description': "This is a description.",
                    'card': {
                        "currency": "IDR",
                        "channel_properties": {
                            "success_return_url": "https://redirect.me/goodstuff",
                            "failure_return_url": "https://redirect.me/badstuff"
                        },
                        "card_information": {
                            "card_number": "4000000000001091",
                            "expiry_month": "12",
                            "expiry_year": "2027",
                            "cvv": "123",
                            "cardholder_name": "John Doe"
                        }
                    }
                }
            )
            print("Response create_payment_method\n", pm_response)
            self.assertIsNotNone(pm_response)
            self.assertEqual(pm_response.status, "PENDING")

            # Create Payment Request
            pr_response = self.payment_request_instance.create_payment_request(
                payment_request_parameters={
                    "amount": 10000,
                    "currency": "IDR",
                    "payment_method_id": pm_response.id,
                    "description": "This is a description."
                }
            )

            print("Response create_payment_request\n", pr_response)
            self.assertIsNotNone(pr_response)
            self.assertEqual(pr_response.payment_method.id, pm_response.id)
            self.assertEqual(pr_response.status, "REQUIRES_ACTION")
            self.assertTrue(len(pr_response.actions) > 0)


        except Exception as error:
            print("Error test_create_card_payment\n", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

    def test_create_direct_debit_payment(self):
        try:
            # Prerequisite: Having a customer created

            # Create payment method
            pm_response = self.payment_method_instance.create_payment_method(
                payment_method_parameters={
                    "type": "DIRECT_DEBIT",
                    "direct_debit": {
                        "channel_code": "BRI",
                        "channel_properties": {
                            "mobile_number": "+62818555988",
                            "card_last_four": "8888",
                            "card_expiry": "06/24",
                            "email": "email@email.com"
                        }
                    },
                    "reusability": "ONE_TIME_USE",
                    "customer_id": "cust-59660fb7-dcf2-4bb9-b864-f69b081219d7"
                }
            )
            print("Response create_payment_method\n", pm_response)
            self.assertIsNotNone(pm_response)
            self.assertEqual("REQUIRES_ACTION", pm_response.status)
            self.assertTrue(len(pm_response.actions) > 0)

            # Perform Payment Method Authentication
            auth_response = self.payment_method_instance.auth_payment_method(
                payment_method_id=pm_response.id,
                payment_method_auth_parameters={
                    'auth_code': "333000",
                }
            )

            print("Response auth_payment_method",auth_response)
            self.assertIsNotNone(auth_response)
            self.assertEqual(auth_response.status,"ACTIVE")
            self.assertEqual(auth_response.actions, 0)

            # Create Payment Request
            pr_response = self.payment_request_instance.create_payment_request(
                payment_request_parameters={
                    "amount": 1500,
                    "currency": "IDR",
                    "payment_method_id": pm_response.id,
                    "customer_id": "cust-59660fb7-dcf2-4bb9-b864-f69b081219d7",
                    "description": "This is a description.",
                }
            )

            print("Response create_payment_request\n", pr_response)
            self.assertIsNotNone(pr_response)
            self.assertEqual(pr_response.payment_method.id, pm_response.id)
            self.assertEqual(pr_response.status, "REQUIRES_ACTION")
            self.assertTrue(pr_response.actions > 0)

        except Exception as error:
            print("Error test_create_direct_debit_payment\n", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

    def test_create_ewallet_payment(self):
        try:
            # Create payment method
            pm_response = self.payment_method_instance.create_payment_method(
                payment_method_parameters={
                    'type': "EWALLET",
                    'reusability': "ONE_TIME_USE",
                    "customer_id": "cust-59660fb7-dcf2-4bb9-b864-f69b081219d7",
                    'description': "This is a description.",
                    'ewallet': {
                        "channel_code": "OVO",
                        "channel_properties": {
                            "success_return_url": "https://redirect.me/goodstuff",
                            "failure_return_url": "https://redirect.me/badstuff",
                            "cancel_return_url": "https://redirect.me/nostuff"
                        }
                    }
                }
            )
            print("Response create_payment_method\n", pm_response)
            self.assertIsNotNone(pm_response)
            self.assertEqual(pm_response.status, "PENDING")
            self.assertEqual(pm_response.status, "ACTIVE")
            self.assertTrue(len(pm_response.actions) == 0)


            # Create Payment Request
            pr_response = self.payment_request_instance.create_payment_request(
                payment_request_parameters={
                    "amount": 15000,
                    "currency": "IDR",
                    "payment_method_id": pm_response.id,
                    "customer_id": "cust-59660fb7-dcf2-4bb9-b864-f69b081219d7",
                    "description": "This is a description.",
                }
            )

            print("Response create_payment_request\n", pr_response)
            self.assertIsNotNone(pr_response)
            self.assertEqual("PENDING", pr_response.status)
            self.assertEqual(pr_response.payment_method.id, pm_response.id)


        except Exception as error:
            print("Error test_create_ewallet_payment\n", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

    def test_over_the_counter_payment(self):
        try:
            # Create Payment Request and Payment Method bundled
            pr_response = self.payment_request_instance.create_payment_request(
                payment_request_parameters={
                    "amount": 10000,
                    "currency": "IDR",
                    "country": "ID",
                    "payment_method": {
                        "type": "OVER_THE_COUNTER",
                        "reusability": "ONE_TIME_USE",
                        "over_the_counter": {
                            "channel_code": "ALFAMART",
                            "channel_properties": {
                                "customer_name": "John Doe"
                            }
                        }
                    },
                }
            )

            print("Response create_payment_request\n", pr_response)
            self.assertIsNotNone(pr_response)
            self.assertEqual(pr_response.status, "PENDING")

        except Exception as error:
            print("Error test_over_the_counter_payment\n", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

    def test_qr_payment(self):
        try:
            # Create Payment Request and Payment Method bundled
            pr_response = self.payment_request_instance.create_payment_request(
                payment_request_parameters={
                    "amount": 15000,
                    "currency": "IDR",
                    "payment_method": {
                        "type": "QR_CODE",
                        "reusability": "ONE_TIME_USE",
                        "qr_code": {
                            "channel_code": "DANA"
                        }
                    },
                    "description": "sample description",
                }
            )

            print("Response create_payment_request\n", pr_response)
            self.assertIsNotNone(pr_response)
            self.assertEqual(pr_response.status, "PENDING")

        except Exception as error:
            print("Error test_qr_payment\n", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

    def test_virtual_account_payment(self):
        try:
            # Create Payment Request and Payment Method bundled
            pr_response = self.payment_request_instance.create_payment_request(
                payment_request_parameters={
                    "currency": "IDR",
                    "amount": 100000,
                    "payment_method": {
                        "type": "VIRTUAL_ACCOUNT",
                        "reusability": "ONE_TIME_USE",
                        "reference_id": TestUtil.generate_unique_id_for_business(os.getenv("BUSINESS_ID")),
                        "virtual_account": {
                            "channel_code": "BRI",
                            "channel_properties": {
                                "customer_name": "John Doe"
                            }
                        }
                    },
                    "metadata": {
                        "sku": "ABCDEFGH"
                    }
                }
            )

            print("Response create_payment_request\n", pr_response)
            self.assertIsNotNone(pr_response)
            self.assertEqual(pr_response.status, "PENDING")

        except Exception as error:
            print("Error test_virtual_account_payment\n", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

    def test_get_payment_method(self):
        try:
            # Create Payment Request and Payment Method bundled
            pm_response = self.payment_method_instance.get_payment_method_by_id(payment_method_id="pm-89a09e44-3a9f-4bf3-903e-3f68ec170723")

            print("Response get_payment_method_by_id\n", pm_response)
            self.assertIsNotNone(pm_response)

        except Exception as error:
            print("Error test_get_payment_method\n", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

    def test_get_payment_request(self):
        try:
            # Create Payment Request and Payment Method bundled
            pr_response = self.payment_request_instance.get_payment_request_by_id(payment_request_id="pr-6fd4595a-d6da-4939-9b65-b9f57ebf78dc")

            print("Response get_payment_request_by_id\n", pr_response)
            self.assertIsNotNone(pr_response)

        except Exception as error:
            print("Error test_get_payment_request\n", error)

            if type(error) == xendit.XenditSdkException and error.errorCode not in self.ignore_error_codes:
                raise error

if __name__ == '__main__':
    unittest.main()
