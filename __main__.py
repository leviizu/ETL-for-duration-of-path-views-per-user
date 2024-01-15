
from factory import DataProcessor

if __name__ == "__main__":
    _root_url = "https://public.wiwdata.com/engineering-challenge/data/"
    _beginning = "a"
    _ending = "z"
    _filename = "path_duration.csv"

    processor = DataProcessor(_root_url, _beginning, _ending, _filename)
    try:
        processor.run_pipeline()
    except Exception as e:
        print(f"An error occurred in the __main__ block: {e}")


