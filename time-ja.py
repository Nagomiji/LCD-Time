import time
import datetime
from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1306

# OLEDディスプレイの初期化
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_address=0x3C)
disp.begin()

# 画面を消す
disp.clear()
disp.display()

# 画像
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# フォント
font_path = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf"
font = ImageFont.truetype(font_path, 15)

try:
    now = datetime.datetime.now()
    weekdays = ['月', '火', '水', '木', '金', '土', '日']
    while True:

        if now.second != datetime.datetime.now().second:
            now = datetime.datetime.now()
            weekday_str = weekdays[now.weekday()]
            text = now.strftime('%Y/%m/%d') + f' {weekday_str}\n' + now.strftime('%H:%M:%S')
            if now.minute == 0 and now.second == 0:
                draw.rectangle((0, 0, width, height), outline=0, fill=1)
                draw.text((0, 0), text, font=font, fill=0)
                disp.image(image)
                disp.display()
                while now.second < 10:
                    if now.second != datetime.datetime.now().second:
                        now = datetime.datetime.now()
                        weekday_str = weekdays[now.weekday()]
                        text = now.strftime('%Y/%m/%d') + f' {weekday_str}\n' + now.strftime('%H:%M:%S')
                        draw.rectangle((0, 0, width, height), outline=0, fill=1)
                        draw.text((0, 0), text, font=font, fill=0)
                        disp.image(image)
                        disp.display()

            else:
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((0, 0), text, font=font, fill=1)
                disp.image(image)
                disp.display()

# Ctrl + C
except KeyboardInterrupt:
        disp.clear()
        disp.display()
