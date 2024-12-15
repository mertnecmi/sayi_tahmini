import random
ist = []
while True:
    aralik = random.randint(1,99)
    deneme = 1
    for i in range(99):
        secim = int(input("1-99 Arası bir sayı giriniz (Çıkış : 0): "))
        if secim == aralik:
            print(deneme, " kerede bildiniz. doğru cevap ", aralik)
            ist.append(deneme)
            break
        elif secim == 0:
            break
        else: 
            if secim < aralik:
                print("küçük yazdınız")
            elif secim > aralik:
                print("büyük yazdınız")
            deneme +=1
            print(deneme, ".kez deniyorsun")

    if len(ist) > 0:
        print("\t" ,len(ist), " kere denediniz ve ortalamanız : " , sum(ist)/len(ist))
    if secim == 0:
        print("0 seçtiniz ve çıktınız....")
        break
