from collections import Counter


class BaseIntegrationTest:
    def assert_returned_object_has_same_key_as_sample_response(
        self, returned_object, sample_response
    ):
        """
        Assert the returned object have the same keys as the given sample response.
        The comparison are done with the assumption that both of them doesn't have the same order.
        """
        expected_key_list = [*sample_response]
        actual_key_list = [*(vars(returned_object))]
        assert Counter(actual_key_list) == Counter(expected_key_list)
