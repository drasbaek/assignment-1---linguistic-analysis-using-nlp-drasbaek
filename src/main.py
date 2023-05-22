""" main.py
Author:
    Anton Drasbæk Schiønning (202008161), GitHub: @drasbaek

Desc:
    This script is the solution to assignment 1 in the course "Language Analytics" at Aarhus University.
    It is used to lingustic analysis on the USECorpus dataset, extracting various lingustic features, using a spaCy model.
    The output of the script can be found in the folder "out" in the root directory of the project.

Usage:
    $ python src/main.py
"""

# install packages
import spacy
import pandas as pd
import os
import re
from pathlib import Path
from tqdm import tqdm
import argparse


def define_paths():
    """
    Defines the paths to the input and output directories.

    Returns:
        inpath (pathlib.PosixPath): The path to the input directory.
        outpath (pathlib.PosixPath): The path to the output directory.
    """

    # define paths
    path = Path(__file__)

    # define input dir
    inpath = path.parents[1] / "in" / "USECorpus"

    # define output dir
    outpath = path.parents[1] / "out"

    return inpath, outpath


def arg_parse():
    """
    Parse command line arguments.
    It is possible to specify which spacy model to apply for the linguistic analysis.

    Returns:
        args (argparse.Namespace): The parsed arguments.
    """
    
    # define parser
    parser = argparse.ArgumentParser(description = "Specify which spacy model to apply for the linguistic analysis.")

    # add argument
    parser.add_argument("-m", "--model", type = str, default = "en_core_web_md", help = "Specify which spacy model to apply for the linguistic analysis.")

    # parse arguments
    args = parser.parse_args()

    return args


def read_file(folder_path, file_name):
    """
    Read a file from a given folder path and file name.

    Args:
    - folder_path (str): a string representing the path to the folder containing the file to be read
    - file_name (str): a string representing the name of the file to be read

    Returns:
    - text (str): a string representing the text of the file

    """

    # define filepath
    file_path = os.path.join(folder_path, file_name)
        
    # open file
    with open(file_path, "r", encoding = "latin-1") as file:
            
        # read file
        text = file.read()
    
    return text


def clean_txt(text):
    """
    Clean a given text by removing tags in angle brackets.
    
    Args:
    - text (str): a string representing the text to be cleaned
    
    Returns:
    - text (str): a string representing the cleaned text

    """
    
    # remove all tags in < > brackets from the text
    text = re.sub('<.*?>', '', text)
    
    return text


def extract_pos(doc):
    """
    Extract the relative frequency of relevant POS tags from a given spacy doc.
    
    Args:
        - doc (spacy.tokens.doc.Doc): a spacy doc object representing the text to extract POS tags from
    
    Returns:
        - noun_counter (int): an integer representing the relative frequency of nouns per 10,000 words
        - verb_counter (int): an integer representing the relative frequency of verbs per 10,000 words
        - adj_counter (int): an integer representing the relative frequency of adjectives per 10,000 words
        - adv_counter (int): an integer representing the relative frequency of adverbs per 10,000 words
    """
    
    # define the list of relevant POS tags
    relevant_pos_tags = ["NOUN", "VERB", "ADJ", "ADV"]
    
    # initialize counters for each POS tag
    noun_counter = 0
    verb_counter = 0
    adj_counter = 0
    adv_counter = 0
    
    # loop over each token in the doc
    for token in doc:

        # check if the token's POS tag is relevant (this saves us from having to check for each POS tag)
        if token.pos_ in relevant_pos_tags:

            # increment the corresponding POS tag counter
            if token.pos_ == "NOUN":
                noun_counter += 1
            elif token.pos_ == "VERB":
                verb_counter += 1
            elif token.pos_ == "ADJ":
                adj_counter += 1
            elif token.pos_ == "ADV":
                adv_counter += 1
    
    # calculate the relative frequency per 10,000 words for each POS tag
    noun_counter = round(noun_counter / len(doc) * 10000)
    verb_counter = round(verb_counter / len(doc) * 10000)
    adj_counter = round(adj_counter / len(doc) * 10000)
    adv_counter = round(adv_counter / len(doc) * 10000)
    
    return noun_counter, verb_counter, adj_counter, adv_counter


def extract_ner(doc):
    """
    Extract the number of unique named entities of each relevant type from a given spacy doc.
    
    Args:
        - doc (spacy.tokens.doc.Doc): a spacy doc object representing the text to extract named entities from
    
    Returns:
        - person_count (int): an integer representing the number of unique persons in the text
        - location_count (int): an integer representing the number of unique locations in the text
        - org_count (int): an integer representing the number of unique organizations in the text
    """
    
    # define the list of relevant named entity types
    relevant_entities = ["PERSON", "LOC", "ORG"]
    
    # initialize empty lists for each entity type
    person_list = []
    location_list = []
    org_list = []
    
    # loop over each named entity in the doc
    for ent in doc.ents:
        # check if the entity type is relevant
        if ent.label_ in relevant_entities:
            # add the named entity to the corresponding list
            if ent.label_ == "PERSON":
                person_list.append(ent.text)
            elif ent.label_ == "LOC":
                location_list.append(ent.text)
            elif ent.label_ == "ORG":
                org_list.append(ent.text)
    
    # count the number of unique named entities for each entity list
    person_count = len(set(person_list))
    location_count = len(set(location_list))
    org_count = len(set(org_list))
    
    return person_count, location_count, org_count


def linguistic_analysis(inpath, folder, nlp, outpath):
    """
    Perform linguistic analysis on all texts in a given folder.
    Saves the results in a csv file which is placed in the specified output folder in the outpath.

    Args:
        - inpath (pathlib.PosixPath): a string representing the path to the folder containing the texts to be analyzed
        - folder (str): a string representing the name of the folder containing the texts to be analyzed
        - nlp (spacy.lang): a spacy language model to be used for the linguistic analysis
        - outpath (pathlib.PosixPath): a string representing the path to the folder where the output should be saved
    """

    # define folder path
    folder_path = os.path.join(inpath, folder)

    # create empty dataframe
    df = pd.DataFrame(columns = ["Filename", "RelFreq NOUN", "RelFreq VERB", "RelFreq ADJ", "RelFreq ADV", "Unique PER", "Unique LOC", "Unique ORG"])

     # loop over each file in the folder
    for i, file_name in enumerate(sorted(os.listdir(folder_path))):
        
        # read file
        text = read_file(folder_path, file_name)

        # clean text
        text = clean_txt(text)
        
        # create doc
        doc = nlp(text)
        
        # extract POS
        noun_count, verb_count, adj_count, adv_count = extract_pos(doc)
        
        # extract NER
        person_count, location_count, org_count = extract_ner(doc)

        # append data as a row in the data frame
        df.loc[i] = [file_name, noun_count, verb_count, adj_count, adv_count, person_count, location_count, org_count]

    # write dataframe to csv
    df.to_csv(f'{outpath}/{folder}.csv', index = False)


def main():
    # parse arguments
    args = arg_parse()

    # define paths
    inpath, outpath = define_paths()

    # load spacy model
    nlp = spacy.load(args.model)

    # define folder dir
    folder_dir = sorted(os.listdir(inpath))

    # loop over each folder in the inpath
    for folder in tqdm(folder_dir, desc = "Performing linguistic analysis on each subdirectory"):

        # perform linguistic analysis
        linguistic_analysis(inpath, folder, nlp, outpath)

# run main
if __name__ == "__main__":
    main()