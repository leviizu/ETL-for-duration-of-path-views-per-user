import os
import pandas as pd
from etl_app import Loader
import pytest


class TestLoader:
    @pytest.fixture
    def loader_instance(self):
        # Set up a Loader instance for testing
        filename = 'test_file.csv'
        loader = Loader(filename)
        yield loader
        # Removing the test file if it exists
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

    def test_write_to_file(self, loader_instance):
        """
        Test the write_to_file method of the Loader class.
        """

        # GIVEN: A Loader instance and expected data to write to a file
        expected_data = pd.DataFrame({'foo': ['foobar', 'barfoo', 'foobar'], 'bar': [4, 5, 6], 'bar2': [4, 5, 6]})

        # WHEN: The write_to_file method is called with the expected data
        loader_instance.write_to_file(expected_data)

        # THEN: The file is written, and the actual data read from the file matches the expected data
        actual_data = pd.read_csv(loader_instance.filename, index_col=0)
        pd.testing.assert_frame_equal(actual_data, expected_data)

