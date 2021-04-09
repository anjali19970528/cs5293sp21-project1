import pytest
import os
import sys
sys.path.insert(0,"/home/anjalireddytippana/proj1/cs5293sp21-project1/project1")
import main

sample_doc="she is a good girl"
result_dict={"genders":["she"]}
def test_redacted_doc():
    redacted_nlp_doc= main.redacted_doc(result_dict,sample_doc)
    print(redacted_nlp_doc)
    assert redacted_nlp_doc==("\u2588 is a good girl")
