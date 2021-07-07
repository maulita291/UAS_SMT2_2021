ulang = 'y'
while ulang == 'y':
    #Format UANG
    def rp(uang):
            x = str(uang)
            if len(x) <= 3:
                return 'Rp. ' + x
            else:
                a = x[:-3]
                b = x[-3:]
                return rp(a) + '.' + b
    #SiapkanVar
    kode = ['1','2','3']
    uang = [2500000, 4500000, 6500000]
    tunjanganIstri = [0.01, 0.03, 0.05]
    tunjanganAnak = 0.02
    biayaJabatan = 0.005
    biayaPensiun = 15500
    biayaOrganisasi  = 3500
    #Tampilkan inputan
    nama   = input('Masukkan Nama                 = ')
    gol    = input('Golongan Anda                  = ')
    gender = input('Jenis Kelamin(L/P)             = ')
    sts    = input('Status Kawin(S/B)      = ')
    print()
     #Hitung gaji
    i = 0
    while i<len(uang):
        if kode[i] == gol:
            gaji = uang[i]
            tunj = tunjanganIstri[i] 
        i+=1
         #TunjanganIstri    
    if gender == 'l' and sts =='s':
       istri = tunj * gaji
    else:
       istri = 0
        
        #Tunjangan anak
    if sts == 's':
        anak = tunjanganAnak * gaji
    else:
        anak = 0
            #Gaji bruto
    bruto = gaji + istri + anak
    
    #Biaya jabatan
    jbtn = biayaJabatan * bruto
    
    #Gaji netto
    netto = bruto - biayaJabatan - biayaPensiun - biayaOrganisasi
    #Tampilkan Hasil
    print('SLIP GAJI'.center(50))
    #Input tanggal
    from datetime import date
    x = date.today()
    print('              Tanggal :', x.strftime('%d %B %Y'))
    print('=============================================')
    print('Gaji Pokok            :', rp (str(gaji)))
    print('Tunjangan Istri       :', rp (str(istri)))
    print('Tunjangan Anak        :', rp (str(anak)))
    print('--> Gaji Bruto        :', rp (str(bruto)))
    print('---------------------------------------------')
    print('Biaya Jabatan         :', rp (str(jbtn)))
    print('Iuran Pensiun         :', rp (str(biayaPensiun)))
    print('Iuran Organisasi      :', rp (str(biayaOrganisasi)))
    print('--> Gaji Netto        :', rp (str(netto)))
    
    ulang = input('Ulangi Program? Y/T:')
    print()
    if ulang == 't':
        break