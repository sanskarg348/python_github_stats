import requests

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer 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',
}

response = requests.get('https://api.github.com/repos/Atri-Labs/atrilabs-engine/traffic/popular/referrers', headers=headers)

print(response.text)