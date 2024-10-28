import requests
import json
import itertools
import string

cookies = {
    
}

headers = {
    
}

url = {

}

params = {

    'q': 'aa'
}

st = string.ascii_lowercase
 
per = itertools.permutations(st, 2)

for i in per:
    params["q"] = ''.join(i)
    response = requests.get(
        url=url,
        params=params,
        cookies=cookies,
        headers=headers,)

    print(response.json())