import pytest
import os
import sys
sys.path.insert(0,"/home/anjalireddytippana/proj1/cs5293sp21-project1/project1")
import main

sample_doc="Call me at (405) 666 7959 or 123-456-7569 and (456) 708-1234"
def test_phones()
    red_phones = main.phones(sample_doc)
    assert len(red_phones[1]) == 3
