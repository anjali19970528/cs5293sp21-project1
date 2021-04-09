import pytest
import os
import sys
sys.path.insert(0,"/home/anjalireddytippana/proj1/cs5293sp21-project1/project1")
import main

sample_doc="Anthony Stephen Fauci was born December 24th, 1940. On Dec 3, 2020, President-elect Joe Biden asked Fauci to serve as the chief medical advisor to the president in the Biden administration. Fauci was admitted as an honorary fellow of the Royal College of Physicians of Ireland on 03-23-2021. "
def test_dates():
    red_dates = main.dates(sample_doc)
    assert len(red_dates[1]) == 3
