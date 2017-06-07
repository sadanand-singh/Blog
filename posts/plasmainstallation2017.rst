.. title: My Complete Arch Linux Setup with Plasma 5
.. slug: CompleteSetupArchPlasma
.. date: 2017-06-05 15:00:00 UTC-07:00
.. tags: Linux, Arch Linux, Plasma 5, KDE
.. category: Computers
.. link:
.. description:
.. disqus_identifier: CompleteSetupArchPlasma.sadanand
.. type: text
.. author: Sadanand Singh

|Arch|_ is a general purpose GNU/Linux distribution that provides most up-to-
date softwares by following the rolling-release model. Arch Linux allows you to use updated cutting-edge
softwares and packages as soon as the developers released them.
`KDE Plasma 5`_ is the current generation of the desktop environment created by
KDE primarily for Linux systems.

In this post, we will do a complete installation of Arch Linux with Plasma 5
as the desktop environment. Our setup will also involve encryption of the
root partition that will be formatted in btrfs_. This post is an updated
and a more complete version of my previous posts on
:doc:`Arch Linux <archInstall>` and
:doc:`Plasma 5 Installation <plasmaInstall>`.

.. more

.. contents:: Table of Contents

.. image:: http://i.imgur.com/Jrt0ZyL.jpg?1
   :alt: My Current Desktop
   :width: 680pt
   :align: center


.. |Arch| replace:: Arch Linux
.. _Arch: https://www.archlinux.org
.. _KDE Plasma 5: https://en.wikipedia.org/wiki/KDE_Plasma_5
.. _btrfs: https://en.wikipedia.org/wiki/Btrfs


Base Installation
=====================

{{% alert info %}}

NOTE: I do not wish to repeat <a href="https://wiki.archlinux.org/index.php/installation_guide">Arch Installation Guide</a> here.

Do not forget about <a href="https://wiki.archlinux.org/">Arch Wiki</a>,
the best documentation in the world! Most of the content in this
post has been compiled from the Arch wiki.

{{% /alert %}}

Before beginning this guide, I would assume that you have a
bootable USB of the latest Arch Linux Installer. If not, please follow
the `Arch wiki guide`_ to create one for you.

.. _Arch wiki guide: https://wiki.archlinux.org/index.php/USB_flash_installation_media

Once you login in the installer disk, You will be logged in on the first virtual console as the root user, and presented with a zsh shell prompt. I will assume you have an Ethernet connection and hence will be
connected to Internet by default. If you have to rely on wifi, please
refer to the `Wireless Network Configuration`_ wiki page for the
detailed setup. **You must have internet connection at this stage before proceeding any further.**

.. _Wireless Network Configuration: https://wiki.archlinux.org/index.php/Wireless_network_configuration

You should boot into UEFI mode if you have a UEFI motherboard and UEFI mode enabled.

To verify you have booted in UEFU mode, run:

.. code:: bash

    efivar -l


This should give you a list of set UEFI variables. Please look at the
`Arch Installation Guide`_ in case you do not get any list of UEFI variables.

.. _Arch Installation Guide: https://wiki.archlinux.org/index.php/installation_guide

The very first thing that annoys me in the virtual console is how tiny
all the fonts are. We will fix that by running the following commands:

.. code:: bash

    pacman -Sy
    pacman -S terminus-font
    setfont ter-132n

We are all set to get started with the actual installation process.

HDDs Partitioning
------------------

First find the hard drive that you will be using as the main/root disk.

.. code:: bash

    cat /proc/partitions

    # OUTPUT eg.
    # major minor  #blocks  name

    # 8        0  268435456 sda
    # 9        0  268435456 sdb
    # 19       0  268435456 sdc
    # 11       0     759808 sr0
    # 7        0     328616 loop0


Say, we will be using */dev/sda* as the main disk and */dev/sdb*
as */data* and */dev/sdc* as */media* .

Because we are creating an encrypted file system it’s a good idea to overwrite it with random data.

We’ll use **badblocks** for this. Another method is to use
*dd if=/dev/random of=/dev/xxx*, the *dd* method is probably the
best method, but is a lot slower. **The following step should take about 20 minutes on a 240 GB SSD.**

