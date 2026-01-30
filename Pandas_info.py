import pandas as pd
rows = [
    {"Candy": "Sour Patch Kids", "Value": "Good", "Flavour": "Very sour and acidic", "Rating": "9/10"},
    {"Candy": "Kit Kat", "Value": "Great", "Flavour": "Sweet and crunchy", "Rating": "7/10"},
    {"Candy": "Fuzzy Peaches", "Value": " Very Good", "Flavour": "Fuzzy, Fruity and Sorta sweet", "Rating": "9/10"},
    {"Candy": "Aero", "Value": "Good", "Flavour": "Bubnly Crunchy and right amount of sweetness", "Rating": "9.5/10"},
    {"Candy": "Skittles", "Value": "Okay", "Flavour": "Aritficially fruity and tastes like sand and weird", "Rating": "-4/10"},
    {"Candy": "Snickers", "Value": "Great", "Flavour": "Unique, with peanuts caramel and nougat going well", "Rating": "8/10"},
]

data = pd.DataFrame(rows)

data.head()
data.info()
data.columns

data.to_csv("cool_spreadsheet.csv", index=False)
print(".csv file saved")