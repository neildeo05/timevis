# Using a hierarchy to visualize data

## Compilation
Use pypy3 over python for large datasets (in the millions)
```console
$ pip3 install pypy3
$ pypy3 main.py
```
Since there are no external dependencies, there are no requirements


## Refactoring / Updates
- [X] Port to numpy - always faster (in decompress functions)
- [ ] Multithreading/Multiprocessing/Ray for utilizing more cores
- [ ] Faster way to load data?
- [ ] Add support for more frontends
  - [ ] Altair
  - [ ] Vega/Vega-lite
  - [ ] D3?

