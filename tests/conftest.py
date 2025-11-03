"""Pytest configuration and fixtures."""
import pytest
import pandas as pd


@pytest.fixture
def sample_data():
    """Create sample Nobel Prize data for testing."""
    return pd.DataFrame(
        {
            "award_year": [1901, 1902, 1903, 1904, 1905],
            "category": ["Physics", "Chemistry", "Physics", "Literature", "Peace"],
            "sex": ["male", "female", "male", "male", "female"],
            "birth_country": ["Germany", "Poland", "France", "USA", "Sweden"],
            "known_name": [
                "Person A",
                "Person B",
                "Person C",
                "Person D",
                "Person E",
            ],
            "laureate_id": [1.0, 2.0, 3.0, 4.0, 5.0],
            "motivation": [
                "For discovery A",
                "For discovery B",
                "For discovery C",
                "For work D",
                "For peace work",
            ],
            "is_shared": [0, 1, 0, 0, 1],
            "prize_amount": [100000, 100000, 100000, 100000, 100000],
        }
    )
