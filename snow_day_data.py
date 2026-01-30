import pandas as pd
rows = [
    {"Day": "1", "Snow": "4", "Cold": "5"},
    {"Day": "2", "Snow": "5", "Cold": "5"},
    {"Day": "3", "Snow": "3", "Cold": "4"},
    {"Day": "4", "Snow": "5", "Cold": "5"},
    {"Day": "5", "Snow": "4", "Cold": "5"},
    {"Day": "6", "Snow": "2", "Cold": "4"},
    {"Day": "7", "Snow": "5", "Cold": "3"},
    {"Day": "8", "Snow": "4", "Cold": "4"},
    {"Day": "9", "Snow": "3", "Cold": "5"},
    {"Day": "10", "Snow": "3", "Cold": "4"},
    {"Day": "11", "Snow": "5", "Cold": "3"},
    {"Day": "12", "Snow": "4", "Cold": "5"},
    {"Day": "13", "Snow": "5", "Cold": "5"},
    {"Day": "14", "Snow": "3", "Cold": "4"},
    {"Day": "15", "Snow": "4", "Cold": "5"}
]

data = pd.DataFrame(rows)

data.head()
data.info()
data.columns

data.to_csv("snow.csv", index=False)
print(".csv file saved")