import os
import json
class artist:
    def __init__(self, name, uid,avatar):
        self.name = name
        self.id = uid
        self.avatar = avatar
        #确认目录存在
        if os.path.exists('Data') == False:
            os.mkdir('Data')
        artist_path = os.path.join('Data',self.uid)
        if os.path.exists(artist_path) == False:
            os.mkdir(artist_path)
        self.path = artist_path

    def __str__(self):
        return 'artist:'+self.name
        
    def save(self):
        #保存头像
        if self.avatar != None:
            with open(os.path.join(self.path,self.uid,'头像.png'),'wb') as f:
                f.write(self.avatar)
        #保存元数据
        js = json.dumps(self.__dict__,ensure_ascii=False)
        with open(os.path.join('Data',self.uid,'元数据.json'),'w',encoding='utf-8') as f:
            f.write(js)
        