.. code:: bash

    badblocks -c 10240 -s -w -t random -v /dev/sda

Next, we will create GPT partitions on all disks.

.. code:: bash

    $ dd if=/dev/zero of=/dev/sda bs=1M count=5000
    $ gdisk /dev/sda
    Found invalid MBR and corrupt GPT. What do you want to do? (Using the
    GPT MAY permit recovery of GPT data.)
     1 - Use current GPT
     2 - Create blank GPT

Then press 2 to create a blank GPT and start fresh

.. code:: bash

    ZAP:
    $ press x - to go to extended menu
    $ press z - to zap
    $ press Y - to confirm
    $ press Y - to delete MBR

It might now kick us out of gdisk, so get back into it:

.. code:: bash

    $ gdisk /dev/sda

    $ Command (? for help): m
    $ Command (? for help): n

    $ Partition number (1-128, default 1):
    $ First sector (34-500118158, default = 2048) or {+-}size{KMGTP}:
    $ Last sector (2048-500118, default = 500118) or {+-}size{KMGTP}: 512M
    $ Current type is 'Linux filesystem'
    $ Hex code or GUID (L to show codes, Enter = 8300): ef00
    $ Changed type of partition to 'EFI System'

    $ Partition number (2-128, default 2):
    $ First sector (34-500118, default = 16779264) or {+-}size{KMGTP}:
    $ Last sector (16779264-500118, default = 500118) or {+-}size{KMGTP}:
    $ Current type is 'Linux filesystem'
    $ Hex code or GUID (L to show codes, Enter = 8300):
    $ Changed type of partition to 'Linux filesystem'

    $ Command (? for help): p
    $ Press w to write to disk
    $ Press Y to confirm

Repeat the above procedure for */dev/sdb* and */dev/sdc*, but create just one partition
with all values as default. At the end we will have three partitions:
*/dev/sda1, /dev/sda2, /dev/sdb1* and */dev/sdc1*


Setup Disk Encryption
-----------------------

Our /boot partition will be on */dev/sda1*, while the main
installation will be on */dev/sda2*. In this setup, we will be
enabling full encryption on */dev/sda2* only.

In order to enable disk encryption, we will first create a root luks volume, open it and then format it.

.. code:: bash

    # first, we need to prepare the encrypted (outer) volume
    cryptsetup --cipher aes-xts-plain64 --hash sha512 --use-random --verify-passphrase luksFormat /dev/sda2

    # I really hope I don't have to lecture you on NOT LOSING this
    # password, lest all of your data will be forever inaccessible,
    # right?

    # then, we actually open it as a block device, and format the
    # inner volume later
    cryptsetup luksOpen /dev/sda2 root


{{% alert success %}} Automatic Key Login from an USB/SD Card {{% /alert %}}

If you want to automatically login the encrypted disk password from an externally attached USB or SD card, you will first need to create a key file.

.. code:: bash

    dd bs=512 count=4 if=/dev/urandom of=KEYFILE

Then, add this key to the luks container, so that it can be later used to open the encrypted drive.

.. code:: bash

    cryptsetup luksAddKey /dev/sda2 KEYFILE


{{% hl-text warning %}} Note that the KEYFILE here should be kept on a separate USB drive or SD card. {{%  /hl-text %}}
The recommended way of using such a disk would be as follows:

.. code:: bash

    # assuming our USB of interest is /dev/sdd  and can be format
    #
    # Format the drive
    dd if=/dev/zero of=/dev/sdd bs=1M
    # Create partitions using gdisk
    #
    gdisk /dev/sdd
    #
    # Follow along to create one partition (/dev/sdd1) of type 0700
    #
    # format /dev/sdd1
    mkfs.fat /dev/sdd1

    # mount the newly format disk on /mnt and then copy the KEYFILE
    mount /dev/sdd1 /mnt
    mv KEYFILE /mnt/KEYFILE
    umount /mnt

We will be later using this KEYFILE in boot loader setup.


Format HDDs
--------------

At this point, we have following drives ready for format:
*/dev/sda1*, */dev/mapper/root*, */dev/sdb1* and */dev/sdc1*.

