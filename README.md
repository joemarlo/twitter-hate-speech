# Hate speech on Twitter

A 2023 extension of [2021 capstone on Twitter hate speech](https://github.com/joemarlo/hate-speech)

**Warning: this project contains vulgar and offensive language.**


### Directory structure

    .
    ├── README.md
    ├── analysis
    │   ├── classifier                    Scripts for building / using the hate speech classifier
    │   └── time-series                   Scripts for time-series analysis
    ├── data
    │   └── tweets.db                     sqlite database containing the tweets
    ├── outputs                           Final, created files such as plots and writing
    ├── renv
    └── twitter-hate-speech.Rproj


## Dependencies

For R, we're using [`renv`](https://rstudio.github.io/renv/index.html). To install all the packages, use `renv::restore()`. To update the package list, use `renv::snapshot()`.

For python, set up your virtual environment initially using `python3 -m venv venv`. Then during each session, activate it using `source venv/bin/Activate`. Install dependencies via `pip install -r requirements.txt`. To update dependencies, `pip freeze > requirements.txt`. To shut down the virtual environemnt, `deactivate`.

