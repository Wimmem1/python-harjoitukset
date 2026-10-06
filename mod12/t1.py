import json

li1 = [2, 6, 'hello', (3, 4), [5, 4]]


with open("muisiti.txt", "w") as f: 
    json.dump(li1, f)