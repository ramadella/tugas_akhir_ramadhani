import cv2

# Membuka kamera (0 untuk kamera default, bisa ubah ke 1, 2, dst. untuk kamera lain)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()

    # Jika frame tidak terbaca, keluar dari loop
    if not ret:
        print("Tidak dapat menerima frame (end of stream?)")
        break

    # Menampilkan frame
    cv2.imshow('Kamera', frame)

    # Tekan 'q' untuk keluar dari loop
    if cv2.waitKey(1) == ord('q'):
        break

# Melepas kamera dan menutup jendela
cap.release()
cv2.destroyAllWindows()
