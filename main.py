import pandas as pd
from set_data import filenames

analysis = "Percentage of the mean of all affirmative votes in the United Nations Human Rights Council per year:\n\n"
def analyse_percentage(series):
    global analysis
    year = 2006
    for i in range(len(filenames)-1):
        df = pd.read_csv(filenames[i])
        analysis += str(year) + ": " + (str(round(df[series].mean())) + "%")
        year += 1
        if i != (len(filenames)-2):
            analysis += "\n"
analyse_percentage("Pro_percentage")
analysis += "\n\n"
analysis += "Percentage of the mean of all negative votes in the United Nations Human Rights Council per year:\n\n"
analyse_percentage("Dissapproval_percentage")
with open("analysis.txt", "w") as file:
    file.write(analysis)