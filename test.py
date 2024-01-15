import pytest


# Run the tests
def run_tests():
    pytest.main(['-v', 'tests/test_extractor.py'])
    pytest.main(['-v', 'tests/test_transformer.py'])
    pytest.main(['-v', 'tests/test_loader.py'])


if __name__ == "__main__":
    run_tests()
