import requests
import json
import os
def get_request(url):

    req = requests.get(url)
    while req.status_code != 200:
        req=requests.get(url)

    content = req.content

    return content

url=input('Type url : ')
r = get_request(url)


FILE_OUTPUT = 'output.avi'

# Checks and deletes the output file
# You cant have a existing file or it will through an error
if os.path.isfile(FILE_OUTPUT):
    os.remove(FILE_OUTPUT)

# opens the file 'output.avi' which is accessable as 'out_file'
with open(FILE_OUTPUT, "wb") as out_file:  # open for [w]riting as [b]inary
    out_file.write(r)