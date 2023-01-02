from PIL import Image

# Baca file binary
with open("filename_bits.txt", "r") as f:
  binary = f.read()

# Buat gambar baru dengan ukuran sesuai dengan panjang data binary
width = 800#len(binary)
height = 600
image = Image.new("RGB", (width, height))
#image = Image.new("RGB", (len(binary), 1))
# Isi gambar dengan warna merah atau hijau sesuai dengan nilai binary
pixels = image.load()
for i in range(width):
  if binary[i] == "1":
    pixels[i, 0] = (255, 0, 0)  # Merah
  else:
    pixels[i, 0] = (0, 255, 0)  # Hijau

# Simpan gambar ke file
image.save("binary.png")