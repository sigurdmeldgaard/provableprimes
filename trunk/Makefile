a.dat: mauertimings.dat
	python prepare.py mauertimings.dat > a.dat
b.dat: millerrabintimings.dat
	python prepare.py millerrabintimings.dat > b.dat
plot.pdf: a.dat b.dat
	gnuplot plot.plot > plot.pdf