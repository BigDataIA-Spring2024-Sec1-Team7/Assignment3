import pytest
from urlclass import URLClass

# Tests if url class creation fails with year less than 1800
def test_year_must_be_valid_lessthan_failure():
    with pytest.raises(Exception):
        obj = URLClass(topic="topic", year=1799, level="Level I", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation fails with year greater than 2024
def test_year_must_be_valid_greaterthan_failure():
    with pytest.raises(Exception):
        obj = URLClass(topic="topic", year=2025, level="Level I", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation succeeds with correct year
def test_year_must_be_valid_success():
    obj = URLClass(topic="topic", year=2023, level="Level I", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation fails with html tags in intro
def test_text_should_not_contain_html_failure():
    with pytest.raises(Exception):
        obj = URLClass(topic="topic", year=2023, level="Level I", introduction="intro<h1>", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation succeeds without html tags in intro
def test_text_should_not_contain_html_success():
    obj = URLClass(topic="topic", year=2023, level="Level I", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation succeeds with level of right pattern
def test_level_must_match_pattern_success():
    obj = URLClass(topic="topic", year=2023, level="Level I", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation fails with level of wrong pattern
def test_level_must_match_pattern_failure():
    with pytest.raises(Exception):
        obj = URLClass(topic="topic", year=2023, level="Level IIII", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation fails with invalid link
def test_link_is_valid_failure():
    with pytest.raises(Exception):
        obj = URLClass(topic="topic", year=2023, level="Level I", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="test.com", link_pdf="https://test.com")

# Tests if url class creation succeeds with valid link
def test_link_is_valid_success():
    obj = URLClass(topic="topic", year=2023, level="Level I", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation fails with none in topic
def test_topic_never_none_success():
    with pytest.raises(Exception):
        obj = URLClass(topic=None, year=2023, level="Level I", introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")

# Tests if url class creation fails with none in level
def test_level_never_none_success():
    with pytest.raises(Exception):
        obj = URLClass(topic="topic", year=None, level=None, introduction="intro", learning_outcomes="learning outcomes", summary="summary", link_summary="https://test.com", link_pdf="https://test.com")