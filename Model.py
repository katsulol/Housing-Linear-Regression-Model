import pandas as pd

df = pd.read_csv("Housing.csv")

x = sum(df["area"])
y = sum(df["price"])
xy = sum(df["area"] * df["price"])
x2 = sum(df["area"]**2)
n = len(df["price"])

slope = (n * xy - x * y) / (n * x2 - x**2)
intercept = (y - slope * x) / n
size = int(input("Enter the Size of your house in Square Metre: "))
price = size * slope + intercept
print("Price is: {}".format(price))
