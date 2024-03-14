d1 = dict()
d2 = {'a': 5, 'm': 22, 'k': 88}
d2['r'] = 18
d2['k'] = 33  # overwrite previous value
del d2['m']
print(f"{d2 = }\n")


d3 = {}  # empty dict

st_capitals = {}
st_capitals['VA'] = 'Richmond'
st_capitals['TX'] = 'Austin'
print(f"{st_capitals = }\n")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['RDU'] = }")
print(f"{airports['LHR'] = }")
# print(f"{airports['LAX'] = }")
print(f"{airports.get('LAX') = }")
print(f"{airports.get('MCO') = }")
print(f"{airports.get('LAX', 'NOT FOUND') = }")

#  DICT.keys()  DICT.values()  DICT.items()

for code, name in airports.items():
    print(code, name)
print('-' * 60)


