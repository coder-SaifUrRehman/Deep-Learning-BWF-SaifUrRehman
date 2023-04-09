import numpy as np
import pandas as pd

np.random.seed(123)
df = pd.DataFrame(np.random.randn(5, 3))
print(df)

df[np.abs(df) > 1] = np.sign(df) * 3
print(df)
