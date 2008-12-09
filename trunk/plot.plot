set term pdf
set key left top
f(x) = x**4/log(x)*a
fit f(x) "a.dat" via a
g(x) = x**3*log(x)*b
fit g(x) "b.dat" via b
set ylabel 'Time in seconds'
set xlabel 'k in bits'
set xrange [0:1450]
#h(x) = x**3*c
#fit h(x) "c.dat" via c
plot "a.dat" title 'mauer', f(x),\
     "b.dat" title 'miller-rabin', g(x), 2*g(x) #, \
 #    "c.dat", h(x)