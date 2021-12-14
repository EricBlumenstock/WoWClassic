import matplotlib.pyplot as plt


# https://lightshope.org/stats
# Assumes data has both horde and alliance combined
data = {'Warrior':635291,
'Paladin':195989,
'Hunter':363468,
'Rogue':400608,
'Priest':271420,
'Shaman':188690,
'Mage':409560,
'Warlock':311723,
'Druid':209509}


# Assume Horde and Alliance are roughly equal in terms of raid composition. Horde loses 1 priest and 1 druid in favor of
# two more shamans than Alliance has paladins.
# https://www.reddit.com/r/classicwow/comments/ap47xy/feedback_on_40man_raid_composition/
# https://www.youtube.com/watch?v=AERpvRRvHWk
# https://www.reddit.com/r/classicwow/comments/8n03m7/to_all_future_raiders_the_ideal_40man_raid/
# https://www.reddit.com/r/classicwow/comments/a7yikq/class_and_spec_viability/
raidCompWeight = {'Warrior':8,
'Paladin':4,
'Hunter':3,
'Rogue':6,
'Priest':5,
'Shaman':6,
'Mage':6,
'Warlock':5,
'Druid':3}

for key,value in data.items():
    if not (key is 'Shaman' or key is 'Paladin'):
        data[key] = value/2 # Divide by two if not a Shaman or Paladin
    data[key] = value/raidCompWeight[key]

plt.style.use('dark_background')
plt.figure(figsize=(8,7))
plt.title('Supply of Classes in Raids')
plt.bar(data.keys(), data.values(),
        color=[(0.78,0.61,0.43), (0.96,0.55,0.73), (0.67,0.83,0.45), (1.00,0.96,0.41), (1,1,1), (0.00,0.44,0.87),
               (0.25,0.78,0.92), (0.53,0.53,0.93), (1.00,0.49,0.04)])
plt.savefig("results.png")
