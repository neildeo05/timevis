# Timevis
A visualization tool that allows users to view large timeseries (1-100 million timeticks)

## Project Goals
- Visualize arbitrary length timeseries
- Draw the viewer's attention to strange(anomalous) points
- Display and analyze multiple timeseries at the same time (upwards of 100 timeseries)

## How it works
`data.csv` has 29 million points

`preprocess.py` constructs a tree with each level containing the minimum and maximum of 4 points in the previous level, so that each level has half as many points as the previous level. It writes each level to a file in the `data/` directory. This process takes the most time.

`main.py` Utilizes streamlit to display certain levels of the graph


## Current Accomplishments
Right now, the tool can compress the large timeseries into multiple levels, using min/max compression. It can display a certain range of the data using user input with sliders. The UI for graphing anomalous points works as well.

## Todo
 - [ ] Separate the graph into min/max/all
 - [ ] Implement isolation forests to detect anomalous points
 - [ ] Add support for graphing multiple timeseries at the same time

## Quickstart
When you first downlaod the repository: 
- Rename the csv file you want to read from to "data.csv", or use synthetic data by running`download.py`
```console
$ python synthetic_donwload.py
$ make install
$ make preprocess
$ make frontend
```
`make install` installs all necessary packages from PyPI

`make preprocess` creates a tree and writes the contents of that tree to files in the `data/` directory

`make frontend` runs streamlit on `frontend.py`

