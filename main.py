import pandas as pd
from set_data import filenames

analysis = "Percentage of the mean of all affirmative votes in the United Nations Human Rights Council per year:\n\n"
year = 2006
for i in range(len(filenames)-1):
    df = pd.read_csv(filenames[i])
    analysis += str(year) + ": " + (str(round(df["Pro_percentage"].mean())) + "%")
    year += 1
    if i != (len(filenames)-2):
        analysis += "\n"
with open("analysis.txt", "w") as file:
    file.write(analysis)