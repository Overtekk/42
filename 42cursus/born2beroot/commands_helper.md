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

`dep` ➡️ see information about disk usage\
`df -m | grep "/dev/" | grep -v "/boot" | awk '{memory_use += $3} END {print memory_use}'` ➡️ see final
`df -m | grep "/dev/" | grep -v "/boot" | awk '{use += $3} {total += $2} END {printf("(%d%%)\n"), use/total*100}'` ➡️ see total disk usage in percentage\

`vmstat` ➡️ show VM statistics\
`vmstat 1 4 | tail -1 | awk '{print $15}'` ➡️ get CPU usage\

`who` ➡️ see informations about users\
`who -b | awk '$1 == "system" {print $3 " " $4}'` ➡️ get date and time of last reboot\

`lsblk` ➡️ see informations about LVM\
`'if [ $(lsblk | grep "lvm" | wc -l) -gt 0 ]; then echo yes; else echo no; fi` ➡️ to know if LVM is active or not\

`ss` ➡️ check number of TCP connections\
`ss -ta | grep ESTAB | wc -l` ➡️ get number of TCP connections\

`users` ➡️ show informations about users\
`users | wc -w` ➡️ get numbers of users\

`hostname -I` ➡️ obtain the MAC\
`ip link` ➡️ show network interface\
`ip link | grep "link/ether" | awk '{print $2}'` ➡️ to get adress of MAC\

`journaclctl` ➡️ collect and manage system logs\
`journalctl _COMM=sudo | grep COMMAND | wc -l` ➡️ to get number of executed commands with sudo\
