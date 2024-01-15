import pytest
import pandas as pd
from io import BytesIO
from unittest.mock import patch, Mock
from etl_app import Extractor


class TestExtractor:
    root_url = "https://example.com/"
    beginning = "A"
    ending = "C"
    content = "1,2,3\n4,5,6\n7,8,9"

    @pytest.fixture
    def mock_requests_get(self):
        with patch('requests.get') as mock_get:
            yield mock_get

    @pytest.fixture
    def mock_download_data(self, mocker):
        return mocker.patch.object(Extractor, 'download_data', autospec=True)

    @staticmethod
    def setup_extractor(file):
        """
        Common setup for creating an Extractor instance and a mock response.
        """
        extractor = Extractor(TestExtractor.root_url, TestExtractor.beginning, TestExtractor.ending)
        mock_response = Mock()
        mock_response.content = TestExtractor.content.encode()
        return extractor, mock_response

    def test_download_data(self, mock_requests_get):
        """
        Test the download_data method of the Extractor class.
        """
        # GIVEN: A configured Extractor instance and a mock response from requests.get
        file = "A.csv"
        extractor, mock_response = self.setup_extractor(file)
        mock_requests_get.return_value = mock_response

        # WHEN: The download_data method is called
        result = extractor.download_data(file)

        # THEN: The method should make a request, and the result should match the expected DataFrame
        mock_requests_get.assert_called_once_with(f"{TestExtractor.root_url}{file}")
        assert result.equals(pd.read_csv(BytesIO(TestExtractor.content.encode())))

    @pytest.mark.parametrize("file, content", [("A.csv", "1,2,3\n4,5,6\n7,8,9")])
    def test_extract_data(self, mock_download_data, file, content):
        """
        Test the extract_data method of the Extractor class.

        """
        # GIVEN: A configured Extractor instance and mocked download_data method
        extractor, mock_response = self.setup_extractor(file)
        mock_download_data.return_value = pd.read_csv(BytesIO(mock_response.content))

        # WHEN: The extract_data method is called
        result = extractor.extract_data()

        # THEN: The method should call download_data for each file, and the result should match the expected list of
        # DataFrames
        assert len(result) == len(extractor.files)
        for i, file_data in enumerate(result):
            assert file_data.equals(pd.read_csv(BytesIO(content.encode())))

            mock_download_data.assert_any_call(extractor, file=extractor.files[i])
