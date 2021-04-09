import spacy
from spacy.matcher import Matcher
import re
import nltk
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize
import sys
nlp = spacy.load("en_core_web_sm")

def names(nlp_doc):
    doc = nlp(nlp_doc)
    red_names=[]
    for X in doc.ents:
        if X.label_=='PERSON' or X.label_=='ORG' or X.label_=='GPS' or X.label_=='NORP':
            red_names.append(X.text)
    return nlp_doc,red_names


def genders(nlp_doc):
    doc = nlp(nlp_doc)
    red_gender=[]
    matcher = Matcher(nlp.vocab)
    pattern = [{"TEXT": {"REGEX": "^[hH]e$|^[hH]is$|^[hH]im$|^[mM]an$|^[mM]en$|^[mM]ale$|^[mM]r$|^[uU]ncle$|^[bB]rother$|^[fF]ather$|^[sS]he$|^[hH]ers?$|^[wW]omen$|^[wW]oman$|^[fF]emale$|^[sS]ister$|^[aA]unt$|^[mM]rs$|^[mM]s$|^[mM]other$|^[wW]ife$|^[hH]usband$|^[sS]on$|^[dD]aughters?$"}}]
    matcher.add("GENDER", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
    #     print(start, end, span.text) 
        red_gender.append(span.text)
    return nlp_doc,red_gender


def dates(nlp_doc):
    doc = nlp(nlp_doc)
    red_dates=[]
    expression = r"[0-9]{2}[/-][0-9]{2}[/-][0-9]{4}|[0-9]{2}[/-][0-9]{2}[/-][0-9]{2}|(\b\d{1,2}\D{0,3})?\b(?:[jJ]an(?:uary)?|[fF]eb(?:ruary)?|[mM]ar(?:ch)?|[aA]pr(?:il)?|[mM]ay|[jJ]un(?:e)?|[jJ]ul(?:y)?|[aA]ug(?:ust)?|[sS]ep(?:tember)?|[oO]ct(?:ober)?|([nN]ov|[dD]ec)(?:ember)?)\D?(\d{1,2}(st|nd|rd|th)?)?(([,.\-\/])\D?)?((19[7-9]\d|20\d{2})|\d{2})*|[tT]oday|tomorrow|yesterday"
   
    for match in re.finditer(expression, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
    #         print("Found match:", span.text)
            red_dates.append(span.text)
    return nlp_doc,red_dates

def phones(nlp_doc):
    doc = nlp(nlp_doc)
    red_phone_num=[]
    expression = r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))"
    for match in re.finditer(expression, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        # This is a Span object or None if match doesn't map to valid token sequence
        if span is not None:
            red_phone_num.append(span.text)
    return nlp_doc,red_phone_num


def concept(nlp_doc,concept_name):
    sentences_list=[]
    synonyms_list=[]
    for synonym in wordnet.synsets(concept_name):
    #     print(synonym)
        for syn in synonym.lemmas():
    #         print(syn)
            synonyms_list.append(syn.name())
    synonyms_list=list(set(synonyms_list))
    for a in synonyms_list:
        for sentence in sent_tokenize(nlp_doc): 
    #         print(sentence)
            if a in sentence:
                sentences_list.append(sentence) 
    return nlp_doc,sentences_list


def redacted_doc(result_dict,nlp_doc):
    unic_char = '\u2588'
    total_redacted_list=[]
    phones_list=[]
    for k,v in result_dict.items():
        if k in ['phones']:
            phones_list += v
        else:
            total_redacted_list+=v 
    for i,j in enumerate(total_redacted_list):
        j= r'\b' + j + r'\b'
#         print(j)
        nlp_doc=re.sub(j,unic_char,nlp_doc)
    if len(phones_list) > 0:
        for phone_no in phones_list:
            nlp_doc = nlp_doc.replace(phone_no, unic_char)
    return nlp_doc

def stats(result_dict):
    red_info=""
    total_redacted=0
    for k,v in result_dict.items():
        red_info +="{} {} are redacted from this file \n".format(len(v),k)
        total_redacted +=len(v) 
    red_info=red_info + "Total number of redacted words and sentences for this file are {} \n".format(total_redacted)
    return red_info
