import calc_bmi

h = int(input("身長: "))
w = int(input("体重: "))
bmi = calc_bmi.cal_bmi(h, w)
print(bmi)
