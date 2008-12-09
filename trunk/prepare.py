import sys


f = open(sys.argv[1])
try:
    while True:
	bit_length = int(f.next())
	data = [float(f.next()) for i in range(10)]
	print bit_length, sum(data)/len(data) #, (max(data) - min(data)) / 2
except:
    pass
finally:
    pass
