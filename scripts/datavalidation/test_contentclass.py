import pytest
from contentclass import ContentClass


# Tests if content class creation fails with none in level
def test_level_none_failure():
    with pytest.raises(Exception):
        obj = ContentClass(level = None, title= "Title", topic= "Topic",learning_outcomes= "learning_outcome")

# Tests if content class creation fails with none in title
def test_title_none_failure():
    with pytest.raises(Exception):
        obj = ContentClass(level = "Level I", title= None, topic= "Topic",learning_outcomes= "learning_outcome")

# Tests if content class creation fails with none in topic
def test_topic_none_failure():
    with pytest.raises(Exception):
        obj = ContentClass(level = "Level I", title= "Title", topic= None,learning_outcomes= "learning_outcome")

# Tests if content class creation fails with not none in topic, level, title
def test_never_none_success():
    obj = ContentClass(level = "Level I", title= "Title", topic= "topic" ,learning_outcomes= "learning_outcome")


# Tests if content class creation succeeds with level of right pattern
def test_level_must_match_pattern_success():
   obj = ContentClass(level = "Level I", title= "Title", topic= "topic" ,learning_outcomes= "learning_outcome")

# Tests if content class creation fails with level of wrong pattern
def test_level_must_match_pattern_failure():
    with pytest.raises(Exception):
       obj = ContentClass(level = "Level 1", title= "Title", topic= "topic" ,learning_outcomes= "learning_outcome")


# Tests if content class creation fails with xml tags in topic
def test_topic_should_not_contain_xml_failure():
    with pytest.raises(Exception):
        obj = ContentClass(level = "Level 1", title= "Title", topic= "topic<xml>" ,learning_outcomes= "learning_outcome")

# Tests if content class creation succeeds without tpoic tags in topic
def test_topic_should_not_contain_xml_success():
    obj = ContentClass(level = "Level I", title= "Title", topic= "topic" ,learning_outcomes= "learning_outcome")


# Tests if content class creation fails with xml tags in title
def test_title_should_not_contain_xml_failure():
    with pytest.raises(Exception):
        obj =  ContentClass(level = "Level II", title= "Title<xml>", topic= "topic<xml>" ,learning_outcomes= "learning_outcome")

# Tests if content class creation succeeds without tpoic tags in title
def test_title_should_not_contain_xml_success():
    obj = ContentClass(level = "Level I", title= "Title", topic= "topic" ,learning_outcomes= "learning_outcome")


# Tests if content class creation fails with xml tags in learning_outcome
def test_learning_outcome_should_not_contain_xml_failure():
    with pytest.raises(Exception):
        obj = ContentClass(level = "Level I", title= "Title", topic= "topic" ,learning_outcomes= "learning_outcome<xml>")

# Tests if content class creation succeeds without tpoic tags in learning_outcome
def test_learning_outcome_should_not_contain_xml_success():
    obj =  ContentClass(level = "Level I", title= "Title", topic= "topic" ,learning_outcomes= "learning_outcome")














