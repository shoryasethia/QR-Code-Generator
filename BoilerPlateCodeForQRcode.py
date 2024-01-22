import qrcode
img=qrcode.make("https://github.com/shoryasethia")
img.save("GitHub.png")
img.show()