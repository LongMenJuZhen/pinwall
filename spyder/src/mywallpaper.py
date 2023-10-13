#!/usr/bin/env python3
import dbus
import wallpaper
import os
import platform
import notifypy
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