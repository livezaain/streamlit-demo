"""Unit tests for app.py functions."""
import pytest
import pandas as pd
import os
from app import load_data, filter_data, calculate_stats


def test_data_file_exists():
    """Test that the Nobel Prize data file exists."""
    assert os.path.exists('data/nobel_prizes_1901-2025_cleaned.csv'), \
        "Data file not found"


def test_load_data():
    """Test data loading function."""
    df = load_data('data/nobel_prizes_1901-2025_cleaned.csv')
    
    assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
    assert len(df) > 0, "DataFrame should not be empty"
    assert 'award_year' in df.columns, "Should have award_year column"
    assert 'category' in df.columns, "Should have category column"


def test_filter_data(sample_data):
    """Test filtering logic with sample data."""
    # Test year range filter
    filtered = filter_data(sample_data, (1902, 1904), [], 'All', 'All')
    assert len(filtered) == 3, "Should filter by year range"
    assert filtered['award_year'].min() >= 1902
    assert filtered['award_year'].max() <= 1904
    
    # Test category filter
    filtered = filter_data(sample_data, (1901, 1905), ['Physics'], 'All', 'All')
    assert len(filtered) == 2, "Should filter by category"
    assert all(filtered['category'] == 'Physics')
    
    # Test gender filter
    filtered = filter_data(sample_data, (1901, 1905), [], 'Female', 'All')
    assert len(filtered) == 2, "Should filter by gender"
    assert all(filtered['sex'] == 'female')
    
    # Test country filter
    filtered = filter_data(sample_data, (1901, 1905), [], 'All', 'Germany')
    assert len(filtered) == 1, "Should filter by country"
    assert all(filtered['birth_country'] == 'Germany')


def test_calculate_stats(sample_data):
    """Test statistics calculation."""
    stats = calculate_stats(sample_data)
    
    assert 'total_prizes' in stats, "Should have total_prizes"
    assert 'total_laureates' in stats, "Should have total_laureates"
    assert 'countries_count' in stats, "Should have countries_count"
    assert 'gender_split' in stats, "Should have gender_split"
    
    assert stats['total_prizes'] == 5, "Should count all prizes"
    assert stats['total_laureates'] == 5, "Should count unique laureates"
    assert stats['countries_count'] == 5, "Should count unique countries"
    assert 'male' in stats['gender_split'], "Should have male count"
    assert 'female' in stats['gender_split'], "Should have female count"


def test_filter_data_empty_result(sample_data):
    """Test filtering that results in empty DataFrame."""
    # Filter for non-existent category
    filtered = filter_data(sample_data, (1901, 1905), ['Economics'], 'All', 'All')
    assert len(filtered) == 0, "Should return empty DataFrame for no matches"


def test_filter_data_all_categories(sample_data):
    """Test filtering with all categories selected."""
    all_categories = sample_data['category'].unique().tolist()
    filtered = filter_data(sample_data, (1901, 1905), all_categories, 'All', 'All')
    assert len(filtered) == len(sample_data), "Should return all data when all categories selected"

