from mSentsTokenizer.library import spacy_support
from mSentsTokenizer.library import bltk_support
from mSentsTokenizer.library import indic_support
from mSentsTokenizer.library import pysbd_support
from mSentsTokenizer.library import nltk_support
from mSentsTokenizer import languages_support

def tokenize(text:str,language:str):
    """
    Tokenize document at sentences level
    Arguments:
        text: Document string 
        language: Language ID i.e. ISO:639-2 code. 
    Returns:
        List of strings
    """
    support_library = languages_support.get_support_library(language=language)

    if support_library == 'spacy':
        return spacy_support.sentence_tokenize(text=text, lang=language)
    elif support_library == 'bltk':
        return bltk_support.sentence_tokenize(text=text)
    elif support_library == 'nltk':
        return nltk_support.sentence_tokenize(text=text, lang=language)
    elif support_library == 'indic':
        return indic_support.sentence_tokenize(text=text, lang=language)
    elif support_library == 'pysbd':
        return pysbd_support.sentence_tokenize(text=text, lang=language)

    

