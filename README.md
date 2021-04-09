**Name: Anjali Reddy Tippana**

**Project descripiton:**

In this project, I'm going to redact sensitive details like names, genders, dates, phones, concepts in documents such as police reports, court transcripts, and hospital records all containing sensitive information.  

**How to run:**

To run the code first you need to intsall and setup python3 environment with packages mentioned in pipfile or requirements.txt

**Commands used to install python3 and setup python environment:**

pyenv install python 3.8.6

pyenv virtualenv 3.8.6 folder_name

**Commands used to install packages:**

pipenv install spacy

pipenv install matcher  

pipenv install nltk 

pipenv install pytest

**command used to run:**

pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones \
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr

If --stats flag is given stdout as argument then it prints statisticts to the console or if stderr is given as argument then it prints statisticts to the error console or if a file is given it writes to that file.
					
**Example:**

pipenv run python redactor.py --input '*.txt' --names --genders --dates --phones --concept kids --output . --stats stdout

**How to test:**

pipenv run python -m pytest.

**Assumptions:**

I'm assuming al the famous person names, countries, states, cities, organization ,nationalities or religious or political groups names are redacted.

Words like he, him, his, her, she, hers, son, daughter, wife, husband, mother, father, mr, mrs, miss, male, female, daughters, man, men, woman, women, aunt, uncle wich reviels genders are redacted.

Dates in the format of 12/12/1997', '01-12-87', '06/11/86', 'Oct 21, 2014', 'November 21st, 2014', 'Oct 28th, 97', 'April 9th', 'November 2nd, 2015' etc are formated.

Phone numbers in the format of '(405) 666 7959', '123-456-7569', '(456) 708-1234', '123.456.7569' are redacted. 

**Functions used:**

**names(nlp_doc):**
 
This function will take a txt file and labels all the names of people as PERSON, names of countries,states,cities as GPE, name of the organization as ORG and names of nationalities or religious or political groups as NORP using spacy's named entity recognition model. This function returns original doc and list of all specified names.     

**genders(nlp_doc):**

This function is going to take a txt file and using spacy's Token matcher, it is going to match all the words in the form of given pattern. This function returns original doc and list of all words that reviels gender. 

**dates(nlp_doc):**

This function is going to take a txt file and using re.finditer() method it matches all dates patterns given in the regex pattern within given text file. This function returns original doc and list of all dates that matches with the regex pattern. 

**dates(nlp_doc):**

This function is going to take a txt file and using re.finditer() method it matches all phone numbers given in the regex pattern within given text file. This function returns original doc and list of all phone numbers that matches with the regex pattern.

**concepts(nlp_doc):**

This function is going to take a txt file and a concept name and using nltk's interface WordNet.Synset it groups all the synonymous words that state the same meaning as the concept word and it searches for each synonymous word in every sentence(after sentence tokenization) of the txt file. If it finds a match it appends that particular sentence to a list. This function returns original doc and list of all sentences that has similar meaning with the concept word.

**redacted_doc(result_dict,nlp_doc):** 
This function is going to take a txt file and dictionary with names, genders, dates, phones, concepts as key and returned lists from above functions as keys. It masks all words present in txt file that are also present in the lists with a unicode char. This function returns this redacted document. 

**stats(result_dict):**

This function is going to take dictionary with names, genders, dates, phones, concepts as key and returned lists from above functions as keys and this function returns statistics about the count of each type of redacted words of each text file.  
    

**References:**

https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da
https://spacy.io/usage/rule-based-matching#matcher
https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python





