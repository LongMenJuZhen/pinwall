#!/usr/bin/env python3
import dbus
import wallpaper
import os
import platform
import notifypy
import tkinter
import cv2
import json

class mywallpaper:
    
    def __init__(self):
        try:
            self.desketop_enviorment = os.getenv("XDG_CURRENT_DESKTOP")
        except:
            self.desketop_enviorment = "NO_XDG"
        self.system = platform.system()
        

    def set_wallpaper(self,filepath):
        #什么时候我kde才能一统linux天下啊>_<
        if self.desketop_enviorment == "KDE":
            self.set_kde_wallpaper(filepath)
        #if self.desketop_enviorment == "GNOME":
        #    self.set_gnome_wallpaper(filepath)
        #windows
        if self.system == "Windows":
            self.set_windows_wallpaper(filepath)
        if self.system == "Darwin":
            self.set_mac_wallpaper(filepath)
        else:
            notification = notifypy.Notify()
            notification.title = "不支持的桌面环境"
            notification.message = "unsported desktop environment"
            notification.send()

    def set_kde_wallpaper(filepath, plugin='org.kde.image'):
        jscript = """
        var allDesktops = desktops();
        print (allDesktops);
        for (i=0;i<allDesktops.length;i++) {
            d = allDesktops[i];
            d.wallpaperPlugin = "%s";
            d.currentConfigGroup = Array("Wallpaper", "%s", "General");
            d.writeConfig("Image", "file://%s")
        }
        """
        bus = dbus.SessionBus()
        plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
        plasma.evaluateScript(jscript % (plugin, plugin, filepath))

    def set_windows_wallpaper(filepath):
        wallpaper.set_wallpaper(filepath)

    def set_mac_wallpaper(filepath):
        wallpaper.set_wallpaper(filepath)
    
    def get_screen_size():
        screen = tkinter.Tk()
        x = screen.winfo_screenwidth()
        #获取当前屏幕的宽
        y = screen.winfo_screenheight()
        #获取当前屏幕的高
        return x,y

class mysave:
    def save_illust(self,illust):
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


    def save_artist(artist):
        #保存头像
        if artist.avatar != None:
            with open(os.path.join(artist.path,artist.uid,'头像.png'),'wb') as f:
                f.write(artist.avatar)
        #保存元数据
        js = json.dumps(artist.__dict__,ensure_ascii=False)
        with open(os.path.join('Data',artist.uid,'元数据.json'),'w',encoding='utf-8') as f:
            f.write(js)