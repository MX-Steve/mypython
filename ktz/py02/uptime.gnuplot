set xdata time
set timefmt '%H:%M:%S'
set xlabel 'Time'

set ylabel '1 min load'
set yrange [0:]

plot 'tmp' using 1:2 with line
