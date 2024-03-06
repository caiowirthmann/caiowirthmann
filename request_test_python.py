import requests

class_card = "rogue"
url = f"https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/classes/{class_card}"

headers = {
    "X-RapidAPI-Key": "0310d44017msh95947a099754749p15443ajsncb22a165cdd5",    
    'x-rapidapi-host': 'omgvamp-hearthstone-v1.p.rapidapi.com'
    }

response = requests.request("GET", url, headers=headers)

print (response.content)
