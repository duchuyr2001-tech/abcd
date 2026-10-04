chieu_dai = int(input("Hãy nhập chiều dài: "))
chieu_rong = int(input("Hãy nhập chiều rộng: "))
chu_vi = ((chieu_dai + chieu_rong)*2)
dien_tich = (chieu_dai * chieu_rong)
print("Chu vi:", chu_vi,"\nDiện Tích:", dien_tich)

Time = int(input("Hãy nhập thời gian: "))
Hour = Time // 60
Minute = Time % 60
print(Hour, "giờ", Minute, "phút")
