from dagster import asset

@asset
def raw_data():
    """
    The initial raw data for our price prediction service.
    """
    return [1, 2, 3]
