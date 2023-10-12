import pixivpy3 as vpy
import requests
import bs4
import json

class Pixiv:
    def __init__(self):
    
        self.base_url = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
        self.album_url='https://www.pixiv.net/ajax/user/USERID/profile/all?lang=zh'
        self.illust_url='https://www.pixiv.net/artworks/ILLUSTID'
        self.artist_url='https://www.pixiv.net/users/USERID'

        self.se = requests.session()
        self.headers = {
            'Referer': self.base_url,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    
    def get_artist_info(self,USERID):
        
        #用户信息
        url1=self.artist_url.replace('USERID',USERID)
        response1=self.se.get(url1,headers=self.headers)
        html=response1.text
        soup=bs4.BeautifulSoup(html,'html.parser')
        attr=soup.find('meta',attrs={'name': 'preload-data', 'id': 'meta-preload-data'})
        content = attr['content']  
        data = json.loads(content)  
        user_data=data['user']['23223750']
        #作品列表
        url2=self.album_url.replace('USERID',USERID)
        response = self.get_html(url2)
        js=response.json()
        illust_list=list(js['body']['illusts'].keys())
        if len(illust_list)>10:
            illust_list=illust_list[:10]
        #头像
        avator_url=user_data['imageBig']
        avator_content=self.get_html(avator_url).content

        return user_data,illust_list,avator_content
    
    def get_illust_info(self,ILLUSTID):
        url=self.illust_url.replace('ILLUSTID',ILLUSTID)
        html=self.get_html(url).text
        #解析作品信息
        soup=bs4.BeautifulSoup(html,'html.parser')
        attrs=soup.find('meta',attrs={'name': 'preload-data', 'id': 'meta-preload-data'})
        content = attrs['content']
        js = json.loads(content)
        js2 = js["illust"][ILLUSTID]
        #插图本体
        image_url = js["urls"]["original"]
        image_content = self.get_html(image_url).content
        return js2,image_content


    #辅助函数，不需要直接调用
    def get_html(self, url):
            response = self.se.get(url, headers=self.headers)
            return response