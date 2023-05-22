# Assignment 1: Linguistic Analysis

## Repository Overview
1. [Description](#description)
2. [Repository Tree](#tree)
3. [Usage](#gusage)
4. [Modified Usage](#musage)
5. [Example of Results](#results)


## Description <a name="description"></a>
This repository is the solution by *Anton Drasbæk Schiønning (202008161)* to assignment 1 in the course "Language Analytics" at Aarhus University.

It sets out to conduct a lingustic analysis on the [USECorpus dataset](https://www.engelska.uu.se/research/english-language/electronic-resources/use/). This dataset contains a collection of essays from the English department at Uppsala University in Sweden. This lingustic analysis is set up to utilize a [spaCy model](https://spacy.io/models) and extract the following information for each text in the corpus:
* Relative frequency counts of **nouns**, **verbs**, **adjectives** and **adverbs** per 10K words in the text.
* The number of unique **persons**, **locations** and **organizations** in the text.
</br></br>


## Repository Tree <a name="tree"></a>

```
├── README.md
├── assign_desc.md
├── in
│   ├── USEcorpus    <---- the Uppsala Student English Corpus dataset
│   │   ├── a1
│   │   │   ├── 0100.a1.txt   <---- example of text file to be analyzed
│   │   │   ├── 0101.a1.txt
│   │   │   ├── ...
│   │   │   ├── 5022.a1.txt
│   │   │   └── 5031.a1.txt
│   │   ├── a2
│   │   ├── a3
│   │   ├── ...
│   │   ├── b8
│   │   └── c1
│   └── README.md
├── out
│   ├── a1.csv      <---- analysis of all txt files in a1 in-folder
│   ├── a2.csv
│   ├── ...
│   ├── b8.csv
│   └── c1.csv
├── requirements.txt
├── run.sh
├── setup.sh
└── src
    └── main.py   <---- script for completing full lingustic analysis           
```
<br>

## Usage <a name="gusage"></a>
Running the analysis only assumes that you have Python3 installed and clone this repository. To run the full analysis, execute the run file from the root directory of the project as such:
```
bash run.sh
```

This will complete the following steps: <br>
<ol>
  <li>Create and activate a virtual environment</li>
  <li>Install requirements to that environment</li>
  <li>Install the SpaCy model</li>
  <li>Run the analysis script</li>
  <li>Deactivate the environment</li>
</ol>

The results are saved to the `out` directory, structured as seen on the *repository tree*.
</br></br>

## Modified Usage <a name="musage"></a>
### Setup
The analysis can also be run part-by-part which enables the usage of different SpaCy models. To achieve this, firstly run the setup shell script:
```
bash setup.sh
```
<br>

This creates a virtual environment, installs requirements and downloads the following SpaCy Models: `en_core_web_md`, `en_core_web_sm` and `en_core_web_trf`. If you wish to use another SpaCy model than those three, please install it as such:
```
python3 -m spacy download <INSERT MODEL NAME>
```

### Run Modified Analysis
With the setup complete, you can use the `--model` arugment for `main.py` to specify which SpaCy model should be used:
```
# run analysis with small model instead of medium
python3 src/main.py --model "en_core_web_sm"
```
Again, results will be saved to `out`.
</br></br>

## Example of Results <a name="results"></a>
The full results for the analysis are found in the `out` folder. An example of results for the text files in the `b7` folder is seen below, the rest of the files have the same general structure
| Filename      | RelFreq NOUN | RelFreq VERB | RelFreq ADJ | RelFreq ADV | Unique PER | Unique LOC | Unique ORG |
|-------------- | ------------ | ------------ | ----------- | ----------- | ---------- | ---------- | ---------- |
| 0106.b7.txt   | 1763         | 1258         | 835         | 515         | 0          | 1          | 0          |
| 0107.b7.txt   | 1633         | 1081         | 1036        | 541         | 0          | 1          | 6          |
| 0137.b7.txt   | 2109         | 965          | 816         | 348         | 4          | 1          | 2          |
| 0151.b7.txt   | 1934         | 1075         | 910         | 442         | 2          | 0          | 2          |
| 0157.b7.txt   | 1271         | 1224         | 882         | 588         | 5          | 1          | 1          |
| 0158.b7.txt   | 1838         | 1230         | 738         | 492         | 1          | 1          | 0          |
| 0178.b7.txt   | 1979         | 1022         | 949         | 716         | 4          | 0          | 3          |
| 0185.b7.txt   | 1815         | 1156         | 822         | 619         | 1          | 0          | 0          |
| 0186.b7.txt   | 1714         | 1095         | 738         | 643         | 0          | 0          | 1          |
| 0198.b7.txt   | 2025         | 1080         | 810         | 503         | 0          | 0          | 2          |
| 0219.b7.txt   | 2095         | 1002         | 1014        | 586         | 1          | 1          | 0          |
| 0223.b7.txt   | 1982         | 1041         | 862         | 448         | 0          | 0          | 1          |
| 0224.b7.txt   | 2102         | 1030         | 948         | 316         | 1          | 1          | 1          |
| 0238.b7.txt   | 1688         | 1186         | 716         | 556         | 1          | 0          | 2          |
| 0318.b7.txt   | 2077         | 913          | 820         | 516         | 1          | 0          | 0          |






