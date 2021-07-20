# Timevis
A visualization tool that allows users to view large timeseries (1-100 million timeticks)

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

`make frontend` runs streamlit on `main.py`


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

1. After you run make frontend, a streamlit session should open up on your browser. There you will be greeted by two sliders and a graph. This is the range graph mode, and you can specify a range of the data that you want to graph. The smaller the range is, the less compressed the data will be
2. If you switch to the center/radius graph mode, you can specify a center point, and radius. Depending on the size of the radius, data compression will get smaller
3. If you switch to the anomalous points graph mode, you will see specific points that were designated as anomalous, and you can focus on those points. In order to generate anomalous points, run `detect.py`, and a file called `anomalous_points.csv` will be created, which contains all of the anomalous points.

## TODO
 - [ ] Separate the graph into min/max/all
 - [ ] Implement isolation forests to detect anomalous points
 - [ ] Add support for graphing multiple timeseries at the same time
 - [ ] Preprocess the anomalous points, and allow for a dynamic radius

## Developer Documentation
There are five source files: `backend.py`, `preprocess.py`, `main.py`, `detect.py`, and `synthetic_download.py`