These can be format as follows:

.. code:: bash

    $ mkfs.vfat -F32 /dev/sda1
    $ mkfs.btrfs -L arch /dev/mapper/root
    $ mkfs.btrfs -L data /dev/sdb1
    $ mkfs.btrfs -L media /dev/sdc1


Now, we will create btrfs subvolumes and mount them properly for
installation and final setup.

.. code:: bash

    $ mount /dev/mapper/root /mnt
    $ btrfs subvolume create /mnt/ROOT
    $ btrfs subvolume create /mnt/home
    $ umount /mnt

    $ mount /dev/sdb1 /mnt
    $ btrfs subvolume create /mnt/data
    $ umount /mnt

    $ mount /dev/sdc1 /mnt
    $ btrfs subvolume create /mnt/media
    $ umount /mnt

Now, once the sub-volumes have been created, we will mount them in
appropriate locations with optimal flags.

.. code:: bash

    $SSD_MOUNTS="rw,noatime,nodev,compress=lzo,ssd,discard,
        space_cache,autodefrag,inode_cache"
    $ HDD_MOUNTS="rw,nosuid,nodev,relatime,space_cache"
    $ EFI_MOUNTS="rw,noatime,discard,nodev,nosuid,noexec"
    $ mount -o $SSD_MOUNTS,subvol=ROOT /dev/mapper/root /mnt
    $ mkdir -p /mnt/home
    $ mkdir -p /mnt/data
    $ mkdir -p /mnt/media
    $ mount -o $SSD_MOUNTS,nosuid,subvol=home /dev/sda2 /mnt/home
    $ mount -o $HDD_MOUNTS,subvol=data /dev/sdb1 /mnt/data
    $ mount -o $HDD_MOUNTS,subvol=media /dev/sdc1 /mnt/media

    $ mkdir -p /mnt/boot
    $ mount -o $EFI_MOUNTS /dev/sda1 /mnt/boot

{{% hl-text cyan %}} Save the current /etc/resolv.conf file for future use! {{%  /hl-text %}}

.. code:: bash

    cp /etc/resolv.conf /mnt/etc/resolv.conf


Base System Installation
---------------------------

Now, we will do the actually installation of base packages.

.. code:: bash

    $ pacstrap /mnt base base-devel btrfs-progs
    $ genfstab -U -p /mnt >> /mnt/etc/fstab


Initial System Setup
----------------------

Edit the /mnt/ect/fstab file to add following /tmp mounts.

.. code:: bash

    tmpfs /tmp tmpfs rw,nodev,nosuid 0 0
    tmpfs /dev/shm tmpfs rw,nodev,nosuid,noexec 0 0

Finally  bind root for installation.

.. code:: bash

    $ arch-chroot /mnt bash
    $ pacman -Syy
    $ pacman -Syu
    $ pacman -S sudo vim
    $ vim /etc/locale.gen

    ...
    # en_SG ISO-8859-1
    en_US.UTF-8 UTF-8
    # en_US ISO-8859-1
    ...

    $ locale-gen
    $ echo LANG=en_US.UTF-8 > /etc/locale.conf
    $ export LANG=en_US.UTF-8
    $ ls -l /usr/share/zoneinfo
    $ ln -sf /usr/share/zoneinfo/Zone/SubZone /etc/localtime
    $ hwclock --systohc --utc
    $ sed -i "s/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/" /etc/sudoers
    $ HOSTNAME=euler
    $ echo $HOSTNAME > /etc/hostname
    $ passwd


We will also add *hostname* to our /etc/hosts file:

.. code:: bash

    $ vim /etc/hosts
    ...
    127.0.0.1       localhost.localdomain   localhost
    ::1             localhost.localdomain   localhost
    127.0.0.1       $HOSTNAME.localdomain   $HOSTNAME
    ...

We also need to fix the mkinitcpio.conf to contain what we actually need.

