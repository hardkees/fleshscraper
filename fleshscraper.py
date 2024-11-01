import requests
import json
import itertools
import string
import argparse
import ast
import sys


ascii_string = string.ascii_lowercase
permutation_string = itertools.permutations(ascii_string, 2)
params = {"q": '~'}


parser = argparse.ArgumentParser(prog='fresh-mailer')
parser.add_argument("url", help="URL to FreshService support portal, example: 'https://michaelsoft.freshservice.com/search/autocomplete/agents_and_requesters/'")
parser.add_argument("-c", "--cookie", action="store", help="Enter the file name you would like to open the cookie file from")
parser.add_argument("-H", "--header", action="store", help="Enter the file name you would like to open the header file from, rember to use capital '-H'")
parser.add_argument("-o", "--output", action="store", help="Enter the directory you would like to store the JSON out file to")
parser.add_argument("-v", "--verbose", action="store_true", help="Add a constant output stream to the terminal")
args = parser.parse_args()

with open(args.cookie, "r") as file:
    cookies = (file.read())
    cookies = cookies.replace("cookies = ",'')    
    cookies = ast.literal_eval(cookies)
    
with open(args.header, "r") as file:
    headers = (file.read())
    headers = headers.replace("headers = ",'')    
    headers = ast.literal_eval(headers)
   

session = requests.Session()

list_output = []
count = 0
request = requests.get(url=args.url, params=params, cookies=cookies, headers=headers)
if request.text not in "[]":
    print(f"{args.url} not valid. Did not receive expected expected response")
    print("Status code: " + str(request.status_code))
    print("Response: " + request.text)
    sys.exit()

with open(str(args.output), "w") as output_file:
    print("Enumerating users...")
    for i in permutation_string:
        count += 1
        percent = (count / 650) * 100
        sys.stdout.write(f"\r{percent:.2f}% complete")
        
        params["q"] = ''.join(i)
        response = session.get(
            url=args.url,
            params=params,
            cookies=cookies,
            headers=headers,)
        if args.verbose and response.text != '[]':
            sys.stdout.write(f"\r{response.text}\n")
        sys.stdout.flush()    

        if response.text != '[]':
            
            json_list = response.json()
            for i in json_list:
                for o in i.get('children'):
                    if o not in list_output:
                        list_output.append(o)
    json.dump(list_output, output_file, ensure_ascii=False, indent=4)
                        

                
            
    
