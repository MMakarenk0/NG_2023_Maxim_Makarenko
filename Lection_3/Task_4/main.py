import requests

# Function for getting status code from link
def getStatusCode(linkList):
    for link in linkList:
        response = requests.get(link)
        if response:
            print(f"{response.status_code}: OK")
        elif response.status_code == 418:
            print(f"{response.status_code}: I'm a teapot")
        else:
            print(f"{response.status_code}: FAIL")

linkList = ["https://tasks.ngcourses.net/b/eLR8Hn6qpLx7WS6Nj/python-maxim-makarenko/juRv57w9y4NNAo3fs", 
            "https://www.youtube.com/", "https://www.google.com/teapot", "https://www.google.com/pagenotfound", 
            "https://www.google.com/Aboba"]
getStatusCode(linkList)
    
  