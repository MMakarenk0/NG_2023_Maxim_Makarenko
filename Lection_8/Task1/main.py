import requests
import re
import threading

def threadManager(threadNumber, imagesURL):
    
    threads = []
    for threadIndex in range(threadNumber):
        threads.append(threading.Thread(target=downloadImages, args=(threadIndex, imagesURL[threadIndex::threadNumber])))
        
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
        

def downloadImage(imageURL, savePath, threadIndex):
    response = requests.get(imageURL)
    if response.status_code == 200:
        with open(savePath, 'wb') as file:
            file.write(response.content)
            print(f"Thread{threadIndex}: Image saved!")
    else:
        print("url error")

def downloadImages(threadIndex, imagesURL):
    for index in range(len(imagesURL)):
        try:
            downloadImage(imageURL=imagesURL[index], savePath=f'D:/downloaded_images/{str(threadIndex)+str(index)}.jpg', threadIndex=threadIndex)
        except:
            None

url = 'https://uk.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D0%B7%D0%B8%D1%81%D1%82%D0%BE%D1%80'

response = requests.get(url)
html = response.text

imagesURL = re.findall(r'<img.+src="([^"]+)', html)

for index in range(len(imagesURL)):
    if "https" not in imagesURL[index]:
        imagesURL[index] = "https:" + imagesURL[index]

threadManager(threadNumber=4, imagesURL=imagesURL)

