from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
wait_time = 1

filename = sys.argv[1]
savedir = "./" + filename

flickr = FlickrAPI(API_KEY, API_SECRET, format='parsed-json')
result = flickr.photos.search(
    text        = 'cat',
    per_page    = 400,
    media       = 'photos',
    sort        = 'relevance',
    safe_search = 1,
    extras      = 'url_q, licence'
)

photos = result['photos']
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)