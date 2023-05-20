# import text2emotion
# inp = "I am very angry today please Google can you open Google"
# emotion = text2emotion.get_emotion(inp)
# if emotion:
#     print(emotion)
#     print(max(zip(emotion.values(), emotion.keys()))[1])



import pandas as pd
import random 

movies = pd.read_csv('movies.csv')

a = movies['Year'].tolist()

ran = random.randint(0,100)
print(a[ran])

