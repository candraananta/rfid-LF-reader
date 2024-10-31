import serial #unutk komunikasi dengan rfid via serial
import json #untuk membaca file json
import os
import time

#MEMBACA FILE JSON
def read_config(config_file):
    try:
        with open(config_file,'r') as rf:
            config = json.load(rf)
            print("file konfigurasi berhasil dibaca")
        return config
    except Exception as f:
        print(f"error : {f}")
        return None
    
       
config = read_config('settingan.json')

# Inisialisasi koneksi serial

ser = serial.Serial(
    port=config['serial_port'],       # Ganti dengan port tempat RFID reader terhubung
    baudrate=config['baudrate'],     # Sesuaikan baudrate dengan spesifikasi reader
    timeout=config['timeout']
)

def read_epc():
    try:
        # Kirim perintah untuk membaca kartu (sesuai manual reader)
        ser.write(b'\xA0\x03\x01\x02\xD4')  # Contoh perintah, ganti sesuai dengan reader
        response = ser.read(16)  # Baca respons dari reader
        
        # Proses respons (misalnya, ambil EPC dari respons)
        epc = response.hex()  # Mengonversi respons ke format hexadecimal
        return epc
     
    except Exception as e:
        print(f"Error: {e}")
    # finally:
    #     ser.close()

  
# Main program
if __name__ == "__main__":
    os.system('cls')  # Bersihkan layar (Windows)

    print("\n==================================================")
    print("------ EPC Readers Tools - khusus rfid DRIVER ------")
    print("====================================================")
    print("----------------------------------------------------\n")

    
    print("Aplikasi standby, tekan Ctrl+C untuk berhenti")
    print("\n")
    # last_epc = None  # Variabel untuk menyimpan EPC yang terakhir dibaca
    
    
    try:
        # Loop yang akan terus membaca kartu RFID
        while True:
            # last_epc = None  # Variabel untuk menyimpan EPC yang terakhir dibaca
            epc_value = read_epc()
            
            if epc_value:
                print(f"EPC Terbaca: {epc_value}")
                pilihan = input("tekan 'Enter' untuk melanjutkan..")

                # Bandingkan EPC baru dengan EPC sebelumnya
                # if epc_value != last_epc:
                    # print(f"EPC Terbaca: {epc_value}")
                    # last_epc = epc_value  # Simpan EPC yang baru terbaca
            else:
                # print("Tidak ada kartu RFID terdeteksi.")
                pilihan = input("tekan 'Enter' untuk melanjutkan..")
        
            # Jeda sebentar sebelum pembacaan berikutnya untuk mengurangi beban pembacaan
            time.sleep(0.5)
            
    
    except KeyboardInterrupt:
        print("\n")
        print("Aplikasi dihentikan dengan Ctrl+C")
    
    finally:
        # Tutup koneksi serial saat aplikasi selesai
        ser.close()
