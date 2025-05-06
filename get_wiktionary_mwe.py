import requests

def get_mwe_titles():
    url = "https://en.wiktionary.org/w/api.php"
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": "Category:English_multiword_terms",
        "cmlimit": "max",
        "format": "json"
    }

    with open("wiktionary_mwes.txt", "w") as out:
        while True:
            response = requests.get(url, params=params).json()
            members = response.get('query', {}).get('categorymembers', [])

            for member in members:
                out.write("%s\n" % member["title"])

            if 'continue' in response:
                params.update(response['continue'])
            else:
                break

mwe_titles = get_mwe_titles()
