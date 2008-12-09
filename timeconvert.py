import sys

a = sys.stdin.readline()
m, s = a.split('m')
print int(m)*60 + float(s[:-2])
