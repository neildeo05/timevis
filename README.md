<p align="center">
  <img src="https://raw.githubusercontent.com/neildeo05/timevis/master/thumbnails/thumbnail_00.png">
</p>

--------------------------------------------------------------------

# Timevis
A visualization tool that allows users to view large timeseries (1-100 million timeticks)

## Quickstart
When you first download the repository: 

- If you have a source datafile that you want to use, update `vars.conf` such that SOURCE\_DIR and SOURCE\_FILE point to the folder and source csv file

- If you want to use synthetic data, then run

    ```console
	    $ ./build.sh generate
	```
- When you want to run the tool for the first time, run this command:

    ```console
        $ ./build.sh all
    ```
	
`install` installs all necessary packages from PyPI

`preprocess` creates a tree and writes the contents of that tree to files in the `data/` directory

`detect` runs the anomaly detection tool

`frontend` runs streamlit on `main.py`

- After you have completed all of the preprocessing steps, running the frontend tool is as simple as 

```console
$ ./build.sh frontend
```

or 

```console
$ ./build.sh
```

## Project Goals
- Visualize arbitrary length timeseries
- Draw the viewer's attention to strange(anomalous) points
- Display and analyze multiple timeseries at the same time (upwards of 100 timeseries)

## How it works
`data.csv` has 29 million points

`preprocess.py` constructs a tree with each level containing the minimum and maximum of 4 points in the previous level, so that each level has half as many points as the previous level. It writes each level to a file in the `data/` directory. This process takes the most time.

`main.py` Utilizes streamlit to display certain levels of the graph

## Profiling
If you want to profile a specific python script, you can use `src/profiler.py`
```console
$ ./build.sh profile "isolation_forests.py"
    python isolation_forests.py:
        {5.0: -7, 2.0: -10291, 1.0: 4999999}
        [4999999, -10291]
    
    The process finished executing in 0:00:01.012733 seconds...
    The process used 43 megabytes of memory
    The total memory usage of the process was 0.53%
```

If you want to profile a specific function, you can use the `@profile_function` decorator

foo.py:
```python
@profile_function
def foo():
	for i in range(100):
		print(i)
```

```console
$ python foo.py
    OUTPUT:
    foo
    foo
    foo
    foo
    foo
    foo
    foo
    foo
    foo
    foo
    
    The process finished executing in 0:00:00.000075 seconds...
    The process used 9 megabytes of memory
    The total memory usage of the process was 0.12%
```

## Current Accomplishments
Right now, the tool can compress the large timeseries into multiple levels, using min/max compression. It can display a certain range of the data using user input with sliders. The UI for graphing anomalous points works as well.

1. After you run make frontend, a streamlit session should open up on your browser. There you will be greeted by two sliders and a graph. This is the range graph mode, and you can specify a range of the data that you want to graph. The smaller the range is, the less compressed the data will be
2. If you switch to the center/radius graph mode, you can specify a center point, and radius. Depending on the size of the radius, data compression will get smaller
3. If you switch to the anomalous points graph mode, you will see specific points that were designated as anomalous, and you can focus on those points. In order to generate anomalous points, run `detect.py`, and a file called `anomalous_points.csv` will be created, which contains all of the anomalous points.

## TODO
## Necessary
 - [X] Update vars.conf to include anomalous points radius
 - [X] Update build.sh to include flags for preprocessing and frontend
 - [X] Update README.md file
 - [X] Separate the graph into min/max/all
 - [X] Implement isolation forests to detect anomalous points
 - [X] Preprocess the anomalous points, and allow for a dynamic radius
 - [X] Pick a few interesting images from the task above and add to `README.md` 
 - [X] Find a way to use real timetick values on x axis in center/radius mode
 - [X] Add a simple performance and memory usage profiling script that can be run for quick diagnostics
 - [X] Based on available memory on the machine, recommend the best value for `g_max_value`. `g_max_value` is used to define the maximum amount of points graphed, which determines the level to be picked. Add this part to the developer/user documentation
 - [X] Extend the profiler to profile individual functions
 - [ ] Run the tool on a few real datasets and capture output images for each level, for a few center/radius combinations, and for anomalous points. Add these images to a document per dataset that highlights interpretations of the dataset
 - [ ] Add Developer Documentation
## Nice to implement
 - [ ] Add support for graphing multiple timeseries at the same time
 - [ ] Switch from streamlit to HTML5 canvas

