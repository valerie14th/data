import string
import random
mahasiswa_template = {
    'nama':'nama',
    'tinggal':'Kota, Provinsi',
    'sks':0,
    'sklh':'SD,SMP,SMA/SMK,KULIAH'
}
data_mahasiswa = {}

while True:
    print(f"\n\n{'SELAMAT DATANG':^55}\n\n")
    print(f"{'DATA MAHASISWA':^55}")
    print(59*"_")

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    print(mahasiswa)
    
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['tinggal'] = input("Tempat Tinggal: ")
    mahasiswa['sks'] = input("SKS Lulus: ")
    mahasiswa['sklh'] = input("Sekolah: ")
    KEY = "".join((random.choice(string.ascii_lowercase) for i in range(7)))
    
    print("\n\n")
    data_mahasiswa.update({KEY:mahasiswa})
    
    
    print(f"{'key':<9} {'nama':<13} {'tinggal':<11} {'sks':<13} {'sklh':<8}")
    print(59*"—")
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        
        NAMA = data_mahasiswa[KEY]['nama']
        TINGGAL = data_mahasiswa[KEY]['tinggal']
        SKS = data_mahasiswa[KEY]['sks']
        SEKOLAH = data_mahasiswa[KEY]['sklh']
        print(f"{KEY:<9} {NAMA:<13} {TINGGAL:<10} {SKS:<13} {SEKOLAH:<8}")
    
    isDone = str(input("want to add again (y/n) ? "))
    if isDone == "n":
        print("\nPROGRAM SELESAI, TERIMA KASIH")
        break
    elif isDone == "y":
        continue