.. code:: bash

    vi /etc/mkinitcpio.conf
    # on the MODULES section, add "vfat aes_x86_64 crc32c-intel"
    # (and whatever else you know your hardware needs. Mine needs i915 too)
    # on the BINARIES section, add "/usr/bin/btrfsck", since it's useful
    # to have in case your filesystem has troubles
    # on the HOOKS section:
    #  - add "encrypt" before "filesystems"
    #  - remove "fsck" and
    #  - add "btrfs" at the end
    #
    # re-generate your initrd images
    mkinitcpio -p linux


Boot Manager Setup
--------------------

*systemd-boot*, previously called *gummiboot*, is a simple UEFI boot manager
which executes configured EFI images. The default entry is selected by
a configured pattern (glob) or an on-screen menu.
It is included with the *systemd*, which is installed on an Arch systems by default.

Assuming */boot* is your boot drive, first run the following command to get started:

.. code:: bash

    $ bootctl --path=/boot install

It will copy the systemd-boot binary to your EFI System Partition
( `/boot/EFI/systemd/systemd-bootx64.efi` and `/boot/EFI/Boot/BOOTX64.EFI`
- both of which are identical - on x64 systems ) and add systemd-boot
itself as the default EFI application (default boot entry) loaded by
the EFI Boot Manager.

Finally to configure out boot loader, we will need the UUID of
some of our hard drives. These can ne easily done using the blkid command.

.. code:: bash

    blkid /dev/sda1 > /boot/loader/entries/arch.conf
    blkid /dev/sda2 >> /boot/loader/entries/arch.conf
    blkid /dev/mapper/root >> /boot/loader/entries/arch.conf
    blkid /dev/sdd1 >> /boot/loader/entries/arch.conf

    # for this example, I'm going to mark them like this:
    # /dev/sda1 LABEL="EFI"                 UUID=11111111-1111-1111-1111-111111111111
    # /dev/sda2 LABEL="arch"      UUID=33333333-3333-3333-3333-333333333333
    # /dev/mapper/root LABEL="Arch Linux"   UUID=44444444-4444-4444-4444-444444444444
    # /dev/sdd1 LABEL="USB"     UUID=0000-0000  # this is the drive where KEYFILE exists


Now, make sure that the following two files look as follows,
where UUIDs is the value obtained from above commands.

{{% hl-text warning %}} Do not forget to modify UUIDs and KEYFIL entries! {{%  /hl-text %}}

.. code:: bash

    $ vim /boot/loader/loader.conf
    ...
    timeout 3
    default arch
    ...
    $ vim /boot/loader/entries/arch.conf
    ...

    title Arch Linux
    linux /vmlinuz-linux
    initrd /initramfs-linux.img
    options ro cryptdevice=UUID=33333333-3333-3333-3333-333333333333:luks-33333333-3333-3333-3333-333333333333 root=UUID=44444444-4444-4444-4444-444444444444 rootfstype=btrfs rootflags=subvol=ROOT cryptkey=UUID=0000-0000:vfat:KEYFILE
    ...


Network Setup
----------------

At first we will need to figure out the ethernet controller on which cable is
connected.

.. code:: bash

    networkctl
    #
    # IDX LINK             TYPE               OPERATIONAL SETUP
    #   1 lo               loopback           carrier     unmanaged
    #   2 enp3s0           ether              no-carrier  unmanaged
    #   3 wlp6s0           wlan               no-carrier  unmanaged
    #   4 enp0s25          ether              routable    configured
    #

In our case, the name of the device is *enp0s25*.

Using this name of the device, we need to configure, and enable the
*systemd-networkd.service* service.

Note that we will using the resolv.conf that we saved from this session.

Network configurations are stored as \*.network in */etc/systemd/network*.
We need to create ours as follows.:

.. code:: bash

    $ vim /etc/systemd/network/50-wired.network
    $
    ...
    [Match]
    Name=enp0s25

    [Network]
    DHCP=ipv4

    ...

    $

Now enable these services:

.. code:: bash

    systemctl enable systemd-networkd.service


Your network should be ready for the first use!

Sync time automatically using the systemd service:

