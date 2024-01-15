
from etl_app import (Extractor, Transformer, Loader)


class DataProcessor:
    """Class for processing data through the extraction, transformation, and loading pipeline."""

    def __init__(self, root_url, beginning, ending, filename):
        self.extractor = Extractor(root_url, beginning, ending)
        self.transformer = Transformer()
        self.loader = Loader(filename)

    def run_pipeline(self):

        try:
            # Extract
            extracted_df = self.extractor.extract_data()

            # Transform
            # data = pd.concat(extracted_df, ignore_index=True)
            aggregated_df = self.transformer.aggregate_data(extracted_df)
            pivoted_df = self.transformer.pivot_data(aggregated_df)

            # Load
            self.loader.write_to_file(pivoted_df)

        except Exception as e:
            print(f"An error occurred while processing file: {e}")
            raise




