#!/bin/bash
ps=7
pe=$[ps+1]
sed  -n "${ps},${pe}p" $0 | base64 -d | gzip -d | bash
exit
echo '
H4sICG9POVwAA2Euc2gAU1bUT8rM009KLM7gSk3OyFfQTVVQiqkwTIo2NswF06a5Hqk5OfkK5flF
OSlgESNTiIyxZa4SFwDpNjIVQQAAAA==
'
