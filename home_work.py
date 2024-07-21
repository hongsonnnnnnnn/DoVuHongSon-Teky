# cho 1 chuỗi số bất kỳ, số lượng bất kỳ, tìm giá trị lớn nhất

# Mô tả
# Viết chương trình cho người dùng nhập cân nặng và chiều cao của mình. Sau đó hãy in ra chỉ số BMI (Body mass index), và tình trạng cơ thể của họ dựa theo công thức và bảng giá trị sau:
# BMI = cân nặng / (chiều cao ^ 2)
# Trong đó cân nặng tính bằng kg và chiều cao tính bằng m
# Chỉ số BMI đối với người trên 20 tuổi được phân loại và diễn giải theo bảng sau:
# BMI < 16: Gầy cấp độ III
# 16 <= BMI < 17:  Gầy cấp độ II
# 17<= BMI < 18.5: Gầy cấp độ I
# 18.5 <= BMI < 25: Bình thường
# 25 <= BMI < 30: Thừa cân
# 30 <= BMI < 35 : Béo phì cấp độ I
# 35 <= BMI < 40: Béo phì cấp độ II
# BMI > 40: Béo phi cap do III
print('chào mừng tới BMI web')
cân_nặng=float(input("nhập cân nặng(kg):"))
chiều_cao=float(input("nhập chiều cao(m):"))
BMI=cân_nặng/chiều_cao**2
if BMI < 16:
    print('Gầy cấp độ III')
elif BMI >= 16 and BMI <17:
    print('Gầy cấp độ II')
elif BMI >=17 and BMI <18.5:
    print('Gầy cấp độ I')
elif BMI >=18.5 and BMI <25:
    print('Bình thường')
elif BMI >=25 and BMI <30:
    print('Thừa cân')
elif BMI >=30 and BMI <35:
    print('Béo phì cấp độ I')
elif BMI >=35 and BMI <40:
    print('Béo phì cấp độ II')
elif BMI >40:
    print('Béo phì cấp độ III')



