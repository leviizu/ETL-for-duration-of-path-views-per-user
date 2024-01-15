
class Loader:
    """Loader for loading data to a csv file."""

    def __init__(self, filename: str):
        """
        Initialize the Loader
        :param filename: The name of the file to which data will be written
        """
        self.filename = filename

    def write_to_file(self, output_data):
        """
        Write Pandas DataFrame to a CSV file
        :param output_data: The Pandas DataFrame to be written to the file
        :return: None
        """
        try:
            output_data.to_csv(self.filename, mode='w', index=True, header=True, sep=',')
            print("loaded data to csv file")
        except Exception as e:
            print(f"An error occurred during writing to file: {e}")
            raise
