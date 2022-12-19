import cv2
from pytesseract import image_to_string

try:
    image_avail = ["image1", "image2", "image3", "image4"]
    image_name = input("Nhập vào tên ảnh: ")
    if image_name not in image_avail:
        raise Exception("Ảnh không tồn tại")
    img = cv2.imread(f"{image_name}.png")
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w*2, h*2))
    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
    thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = image_to_string(thr)
    print("=============================\n")
    print("Text mà tôi đọc được trong ảnh là:", text)
    print("\n=============================")
except Exception as e:
    print("Error:", e)