import numpy as np
import pandas as pd

COLUMNS = ['x', 'y']
data = np.random.randint(0, 9, size=(20, len(COLUMNS)))
df = pd.DataFrame(data=data, columns=COLUMNS)
print(df.head())