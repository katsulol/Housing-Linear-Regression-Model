import pandas as pd
import numpy as np
import matplotlib as plt



df = pd.read_csv("Housing.csv")
features = df.drop("price", axis=1)
target = df["price"]
print(features)
print(target)


