import random
data = []
for i in range(1000):
    data.append({'height':random.gauss(2, 1),
                 'weight':random.gauss(40,5),
                'species':'dog'})


for i in range(1000):
    data.append({'height':random.gauss(1, 0.5),
                 'weight':random.gauss(10,2),
                'species':'cat'})

for i in range(1000):
    data.append({'height':random.gauss(5, 1),
                 'weight':random.gauss(60,0),
                'species':'human'})

import json
json.dump(data, open('data.json','w'))

