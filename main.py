import pandas as pd

df = pd.read_excel("data.xlsx")

for index, row in df.iterrows():
    name = row["name"]
    password = row["password"]
    print("Name: ", name)
    print("Password: ",password)
    print("-"*20)