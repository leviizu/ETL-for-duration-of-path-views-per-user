import pandas as pd
import requests
from io import BytesIO


class Extractor:
    """
    Extractor for extracting data from a s3 bucket via url
    """
    def __init__(self, root_url: str, beginning: str, ending: str):
        """
        Initialize the Extractor
        :param root_url: Root URL for data extraction
        :param beginning: Starting character for file names
        :param ending: Ending character for file names
        """
        self.root_url = root_url
        self.files = [chr(i) + ".csv" for i in range(ord(beginning), ord(ending) + 1)]

    def download_data(self, file):
        """
        Download data from a specified file in the S3 bucket via URL.

        This method sends a GET request to the specified file URL in the S3 bucket, retrieves the data,
        and returns it as a Pandas DataFrame
        :param file: The name of the file to download
        :return: DataFrame: A Pandas DataFrame containing the data from the specified file
        """
        try:
            response = requests.get(f"{self.root_url}{file}")
            response.raise_for_status()
            print(f"downloading data for {self.root_url}{file}")
            return pd.read_csv(BytesIO(response.content))
        except requests.exceptions.RequestException as e:
            print(f"Failed to download data from {self.root_url}{file}: {e}")
            raise

    def extract_data(self):
        """
        Extract data from multiple files in the S3 bucket.

        This method iterates over a list of files, downloads data from each file using the `download_data` method,
        and appends the resulting Pandas DataFrames to a list. The list of extracted DataFrames is then returned.

        :return: list: A list of Pandas DataFrames, each containing the data extracted from a corresponding file
        """
        extracted_data = []
        try:
            for file in self.files:
                data = self.download_data(file)
                extracted_data.append(data)
            return extracted_data
            print("extracted data")
        except Exception as e:
            print(f"An error occurred during data extraction: {e}")
            raise





