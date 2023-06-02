import requests



def getItems (limit,offset):
    api_url = 'https://europe.juna-life.ru/pagination.php'
    response = requests.get("{}?limit={}&offset={}".format(api_url,limit, offset))
    print(response.json())
    return response.json()

