import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox
obj={"fruits":["strawberry", "banana", "pineapple", "strawberry", "strawberry","pineapple","banana","strawberry","strawberry","banana"],"weight":[10, 118, 800, 11, 12, 900, 124, 13, 11, 131]}
df = pd.DataFrame(obj)


groups = df.groupby("fruits")["weight"].mean().reset_index()
groups



===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

df = pd.DataFrame()
df["screenid"] = ["100034","100053","100061", "100088", "100097"]
df["width"] = [6.7, 17.1, 33.2, 52.4, 112.8]
df["height"]=[13.8, 24.1, 20.8, 29.3, 63.2]
df["area"] = df.eval("width * height")

df

df.query("area > 500")

# df


===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox
obj={"fruits":["strawberry", "banana", "pineapple", "strawberry", "strawberry","pineapple","banana","strawberry","strawberry","banana"],"weight":[10, 118, 800, 11, 12, 900, 124, 13, 11, 131]}
df = pd.DataFrame(obj)


groups = df.groupby("fruits")["weight"].mean().reset_index()
groups



===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

df = pd.DataFrame()
df["screenid"] = ["100034","100053","100061", "100088", "100097"]
df["width"] = [6.7, 17.1, 33.2, 52.4, 112.8]
df["height"]=[13.8, 24.1, 20.8, 29.3, 63.2]
df["area"] = df.eval("width * height")

# df

# df.query("area > 500")

# df

plt.scatter(df["width"], df["height"])

===


import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox
obj={"fruits":["strawberry", "banana", "pineapple", "strawberry", "strawberry","pineapple","banana","strawberry","strawberry","banana"],"weight":[10, 118, 800, 11, 12, 900, 124, 13, 11, 131]}
df = pd.DataFrame(obj)


groups = df.groupby("fruits")["weight"].mean().reset_index()
groups



===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

df = pd.DataFrame()
df["screenid"] = ["100034","100053","100061", "100088", "100097"]
df["width"] = [6.7, 17.1, 33.2, 52.4, 112.8]
df["height"]=[13.8, 24.1, 20.8, 29.3, 63.2]
df["area"] = df.eval("width * height")

# df

# df.query("area > 500")

# df

# plt.scatter(df["width"], df["height"])

robot = pd.DataFrame()
robot["time"]=["08:00:00", "08:15:00", "08:45:00", "09:05:00", "10:00:00", "10:20:00"]
robot["activity"] = ["idle","moving","idle","moving","charging","moving","idle"]
robot["minutes"]=[15,30,20,40,25,10,35]

robot.groupby("activity")["minutes"].sum()

===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox
obj={"fruits":["strawberry", "banana", "pineapple", "strawberry", "strawberry","pineapple","banana","strawberry","strawberry","banana"],"weight":[10, 118, 800, 11, 12, 900, 124, 13, 11, 131]}
df = pd.DataFrame(obj)


groups = df.groupby("fruits")["weight"].mean().reset_index()
groups



===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

# df = pd.DataFrame()
# df["screenid"] = ["100034","100053","100061", "100088", "100097"]
# df["width"] = [6.7, 17.1, 33.2, 52.4, 112.8]
# df["height"]=[13.8, 24.1, 20.8, 29.3, 63.2]
# df["area"] = df.eval("width * height")

# df

# df.query("area > 500")

# df

# plt.scatter(df["width"], df["height"])

robot = pd.DataFrame()
robot["time"]=["08:00:00", "08:15:00", "08:45:00", "09:05:00", "10:00:00", "10:20:00"]
robot["activity"] = ["idle","moving","idle","moving","charging","moving","idle"]
robot["minutes"]=[15,30,20,40,25,10,35]

# robot.groupby("activity")["minutes"].sum()
# robot.groupby("activity")["minutes"].sum().reset_index()

robot.groupby("activity")["minutes"].sum()



time_spent = pd.DataFrame()
time_spent["activity"] = ["charging","idle","moving"]
time_spent["minutes"]=[25,70,80]

plt.barh(time_spent["activity"], time_spent["minutes"])

===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox
obj={"fruits":["strawberry", "banana", "pineapple", "strawberry", "strawberry","pineapple","banana","strawberry","strawberry","banana"],"weight":[10, 118, 800, 11, 12, 900, 124, 13, 11, 131]}
df = pd.DataFrame(obj)


groups = df.groupby("fruits")["weight"].mean().reset_index()
groups



===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

# df = pd.DataFrame()
# df["screenid"] = ["100034","100053","100061", "100088", "100097"]
# df["width"] = [6.7, 17.1, 33.2, 52.4, 112.8]
# df["height"]=[13.8, 24.1, 20.8, 29.3, 63.2]
# df["area"] = df.eval("width * height")

# df

# df.query("area > 500")

# df

# plt.scatter(df["width"], df["height"])

robot = pd.DataFrame()
robot["time"]=["08:00:00", "08:15:00", "08:45:00", "09:05:00", "10:00:00", "10:20:00"]
robot["activity"] = ["idle","moving","idle","moving","charging","moving","idle"]
robot["minutes"]=[15,30,20,40,25,10,35]

# robot.groupby("activity")["minutes"].sum()
# robot.groupby("activity")["minutes"].sum().reset_index()

# robot.groupby("activity")["minutes"].sum()



time_spent = pd.DataFrame()
time_spent["activity"] = ["charging","idle","moving"]
time_spent["minutes"] = [25,70,80]

plt.barh(time_spent["activity"], time_spent["minutes"])
plt.title("Total time spent")


===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox
obj={"fruits":["strawberry", "banana", "pineapple", "strawberry", "strawberry","pineapple","banana","strawberry","strawberry","banana"],"weight":[10, 118, 800, 11, 12, 900, 124, 13, 11, 131]}
df = pd.DataFrame(obj)


groups = df.groupby("fruits")["weight"].mean().reset_index()
groups



===

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

import pandas as pd
import matplotlib.pyplot as plt

# coding sandbox

print("👋 hello 😊")

# df = pd.DataFrame()
# df["screenid"] = ["100034","100053","100061", "100088", "100097"]
# df["width"] = [6.7, 17.1, 33.2, 52.4, 112.8]
# df["height"]=[13.8, 24.1, 20.8, 29.3, 63.2]
# df["area"] = df.eval("width * height")

# df

# df.query("area > 500")

# df

# plt.scatter(df["width"], df["height"])

robot = pd.DataFrame()
robot["time"]=["08:00:00", "08:15:00", "08:45:00", "09:05:00", "10:00:00", "10:20:00"]
robot["activity"] = ["idle","moving","idle","moving","charging","moving","idle"]
robot["minutes"]=[15,30,20,40,25,10,35]

# robot.groupby("activity")["minutes"].sum()
# robot.groupby("activity")["minutes"].sum().reset_index()

# robot.groupby("activity")["minutes"].sum()



time_spent = pd.DataFrame()
time_spent["activity"] = ["charging","idle","moving"]
time_spent["minutes"] = [25,70,80]

plt.barh(time_spent["activity"], time_spent["minutes"], title="Total time spent")
# plt.title("Total time spent")
