set terminal png
set output './tmp.png'
set xdata time
set timefmt '%H:%M:%S'
set xlabel 'Time'

set ylabel '1 min load'
set yrange [0:]

plot 'tmp' using 1:2 title '1 load' with line , 'tmp' using 1:3 title '5 load' with line , 'tmp' using 1:4 title '15 load' with line
