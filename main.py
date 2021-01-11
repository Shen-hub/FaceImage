import cognitive_face as CF
from urllib.request import urlopen
from PIL import Image


KEY = '196f6913f1ad4394821ce3d8915ec2dd'
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)
    
img_url = 'https://im0-tub-ru.yandex.net/i?id=914ebc897ce56f098cf3ca2f2e9d128d&n=13&exp=1'
result = CF.face.detect(img_url)
result = result[0]['faceRectangle'];

original_img = Image.open(urlopen(img_url))
original_img.save('original_img.png')
cropped_face = original_img.crop((result['left'], result['top'], result['left']+result['width'], result['top']+result['height']))
cropped_face.save('cropped_face.png')
