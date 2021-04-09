import pytest
import os
import sys
sys.path.insert(0,"/home/anjalireddytippana/proj1/cs5293sp21-project1/project1")
import main

sample_doc="He married Christine Grady, a nurse and bioethicist with the NIH, after they met while treating a patient. She is chief of the Department of Bioethics at the National Institutes of Health Clinical Center. They have three adult daughters"
def test_genders():
    red_genders = main.genders(sample_doc)
    assert len(red_genders[1]) == 3
