# galaxy-tool-nucleotide-translation
Translate nucleotide sequences and count stop codons
## Getting Started
### Installing
Installing the tool for use in Galaxy
```
cd /home/galaxy/Tools
sudo git clone https://github.com/naturalis/galaxy-tool-nucleotide-translation
sudo chmod 777 galaxy-tool-nucleotide-translation/translatenucleotide.py
```
Add the following line to /home/galaxy/galaxy/config/tool_conf.xml
```
<tool file="/home/galaxy/Tools/galaxy-tool-nucleotide-translation/translatenucleotide.xml" />
```
Restart Galaxy to see the tool in the menu
