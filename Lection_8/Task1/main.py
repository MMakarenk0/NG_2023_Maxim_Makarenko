import requests
import re
import threading
import argparse

def threadManager(threadNumber, imagesURL, path):
    
    threads = []
    for threadIndex in range(threadNumber):
        threads.append(threading.Thread(target=downloadImages, args=(threadIndex, imagesURL[threadIndex::threadNumber], path)))
        
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

def downloadImages(threadIndex, imagesURL, path):
    for index in range(len(imagesURL)):
        try:
            downloadImage(imageURL=imagesURL[index], savePath=f'{path}/{str(threadIndex)+str(index)}.jpg', threadIndex=threadIndex)
        except:
            None

def getImagesURLS(url):
    response = requests.get(url)
    html = response.text

    imagesURL = re.findall(r'<img.+src="([^"]+)', html)

    for index in range(len(imagesURL)):
        if "https" not in imagesURL[index]:
            imagesURL[index] = "https:" + imagesURL[index]
    
    return imagesURL


parser = argparse.ArgumentParser()
    

parser.add_argument('--url', required=True, help='Link of the site from which we will download the images.')
parser.add_argument('--path', required=True, help='The folder to save downloaded pictures.')
parser.add_argument('--threads', required=False, default=4, help='(optional)The number of threads for programme(WARNING! Do not use very large number! Default number: 4)')


args = parser.parse_args()



threadManager(threadNumber=args.threads, imagesURL=getImagesURLS(args.url), path=args.path)

