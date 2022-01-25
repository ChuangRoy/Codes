import requests

base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'    # 端點
key = '3aebb4c9bef249aba9dad2b2299067c3'                                # 你的金鑰
headers_json = {'Ocp-Apim-Subscription-Key': key,     
                'Content-Type': 'application/json'}

def face_identify(faceId):
    idy_url = f'{base}/identify'                                            # 臉部偵測的請求路徑
    body = str({'personGroupId': '群組 id', 
    			'faceIds': [faceId]})
    response = requests.post(idy_url,       # 臉部驗證請求 POST 
                             headers=headers_json, 
                             data=body)  
    if response.status_code == 200:
        person = response.json()
        if not person[0]['candidates'] :
            print('找不到相符的身分')
            return None 
        else:
            print(person)
            personId = person[0]['candidates'][0]['personId']   # 取得 personId
            print(personId)
            return personId

