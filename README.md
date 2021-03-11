# timevis
Large (>10 million) dataset visualization using Vega and Altair



## Scaling Functions
  - In order to plot this much data without lag/poor performance, the data has to be scaled down. Using a step, a 'box' is generated. We can plot certain points in that box that are represntative of the trend:
    - median of box
    - min/median/max of the box
    - min/first quartile/median/third quartile/max
  - These scaling functions take a step and a function responsible for generating this data from a list/array


## Quickstart

```console
$ open tests.html
```
