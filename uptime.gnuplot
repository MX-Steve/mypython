set xdata time
set timefmt '%H:%M:%S'
set xlabel 'Time'
#set format x '%H:%M:%S'

set ylabel '15-minute load average'
set yrange [0:]

set terminal png
set output "/tmp/loadavg.png"

plot '/tmp/uptime' using 1:2 title '1-min' with lines , \
'/tmp/uptime' using 1:3 title '5-min' with lines , \
'/tmp/uptime' using 1:4 title '15-min' with lines

