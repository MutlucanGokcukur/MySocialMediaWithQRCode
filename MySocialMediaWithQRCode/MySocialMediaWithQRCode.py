# -*- coding: cp1254 -*-
import qrcode
from PIL import Image


print("""
Ulaşmak istediğiniz sosyal medya platformunu seçiniz
1-İnstagram
2-LinkedIn
3-GitHub
4-E-Mail Adres
""")

try:
    secim=int(input("Seçiminizi giriniz: "))
    if secim==1:
        code=qrcode.make('https://www.instagram.com/mutlucan_gokcukur/')
        code.save("insta.png")
        img=Image.open("insta.png")
        img.show()
    elif secim==2:
        code=qrcode.make('https://www.linkedin.com/in/mutlucan-g%C3%B6k%C3%A7ukur-12165021b')
        code.save("LinkedIn.png")
        img=Image.open("LinkedIn.png")
        img.show()
    elif secim==3:
        code=qrcode.make('https://github.com/MutlucanGokcukur')
        code.save("github.png")
        img=Image.open("github.png")
        img.show()
    elif secim==4:
        img=Image.open("E-Mail Karekod.png")
        img.show()
except ValueError:
    print("Lütfen sayısal bir değer giriniz...")
except:
    print("Bir hata meydana geldi...")
