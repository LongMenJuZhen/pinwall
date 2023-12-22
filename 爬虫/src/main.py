from web import Pixiv
from artwork import Illust
import json
import cv2
import os
import numpy as np
#指定用户ID返回作品列表

pixiv = Pixiv()
illust_list=pixiv.get_artist_info("31430204")[1]
print(illust_list)

#指定作品ID返回作品信息

id = illust_list[0]
content = pixiv.get_illust_info(illust_list[0])[1]
arr = np.frombuffer(content, np.uint8)
img = cv2.imdecode(arr, -1)
#js2 = pixiv.get_illust_info(illust_list[0])[0]
cv2.imwrite(str(id)+".jpg",img)