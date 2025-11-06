## Useful commands

`uname -a` ➡️ see GPU architecture\

`grep "physical id" /proc/cpuinfo | wc -l` ➡️ see number of physical cores\
>[!NOTE]
> *grep : search in lines for a specific pattern*\
> */proc/cpuinfo/ : folder and file to look to*\
> *"physical id" : the pattern to searc for*\
> *wc -l : to count the lines*\

`grep processor /proc/cpuinfo | wc -l` ➡️ see number of virtual cores\

`grep processor /proc/cpuinfo | wc -l` ➡️ see informations about RAM\
`free --mega | awk '$1 == "Mem:" {print $3}'` ➡️ get number of mb of usef memory\
`free --mega | awk '$1 == "Mem:" {print $2}'` ➡️ get number of total nb memory\
`free --mega | awk '$1 == "Mem:" {printf("(%.2f%%)\n", $3/$2*100)}'` ➡️ get pourcent of used memory\
>[!NOTE]
> *--mega : show ouput in mb*\
> *awk pattern {action}*\
