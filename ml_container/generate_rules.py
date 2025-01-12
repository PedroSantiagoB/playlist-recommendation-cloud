from fpgrowth_py import fpgrowth
import pandas as pd
import pickle

df = pd.read_csv("../mnt/data/2023_spotify_ds1.csv")

itemSetList = df.groupby("pid")["track_name"].apply(list).tolist()

freqItemSet, rules = fpgrowth(itemSetList, minSupRatio=0.1, minConf=0.5)

with open("../mnt/data/association_rules.pickle", "wb") as f:
    pickle.dump(rules, f)
