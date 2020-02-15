#! /bin/bash
cd ~
mkdir OPT2
mkdir OPT2/Test
wget http://codecopsiiitu.c1.biz/script.txt
wget http://codecopsiiitu.c1.biz/test.txt
mv script.txt script.py
mv test.txt OPT2/test.py
python3 script.py
rm script.py
cd ~/OPT2
