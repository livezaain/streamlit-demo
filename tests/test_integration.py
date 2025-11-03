"""Integration tests for the Streamlit app."""
import pytest
from streamlit.testing.v1 import AppTest


def test_app_runs():
    """Test that the app loads without errors."""
    at = AppTest.from_file("app.py")
    at.run()
    assert not at.exception, f"App should run without exceptions: {at.exception}"


def test_app_has_title():
    """Test that the app has a title."""
    at = AppTest.from_file("app.py")
    at.run()
    assert len(at.title) > 0, "App should have a title"
    assert "Nobel Prize" in at.title[0].value, "Title should mention Nobel Prize"


def test_app_has_sidebar():
    """Test that the app has sidebar elements."""
    at = AppTest.from_file("app.py")
    at.run()
    # Check for sidebar elements (filters)
    assert len(at.sidebar) > 0, "App should have sidebar content"


def test_app_displays_metrics():
    """Test that the app displays metrics."""
    at = AppTest.from_file("app.py")
    at.run()
    # Check that metrics are displayed
    assert len(at.metric) > 0, "App should display metrics"


def test_app_has_download_button():
    """Test that the app has a download button."""
    at = AppTest.from_file("app.py")
    at.run()
    # Check for download button
    assert len(at.download_button) > 0, "App should have a download button"

