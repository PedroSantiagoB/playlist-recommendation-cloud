from fpgrowth_py import fpgrowth
import pandas as pd
import pickle
import os

dataset_path = os.getenv('DATASET_PATH')

df = pd.read_csv(dataset_path)

itemSetList = df.groupby("pid")["track_name"].apply(list).tolist()

freqItemSet, rules = fpgrowth(itemSetList, minSupRatio=0.1, minConf=0.5)

with open("../mnt/data/association_rules.pickle", "wb") as f:
    pickle.dump(rules, f)
