import requests

base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'    # 端點
gId = 'gp01'    # 要訓練的群組
train_url = f'{base}/persongroups/{gId}/training' # 請求路徑
key = '5ffa5cfdaf804535ab5580caa7c60c60'        # 你的金鑰
headers = {'Ocp-Apim-Subscription-Key': key}    # 請求標頭
response = requests.get(train_url,              # GET 請求
                        headers = headers)
if response.status_code == 200:     
    print("訓練結果：", response.json())
else:
    print("查看失敗", response.json())

