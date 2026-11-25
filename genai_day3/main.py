import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=10)

'''
print(response.status_code)
print(type(response.json()))
#print(response.text)
#print(json.dumps(response.json(), indent=4))
print(response.headers['Content-Type'])
'''

users = response.json()

print("User's List ",users)
"""
print(type(users))

for user in users:
    print(user["name"], user["email"],sep="#")
"""    
    
