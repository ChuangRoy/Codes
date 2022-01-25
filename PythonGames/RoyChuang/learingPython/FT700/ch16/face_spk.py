import face_spk_module as m   # 匯入有語音功能的自訂模組

base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # 端點
key = '5ffa5cfdaf804535ab5580caa7c60c60'                             # 你的金鑰
gid = 'gp01'                                                         # 群組 Id
pid = '4b19526e-69a0-4d1a-89f1-285e9cb18c12'                         # 成員 Id

m.face_init(base, key)  # 初始化端點和金鋪
m.face_use(gid, '')    # 指定要操作的 gid 和 pid
m.face_shot('who')      # 呼叫拍照函式來拍照並上傳到Azuse新增成員人臉影像
