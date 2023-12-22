import os
import cv2
import json
from artist import artist

class Illust(artist):
    def __init__(self,iid,title,url,date,content,tag):
        self.id=iid
        self.title=title
        self.url=url
        self.date=date
        self.content=content
        self.tag = tag

    def __str__(self):
        return "id: "+self.title
    def __dict__(self):
        return {"id":self.id,"title":self.title,"url":self.url,"date":self.date,"content":self.content,"tag":self.tag}

    def save(self,illust):
        #确认目录存在
        data_path = os.path.join('Data')
        if os.path.exists(data_path) == False:
            os.mkdir(data_path)
        artist_path = os.path.join(data_path,illust.artist.uid)
        if os.path.exists(artist_path) == False:
            os.mkdir(artist_path)
        illust_path = os.path.join(artist_path,illust.iid)
        if os.path.exists(illust_path) == False:
            os.mkdir(illust_path)
        #保存文件
        cv2.imwrite(os.path.join(illust_path,illust.title+".jpg"),self.content)
        with open(os.path.join(illust_path,illust.title+".json"),"w") as f:
            json.dump(self.__dict__(),f)
    
    def setwallpaper(self,illust):
        return
    def ai_expand():
        return
    