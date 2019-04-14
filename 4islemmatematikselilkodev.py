# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("""
      
*************************************

İşlemler:
    
    1.toplama
    2.çıkarma
    3.çarpma
    4.bölme
    
(çıkmak için 'z' tuşunu girin.)

************************************""")
    
while True:
    secilenislem = input("işlem seçiniz:")
    if (secilenislem == "1"):
        ilkdeger = int(input("1.sayıyı girin:"))
        ikincideger = int(input("2.sayıyı girin:"))
        print("{} ve {} sayılarına {} işlemi yapılıyor".format(ilkdeger,ikincideger,"toplama"))
        print("işlemin sonucu:", ilkdeger + ikincideger)
    elif (secilenislem == "2"):
        ilkdeger = int(input("1.sayıyı girin:"))
        ikincideger = int(input("2.sayıyı girin:"))
        print("{} ve {} sayılarına {} işlemi yapılıyor.".format(ilkdeger,ikincideger,"çıkarma"))
        print("işlemin sonucu:", ilkdeger - ikincideger)
    elif (secilenislem == "3"):
        ilkdeger = int(input("1.sayıyı girin:"))
        ikincideger = int(input("2.sayıyı girin:"))
        print("{} ve {} sayılarına {} işlemi yapılıyor.".format(ilkdeger,ikincideger,"çarpma"))
        print("işlemin sonucu:", ilkdeger * ikincideger)
    elif (secilenislem == "4"):
        ilkdeger = int(input("1.sayıyı girin:"))
        ikincideger = int(input("2.sayıyı girin:"))
        print("{} ve {} sayılarına {} işlemi yapılıyor.".format(ilkdeger,ikincideger,"bölme"))
        print("işlemin sonucu:", ilkdeger / ikincideger)
    if (secilenislem == "z"):
        print("program sonlanıyor...")
        break
    