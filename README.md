# timevis
Large (>10 million) dataset visualization using Vega and Altair



## Scaling Functions
  - In order to plot this much data without lag/poor performance, the data has to be scaled down. Using a step, a 'box' is generated. We can plot certain points in that box that are represntative of the trend:
    - median of box
    - min/median/max of the box
    - min/first quartile/median/third quartile/max
  - These scaling functions take a step and a function responsible for generating this data from a list/array

## Data
The scaled down data is found [here](https://gist.githubusercontent.com/neildeo05/1eaace0c48138020d1d88f53dcc239a3/raw/451ec8de369c14108d7902f1c0f89ea8082cd1dc/lotsofdata.csv)


## Quickstart

to serve local data:
  ```console
  $ make -B http
  ```


## TODO
 - [ ] Load full (29 million points) data
 - [ ] Finish Scaling Functions
