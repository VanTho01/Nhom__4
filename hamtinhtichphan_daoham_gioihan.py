from sympy import symbols, integrate, diff, limit, simplify

# Hàm tính tích phân không xác định
def tich_phan_khong_xac_dinh():
    bien= symbols('x')
    gia_tri_nhap = input("Nhap bieu thuc can tich phan khong xac đinh theo x: ")
    ket_qua = integrate(gia_tri_nhap, bien)
    return ket_qua

# Hàm tính tích phân xác định
def tich_phan_xac_dinh():
    bien= symbols('x')
    gia_tri_nhap = input("Nhap bieu thuc can tich phan xac đinh theo x: ")
    lower_bound = float(input("Nhap gioi han duoi: "))
    upper_bound = float(input("Nhap gioi han tren: "))
    ket_qua = integrate(gia_tri_nhap, (bien, lower_bound, upper_bound))
    return ket_qua

# Hàm tính đạo hàm
def dao_ham():
    bien= symbols('x')
    gia_tri_nhap = input("Nhap bieu thuc can tinh đao ham theo x: ")
    ket_qua = diff(gia_tri_nhap, bien)
    return ket_qua

# Hàm tính giới hạn
def gioi_han():
    bien= symbols('x')
    gia_tri_nhap = input("Nhập biểu thức cần tính giới hạn khi x tiến đến giá trị: ")
    value = float(input("Nhập giá trị x tiến đến: "))
    ket_qua = limit(gia_tri_nhap, bien, value)
    return ket_qua

def main():
    while True:
        print("\nChọn một tùy chọn:")
        print("1. Tính tích phân không xác định")
        print("2. Tính tích phân xác định")
        print("3. Tính đạo hàm")
        print("4. Tính giới hạn")
        print("5. Thoát")
        
        lua_chon = input("Nhập lựa chọn: ")

        if lua_chon == '1':
            ket_qua = tich_phan_khong_xac_dinh()
            print(f"Kết quả tích phân không xác định: {ket_qua}")
        elif lua_chon == '2':
            ket_qua = tich_phan_xac_dinh()
            print(f"Kết quả tích phân xác định: {ket_qua}")
        elif lua_chon == '3':
            ket_qua = dao_ham()
            print(f"Kết quả đạo hàm: {ket_qua}")
        elif lua_chon == '4':
            ket_qua = gioi_han()
            print(f"Kết quả giới hạn: {ket_qua}")
        elif lua_chon == '5':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy chọn lại.")

if __name__ == "__main__":
    main()
