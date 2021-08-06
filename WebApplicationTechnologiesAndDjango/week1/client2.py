from urllib.request import urlopen

fhand = urlopen('http://127.0.0.1:9000/get.txt')
for line in fhand:
   print(line.decode().strip())