import random

def oyun_oyna():
    # Bu fonksiyon her oyunu başlatacak ve deneme sayısını geri döndürecek.
    tutulansayi = random.randint(1, 99)
    deneme = 0

    while True:
        try:
            secim = int(input("1-99 Arası bir sayı giriniz (Çıkış için 0 yazın): "))
        except ValueError:  # Geçersiz giriş
            print("Lütfen geçerli bir sayı giriniz.")
            continue

        if secim == 0:
            return None  # Kullanıcı çıkış yapmak istiyorsa, None döndür

        deneme += 1
        if secim == tutulansayi:
            print(f"Tebrikler! {deneme}. denemede doğru cevabı bildiniz: {tutulansayi}")
            return deneme  # Doğru cevap bulunduğunda deneme sayısını döndür
        elif secim < tutulansayi:
            print("Daha büyük bir sayı giriniz.")
        else:
            print("Daha küçük bir sayı giriniz.")

        print(f"{deneme} kez denediniz.")

def main():
    ist = []  # Deneme sayılarının listesi

    while True:
        print("\nYeni oyun başlatılıyor...")
        deneme_sayisi = oyun_oyna()
        if deneme_sayisi is None:
            print("Oyundan çıkıyorsunuz.")
            break  # Eğer çıkış yaparsa, ana döngü sonlanır

        ist.append(deneme_sayisi)  # Doğru tahminde bulunulan deneme sayısını ekleyin

        # Ortalama hesaplama ve gösterim
        ortalama = sum(ist) / len(ist)
        print(f"Şu ana kadar {len(ist)} oyun oynadınız ve ortalama deneme sayınız: {ortalama:.2f}")

if __name__ == "__main__":
    main()
