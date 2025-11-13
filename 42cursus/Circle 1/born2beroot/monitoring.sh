#!/bin/bash

# ARCHITECTURE
arch=$(uname -a)

# CPU PHYSICAL
cpuf=$(grep -c "physical id" /proc/cpuinfo)
cpuv=$(grep -c "processor" /proc/cpuinfo)

# RAM
ram_total=$(free --mega | awk '$1 == "Mem:" {print $2}')
ram_use=$(free --mega | awk '$1 == "Mem:" {print $3}')
ram_percent=$(free --mega | awk '$1 == "Mem:" {printf("%.2f"), $3/$2*100}')

# DISK
disk_total=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_t += $2} END {printf ("%.1fGb\n"), disk_t/1024}')
disk_use=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_u += $3} END {print disk_u}')
disk_percent=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_u += $3} {disk_t+= $2} END {printf("%d"), disk_u/disk_t*100}')

# CPU LOAD
cpu_fin=$(vmstat 1 2 | tail -1 | awk '{printf "%.1f", 100 - $15}')

# LAST BOOT
lb=$(who -b | awk '$1 == "system" {print $3 " " $4}')

# LVM USE
if lsblk | grep -q "lvm"; then
  lvmu="yes"
else
  lvmu="no"
fi

# TCP CONNEXIONS
tcpc=$(ss -ta | grep -c ESTAB)

# USER LOG
ulog=$(users | wc -w)

# NETWORK
ip=$(hostname -I)
mac=$(ip link | grep "link/ether" | awk '{print $2}')

# SUDO
cmnd=$(journalctl _COMM=sudo | grep -c COMMAND)

wall "
Architecture: $arch
CPU physical: $cpuf
vCPU: $cpuv
Memory Usage: $ram_use/${ram_total}MB ($ram_percent%)
Disk Usage: $disk_use/${disk_total} ($disk_percent%)
CPU Load: $cpu_fin%
Last Boot: $lb
LVM Use: $lvmu
Connections TCP: $tcpc ESTABLISHED
User Log: $ulog
Network: IP $ip ($mac)
Sudo: $cmnd cmd
"
