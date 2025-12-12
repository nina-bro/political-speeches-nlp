# Bundestag Speech Analysis: Lexicon vs. Model-based Approaches

This notebook looks at lexicon-based approaches for:
- Named Entity Recognition (NER)
- Sentiment Analysis

It was created for a workshop for the [Center for Political Practices and Orders](https://www.uni-erfurt.de/staatswissenschaftliche-fakultaet/forschung/wissenschaftliche-karriere/nachwuchskollegs/center-for-political-practices-and-orders-c2po).
## Running on Binder

Click the button below to launch an interactive session:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nina-bro/political-speeches-nlp/HEAD?urlpath=%2Fdoc%2Ftree%2Flexicon-based-approaches.ipynb)

## Local Setup
```bash
pip install -r requirements.txt
jupyter notebook
```

## Data

- `eu_speeches_2024_english.csv`: EU parliament speeches, extracted from [ParlLawSpeech](https://parllawspeech.org/data/)
- `vader.txt`: English sentiment lexicon, extracted from [vaderSentiment](https://pypi.org/project/vaderSentiment/)

## Author

Nina Brolich - University of Erfurt
