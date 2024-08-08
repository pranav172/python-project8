import requests, json
myEvents = []
result = requests.get("https://icanhazdadjoke.com/", headers = {"Accept": "application/json"})
# print(result.content)

joke = result.json()
f = open("jokes.txt", "a+")
f.write(str(joke["joke"]))
f.close()  
print(joke["joke"])

