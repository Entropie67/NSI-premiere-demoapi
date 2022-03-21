# Liste ultime d'API
# https://github.com/public-apis/public-apis
# Exemples :
# http://numbersapi.com/#42
# https://picsum.photos/
# http://ccdb.hemiola.com/
# https://www.wordsapi.com/docs/
# https://dictionaryapi.dev/

import requests
nombre = input("Quel est votre nombre préféré ?")
url = f"http://numbersapi.com/{nombre}"
r = requests.get(url)
if r.status_code == 200:
    print(r.text)
else:
    print("Erreur avec l'API")



"""
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json
{u'private_gists': 419, u'total_private_repos': 77, ...}"""