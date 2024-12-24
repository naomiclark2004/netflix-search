import pandas as pd

df = pd.read_csv("netflix_data.csv")


def search_director(name):
    info = []
    for i in range(len(df["director"])):
        if name in df["director"][i]:
            info.append(df.loc[i])

    if info == []:
        return "Error"
    else:
        return info


def search_title(name):
    info = []
    for i in range(len(df["title"])):
        if df["title"][i] == name:
            info.append(df.loc[i])

    if info == []:
        return "Error"
    else:
        return info


def search_actor(name):
    info = []
    for i in range(len(df["cast"])):
        if name in df["cast"][i]:
            info.append(df.loc[i])

    if info == []:
        return "Error"
    else:
        return info
