import pandas as pd

print(pd.__version__)
dict1 = {
    "no" : ["ONE","TWO "],
    "name" : ["Aakash", "Pratik"]
    }
a = pd.DataFrame(dict1)
print(a)

b = [1, 2, 3, 4]
print(pd.Series(b, index= ["x", "y", "z", "w"]))
# print(b["y"])
print(b[0])

calories = {"day1": [420, 647, 3664], 
            "day2": [380, 6337],
            "day3": [390, 6734,7364, 288]}
c= pd.Series(calories)

print(c)
pd.options.display.max_rows = 9999
# df = pd.read_csv('data.csv')

# print(df) 

# print("Current working directory:", os.getcwd())  # see where Python looks
# df = pd.read_csv("data.csv")
# print(df.head())

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df) 