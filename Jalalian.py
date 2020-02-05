import datetime
import pytz
import re


class JDate:
    date = datetime.datetime.now()
    tz = 'Asia/Tehran'

    def __init__(self, date_str=None, is_gregorian=True):
        if date_str is not None:
            date_str = trnum(str(date_str).strip())
            error = False
            if is_gregorian:
                if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
                    self.date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date_str):
                    self.date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}$', date_str):
                    self.date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
                elif re.match(r'^\d{4}/\d{2}/\d{2}$', date_str):
                    self.date = datetime.datetime.strptime(date_str, '%Y/%m/%d')
                elif re.match(r'^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}$', date_str):
                    self.date = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M:%S')
                elif re.match(r'^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{6}$', date_str):
                    self.date = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M:%S.%f')
                else:
                    error = True
            else:
                jy = jm = jd = ''
                if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
                    temp = date_str.split('-')
                    temp = jalali_to_gregorian(temp[0], temp[1], temp[2])
                    date_str = str(temp.year) + '-' + str(temp.month) + '-' + str(temp.day)
                    self.date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date_str):
                    date, time = date_str.split(' ')
                    date = date.split('-')
                    temp = jalali_to_gregorian(date[0], date[1], date[2])
                    date_str = str(temp.year) + '-' + str(temp.month) + '-' + str(temp.day) + ' ' + time
                    self.date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}$', date_str):
                    date, time = date_str.split(' ')
                    date = date.split('-')
                    temp = jalali_to_gregorian(date[0], date[1], date[2])
                    date_str = str(temp.year) + '-' + str(temp.month) + '-' + str(temp.day) + ' ' + time
                    self.date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
                elif re.match(r'^\d{4}/\d{2}/\d{2}$', date_str):
                    temp = date_str.split('/')
                    temp = jalali_to_gregorian(temp[0], temp[1], temp[2])
                    date_str = str(temp.year) + '/' + str(temp.month) + '/' + str(temp.day)
                    self.date = datetime.datetime.strptime(date_str, '%Y/%m/%d')
                elif re.match(r'^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}$', date_str):
                    date, time = date_str.split(' ')
                    date = date.split('/')
                    temp = jalali_to_gregorian(date[0], date[1], date[2])
                    date_str = str(temp.year) + '/' + str(temp.month) + '/' + str(temp.day) + ' ' + time
                    self.date = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M:%S')
                elif re.match(r'^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{6}$', date_str):
                    date, time = date_str.split(' ')
                    date = date.split('/')
                    temp = jalali_to_gregorian(date[0], date[1], date[2])
                    date_str = str(temp.year) + '/' + str(temp.month) + '/' + str(temp.day) + ' ' + time
                    self.date = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M:%S.%f')
                else:
                    error = True
            if error:
                print("Date Time Must Be In Below Formats:")
                print("year-month-day | For Example: '" + jdate("Y-m-d") + "' Or '" + self.date.strftime("%Y-%m-%d"))
                print("year-month-day hour:minutes:seconds| For Example: '" + jdate("Y-m-d H:i:s") + "' Or '" + self.date.strftime("%Y-%m-%d %H:%M:%S"))
                print("year-month-day hour:minutes:seconds.microseconds| For Example: '" + jdate("Y-m-d H:i:s.u") + "' Or '" + self.date.strftime("%Y-%m-%d %H:%M:%S.%f"))
                print("year/month/day | For Example: '" + jdate("Y/m/d") + "' Or '" + self.date.strftime("%Y/%m/%d"))
                print("year/month/day hour:minutes:seconds| For Example: '" + jdate("Y/m/d H:i:s") + "' Or '" + self.date.strftime("%Y/%m/%d %H:%M:%S"))
                print("year/month/day hour:minutes:seconds.microseconds| For Example: '" + jdate("Y/m/d H:i:s.u") + "' Or '" + self.date.strftime("%Y/%m/%d %H:%M:%S.%f"))
                exit()

    @staticmethod
    def now(result_format, timestamp=0.0, time_zone='Asia/Tehran', tr_num='fa'):
        return jdate(result_format, timestamp, time_zone, tr_num)

    def timezone(self, tz):
        self.tz = tz
        return self

    def format(self, text, tr_num='fa'):
        return jdate(text, self.date.timestamp(), self.tz, tr_num)

    def add(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0, milliseconds=0, weeks=0):
        self.date += datetime.timedelta(days=years*365)
        self.date += datetime.timedelta(days=months*31)
        self.date += datetime.timedelta(milliseconds=seconds*1000)
        self.date += datetime.timedelta(days=days, hours=hours, minutes=minutes, milliseconds=milliseconds, weeks=weeks)
        return self

    def sub(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0, milliseconds=0, weeks=0):
        self.date -= datetime.timedelta(days=years * 365)
        self.date -= datetime.timedelta(days=months * 31)
        self.date -= datetime.timedelta(milliseconds=seconds*1000)
        self.date -= datetime.timedelta(days=days, hours=hours, minutes=minutes, milliseconds=milliseconds, weeks=weeks)
        return self

    def year(self):
        return int(self.format('Y'))

    def month(self):
        return int(self.format('m'))

    def day(self):
        return int(self.format('d'))

    def hour(self):
        return int(self.format('H'))

    def minute(self):
        return int(self.format('i'))

    def seconds(self):
        return int(self.format('s'))

    def milliseconds(self):
        return int(self.format('f'))

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