.. code:: bash

   $ vim /etc/systemd/timesyncd.conf
   $
   ...
   [Time]
   NTP=0.arch.pool.ntp.org 1.arch.pool.ntp.org 2.arch.pool.ntp.org 3.arch.pool.ntp.org
   FallbackNTP=0.pool.ntp.org 1.pool.ntp.org 0.fr.pool.ntp.org
   ...
   $
   $ timedatectl set-ntp true
   $ timedatectl status
   $
   ...
         Local time: Tue 2016-09-20 16:40:44 PDT
     Universal time: Tue 2016-09-20 23:40:44 UTC
           RTC time: Tue 2016-09-20 23:40:44
          Time zone: US/Pacific (PDT, -0700)
    Network time on: yes
   NTP synchronized: yes
    RTC in local TZ: no
    ...
   $

Avahi_ is a tool that allows programs to publish and discover services and
hosts running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to print to,
files to look at and people to talk to.

.. _Avahi: https://wiki.archlinux.org/index.php/avahi

We can easily set it up it as follows:

.. code:: bash

    pacman -S avahi nss-mdns
    systemctl enable avahi-daemon.service

We will also install terminus-font on our system to work with proper fonts on first boot.

.. code:: bash

    pacman -S terminus-font


First Boot Installations
==========================

Now we are ready for the first boot!
Run the following command:

.. code:: bash

    $ exit
    $ umount -R /mnt
    $ reboot

After your new system boots, Network should be setup at the start. Check the status of network using:

.. code:: bash

   # Set readable font first!
   setfont ter-132n
   ping google.com -c 2

   #
   # PING google.com (10.38.24.84) 56(84) bytes of data.
   # 64 bytes from google.com (10.38.24.84): icmp_seq=1 ttl=64 time=0.022 ms
   # 64 bytes from google.com (10.38.24.84): icmp_seq=2 ttl=64 time=0.023 ms
   #
   # --- google.com ping statistics ---
   # 2 packets transmitted, 2 received, 0% packet loss, time 999ms
   # rtt min/avg/max/mdev = 0.022/0.022/0.023/0.004 ms
   #

If you do not get this output, please follow the troubleshooting links
at arch wiki on `setting up network`_.

.. _setting up network: https://wiki.archlinux.org/index.php/systemd-networkd


Adding New User
-----------------

Choose $USERNAME per your liking. I chose ssingh, so in future commands
whenever you see *ssingh* please replace it with your $USERNAME.

.. code:: bash

    $ useradd -m -G wheel -s /bin/bash $USERNAME
    $ chfn --full-name "$FULL_NAME" $USERNAME
    $ passwd $USERNAME


GUI Installation with nvidia
------------------------------

I will be assuming you have an NVIDIA card for graphics installation.

To setup a graphical desktop, first we need to install some basic X
related packages, and some *essential* packages (including fonts):

.. code:: bash

   $ pacman -S xorg-server nvidia nvidia-libgl nvidia-settings mesa

To avoid the possibility of forgetting to update your initramfs after
an nvidia upgrade, you have to use a pacman hook like this:

.. code:: bash

   $ vim /etc/pacman.d/hooks/nvidia.hook
   $
   ...
   [Trigger]
   Operation=Install
   Operation=Upgrade
   Operation=Remove
   Type=Package
   Target=nvidia

   [Action]
   Depends=mkinitcpio
   When=PostTransaction
   Exec=/usr/bin/mkinitcpio -p linux
   ...
   $

Nvidia has a daemon that is to be run at boot. To start the persistence
daemon at boot, enable the `nvidia-persistenced.service`.

.. code:: bash

   $ systemctl enable nvidia-persistenced.service
   $ systemctl start nvidia-persistenced.service


{{% alert info %}} How to Avoid Screen Tearing {{% /alert %}}

Tearing can be avoided by forcing a full composition pipeline, regardless of the compositor you are using.

In order to make this change permanent, We will need to edit nvidia
configuration file. Since, by default there aren't any, we will first need to
create one.

.. code:: bash

    nvidia-xconfig
    mv /etc/X11/xorg.cong /etc/X11/xorg.conf.d/20-nvidia.conf
    #
    # Edit this file as follows:
    vim /etc/X11/xorg.conf.d/20-nvidia.conf
    # -------------------------------------------
    # Section "Screen"
    #     Identifier     "Screen0"
    #     Option         "metamodes" "nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"
    #     Option         "AllowIndirectGLXProtocol" "off"
    #     Option         "TripleBuffer" "on"
    # EndSection
    [...]
    # Section "Device"
    #     [...]
    #     Option         "TripleBuffer" "True"
    #     [...]
    # EndSection
    # [...]
    # ------------------------------------------------

