
import requests
url='https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=d592639cc10a4e7c8a80f99221c4084b&user_id=195791126%40N07&format=json&nojsoncallback=1'
url='https://www.flickr.com/services/rest/?method=flickr.photos.getPopular'
data={
        'api_key':'d592639cc10a4e7c8a80f99221c4084b',
        'user_id':'195791126@N07',
        'format':'json',
        'nojsoncallback':1
    }
res=requests.get(url,data)
print(res.status_code)
if res.status_code ==200:
    print(res.text)
    print(res.json())
else:
    print("Error :",res.message)

