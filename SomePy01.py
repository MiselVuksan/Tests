import shapely.geometry as sh
import numpy as np
import pandas as pd
import multiprocessing as mp

def hypotenuse(r):
    return round((r[0]**2 + r[1]**2)**.5, 2)

if __name__ == '__main__':
    ROWS = 100000
    COLUMNS = ['x', 'y']
    data = np.random.randint(0, 10, size=(ROWS, len(COLUMNS)))
    df = pd.DataFrame(data=data, columns=COLUMNS)
    print(df.head())
    with mp.Pool() as p:
        result = p.imap(hypotenuse, df.itertuples(name=False, index=False), chunksize=10)
        print(list(result)[:5])
    print(hypotenuse((3, 4)))