Specific for Plasma 5, we will also create the following file to avoid any tearing in Plasma.

.. code:: bash

    $ vim /etc/profile.d/kwin.sh
    $
    ...
    export KWIN_TRIPLE_BUFFER=1
    ...

{{% alert info %}} How to Enable Better Resolution During Boot {{% /alert %}}

The kernel compiled in *efifb* module supports high-resolution nvidia
console on EFI systems. This can enabled by enabling the DRM kernel
mode setting. First, we will need to add *nvidia*, *nvidia_modeset*,
*nvidia_uvm* and *nvidia_drm* to MODULES section of the
*mkinitcpio.conf* file. We will also need to pass
the *nvidia-drm.modeset=1* kernel parameter during the boot.

.. code:: bash

    $ vim /etc/mkinitcpio.conf
    $
    ...
    MODULES="vfat aes_x86_64 crc32c-intel nvidia nvidia_modeset nvidia_uvm nvidia_drm"
    ...
    $
    $ vim /boot/loader/entries/arch.conf
    $
    ...
    options ro cryptdevice=UUID=:luks- root=UUID= rootfstype=btrfs rootflags=subvol=ROOT cryptkey=UUID=:vfat:deepmind20170602 nvidia-drm.modeset=1
    ...
    $
    $ mkinitcpio -p linux


Plasma 5 Installation and Setup
---------------------------------

We can now proceed with the installation of Plasma 5. In the process,
we will also install some useful fonts.

.. code:: bash

    pacman -S ttf-hack ttf-anonymous-pro
    pacman -S ttf-dejavu ttf-freefont ttf-liberation
    pacman -S plasma-meta dolphin kdialog kfind
    pacman -S konsole gwenview okular spectacle kio-extras
    pacman -S kompare dolphin-plugins kwallet kwalletmanager
    pacman -S ark yakuake flite

We will also need to select proper themes for the Plasma 5 display manager sddm and then enable its systemd service.

.. code:: bash

    $ vim /etc/sddm.conf

    ....
    [Theme]
    # Current theme name
    Current=breeze

    # Cursor theme used in the greeter
    CursorTheme=breeze_cursors
    ...

    $ systemctl enable sddm
    $ reboot

Once, we boot into the new system, we should have a basic Plasma 5 desktop
waiting for you. In the following section, we will be do installation
and modifications to the system that I prefer.


Post Installation Setup
==========================

Plasma 5 provides a handy network manager applet. However, in order to
use it properly we will need the NetworkManager service to be enabled.
This applet allows user specific enabling of *wifi*, *ethernet* or
even *VPN* connections.

.. code:: bash

    $ sudo pacman -S networkmanager
    $ systemctl enable NetworkManager.service
    $ systemctl start NetworkManager.service


Selecting pacman Mirrors
-------------------------

The *pacman* package provides a Bash script, */usr/bin/rankmirrors*,
which can be used to rank the mirrors according to their connection
and opening speeds to take advantage of using the fastest local mirror.

We will do this only on the US based mirrors. First make a copy of the
mirrors list file and then delete all non-US mirrors. We will
then *rankmirrors* script on the modified list to get the top 6
mirrors for our regular use.

.. code:: bash

    $ cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup
    $ cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.us
    $ vim /etc/pacman.d/mirrorlist.us
    ....
    # Delete all non-US servers
    ....
    $ rankmirrors -n 6 /etc/pacman.d/mirrorlist.us > /etc/pacman.d/mirrorlist


Setup AUR
----------


AUR_ is a community-driven repository for Arch users. This allows you to
install many popular packages that are otherwise not available through
core repositories.

.. |AUR| replace:: The Arch User Repository (AUR)
.. _AUR: https://aur.archlinux.org/

