# fresh-mail
Janky, unfinished script for scraping emails from FreshService written in Python

This script is based off this write-up by Mohammed Moiz Pasha: https://infosecwriteups.com/hundreds-of-companies-internal-data-exposed-part-2-the-freshservice-misconfiguration-a9432c0b5dc8

I have plans to include fields to get the session cookie and automatically format a request, but it's late and I'm tired so I'll do it tomorrow or whenever.

Here's more or less the plan:

scraper.py(url, email, password, output)

login_function(email, password) get authenticated_request return authenticated_request

create_tuple_function() creates tuple return tuple

make_request(tuple) loops through tuple and makes a request for each tuple concats request contents to output file

remove duplicate entries

return outfile
