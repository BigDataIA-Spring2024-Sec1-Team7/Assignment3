import pytest
from metadataclass import MetaDataClass

# Tests if metadata class creation fails with date with wrong format
def test_date_must_be_valid_format_failure():
    with pytest.raises(Exception):
        obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/32")

# Tests if metadata class creation  succeeds with  date with correct format
def test_date_must_be_valid_format_succeed():
    obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# Tests if metadata class creation fails with html tags in intro
def test_text_should_not_contain_html_failure():
    with pytest.raises(Exception):
        obj = MetaDataClass(level="Level I<h1>", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# Tests if metadata class creation succeeds without html tags in intro
def test_text_should_not_contain_html_success():
    obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# Tests if metadata class creation succeeds with level of right pattern
def test_level_must_match_pattern_success():
    obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# Tests if metadata class creation fails with level of wrong pattern
def test_level_must_match_pattern_failure():
    with pytest.raises(Exception):
        obj = MetaDataClass(level="Level 1", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# Tests if metadata class creation fails with invalid link
# def test_link_is_valid_failure():
#     with pytest.raises(Exception):
#         obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="test.com",
#                     s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# # Tests if metadata class creation succeeds with valid link
# def test_link_is_valid_success():
#     obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
#                     s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# Tests if metadata class creation fails with string in numpages
def test_numpages_never_integer_success():
    with pytest.raises(Exception):
       obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= "ab123", s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")
       
# Tests if metadata class creation fails with negative integer in numpages
def test_numpages_never_positive_integer_success():
    with pytest.raises(Exception):
       obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= -123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# Tests if metadata class creation succeeds with positive integer in numpages
def test_numpages_positive_integer_success():
   obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")
   
# Tests if metadata class creation fails with string in file_size_bytes
def test_file_size_bytes_never_integer_success():
    with pytest.raises(Exception):
       obj = MetaDataClass(level="Level I", file_size_bytes= "ab12345", num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")
       
# Tests if metadata class creation fails with negative integer in file_size_bytes
def test_file_size_bytes_never_positive_integer_success():
    with pytest.raises(Exception):
       obj = MetaDataClass(level="Level I", file_size_bytes= -12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")

# Tests if metadata class creation succeeds with positive integer in file_size_bytes
def test_file_size_bytes_positive_integer_success():
   obj = MetaDataClass(level="Level I", file_size_bytes= 12345, num_pages= 123, s3_pypdf_text_link="https://test.com",
                    s3_grobid_text_link= "https://test.com", file_path="user/files", encryption= "Yes", date_updated= "12/09/2023")
       

       


