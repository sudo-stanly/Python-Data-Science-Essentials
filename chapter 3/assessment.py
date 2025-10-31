import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox


df = pd.DataFrame({
    "fruit":["apple", "bananas", "guava", "kiwi", "lemon", "orange", "red chilli", "strawberries"],
    "fiber":["9%", "10%", "20%","12%","11%","8%","6%","5%"],
    "ca":["0%","0%","1%","3%","0%","5%","1%"],
    "fe":["0%","1%","1%","1%","3%","0%","5%","1%"],
    "vitamin_c":["7%","14%","380%","154%","88%","85%","239%","110%"],
    "k":["3%","10%","11%","8%","3%","5%","9%","3%"]
})
df[["fruit", "vitamin_c"]]


===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox


df = pd.DataFrame({
    "fruit":["apple", "bananas", "guava", "kiwi", "lemon", "orange", "red chilli", "strawberries"],
    "fiber":["9%", "10%", "20%","12%","11%","8%","6%","5%"],
    "ca":["0%","0%","1%","3%","0%","5%","1%"],
    "fe":["0%","1%","1%","1%","3%","0%","5%","1%"],
    "vitamin_c":["7%","14%","380%","154%","88%","85%","239%","110%"],
    "k":["3%","10%","11%","8%","3%","5%","9%","3%"]
})
df[["fruit", "vitamin_c"]]
df['vitamin_c'] = df['vitamin_c'].str.replace('%', '')


===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox


# df = pd.DataFrame({
#     "fruit":["apple", "bananas", "guava", "kiwi", "lemon", "orange", "red chilli", "strawberries"],
#     "fiber":["9%", "10%", "20%","12%","11%","8%","6%","5%"],
#     "ca":["0%","0%","1%","3%","0%","5%","1%"],
#     "fe":["0%","1%","1%","1%","3%","0%","5%","1%"],
#     "vitamin_c":["7%","14%","380%","154%","88%","85%","239%","110%"],
#     "k":["3%","10%","11%","8%","3%","5%","9%","3%"]
# })
# df[["fruit", "vitamin_c"]]
# df['vitamin_c'] = df['vitamin_c'].str.replace('%', '')


df=pd.DataFrame({
    "sport":["basketball","cricket","golf","ice hockey","ping pong","rugby","soccer","tennis"],
    "players":[5,11,,6,,15,11,],
    "diameter":[24.2, 7.26, 4.27,,4,,,6.86]
})
df["players"].isna()


===

df=pd.DataFrame({
    "sport":["basketball","cricket","golf","ice hockey","ping pong","rugby","soccer","tennis"],
    "players":[5,11,,6,,15,11,],
    "diameter":[24.2, 7.26, 4.27,,4,,,6.86]
})
df["diameter"].isna().sum()

===

df=pd.DataFrame({
    "type":["igneous","igneous","metamorphic","metamorphic","sedimentary","sedimentary"],
    "rock":["basalt","granite","gneiss","marble","limestone","sandstone"],
    "density":["2.8-3.0","2.6-2.7","2.6-2.9","2.4-2.7","2.3-2.7","2.2-2.8"]
})
df['density'].str.split('-', expand=True).astype(float)

===