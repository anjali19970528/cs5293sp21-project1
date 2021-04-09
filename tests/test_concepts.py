import pytest
import os
import sys
sys.path.insert(0,"/home/anjalireddytippana/proj1/cs5293sp21-project1/project1")
import main

sample_doc="He is a king. His name is abc. He is the king of xyz dynasty"
def test_concept():
    red_concepts = main.concept(sample_doc,"king")
    assert len(red_concepts[1]) == 2
