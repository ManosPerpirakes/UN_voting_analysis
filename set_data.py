import pandas as pd

filenames = [
    "un_voting_2006.csv",
    "un_voting_2007.csv",
    "un_voting_2008.csv",
    "un_voting_2009.csv",
    "un_voting_2010.csv",
    "un_voting_2011.csv",
    "un_voting_2012.csv",
    "un_voting_2013.csv",
    "un_voting_2014.csv",
    "un_voting_2015.csv",
    "un_voting_2016.csv",
    "un_voting_2017.csv",
    "un_voting_2018.csv",
    "un_voting_2019.csv",
    "un_voting_2020.csv",
    "un_voting_2021.csv",
    "un_voting_2022.csv",
    "un_voting_2023.csv",
]
def set_yes(var):
    var = var.split(" | ")[0]
    return int(var[9:])
def set_no(var):
    var = var.split(" | ")[1]
    return int(var[4:])
def set_abtsent(var):
    var = var.split(" | ")[2]
    return int(var[13:])
def set_non_voting(var):
    return int(var.split(" | ")[3][12:])
def set_total(var):
    return int(var.split(" | ")[4][len("Total voting membership: "):])
def set_percentage(var):
    return round(var*100/47)
def set_data():
    global df
    df["Yes"] = df["vote_summary"].apply(set_yes)
    df["No"] = df["vote_summary"].apply(set_no)
    df["Abstention_count"] = df["vote_summary"].apply(set_abtsent)
    df["Non-Voting"] = df["vote_summary"].apply(set_non_voting)
    df["Total"] = df["vote_summary"].apply(set_total)
    df["Pro_percentage"] = df["Yes"].apply(set_percentage)
    df["Dissapproval_percentage"] = df["No"].apply(set_percentage)
    df["Abstention_percentage"] = df["Abstention_count"].apply(set_percentage)
for i in filenames:
    df = pd.read_csv(i)
    set_data()
    df.to_csv(i)