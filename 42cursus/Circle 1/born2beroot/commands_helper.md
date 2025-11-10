## 💻 CPU Info

`uname -a` ➡️ Displays kernel information and CPU architecture (e.g., x86_64).

`lscpu` ➡️ Displays a complete summary of the CPU architecture (easier to read).

`grep "physical id" /proc/cpuinfo | sort -u | wc -l` ➡️ Counts the number of **physical processors** (sockets).

`grep "^processor" /proc/cpuinfo | wc -l` ➡️ Counts the number of **virtual cores** (vCPU / threads).
>[!NOTE]
> *grep: searches for a pattern in a file.*\
> */proc/cpuinfo: file containing detailed CPU information.*\
> *sort -u: sorts and keeps only unique entries.*\
> *wc -l: counts the number of lines.*

---

## 💾 RAM (Memory)

`free -h` ➡️ Displays RAM (and Swap) usage in a human-readable format (GB, MB).

`free --mega | awk '$1 == "Mem:" {print $3}'` ➡️ Displays used RAM (in Mebibytes).

`free --mega | awk '$1 == "Mem:" {print $2}'` ➡️ Displays total RAM (in Mebibytes).

`free --mega | awk '$1 == "Mem:" {printf("(%.2f%%)\n", $3/$2*100)}'` ➡️ Displays the percentage of used RAM.
>[!NOTE]
> *--mega: displays output in Mebibytes (MB).*\
> *-h: displays output in "Human-readable" format.*\
> *awk 'pattern {action}': a tool for processing text line by line.*

---

## 💿 Disk Usage

`df -h` ➡️ Displays usage for all filesystems (disks) in human-readable format.

`df -m | grep "/dev/" | grep -v "/boot" | awk '{memory_use += $3} END {print memory_use "MB"}'` ➡️ Calculates total disk usage (in MB) for main partitions.

`df -m | grep "/dev/" | grep -v "/boot" | awk '{use += $3} {total += $2} END {printf("(%.0f%%)\n", use/total*100)}'` ➡️ Calculates the total disk usage percentage.

---

## 📈 System Load & Uptime

`uptime` ➡️ Shows how long the server has been running (uptime) and the average load.

`vmstat 1 5` ➡️ Displays 5 reports on VM activity (memory, swap, cpu) at 1-second intervals.

`vmstat 1 2 | tail -1 | awk '{print $15}'` ➡️ Displays the percentage of **idle** CPU.

`vmstat 1 2 | tail -1 | awk '{print 100 - $15"%"}'` ➡️ Calculates the percentage of **used** CPU.

---

## 👥 Users & Boot Time

`who` ➡️ Shows who is currently logged into the system.

`last` ➡️ Shows the history of last user logins.

`who -b` ➡️ Shows the date and time of the last system boot.

`users | wc -w` ➡️ Counts the number of currently open user sessions.

---

## 🖴 LVM (Logical Volume Management)

`lsblk` ➡️ Lists storage devices (disks, partitions), very useful for seeing LVM structure.

`vgs` ➡️ Displays LVM Volume Groups.

`lvs` ➡️ Displays LVM Logical Volumes.

`if [ $(lsblk | grep "lvm" | wc -l) -gt 0 ]; then echo "LVM active"; else echo "LVM not active"; fi` ➡️ Checks if LVM is active or not.

---

## 🌐 Network & Connections

`ip a` ➡️ Displays all network interfaces with their IP and MAC addresses (replaces `ifconfig`).

`hostname -I` ➡️ Displays the machine's local IP address.

`ip link | grep "link/ether" | awk '{print $2}'` ➡️ Extracts the MAC address of the main interface.

`ss -tuna` ➡️ Displays all open or listening ports (TCP and UDP), with numerical addresses.

`ss -ta | grep ESTAB | wc -l` ➡️ Counts the number of currently **established** TCP connections.

---

## 🔥 Firewall (UFW)

`sudo ufw status` ➡️ Checks if the UFW (Uncomplicated Firewall) is active.

`sudo ufw status numbered` ➡️ Displays firewall rules with numbers (useful for deleting them).

---

## ⚙️ Services & Logs (Sudo)

`systemctl status sshd` ➡️ Checks the status of the SSH service (very important for this project).

`journalctl` ➡️ Main tool for reading system logs (journals).

`journalctl -u sshd | grep "Failed password"` ➡️ Displays failed SSH login attempts (very useful for spotting attacks!).

`journalctl _COMM=sudo | grep COMMAND | wc -l` ➡️ Counts the number of commands executed with `sudo` and logged.

---

## 🖥️ Hostname

`hostnamectl` ➡️ Displays the current hostname.

`sudo hostnamectl set-hostname yourlogin42` ➡️ Changes the hostname (replace 'yourlogin42').

---

## 👥 User and Group Management

`sudo adduser new_username` ➡️ Creates a new user (starts an interactive prompt).

`sudo addgroup new_group_name` ➡️ Creates a new group.

`sudo usermod -aG new_group_name new_username` ➡️ Adds the user to the group (the `-a` is crucial).

`id new_username` ➡️ Checks which groups the user belongs to.

---

## 🔑 Password Management

`passwd` ➡️ Changes your own password (for the current user).

`sudo passwd root` ➡️ Changes the 'root' account's password.
	if (fd != 0)
        close(fd);
`sudo passwd other_username` ➡️ Changes another user's password.

---

## 📝 Website

`sudo systemctl stop lighttpd.service` ➡️ Stop the lightppd service.

`sudo systemctl start apache2.service` ➡️ Start the apache2 service.

`sudo systemctl reload apache2.service` ➡️ Reload the apache2 service.
>[!NOTE]
> *Can be set for any service.*
