

# fleshscraper
Janky, unfinished script for scraping emails from FreshService written in Python using the "delegate tickets" feature in FreshService

PLEASE DON'T USE THIS SCRIPT FOR EVIL AND MALICE, USE THIS SCRIPT LEGALLY IN A COOL, NICE AND RESPONSIBLE WAY :) 

This script is based off this write-up by Mohammed Moiz Pasha: https://infosecwriteups.com/hundreds-of-companies-internal-data-exposed-part-2-the-freshservice-misconfiguration-a9432c0b5dc8

How to get working: 

1. Login with account to example.freshservice.com/support/login
2. Get cookies and headers via this method here and use the Python method: https://curlconverter.com/ 
3. Create a text file to store cookie information in same location as script. It should look like this "cookies = {lots of stuff}". Make sure it's copied to your new file.
4. Create a text file to store header information in same location as script. It should look like this "headers = {lots of stuff}". Make sure it's copied to your new file.
5. Run script with 'freshmail.py https://example.freshservice.com/search/autocomplete/agents_and_requesters -c cookie.txt -H header.txt -o outputfile.json -v'

NOTE: MAKE SURE YOU USE THIS URL (replacing the example with your FreshService instance: https://example.freshservice.com/search/autocomplete/agents_and_requesters

the script will run and spit out emails and names into a .json file. Run the -v options to watch the emails come out in real time and make sure the script is working properly. 
