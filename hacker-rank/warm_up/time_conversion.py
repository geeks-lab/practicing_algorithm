def timeConversion(s):
    hour, minute, second_AMPM = s.split(':')

    if second_AMPM[2:] == "PM" and hour != '12':
        hour = str(int(hour) + 12)
    if second_AMPM[2:] == "AM" and hour == '12':
        hour = "00"
    if second_AMPM[2:] == "PM" and hour == '12':
        hour = "12"

    conversion_time = hour + ':' + minute + ':' + second_AMPM[0:2]

    print('conversion_time : '+conversion_time)

    return conversion_time

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
