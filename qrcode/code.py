import qrcode
#data example
data = ['javascript', 'python', 'ruby', 'go', 'c++']

#file name
file_name = 'my_qrcode.png'

#generate qr code
img = qrcode.make(data=data)

#save generate qr code as img
img.save(file_name)