In order to make all types of installations uniform, I use pacaur_ as
the preferred tool for installing all packages. One the biggest
advantages of pacaur is that is uses exactly the same options that
regular pacman uses.

.. _pacaur: https://github.com/rmarquis/pacaur

In order to install pacuar, first install dependencies.

.. code:: bash

    sudo pacman -S expac yajl curl gnupg --noconfirm

Create a temp directory for building packages:

.. code:: bash

    mkdir ~/temp
    cp ~ temp

Install *cower* first and then *pacaur*:

.. code:: bash

    gpg --recv-keys --keyserver hkp://pgp.mit.edu 1EB2638FF56C0C53
    curl -o PKGBUILD https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=cower
    makepkg -i PKGBUILD --noconfirm

    curl -o PKGBUILD https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=pacaur
    makepkg -i PKGBUILD --noconfirm

    # Finally cleanup and remove the temp directory
    cd ~
    rm -r ~/temp


Audio Setup
------------

This is pretty simple. Install following packages and you should be done:

.. code:: bash

    sudo pacaur -S alsa-utils pulseaudio pulseaudio-alsa mpv
    sudo pacaur -S libcanberra-pulse libcanberra-gstreamer
    sudo pacaur -S vlc-qt5

Now start the pulseaudio service.

.. code:: bash

    systemctl --user enable pulseaudio.socket


Web Browsers
-------------

My preferred choice of browsers is *google chrome*. However, it is also good to have the KDE native *qupzilla*.

.. code:: bash

    sudo pacaur -S google-chrome qupzilla

*Profile-sync-daemon* (psd) is a tiny pseudo-daemon designed to manage browser profile(s) in *tmpfs* and to periodically sync back to the physical disc (HDD/SSD). This is accomplished by an innovative use of *rsync* to maintain synchronization between a *tmpfs* copy and media-bound backup of the browser profile(s). These features of *psd* leads to following benefits:

-   Transparent user experience
-   Reduced wear to physical drives, and
-   Speed

To setup. first install the *profile-sync-daemon* package.

.. code:: bash

    sudo pacaur -S profile-sync-daemon

Run *psd* the first time which will create a config file at
`$XDG_CONFIG_HOME/psd/psd.conf` which contains all settings.

.. code:: bash

    psd
    # First time running psd so please edit
    # /home/$USERNAME/.config/psd/psd.conf to your liking and run again.


In the config file chnage the BROWSERS variables to "google-chrome qupzilla". Also, enable the use of overlayfs to improve sync speed and to use a smaller memory footprint. Do this in the USE_OVERLAYFS="yes" variable.


{{% hl-text purple %}}
Note: USE_OVERLAYFS feature requires a Linux kernel version of 3.18.0 or greater to work.
{{% /hl-text %}}

In order to use the OVERLAYFS feature, you will also need to give sudo permissions to psd-helper as follows (replace $USERNAME accordingly):

.. code:: bash

    $ vim /etc/sudoers
    ...
    $USERNAME ALL=(ALL) NOPASSWD: /usr/bin/psd-overlay-helper
    ...

Verify the working of configuration using the preview mode of psd:

.. code:: bash

    psd p


git Setup
-----------

Install git and setup some global options as below:

.. code:: bash

    $ sudo pacaur -S git
    $
    $ vim ~/.gitconfig
    ...
    [user]
        name = Sadanand Singh
        email = EMAIL_ADDRESS
    [color]
        ui = auto
    [status]
        showuntrackedfiles = no
    [alias]
        gist = log --graph --oneline --all --decorate --date-order
        find = log --graph --oneline --all --decorate --date-order --regexp-ignore-case --extended-regexp --grep
        rfind = log --graph --oneline --all --decorate --date-order --regexp-ignore-case --extended-regexp --invert-grep --grep
        search = grep --line-number --ignore-case -E -I
    [pager]
        status = true
    [push]
        default = matching
    [merge]
        tool = meld
    [diff]
        tool = meld

    [help]
        autocorrect = 1
    ...

ssh Setup
-----------



zsh Setup
----------



gpg Setup
-----------





User Wallpapers
------------------



conky Setup
------------




Python Setup
-------------



Software Installations
------------------------



