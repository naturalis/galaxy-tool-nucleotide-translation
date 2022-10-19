# galaxy-tool-nucleotide-translation
Translate nucleotide sequences and count stop codons  

## Installation
### Manual
Clone this repo in your Galaxy ***Tools*** directory:  
`git clone https://github.com/naturalis/galaxy-tool-nucleotide-translation`  

Make the python script executable:  
`chmod 755 galaxy-tool-nucleotide-translation/translatenucleotide.py`  

Append the file ***tool_conf.xml***:  
`<tool file="/home/galaxy/Tools/galaxy-tool-nucleotide-translation/translatenucleotide.xml" />`  

### Ansible
Depending on your setup the [ansible.builtin.git](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html) module could be used.  
[Install the tool](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html#examples) by including the following in your dedicated ***.yml** file:  

`  - repo: https://github.com/naturalis/galaxy-tool-nucleotide-translation`  
&ensp;&ensp;`file: translatenucleotide.xml`  
&ensp;&ensp;`version: master` 
