import random

text = 'meditations.txt' # Declaring meditations as our text here

with open(text,'r', encoding="utf-8") as myFile: # This will open the text as myFile, declares data as reading the text
    data = myFile.read()

passage = random.choice(list(data.split(' \n')))

with open('passage.txt', 'w') as f:
    f.write(passage)