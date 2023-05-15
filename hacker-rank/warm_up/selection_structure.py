score = int(input("점수를 입력하세요 : "))
if score > 100 or score < 0:
    print("잘못된 점수 입니다.")
elif score >= 90:
    print("A입니다.")
elif score >= 80:
    print("B입니다.")
elif score >= 70:
    print("C입니다.")
elif score >= 60:
    print("D입니다.")
else:
    print("F입니다.")