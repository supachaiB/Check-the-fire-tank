import qrcode

# ข้อมูล URL หรือข้อความที่ต้องการสร้าง QR code
data_list = [
    "https://www.figma.com/proto/2RlAgjA3E2xbtyaW1l470D/%E0%B8%9C%E0%B8%B1%E0%B8%87%E0%B8%96%E0%B8%B1%E0%B8%87%E0%B8%AD%E0%B8%B1%E0%B8%84%E0%B8%84%E0%B8%B5%E0%B8%A0%E0%B8%B1%E0%B8%A2-V1?type=design&node-id=201-126&t=LdN87MNDYMyKW8LB-0&scaling=scale-down&page-id=0%3A1&starting-point-node-id=201%3A126&show-proto-sidebar=1&device-frame=0",
    "https://www.figma.com/file/2RlAgjA3E2xbtyaW1l470D/%E0%B8%9C%E0%B8%B1%E0%B8%87%E0%B8%96%E0%B8%B1%E0%B8%87%E0%B8%AD%E0%B8%B1%E0%B8%84%E0%B8%84%E0%B8%B5%E0%B8%A0%E0%B8%B1%E0%B8%A2-V1?type=design&node-id=0-1&mode=design&t=LdN87MNDYMyKW8LB-0",
    # เพิ่มข้อมูลเพิ่มเติมตามต้องการ
]

# ลำดับชื่อไฟล์ที่ต้องการให้ QR code ถูกบันทึก
file_names = [
    "index.html_qr",
    "figma_prototype_qr",
    "figma_design_qr",
    # เพิ่มชื่อไฟล์ตามจำนวนข้อมูลที่มี
]

# ลูปเพื่อสร้าง QR code สำหรับข้อมูลแต่ละรายการ
for i, data in enumerate(data_list):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # แปลง QR code เป็นภาพ
    img = qr.make_image(fill_color="black", back_color="white")

    # บันทึก QR code เป็นไฟล์ภาพ
    img.save(f"{file_names[i]}.png")
