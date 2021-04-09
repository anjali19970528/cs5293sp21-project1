import pytest
import os
import sys
sys.path.insert(0,"/home/anjalireddytippana/proj1/cs5293sp21-project1/project1")
import main

sample_doc ="Anthony Stephen Fauci is an American physician-scientist and immunologist who serves as the director of the U.S. National Institute of Allergy and Infectious Diseases and the chief medical advisor to the president"
def test_names():
    red_names = main.names(sample_doc)
    assert len(red_names[1]) == 3
