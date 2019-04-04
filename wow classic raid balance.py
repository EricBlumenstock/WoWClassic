import pandas as pd
import matplotlib.pyplot as plt


# https://lightshope.org/stats
data = {'Warrior':635291,
'Paladin':195989,
'Hunter':363468,
'Rogue':400608,
'Priest':271420,
'Shaman':188690,
'Mage':409560,
'Warlock':311723,
'Druid':209509}

# https://www.reddit.com/r/classicwow/comments/ap47xy/feedback_on_40man_raid_composition/
# https://www.youtube.com/watch?v=AERpvRRvHWk
# https://www.reddit.com/r/classicwow/comments/8n03m7/to_all_future_raiders_the_ideal_40man_raid/
# https://www.reddit.com/r/classicwow/comments/a7yikq/class_and_spec_viability/
raidComp = {'Warrior':8,
'Paladin':4,
'Hunter':3,
'Rogue':6,
'Priest':5,
'Shaman':8,
'Mage':6,
'Warlock':5,
'Druid':3}

for key,value in data.items():
    if not (key is 'Shaman' or key is 'Paladin'):
        data[key] = value/2
    data[key] = value/raidComp[key]


df = pd.Series(data)
print(df)
plt.style.use('dark_background')
ax = df.plot.bar(figsize=(8,7),
color=[(0.78,0.61,0.43), (0.96,0.55,0.73), (0.67,0.83,0.45), (1.00,0.96,0.41), (1,1,1), (0.00,0.44,0.87), (0.25,0.78,0.92), (0.53,0.53,0.93), (1.00,0.49,0.04)])

plt.show()
