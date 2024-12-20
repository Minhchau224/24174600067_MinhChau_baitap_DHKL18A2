danh_sach_mat_hang = []

def nhap_thong_tin_mat_hang():         
    ma_hang = input("Nhập mã hàng: ")  # kiểu chuỗi
    ten_hang = input("Nhập tên hàng: ")  # kiểu chuỗi    bb  bbh0000000000000000000000000
    don_vi_tinh = input("Nhập đơn vị tính: ")  # kiểu chuỗi
    don_gia = float(input("Nhập đơn giá: "))  # kiểu số thực
    so_luong = int(input("Nhập số lượng: "))  # kiểu số nguyên

    thanh_tien = don_gia * so_luong
    
    ty_le_vat = 10
    thue_vat = thanh_tien * ty_le_vat / 100

    mat_hang = {
        'Mã hàng': ma_hang,
        'Tên hàng': ten_hang,
        'Đơn vị tính': don_vi_tinh,
        'Đơn giá': don_gia,
        'Số lượng': so_luong,
        'Thành tiền': thanh_tien,
        'Thuế VAT': thue_vat
    }
    danh_sach_mat_hang.append(mat_hang)
    print("Thông tin mặt hàng đã được thêm vào danh sách.")

