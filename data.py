import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

res = requests.get("https://opentdb.com/api.php", params=parameters)
res.raise_for_status()
data = res.json()

question_data = data["results"]

