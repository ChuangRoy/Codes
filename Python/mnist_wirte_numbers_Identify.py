#!/usr/bin/env python
# coding: utf-8

# %% In[ ]:


# mnist:手寫數字資料
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
from sklearn.metrics import confusion_matrix
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.datasets.mnist import load_data

# 輸入: x 輸出: y
# 訓練(帶回家的): train 測試(小考): test
# ((訓練圖片 訓練答案), (測試圖片 測試答案))
(x_train, y_train), (x_test, y_test) = load_data()


# %% In[ ]:


print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


# %% In[ ]:


print(y_train[0])
# pandas(pd):表格工具 pd.DataFrame: 把東西轉換成表格
pd.DataFrame(x_train[0])


# %% In[ ]:


# https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

plt.imshow(x_train[0], cmap="gray")


# %% In[ ]:


# 創造我們模型: 完整模型model 一層一層layer
# Sequential: layer一定會堆在前一層的上面
# Dense: 稠密層/全連接層
layers = [
    # 128:128根神經, input_dim:784(28*28)
    Dense(128, activation="sigmoid", input_dim=784),
    Dense(10, activation="sigmoid")
]
model = Sequential(layers)
model.summary()


# %% In[ ]:


# 輸出一個: binary crossentropy
# 輸出多個: categorical crossentropy
model.compile(loss="mse",
              metrics=["accuracy"])


# %% In[ ]:


# 預處理
# x: 1.reshape 2.scaling
# y: one-hot
x_train_r = x_train.reshape(-1, 784) / 255
x_test_r = x_test.reshape(-1, 784) / 255
y_train_cat = to_categorical(y_train, num_classes=10)
y_test_cat = to_categorical(y_test, num_classes=10)
print(x_train_r.shape)
print(y_train_cat[0])
print(y_train[0])


# %% In[ ]:


callbacks = [
    EarlyStopping(patience=5, restore_best_weights=True),
    ModelCheckpoint("mlp.h5", save_best_only=True)
]
# validation_split: 切出一部分資料驗證
# batch_size: 看多少筆才做一次調整(梯度下降)
# epochs: 訓練次數(60000-6000筆/epoch)
# 1 epoch 多少次梯度下降: 54000 / 200 -> 270
# verbose: 印出多少log(1:default 0:quiet 2:)
model.fit(x_train_r,
          y_train_cat,
          validation_split=0.1,
          batch_size=200,
          epochs=270,
          verbose=2,
          callbacks=callbacks)


# %% In[ ]:


model.evaluate(x_test_r, y_test_cat)


# %% In[ ]:


# sklearn: predict_proba/predict
# keras: predict/predict_classes
pre = model.predict_classes(x_test_r)
mat = confusion_matrix(y_test, pre)
pd.DataFrame(mat,
             index=["{}(真實)".format(i) for i in range(10)],
             columns=["{}(預測)".format(i) for i in range(10)])


# %% In[ ]:


idx = np.nonzero(pre != y_test)[0][:200]
false_pre = pre[idx]
false_ori = y_test[idx]
false_img = x_test[idx]

plt.figure(figsize=(14, 42))
width = 10
height = len(idx) // width + 1
for i in range(len(idx)):
    plt.subplot(height, width, i+1)
    t = "[O]:{}\n[P]:{}".format(false_ori[i], false_pre[i])
    plt.title(t)
    plt.axis("off")
    plt.imshow(false_img[i])


# %% In[ ]:


# PIL(pillow)
fn = input("檔名")
# img = Image.open(fn).resize((28, 28)).convert("L")
img = load_img(fn, target_size=(28, 28)).convert("L")
img = np.array(img)
img_r = img.reshape(1, 784) / 255
proba = model.predict(img_r)[0]
for i in range(10):
    print(i, "的機率:", round(proba[i], 3))
ans = model.predict_classes(img_r)[0]
print("答案:", ans)
plt.imshow(img)
