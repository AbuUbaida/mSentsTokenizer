from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mSentsTokenizer",
    description="Multilingual Document Tokenization at the Sentence Level",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=[
        "nltk",
        "pysbd",
        "spacy",
        "bltk",
        "indic_sentence_tokenizer @ git+https://github.com/faisaltareque/indic_sentence_tokenizer",
        "zh_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/zh_core_web_sm-3.4.0/zh_core_web_sm-3.4.0.tar.gz",
        "xx_ent_wiki_sm @ https://github.com/explosion/spacy-models/releases/download/xx_ent_wiki_sm-3.4.0/xx_ent_wiki_sm-3.4.0.tar.gz"
    ],
    extras_require ={
        "dev":[
            "pytest >=3.7",
        ]
    },
    python_requires='>=3.6',
)
