# ETL Pipeline README
This README provides an overview of the ETL (Extract, Transform, Load) pipeline implemented in the project, along with instructions for setup, installation, and usage.

## Table of Contents
Overview
Project Structure
Getting Started
Installation
Running the ETL Pipeline
Testing
Dependencies
Contributing
License

## Overview
The ETL pipeline is designed to extract data from a specified S3 bucket, transform the extracted data through aggregation and pivoting, and load the final result into a CSV file. The pipeline consists of three main components: Extractor, Transformer, and Loader.

Extractor: Responsible for downloading data from a specified S3 bucket via URL. It iterates over a range of file names and retrieves data in CSV format using the requests library.

Transformer: Performs data transformation on the extracted data. It aggregates data based on user_id and path, and then pivots the aggregated data to create a structured DataFrame.

Loader: Takes the transformed data and writes it to a CSV file using the pandas library.

## Project Structure
The project is structured as follows:

etl_app:

extractor.py: Contains the Extractor class responsible for downloading data.
transformer.py: Implements the Transformer class for data transformation.
loader.py: Defines the Loader class for writing data to a CSV file.
tests:

test_extractor.py: Unit tests for the Extractor class.
test_transformer.py: Unit tests for the Transformer class.
test_loader.py: Unit tests for the Loader class.
main.py: Entry point for running the ETL pipeline with default parameters.

factory.py: Defines the DataProcessor class, which orchestrates the entire ETL pipeline.

requirements.txt: Lists the project dependencies.

## Getting Started
### Clone the Repository:

```
git clone https://github.com/leviizu/ETL-for-duration-of-path-views-per-user.git
cd <repository_directory>
```
### Install Dependencies:
```
pip install -r requirements.txt
```
## Installation
No additional installation steps are required beyond installing the project dependencies listed in requirements.txt.

## Running the ETL Pipeline
To run the ETL pipeline with default parameters, execute the following command:
```
python __main__.py
```

The pipeline will extract data from the specified S3 bucket, perform transformation, and write the result to a CSV file.

## Testing
Run the unit tests to ensure the functionality of the ETL components:
```
python -m test

pytest -v tests/test_extractor.py
pytest -v tests/test_transformer.py
pytest -v tests/test_loader.py
```
Dependencies
The project has the following dependencies:

certifi==2023.11.17
charset-normalizer==3.3.2
idna==3.6
iniconfig==2.0.0
numpy==1.26.3
packaging==23.2
pandas==2.1.4
pluggy==1.3.0
pytest==7.4.4
pytest-mock==3.12.0
python-dateutil==2.8.2
pytz==2023.3.post1
requests==2.31.0
six==1.16.0
tzdata==2023.4
urllib3==2.1.0
Contributing
If you'd like to contribute to the project, please follow the standard GitHub fork and pull request workflow.

License
This project is licensed under the MIT License.





