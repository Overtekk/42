# Helper for the evaluation (in french 🇫🇷)

## Part 1
`shasum machinename.vdi`\

### **Comment fonctionne une VM / Utilité** => 
* **Utilité :** Simuler un ordinateur.
* **Intérêt :**
    * **Isolation:** Ce qui se passe dans la VM n'affecte pas la machine hôte.
    * **Tests:** Permet de tester des configurations, des logiciels ou des OS sans risque.
    * **Portabilité:** On peut déplacer ou cloner la VM facilement.
  
### **Choix de l'OS** =>
* **Stabilité :** Réputé, idéal pour les serveurs.
* **Communauté :** Énorme communauté et très large documentation.
* **APT :** Utilise le gestionnaire de paquets `.deb` (Advanced Packaging Tool), très puissant.

### **Différences CentOS et Debian** =>
**Debian**
* Stable.
* Facile pour les débutant.
* Immense communauté et documentation.
* Utilise `apt` et les fichiers `.deb`. Très facile à gérer.
**CentOS**
*  Plus utilisée dans les grandes entreprises, pour les admins système en entreprise.
* Utilise `dnf` (ou `yum`) et les fichiers `.rpm`.

### **Apt vs Aptitude** =>
* **APT :** Outil de base en ligne de commande. Simple, rapide, efficace. Parfait pour les scripts.
* **Aptitude :** Interface plus avancée (ligne de commande + interface texte). Gère plus intelligemment les conflits de dépendances et propose des solutions.

### **APPArmor (Application Armor)** =>
* Module de sécurité du noyau Linux.
* **Objectif :** Restreindre les capacités des programmes (fichiers, réseau, etc.) en se basant sur des "profils" de sécurité.
* C'est une alternative à SELinux (utilisé par CentOS, par exemple).

## Part 2
`ls /usr/bin/*session`\

Mot de passe = Un*Cl4vi1ER *(10 caractères / 1 lettre capitale, minuscule, digit / Pas de caractères répété 3 fois / Pas d'username / 7 caractères différents d'avant)*\

`sudo ufw status`\
`sudo service ufw status`\
`sudo service ssh status`\
`uname --kernel-version`

## Part 3
`getent group sudo user42`\
`sudo adduser name_user`\
`nano /etc/login.defs`\
`nano /etc/pam.d/common-password` (- = le min de caractères)\
`sudo addgroup evaluating`\
`sudo adduser name_user evaluating`\

### **Avantages/Désavantages de la politique de mot de passe** =>
### Avantages
* **Anti-Brute Force :** Un mot de passe long et complexe rend les attaques plus difficiles, voire impossibles.
* Empêche les utilisateurs d'utiliser des mots de passe évidents comme `12345` ou `password` ou `root`.
* **Protection de Root :** Le compte le plus important du système.

### Désavantages
* Moins pratique parce qu'on a plus tendance à oublier des mots de passe.
* Rien n'empêche l'utilisateur de l'écrire à un endroit évident (genre sur son bureau), ou qu'il se fasse hacker en cliquant sur le mail d'un prince indien. 
* Demande une configuration manuelle (éditer les fichiers PAM), ce qui peut être intimidant pour un débutant.

## Part 4
`hostname`\
`sudo nano /etc/hostname`\
`sudo nano /etc/hosts`\ 
`sudo reboot`\
`lsblk`\

### **LVM (Logical Volume Manager)** =>
* **Objectif :** Abstrait la gestion des disques. Plus flexible que les partitions classiques.
* **Structure :**
    1.  **PV (Physical Volumes)** : Les disques durs ou partitions physiques (`/dev/sda3`).
    2.  **VG (Volume Group)** : Un gros groupe de stockage créé en combinant les PV.
    3.  **LV (Logical Volumes)** : Les partitions logiques (ex: `/home`, `/var`) que le système utilise, créées depuis le VG.
* **Avantages :** Redimensionner les volumes quand on veut, créer des snapshots pour les backups.

## Part 5
`which sudo`\
`sudo adduser name_user sudo`\
`getent group sudo`\

### **Fonctionnement de Sudo** =>
1.  **Sudo (Super User Do)** permet à un utilisateur autorisé d'exécuter une commande en tant qu'un autre utilisateur (par défaut `root`, donc administrateur).
2.  
`nano /etc/sudoers.d/sudo_config`\
`cd /var/log/sudo`\
`cat sudo_config`

## Part 6
`dpkg -s ufw`\
`sudo service ufw status`\

### **UFW (Uncomplicated Firewall)** =>
* **Objectif :** Interface simplifiée pour `iptables` (le pare-feu complexe du noyau Linux).
* **Rôle :** Filtrer le trafic réseau. Il protège les ports en définissant quelles connexions sont autorisées (entrantes, sortantes) et lesquelles sont bloquées.
* 
`sudo ufw status numbered`\
`sudo ufw allow 8080`\
`sudo ufw delete num_rule`\
`sudo ufw delete (line)`

## Part 6
`which ssh`\
`sudo service ssh status`\

### **SSH (Secure Shell)** =>
* Protocole réseau chiffré.
* **Objectif :** Permet de se connecter à distance à un terminal (shell) de manière sécurisée.
* Toute la communication (mots de passe, commandes) est chiffrée.
* 
`ssh root@localhost -p 2222`\
`ssh newuser@localhost -p 2222`

## Part 7
`sudo crontab -u root -e`

### **Cron** =>
* **Objectif :** Service qui exécute des tâches planifiées à des moments précis.
 
`You can rush whatever you want to make sure the script runs with dynamic values correctly`\

@reboot /home/roandrie/monitoring.sh
