"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 15 Oktober 2022
    Waktu: 00:40:44 WIB
    Magnitudo: 4.9
    Kedalaman: 10 km
    Lokasi: LS=3.83 BT=103.68
    Pusat Gempa: Pusat gempa berada di darat 16 km tenggara Lahat
    Dirasakan: Dirasakan (Skala MMI): III-IV Lahat, III-IV Muara Enim
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '15 Oktober 2022'
    hasil['waktu'] = '00:40:44 WIB'
    hasil['magnitudo'] = 4.9
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 3.83, 'bt': 103.68}
    hasil['pusat'] = 'Pusat gempa berada di darat 16 km tenggara Lahat'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III-IV Lahat, III-IV Muara Enim'
    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']} BT={result['lokasi']['bt']}")
    print(f"Dirasakan: {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
