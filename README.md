# galaxy-tool-nucleotide-translation
Translate nucleotide sequences and count stop codons
## Getting Started
### Prerequisites
Installing the EMBOSS package
```
mkdir /home/galaxy/Tools/emboss
cd /home/galaxy/Tools/emboss
sudo wget ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz
sudo tar -zxvf EMBOSS-6.6.0.tar.gz
cd EMBOSS-6.6.0/
sudo ./configure
sudo make
sudo ln -s /home/galaxy/Tools/emboss/EMBOSS-6.6.0/emboss/transeq /usr/local/bin/transeq
```
### Installing
Installing the tool for use in Galaxy
```
cd /home/galaxy/Tools
sudo git clone https://github.com/naturalis/galaxy-tool-nucleotide-translation
sudo chmod 777 galaxy-tool-nucleotide-translation/translatenucleotide.py
sudo ln -s /home/galaxy/Tools/galaxy-tool-nucleotide-translation/translatenucleotide.py /usr/local/bin/translatenucleotide.py
sudo ln -s /home/galaxy/Tools/galaxy-tool-nucleotide-translation/translatenucleotide.sh /home/galaxy/galaxy/tools/identify/translatenucleotide.sh
sudo ln -s /home/galaxy/Tools/galaxy-tool-nucleotide-translation/translatenucleotide.xml /home/galaxy/galaxy/tools/identify/translatenucleotide.xml
```
