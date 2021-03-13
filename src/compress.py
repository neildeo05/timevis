import pandas as pd
import statistics
dat = pd.read_csv("../data/out.csv")

def compress(a, f, step):
    assert(step < len(a))
    ret = []
    accum = 0
    for i in range(0,len(a),step) :
        if i != 0:
            t = a[accum:i]
            ret.append(min(t))
            # ret.append(f(t))
            ret.append(max(t))
            accum+=step
    return ret

vals = compress(dat.values[:,1].tolist(), statistics.mean, 1000)
compressed_data = [list(a) for a in zip(range(len(vals)), vals)]
df = pd.DataFrame(compressed_data, columns = ['Time', 'Data'])
df.to_csv('../data/compressed.csv')
