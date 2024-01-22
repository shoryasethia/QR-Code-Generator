## To Clone use
```
git clone https://github.com/shoryasethia/QR-Code-Generator
```
## Setup
Install QR code library
```
pip install qrcode
```
# Enter the url here, inside double quotes
```
img=qrcode.make("    ")
```
# Example
## I am generating QR Code for my GitHub Profile
```
import qrcode
img=qrcode.make("https://github.com/shoryasethia")
img.save("GitHub.png")
img.show()
```
## Output
![My GitHub Profile QR Code](https://github.com/shoryasethia/QR-Code-Generator/blob/main/GitHub.png)

# Save
## Save image using
```
img.save(" ")
```
Enter the file name within double quotes and don't forget to add `.png` in the end
