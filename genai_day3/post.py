import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Learning Generative AI",
    "body":"Building my first GenAI application",
    "userid":1
}

response = requests.post(
    url,
    data,
    timeout=10
)

print(response.raise_for_status())
print(response.status_code)
print(response.json())