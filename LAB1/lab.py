import numpy as np
import pandas as pd
data = pd.read_csv("../input/pythonProject1 /lab.csv")
print(data)

h = np.array(data)[:, :-1]
t = np.array(data)[:, -1]

h = ["", ""]


def training_example(H, t):
    for z, x in list(enumerate(H)):
        if t[z] == "Yes":
            for i in range(len(x)):
                if h[i] == "*" and x[i]:
                    h[i] = x[i]
                elif h[i] != x[i] and h[i] != "?":
                    h[i] = "?"

    return h