def jdate(result_format, timestamp=0.0, time_zone='Asia/Tehran', tr_num='fa'):
    t_sec = 0

    if time_zone != 'local':
        tz = pytz.timezone('Asia/Tehran' if time_zone == '' else time_zone)
    else:
        tz = None
    if timestamp == 0.0:
        now = datetime.datetime.now(tz)
    else:
        now = datetime.datetime.fromtimestamp(timestamp)
    date = now.strftime('%H_%M_%d_%m_%z_%z_%S_%w_%Y').split('_')
    j_temp = gregorian_to_jalali(int(date[8]), int(date[3]), int(date[2]))
    j_y = j_temp.year
    j_m = j_temp.month
    j_d = j_temp.day
    doy = (((j_m - 1) * 31) + j_d - 1) if j_m < 7 else ((j_m - 7) * 30) + j_d + 185
    kab = 1 if ((((j_y % 33) % 4) - 1) == (int((j_y % 33) * 0.05))) else 0
    sl = len(result_format)
    out = ''
    step = 0
    while step < sl:
        sub = result_format[step]
        step += 1
        if sub == '\\':
            if result_format[step]:
                out += result_format[step]
            step += 1
            continue
        elif sub in ['H', 'f']:  # G h u #'I'
            out += now.strftime('%' + sub)
        elif sub == 'a':  # a
            out += 'ق.ظ' if int(date[0]) < 12 else 'ب.ظ'
        elif sub == 'A':  # A
            out += 'قبل از ظهر' if int(date[0]) < 12 else 'بعد از ظهر'
        elif sub == 'b':  # b
            out += int(j_m / 3.1) + 1
        elif sub == 'c':  # c
            out += str(j_y) + '/' + str(j_m) + '/' + str(j_d) + ' ،' + date[0] + ':' + date[1] + ':' + date[6] + ' ' + \
                   date[5]
        elif sub == 'C':  # C
            out += int((j_y + 99) / 100)
        elif sub == 'd':  # d
            out += '0' + str(j_d) if j_d < 10 else str(j_d)
        elif sub == 'D':  # D
            out += jdate_words({'kh': date[7]}, ' ')
        elif sub == 'e':  # f
            out += jdate_words({'ff': j_m}, ' ')
        elif sub == 'E':  # F
            out += jdate_words({'mm': j_m}, ' ')
        elif sub == 'i':
            out += date[1]
        elif sub == 'j':
            out += str(j_d)
        elif sub == 'J':
            out += jdate_words({'rr': j_d}, ' ')
        elif sub == 'k':
            out += trnum(100 - int(doy / (kab + 365) * 1000) / 10, tr_num)
        elif sub == 'K':
            out += trnum(int(doy / (kab + 365) * 1000) / 10, tr_num)
        elif sub == 'l':
            out += jdate_words({'rh': date[7]}, ' ')
        elif sub == 'L':
            out += kab
        elif sub == 'm':
            out += '0' + str(j_m) if j_m < 9 else str(j_m)
        elif sub == 'M':
            out += jdate_words({'km': j_m}, ' ')
        elif sub == 'n':
            out += str(j_m)
        elif sub == 'N':
            out += str(int(date[7]) + 1)
        elif sub == 'o':
            jdw = 0 if int(date[7]) == 6 else int(date[7]) + 1
            dny = 364 + kab + doy
            out += str(j_y - 1) if jdw > (doy + 3) and doy < 3 else str(j_y + 1) if (
                                                                                            3 - doy) > jdw and dny < 3 else str(
                j_y)
        elif sub == 'O':
            out += date[4]
        elif sub == 'p':
            out += jdate_words({'mb': j_m}, ' ')
        elif sub == 'P':
            out += date[5]
        elif sub == 'q':
            out += jdate_words({'sh': j_y}, ' ')
        elif sub == 'Q':
            out += kab + 364 + doy
        elif sub == 'r':
            key = jdate_words({'rh': date[7], 'mm': j_m})
            out += date[0] + ':' + date[1] + ':' + date[6] + ' ' + date[4] + ' ' + key['rh'] + '، ' + str(j_d) + ' ' + \
                   key['mm'] + ' ' + str(j_y)
        elif sub == 's':
            out += date[6]
        elif sub == 'S':
            out += 'ام'
        elif sub == 't':
            out += (31 - int(j_m / 6.5)) if j_m != 12 else kab + 29
        elif sub == 'U':
            out += t_sec
        elif sub == 'v':
            out += jdate_words({'ss': j_y % 100}, ' ')
        elif sub == 'V':
            out += jdate_words({'ss': j_y}, ' ')
        elif sub == 'w':
            out += '0' if int(date[7]) == 6 else str(int(date[7]) + 1)
        elif sub == 'W':
            avs = (0 if int(date[7]) == 6 else int(date[7]) + 1) - (doy % 7)
            if avs < 0:
                avs += 7
            num = int((doy + avs) / 7)
            if avs < 4:
                num += 1
            elif num < 1:
                num = 53 if avs == 4 or avs == (5 if (((j_y % 33) % 4) - 2) == int((j_y % 33) * 0.05) else 4) else 52
            aks = avs + kab
            if aks == 7:
                aks = 0
            out += '01' if ((kab + 363 - doy) < aks) and (aks < 3) else ('0' + str(num) if num < 10 else str(num))
        elif sub == 'y':
            out += substr(str(j_y), 2, 2)
        elif sub == 'Y':
            out += str(j_y)
        elif sub == 'z':
            out += str(doy)
        elif sub == 'Z':
            out += tz.zone
        else:
            out += sub
    return trnum(out, 'fa', '.') if tr_num != 'en' else out


