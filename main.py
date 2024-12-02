
from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff("KDDTrain+_20Percent.arff")
veri = pd.DataFrame(data)
print(veri.head())