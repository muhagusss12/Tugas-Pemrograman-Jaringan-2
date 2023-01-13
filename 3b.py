import locale
from datetime import datetime

# Mengubah sistem locale menjadi bahasa Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.utf8')

# Menciptakan objek datetime untuk menyimpan tanggal server saat ini
tanggal = datetime.now()

# Menampilkan tanggal server dengan nama bulan dalam bahasa Indonesia
print(tanggal.strftime("%d %B %Y %H:%M"))