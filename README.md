#Setup
Install QR code library
```
pip install qrcode
```
#Enter the url here, inside double quotes
```
img=qrcode.make("    ")
```
#Example
##I am generating QR Code for my GitHub Profile
```
import qrcode
img=qrcode.make("https://github.com/shoryasethia")
img.save("GitHub.png")
img.show()
```
![My GitHub Profile QR Code](https://github.com/shoryasethia/QR-Code-Generator/blob/main/GitHub.png)
