import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox
df = pd.DataFrame({
    "mammal":["wild land", "wild marine", "goats", "sheep", "buffaloes", "pigs", "humans", "cattle"],
    "biomass":[3,4,5,6,9,21,60,61],
    "color":["C1","C1","C0","C0","C0","C0","C0","C0"]
})
plt.barh(df["mammal"],df["biomass"], color=df["color"])

===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox
df = pd.DataFrame({
    "mammal":["wild land", "wild marine", "goats", "sheep", "buffaloes", "pigs", "humans", "cattle"],
    "biomass":[3,4,5,6,9,21,60,61],
    "color":["C1","C1","C0","C0","C0","C0","C0","C0"]
})
plt.barh(df["mammal"],df["biomass"], color=df["color"])
plt.grid(axis="x", color="black", alpha=0.5)

===

