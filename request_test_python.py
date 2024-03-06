import requests

class_card = "rogue"
url = f"https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/classes/{class_card}"

headers = {
    "X-RapidAPI-Key": "0310d44017msh95947a099754749p15443ajsncb22a165cdd5",    
    'x-rapidapi-host': 'omgvamp-hearthstone-v1.p.rapidapi.com'
    }

response = requests.request("GET", url, headers=headers)

# saving the response on a .txt file

file_path_save = "C:\caio\teste_resposta_request" # retorna com erro PermissionError: [Errno 13] Permission denied: 'C:\\caio' --> checar o porque

f = open(file_path_save, "w")

f.write(response.text.encode("utf-8"))
f.close()


#print (response.content)
