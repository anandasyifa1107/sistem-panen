def input_data_panen():
    print("=== SISTEM PENCATATAN HASIL PANEN ===")
    nama_tanaman = input("Masukkan jenis tanaman: ")
    jumlah_kg = float(input("Masukkan jumlah hasil panen (kg): "))
    with open("data_panen.txt", "a") as file:
        file.write(f"{nama_tanaman},{jumlah_kg}\n")
    print("Data berhasil disimpan!")

def tampilkan_laporan():
    print("\n=== LAPORAN REKAPITULASI PANEN ===")
    try:
        with open("data_panen.txt", "r") as file:
            total_panen = 0
            print(f"{'Tanaman':<15} | {'Jumlah (kg)':<10}")
            print("-" * 30)
            for line in file:
                tanaman, jumlah = line.strip().split(",")
                print(f"{tanaman:<15} | {jumlah:<10}")
                total_panen += float(jumlah)
            print("-" * 30)
            print(f"Total Keseluruhan Panen: {total_panen} kg")
    except FileNotFoundError:
        print("Belum ada data panen yang tercatat.")

if __name__ == "__main__":
    input_data_panen()
    tampilkan_laporan()
