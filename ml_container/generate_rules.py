from fpgrowth_py import fpgrowth
import pandas as pd
import pickle

df = pd.read_csv("2023_spotify_ds1.csv")

itemSetList = df.groupby("pid")["track_name"].apply(list).tolist()

freqItemSet, rules = fpgrowth(itemSetList, minSupRatio=0.1, minConf=0.5)

print(rules[:1])  

with open("../shared_volume/association_rules.pickle", "wb") as f:
    pickle.dump(rules, f)

print("Rules saved to 'association_rules.pickle'")
