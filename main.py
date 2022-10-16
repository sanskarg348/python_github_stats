import requests
import firebase_admin
from datetime import date
import os
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': os.environ.get("USER"),
}

response_views = requests.get('https://api.github.com/repos/Atri-Labs/atrilabs-engine/traffic/views', headers=headers)
response_paths = requests.get('https://api.github.com/repos/Atri-Labs/atrilabs-engine/traffic/popular/paths', headers=headers)
response_sources = requests.get('https://api.github.com/repos/Atri-Labs/atrilabs-engine/traffic/popular/referrers', headers=headers)


if __name__ == '__main__':
    response_views = requests.get('https://api.github.com/repos/Atri-Labs/atrilabs-engine/traffic/views', headers=headers)
    response_paths = requests.get('https://api.github.com/repos/Atri-Labs/atrilabs-engine/traffic/popular/paths', headers=headers)
    response_sources = requests.get('https://api.github.com/repos/Atri-Labs/atrilabs-engine/traffic/popular/referrers', headers=headers)




    cred_obj = firebase_admin.credentials.Certificate('key.json')
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': 'https://app-for-github-credentials-default-rtdb.firebaseio.com/'
    })
    from firebase_admin import db
    ref = db.reference(str(date.today()))
    dic = {'views': response_views.json()['count'], 'unique': response_views.json()['uniques'], 'sources': response_sources.json(), 'paths': response_paths.json()}
    ref.set(dic)
