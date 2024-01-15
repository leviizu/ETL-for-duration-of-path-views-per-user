import pandas as pd
import pytest
from etl_app import Transformer


class TestTransformer:
    @pytest.fixture
    def mock_extracted_data(self):
        # Creating mock data for testing
        extracted_data = [
            pd.DataFrame({'user_id': ['101', '202', '101', '202'],
                          'user_agent': ['Mozilla/5.0 (iPhone)', 'Mozilla/5.0 (windows)', 'Mozilla/5.0 (iPhone)',
                                         'Mozilla/5.0 (windows)'],
                          'length': [7, 9, 6, 8],
                          'drop': [1, 0, 0, 1],
                          'path': ['/features/desktop', '/tutorial/step-one', '/features/desktop',
                                   '/tutorial/step-one']}),
        ]
        return extracted_data

    @pytest.fixture
    def mock_aggregated_data(self):
        # Creating mock data for testing
        mock_aggregated_data = pd.DataFrame({
            'user_id': ['101', '202'],
            'path': ['/features/desktop', '/tutorial/step-one'],
            'length': [13, 17]
        })
        return mock_aggregated_data

    def test_aggregate_data(self, mock_extracted_data):
        """
        Test the aggregate_data method of the Transformer class.
        """

        # GIVEN: Mock extracted data is available
        mock_data = mock_extracted_data

        # WHEN: The aggregate_data method is called with the mock data
        aggregate = Transformer()
        actual_result = aggregate.aggregate_data(mock_data)

        # THEN: The result matches the expected aggregated data
        expected_result = pd.DataFrame({
            'user_id': ['101', '202'],
            'path': ['/features/desktop', '/tutorial/step-one'],
            'length': [13, 17]
        })
        pd.testing.assert_frame_equal(actual_result, expected_result)

    def test_pivot_data(self, mock_aggregated_data):
        """
        Test the pivot_data method of the Transformer class.
        """

        # GIVEN: Mock aggregated data is available
        mock_data = mock_aggregated_data

        # WHEN: The pivot_data method is called with the mock data
        pivot = Transformer()
        actual_result = pivot.pivot_data(mock_data)

        # THEN: The result matches the expected pivoted data
        expected_result = pd.DataFrame({
            'user_id': ['101', '202'],
            'path': ['/features/desktop', '/tutorial/step-one'],
            'length': [13, 17]}).pivot(index='user_id', columns='path', values='length').fillna(0)

        pd.testing.assert_frame_equal(actual_result, expected_result)
        assert len(expected_result) == 2
