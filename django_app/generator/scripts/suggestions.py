import requests, json

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

# q= "terre de diatomée punaise de lit comment utiliser"
def get_title(q):
    results = []
    # client param could be replaced with firefox or other browser
    response = requests.get(f'http://google.com/complete/search?client=chrome&q={q}', headers=headers)
    for result in json.loads(response.text)[1]:
        results.append(result)
    return results