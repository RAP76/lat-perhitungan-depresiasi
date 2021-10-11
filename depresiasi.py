aset = float (input("Metode Garis Lurus\nNominal : "))
lama = int(input("Lama Depresiasi (Tahun) : "))
awal = int(input("Awal Depresiasi: "))
akhir = int(input("Akhir Depresiasi: "))
saldo = float(input ("Residu Aset : "))

def deprec(aset,lama,awal,akhir,saldo):
    if (aset != None and 
        lama != None and 
        awal != None and
        akhir != None and
        saldo != None):
        if (awal < akhir):
            print("\nAset       Th  Akumulasi    Residu")
            susut = (aset - saldo) / lama
            for masa in range(awal, (akhir+1), 1):
                akumulasi = masa * susut
                sisa = aset - akumulasi
                print(aset, masa, akumulasi, sisa)

        else :
            print("Salah")
    else :
        print("STOP")

deprec(aset,lama,awal,akhir,saldo)

