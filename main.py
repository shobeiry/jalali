from shobeiry_jalali.Jalalian import jdate, JDate

jd = JDate('2017-02-01 21:38:48')
print(jd.format('Y/m/d H:i:s'))  # ۱۳۹۵/۱۱/۱۳ ۲۱:۳۸:۴۸
jd.add(years=3, months=2)
print(jd.format('Y/m/d H:i:s'))  # ۱۳۹۹/۰۱/۱۵ ۲۱:۳۸:۴۸
jd.sub(years=1, months=5, hours=10)
print(jd.format('Y/m/d H:i:s'))  # ۱۳۹۷/۰۸/۰۹ ۱۱:۳۸:۴۸

jd = JDate('1398-02-01 21:38:48', False)
print(jd.format('Y/m/d H:i:s'))  # ۱۳۹۸/۰۲/۳۱ ۲۱:۳۸:۴۸
jd.add(years=3, months=2)
print(jd.format('Y/m/d H:i:s'))  # ۱۴۰۱/۰۴/۳۰ ۲۱:۳۸:۴۸
jd.sub(years=1, months=5, hours=10)
print(jd.format('Y/m/d H:i:s'))  # ۱۳۹۹/۱۱/۲۸ ۱۱:۳۸:۴۸

print(jdate('E'))  # بهمن
print(jdate('e'))  # زمستان
print(jdate('H i s'))  # 10 26 53
print(jdate('H:i:s'))  # 10:26:53
print(jdate('Y/n/j'))  # 1389/11/22
print(jdate('Y E j'))  # 22 بهمن 1389print(jdate('V E J')) # بیست و دو بهمن هزار و سیصد و هشتاد و نه
print(jdate('H:i:s'))  # 10:26:53
print(jdate(r'H:\i:s'))  # 10:i:53
print(jdate(r'H : \i\r\a\n'))  # 10 : iran
print(jdate(r'\HH'))  # H10
print(jdate(r'H\H'))  # 10H
print(jdate(r'H\ H'))  # 10 10
print(jdate(r'\HH\H'))  # H10H
print(jdate(r'\H\o\u : H _ \M\i\n : i _ \S\e\c : s'))  # Hou : 10 _ Min : 26 _ Sec : 53
print(jdate(r" \" H \" "))  # " 10 "
print(jdate(r' \' H \' '))  # ' 10 '
print(jdate(' " H " '))  # " 10 "
print(jdate(" ' H ' "))  # ' 10 '
print(jdate(r'\\\\'))  # \\
print(jdate(r'\\\\H'))  # \\10
print(jdate(r'\\\\\H'))  # \\H
print(jdate('E'))  # بهمن
print(jdate('Eماه'))  # بهمنماه
print(jdate('E ماه'))  # بهمن ماه
print(jdate('ماه E'))  # ماه بهمن
print(jdate('J'))  # بیست و دو
print(jdate('Jم'))  # بیست و دوم
print(jdate('Jمین'))  # بیست و دومین
print(jdate('امروز : Jم E است'))  # امروز : بیست و دوم بهمن است
print(jdate('امروز l است'))  # امروز جمعه است
print(jdate('c'))  # ۱۳۸۹/۱۱/۲۲ ,۱۰:۲۶:۵۳ +۰۳:۳۰
print(jdate('r'))  # ۱۰:۲۶:۵۳ +۰۳۳۰ جمعه, ۲۲ بهمن ۱۳۸۹
print(jdate('H:i:s O ,l, j E Y'))  # ۱۰:۲۶:۵۳ +۰۳۳۰ ,جمعه, ۲۲ بهمن ۱۳۸۹
print(jdate('H:i:s P | l, j / E / Y'))  # ۱۰:۲۶:۵۳ +۰۳:۳۰ | جمعه, ۲۲ / بهمن / ۱۳۸۹
print(jdate('H:i:s P | l, j E Y'))  # ۱۰:۲۶:۵۳ +۰۳:۳۰ | جمعه, ۲۲ بهمن ۱۳۸۹
print(jdate('l, J / E / V'))  # جمعه, بیست و دو / بهمن / هزار و سیصد و هشتاد و نه
print(jdate('l, J E V'))  # جمعه, بیست و دو بهمن هزار و سیصد و هشتاد و نه
print(jdate('H:i:s P ,Y/n/j'))  # ۱۰:۲۶:۵۳ +۰۳:۳۰ ,۱۳۸۹/۱۱/۲۲
print(jdate('H:i:s ,Y/n/j'))  # ۱۰:۲۶:۵۳ ,۱۳۸۹/۱۱/۲۲
print(jdate('H:i:s Z ,Y/n/j'))  # ۱۰:۲۶:۵۳ Asia/Tehran ,۱۳۸۹/۱۱/۲۲
print(jdate('H:i:s ,Y/n/j'))  # ۱۰:۲۶:۵۳ ,۱۳۸۹/۱۱/۲۲
