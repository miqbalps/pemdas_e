# buat dictionary data panen
data_panen = {
  'lokasi1': {
    'nama_lokasi': 'Kebun A',
    'hasil_panen': {
      'padi': 1200,
      'jagung': 800,
      'kedelai': 500
    }
  },
  'lokasi2': {
    'nama_lokasi': 'Kebun B',
    'hasil_panen': {
      'padi': 1500,
      'jagung': 900,
      'kedelai': 450
    }
  },
  'lokasi3': {
    'nama_lokasi': 'Kebun C',
    'hasil_panen': {
      'padi': 1100,
      'jagung':750,
      'kedelai': 600
    }
  },
  'lokasi4': {
    'nama_lokasi': 'Kebun D',
    'hasil_panen': {
      'padi': 1300,
      'jagung': 850,
      'kedelai': 550
    }
  },
  'lokasi5': {
    'nama_lokasi': 'Kebun E',
    'hasil_panen': {
      'padi': 1400,
      'jagung': 950,
      'kedelai': 480
    }
  }
}

# 1
print("No. 1")
for i in data_panen.values():
  print(f'Nama lokasi: {i['nama_lokasi']}')
  print(f'Hasil Panen: Padi = {i['hasil_panen']['padi']}, Jagung: {i['hasil_panen']['jagung']}, Kedelai: {i['hasil_panen']['kedelai']}\n')

print()

# 2
print("No. 2")
print(f'Hasil panen jagung dari lokasi 2 sebanyak {data_panen['lokasi2']['hasil_panen']['jagung']}')
print()

# 3
print("No. 3")
print(f'Nama lokasi 3 adalah {data_panen['lokasi3']['nama_lokasi']}')
print()

# 4 dan 5
print("No. 4 dan 5")
jumlah_padi = []
jumlah_kedelai = []

for i in data_panen.values():
  jumlah_padi.append(i['hasil_panen']['padi'])
  jumlah_kedelai.append(i['hasil_panen']['kedelai'])

print(jumlah_padi)
print(jumlah_kedelai)
print()

# 6
print("No. 6")
for i,j in data_panen.items():
  if j['hasil_panen']['padi'] > 1300 or j['hasil_panen']['jagung'] > 800:
    print(f'{i} perlu perhatian khusus')
  else:
    print(f'{i} dalam kondisi baik')
