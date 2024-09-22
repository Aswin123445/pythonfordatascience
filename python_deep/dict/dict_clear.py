import random

di={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
di={x:[] for x in di}
print(di)

di={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

di = {k: [random.randint(10, 100) for x in v] for k, v in di.items()}
print(di)

