![GitHub](https://img.shields.io/github/license/shobeiry/jalali)
[![Downloads](https://pepy.tech/badge/jalali)](https://pepy.tech/project/jalali)
![PyPI - Downloads](https://img.shields.io/pypi/dm/jalali)

## Jalali

 - Jalali calendar is a solar calendar that was used in Persian, variants of which today are still in use in Iran as well as Afghanistan. [Read more on Wikipedia](http://en.wikipedia.org/wiki/Jalali_calendar) or see [Calendar Converter](http://www.fourmilab.ch/documents/calendar/).
## Install
```
pip install jalali
```
## Basic Usage
For Start Import `Jalalian` Library To Your Code Then Use:
```python
from jalali.Jalalian import jdate, JDate

jd = JDate()
jd.format('Y/m/d H:i:s')
jd = JDate('2017-02-01 21:38:48')
jd.format('Y/m/d H:i:s')  # ۱۳۹۵/۱۱/۱۳ ۲۱:۳۸:۴۸
jd.add(years=3, months=2)
jd.format('Y/m/d H:i:s')  # ۱۳۹۹/۰۱/۱۵ ۲۱:۳۸:۴۸
jd.sub(years=1, months=5, hours=10)
jd.format('Y/m/d H:i:s')  # ۱۳۹۷/۰۸/۰۹ ۱۱:۳۸:۴۸

jd = JDate('1398-02-01 21:38:48', False)
jd.format('Y/m/d H:i:s')  # ۱۳۹۸/۰۲/۳۱ ۲۱:۳۸:۴۸
jd.add(years=3, months=2)
jd.format('Y/m/d H:i:s')  # ۱۴۰۱/۰۴/۳۰ ۲۱:۳۸:۴۸
jd.sub(years=1, months=5, hours=10)
jd.format('Y/m/d H:i:s')  # ۱۳۹۹/۱۱/۲۸ ۱۱:۳۸:۴۸

# نکته: اهمّیّت حروف بزرگ و کوچک در نام تابع و کاراکترهای پارامترها  
jdate('E') # بهمن  
jdate('e') # زمستان  
  
# ترکیب دو یا چند کاراکتر با حروف اضافه در یک خروجی  
jdate('H i s') # 10 26 53  
jdate('H:i:s') # 10:26:53  
jdate('Y/n/j') # 1389/11/22  
jdate('Y E j') # 22 بهمن 1389
jdate('V E J') # بیست و دو بهمن هزار و سیصد و هشتاد و نه  
  
# خارج کردن بعضی از کاراکترها یا حروف ، به صورت خام و تبدیل نشده با گذاشتن \ قبل از آن ها  
# منظور از کاراکتر ، تمامی حروف بزرگ و کوچک انگلیسی است که در جدول مربوطه نیز فهرست شده اند  
jdate('H:i:s') # 10:26:53  
jdate(r'H:\i:s') # 10:i:53  
jdate(r'H : \i\r\a\n') # 10 : iran  
jdate(r'\HH') # H10  
jdate(r'H\H') # 10H  
jdate(r'H\ H') # 10 10  
jdate(r'\HH\H') # H10H  
jdate(r'\H\o\u : H _ \M\i\n : i _ \S\e\c : s') # Hou : 10 _ Min : 26 _ Sec : 53  
  
# نکته: قبل از کاراکترهای خاص مثل ' و " حتماً از \ استفاده شود  
jdate(r" \" H \" ") # " 10 "  
jdate(r' \' H \' ') # ' 10 '  
  
# البتّه بستگی به شرایط دارد  
jdate(' " H " ') # " 10 "  
jdate(" ' H ' ") # ' 10 '  
  
# برای خارج کردن خام خود کاراکتر \ از یک \ در قبل از آن استفاده شود  
jdate(r'\\\\') # \\  
jdate(r'\\\\H') # \\10  
jdate(r'\\\\\H') # \\H  
  
# ترکیب حروف اضافه با کلمات خروجی  
jdate('E') # بهمن  
  
jdate('Eماه') # بهمنماه  
  
jdate('E ماه') # بهمن ماه 
  
jdate('ماه E') # ماه بهمن  
  
jdate('J') # بیست و دو  
  
jdate('Jم') # بیست و دوم  
  
jdate('Jمین') # بیست و دومین  
  
jdate('امروز : Jم E است') # امروز : بیست و دوم بهمن است  
  
jdate('امروز l است') # امروز جمعه است  
  
# مرتّب کردن ترکیب حروف و اعداد اضافه در خروجی با ساختار پیچیده  
# ترکیب های پیچیده ، ممکن است نامرتّب یا جا به جا ، نمایش داده شوند.  
# حتماً آن ها را در بین تگ <span dir=ltr></span> قرار دهید. (چپ به راست)  
# چند الگوی کاربردی زیر ، از قبل مرتّب شده اند. می توانید از این ها استفاده نمایید.  
# این الگوها را می توانید ویرایش کنید. حتماً بین تگ <span dir=ltr></span> قرار گیرند.  
  
jdate('c') # ۱۳۹۰/۱۱/۲۲ ,۱۰:۲۶:۵۳ +۰۳:۳۰  
  
jdate('r') # ۱۰:۲۶:۵۳ +۰۳۳۰ جمعه, ۲۲ بهمن ۱۳۹۰  
  
jdate('H:i:s O ,l, j E Y') # ۱۰:۲۶:۵۳ +۰۳۳۰ ,جمعه, ۲۲ بهمن ۱۳۹۰  
  
jdate('H:i:s P | l, j / E / Y') # ۱۰:۲۶:۵۳ +۰۳:۳۰ | جمعه, ۲۲ / بهمن / ۱۳۹۰  
  
jdate('H:i:s P | l, j E Y') # ۱۰:۲۶:۵۳ +۰۳:۳۰ | جمعه, ۲۲ بهمن ۱۳۹۰  
  
jdate('l, J / E / V') # جمعه, بیست و دو / بهمن / هزار و سیصد و هشتاد و نه  
  
jdate('l, J E V') # جمعه, بیست و دو بهمن هزار و سیصد و هشتاد و نه  
  
jdate('H:i:s P ,Y/n/j') # ۱۰:۲۶:۵۳ +۰۳:۳۰ ,۱۳۹۰/۱۱/۲۲  
  
jdate('H:i:s ,Y/n/j') # ۱۰:۲۶:۵۳ ,۱۳۹۰/۱۱/۲۲  
  
jdate('H:i:s Z ,Y/n/j') # ۱۰:۲۶:۵۳ Asia/Tehran ,۱۳۹۰/۱۱/۲۲
```
## Format Help
| Character | Result | Range |
|--|--|--|
|`a`| اوقات روز - به صورت خلاصه | `ق.ض` - `ب.ض` |
|`A`| اوقات روز - به صورت کامل| `قبل از ظهر` - `بعد از ظهر` |
|`b`|شماره ی فصل (ربع) از سال|`1` - `4`|
|`c`| تاریخ با قالب `Y/n/j ,H:i:s P` |-|
|`C`| شماره ی قرن هجری شمسی|... , `15` , `14` , ...|
|`d`| شماره ی روز از ماه|`1` - `31`|
|`e`|نام فصل| `بهار` - `زمستان`|
|`E`|نام ماه|`فروردین` - `اسفند`|
|`f`|میکرو ثانیه|`000000` - `999999`|
|`i`|دقیقه|`00` - `59`|
|`j`|شماره روز از ماه| `1` - `31`|
|`J`|شماره ی روز از ماه به حروف|`یک` - `سی و یک`|
|`k`|درصد باقیمانده از سال|`0` - `100`|
|`K`|درصد گذشت از سال|`0` - `100`|
|`l`|نام روز در هفته|`شنبه` - `جمعه`|
|`L`|سال: 0-غیر کبیسه 1- کبیسه|`0` - `1`|
|`m`|شماره ماه (دو رقمی)|`01` - `12`|
|`M`|نام ماه به صورت خلاصه|`فر` - `اسـ`|
|`n`|شماره ماه|`1` - `12`|
|`N`|عدد روز هفته (1 = یکشنبه)|`1` - `7`|
|`o`|سال هفته ای (به عدد) چهار رقمی|`شماره ی سال`|
|`O`|":" اختلاف ساعت جهانی - بدون|`+1400` , `+1200`|
|`p`|نام باستانی برج ها|`حمل` - `حوت`|
|`P`|اختلاف ساعت جهانی|-|
|`q`|نام حیوانی سال ها|`موش` - `خوک`|
|`Q`|تعداد روز (کامل) باقی مانده از سال	|`365` - `0`|
|`r`|تاریخ با قالب مرکب `H:i:s O Y E j ,l` |-|
|`s`|شماره ثانیه در دقیقه|`0` - `59`|
|`S`|چاپ "ام"|`ام`|
|`t`|تعداد روز های ماه|`29`, `30`, `31`|
|`U`|timestamp (Unix) برچسب زمانی|-|
|`v`|سال به حروف|` ` - `نود و نه`|
|`V`|سال به حروف - کامل|-|
|`w`|عدد روز در هفته - شنبه = 0|`0` - `6`|
|`W`|شماره ی این هفته در سال|`0` - `53`|
|`y`|سال به عدد (2 رقمی)|`00` - `99`|
|`Y`|سال (به عدد) چهار رقمی|-|
|`z`|تعداد روز های گذشته از سال|`0` - `365`|
|`Z`|نام منطقه زمانی|-|