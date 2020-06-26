class BaseIntegrationTest:
    def assert_returned_object_has_same_key_as_sample_response(
        self, returned_object, sample_response
    ):
        expected_key_list = [*sample_response]
        actual_key_list = [*(vars(returned_object))]
        assert actual_key_list == expected_key_list
