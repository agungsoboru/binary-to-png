from PIL import Image

# Baca file binary
with open("filename_bits.txt", "r") as f:
  binary = f.read()

# Tentukan ukuran gambar yang diinginkan
width = 100
height = len(binary) // width + 1

# Buat gambar baru dengan ukuran yang telah ditentukan
image = Image.new("RGB", (width, height))

# Isi gambar dengan warna merah atau hijau sesuai dengan nilai binary
pixels = image.load()
for i in range(len(binary)):
  x = i % width
  y = i // width
  if binary[i] == "1":
    pixels[x, y] = (255, 0, 0)  # Merah
  else:
    pixels[x, y] = (0, 255, 0)  # Hijau

# Simpan gambar ke file
image.save("binary.png")