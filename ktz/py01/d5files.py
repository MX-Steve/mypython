with open('/tmp/m1','r') as m1, open('/tmp/m2','r') as m2, open('/tmp/m3','w') as m3:
    aset=set(m1)
    bset=set(m2)
    m3.writelines(bset-aset)