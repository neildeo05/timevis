# Using a hierarchy to visualize data

## Compilation
Use pypy3 over python for large datasets (in the millions)
```console
$ pip3 install pypy3
$ pypy3 main.py
```
Since there are no external dependencies, there are no requirements


## Refactoring / Updates
- [ ] Port to numpy - always faster
- [ ] Use numba jit/njit to speed up the process for very large values
- [ ] Ditch pypy
- [ ] Faster way to load data?
- [ ] Add support for more frontends
  - [ ] Altair
  - [ ] Vega/Vega-lite
  - [ ] D3?

