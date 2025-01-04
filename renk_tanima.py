import cv2
import numpy as np

# Kullanıcıdan RGB renk değerlerini al
def get_color_input():
    print("Lütfen aradığınız rengin RGB değerlerini girin.")
    red = int(input("Kırmızı (0-255): "))
    green = int(input("Yeşil (0-255): "))
    blue = int(input("Mavi (0-255): "))
    return (blue, green, red)  # OpenCV'nin renk sıralaması BGR'dir

# Renk tanıma işlemi
def detect_color(image, color):
    # Belirtilen rengi belirten bir maske oluşturuyoruz
    lower_bound = np.array([color[0] - 10, color[1] - 10, color[2] - 10])
    upper_bound = np.array([color[0] + 10, color[1] + 10, color[2] + 10])
    
    # Maskeyi uygulayarak sadece belirtilen rengi filtreliyoruz
    mask = cv2.inRange(image, lower_bound, upper_bound)
    result = cv2.bitwise_and(image, image, mask=mask)
    
    return result, mask

# Ana fonksiyon
def main():
    # Görseli yükle
    image = cv2.imread('image.jpg')  # Burada 'image.jpg' yerine kullanmak istediğiniz görseli ekleyebilirsiniz
    if image is None:
        print("Resim yüklenemedi. Lütfen geçerli bir dosya yolu sağlayın.")
        return
    
    # Renk seçimi
    color = get_color_input()

    # Renk tespitini yap
    result, mask = detect_color(image, color)

    # Sonuçları göster
    cv2.imshow("Original Image", image)
    cv2.imshow("Color Detected", result)
    cv2.imshow("Mask", mask)

    # Çıkmak için herhangi bir tuşa basın
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Programı başlat
if __name__ == "__main__":
    main()