def jdate_words(dic, mod=''):
    for type_ in dic:
        num = trnum(dic[type_])
        if type_ == 'ss':
            sl = len(num)
            xy3 = int(substr(num, 2 - sl, 1))
            h3 = h34 = h4 = ''
            if int(xy3) == 1:
                p34 = ''
                k34 = ['ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده']
                h34 = k34[int(substr(num, 2 - sl, 2)) - 10]
            else:
                temp = substr(num, sl - 1, 1)
                xy4 = int(temp if temp else '0')
                p34 = '' if xy3 == 0 or xy4 == 0 else ' و '
                k3 = ['', '', 'بیست', 'سی', 'چهل', 'پنجاه', 'شصت', 'هفتاد', 'هشتاد', 'نود']
                h3 = k3[xy3]
                k4 = ['', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه']
                h4 = k4[xy4]
            if int(num) > 99:
                a = ['12', '13', '14', '19', '20']
                b = ['هزار و دویست', 'هزار و سیصد', 'هزار و چهارصد', 'هزار و نهصد', 'دوهزار']
                dic[type_] = replace_with_list(substr(num, 0, 2), a, b) + ('' if substr(num, 2, 2) == '00' else ' و ')
            else:
                dic[type_] = ''
            dic[type_] += h3 + p34 + h34 + h4
        elif type_ == 'mm':
            key = (
                'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند')
            dic[type_] = key[int(num) - 1]
        elif type_ == 'rr':
            key = (
                'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه', 'ده', 'یازده', 'دوازده', 'سیزده', 'چهارده',
                'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده', 'بیست', 'بیست و یک', 'بیست و دو', 'بیست و سه',
                'بیست و چهار',
                'بیست و پنج', 'بیست و شش', 'بیست و هفت', 'بیست و هشت', 'بیست و نه', 'سی', 'سی و یک')
            dic[type_] = key[int(num) - 1]
        elif type_ == 'rh':
            key = ('یکشنبه', 'دوشنبه', 'سه شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه', 'شنبه')
            dic[type_] = key[int(num)]
        elif type_ == 'sh':
            key = ('مار', 'اسب', 'گوسفند', 'میمون', 'مرغ', 'سگ', 'خوک', 'موش', 'گاو', 'پلنگ', 'خرگوش', 'نهنگ')
            dic[type_] = key[int(num) % 12]
        elif type_ == 'mb':
            key = ('حمل', 'ثور', 'جوزا', 'سرطان', 'اسد', 'سنبله', 'میزان', 'عقرب', 'قوس', 'جدی', 'دلو', 'حوت')
            dic[type_] = key[int(num) - 1]
        elif type_ == 'ff':
            key = ('بهار', 'تابستان', 'پاییز', 'زمستان')
            dic[type_] = key[int(int(num) / 3.1)]
        elif type_ == 'km':
            key = ('فر', 'ار', 'خر', 'تی‍', 'مر', 'شه‍', 'مه‍', 'آب‍', 'آذ', 'دی', 'به‍', 'اس‍')
            dic[type_] = key[int(num) - 1]
        elif type_ == 'kh':
            key = ('ی', 'د', 'س', 'چ', 'پ', 'ج', 'ش')
            dic[type_] = key[int(num)]
        else:
            dic[type_] = int(num)

    return dic if mod == '' else implode_dic(dic, mod)


def trnum(text, mod='en', mf='٫'):
    num_a = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
    key_a = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', mf)
    if mod == 'fa':
        a = num_a
        b = key_a
    else:
        a = key_a
        b = num_a

    return replace_with_list(text, a, b)


def substr(text, start, length):
    return text[start: start + length]


def implode_dic(dic, mod=''):
    result = ''
    sl = len(dic)
    j = 0
    for i in dic:
        j += 1
        result += dic[i] + (mod if j < sl else '')
    return result


def replace_with_list(text, list1, list2):
    text = str(text)
    for i, ch in enumerate(list1):
        text = text.replace(ch, list2[i])
    return text


def gregorian_to_jalali(year, month, day):
    d_4 = year % 4
    g_a = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    doy_g = g_a[month] + day
    if d_4 == 0 and month > 2:
        doy_g += 1
    d_33 = int(((year - 16) % 132) * .0305)
    a = 286 if (d_33 == 3 or d_33 < (d_4 - 1) or d_4 == 0) else 287
    if (d_33 == 1 or d_33 == 2) and (d_33 == d_4 or d_4 == 1):
        b = 78
    else:
        b = 80 if (d_33 == 3 and d_4 == 0) else 79
    if int((year - 10) / 63) == 30:
        a -= 1
        b += 1
    if doy_g > b:
        jy = year - 621
        doy_j = doy_g - b
    else:
        jy = year - 622
        doy_j = doy_g + a
    if doy_j < 187:
        jm = int((doy_j - 1) / 31)
        jd = doy_j - (31 * jm)
        jm += 1
    else:
        jm = int((doy_j - 187) / 30)
        jd = doy_j - 186 - (jm * 30)
        jm += 7

    return Date(jy, jm, jd)


def jalali_to_gregorian(jy, jm, jd):
    jy, jm, jd = trnum(str(jy) + '_' + str(jm) + '_' + str(jd)).split('_')
    jy = int(jy)
    jm = int(jm)
    jd = int(jd)
    if jy > 979:
        gy = 1600
        jy -= 979
    else:
        gy = 621
    days = (365 * jy) + (int(jy / 33) * 8) + (int(((jy % 33) + 3) / 4)) + 78 + jd + (
        ((jm - 1) * 31) if jm < 7 else (((jm - 7) * 30) + 186))
    gy += 400 * int(days / 146097)
    days %= 146097
    if days > 36524:
        days -= 1
        gy += 100 * int(days / 36524)
        days %= 36524
        if days >= 365:
            days += 1
    gy += 4 * int(days / 1461)
    days %= 1461
    gy += int((days - 1) / 365)
    if days > 365:
        days = (days - 1) % 365
    gd = days + 1
    temp = (0, 31, 29 if (((gy % 4) == 0) and ((gy % 100) != 0) or ((gy % 400) == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    gm = 0
    for v in temp:
        gm += 1
        if gd <= v:
            break
        gd -= v
    return Date(gy, gm, gd)


def jmktime(jy='', jm='01', jd='01', h='00', m='00', s='00', timezone='Asia/Tehran'):
    if jy == '':
        jy = int(jdate('Y', '', '', timezone, 'en'))
    jy, jm, jd, h, m, s = trnum(
        str(jy) + '_' + str(jm) + '_' + str(jd) + '_' + str(h) + '_' + str(m) + '_' + str(s)).split('_')
    temp = jalali_to_gregorian(jy, jm, jd)
    date_str = str(temp.year) + '-' + str(temp.month) + '-' + str(temp.day) + ' ' + h + ':' + m + ':' + 's'
    return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').timestamp()
