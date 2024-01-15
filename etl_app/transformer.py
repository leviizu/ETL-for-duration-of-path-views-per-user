import pandas as pd


class Transformer:
    """Transformer for transforming already extracted data."""

    @staticmethod
    def aggregate_data(extracted_data: list):
        """
        Aggregate data based on user_id and path
        :param extracted_data: A list of Pandas DataFrames containing extracted data
        :return: DataFrame: A Pandas DataFrame containing Aggregated data with columns 'user_id', 'path', and the sum
        of 'length' for each group
        """
        try:
            data = pd.concat(extracted_data, ignore_index=True)
            aggregated_data = data.groupby(['user_id', 'path'])['length'].sum().reset_index()
            print("aggregating data")
            return aggregated_data
        except Exception as e:
            print(f"An error occurred during data aggregation: {e}")
            raise

    @staticmethod
    def pivot_data(aggregated_data):
        """
        Pivot aggregated data

        :param aggregated_data: Aggregated data with columns 'user_id', 'path', and 'length'.
        :return: DataFrame: Pivoted data with 'user_id' as index, 'path' as columns, and 'length' as values.
        """
        try:
            pivoted_data = aggregated_data.pivot(index='user_id', columns='path', values='length').fillna(0)
            print("pivoting data")
            return pivoted_data

        except Exception as e:
            print(f"An error occurred during data pivoting: {e}")
            raise

