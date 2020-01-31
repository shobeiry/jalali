from src.Jalalian import jdate

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
