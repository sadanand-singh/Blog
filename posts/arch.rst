.. title: Arch Installation Guide
.. slug: archInstall
.. date: 2015-06-21 11:00:00 UTC-07:00
.. tags: Linux
.. category: Linux
.. link:
.. description:
.. type: text
.. author: Sadanand Singh

You must be thinking - yet another installation guide! There is no
dearth of "*Installation*" guides of Arch on web. So why another one?

With advancements like BTRFS file system, UEFI motherboards and modern
*in-development* desktop environment like Plasma 5; traditional `Arch
Wiki <https://wiki.archlinux.org/index.php/Installation_guide>`__ guide
and `Arch Beginners'
Guide <https://wiki.archlinux.org/index.php/Beginners%27_guide>`__ can
only be of a limited help. After I got my new :doc:`my new desktop <myNewCompSpecs>` , my goal
was to setup it with a *modern* setup. I decided to go with Arch Linux
with btrfs file system and Plasma 5 desktop. Coming from OSX, I just
love how far linux has come in terms of looks - *far better than OSX!*

.. TEASER_END

For all of you who love installation videos-

.. youtube:: MMkST5IjSjY
    :align: center

I will cover this in two parts. First in this post, I will install the
base system. Then, in a follow up post, I will discuss details of
setting up final working Plasma 5 desktop.

.. figure:: http://i.imgur.com/f10HO0r.jpg
   :alt: Plasma 5 Looks

   Plasma 5 Looks

Initial Setup
=============

Download the latest iso from Arch website and create the uefi usb
installation media. I used my mac to do this on terminal:

.. code:: bash

    $ diskutil list
    $ diskutil unmountDisk /dev/disk1
    $ dd if=image.iso of=/dev/rdisk1 bs=1m
    20480+0 records in
    20480+0 records out
    167772160 bytes transferred in 220.016918 secs (762542 bytes/sec)

    $ diskutil eject /dev/disk1

Use this media to boot into your machine. You should boot into UEFI mode
if you have a
`UEFI <https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface>`__
motherboard and UEFI mode enabled.

To verify you have booted in UEFU mode, run:

.. code:: bash

    $ efivar -l

This should give you a list of set UEFI variables. Please look at the
`Begineers'
Guide <https://wiki.archlinux.org/index.php/Beginners%27_guide>`__ in
case you do not get any list of UEFI variables.

Ethernet/Wifi
--------------

Ethernet should have started by default on your machine.
If you do not plan to use wifi during installation, you can skip
to the next section. If desired later, wifi will still be configurable after you are done
with all the installation.

To setup wifi simply run:

.. code:: bash

    $ wifi-menu

This is a pretty straight forward tool and will setup wifi for you for
this installation session.

This will also create a file at */etc/netctl/*. We will use this file
later to enable wifi at the first session after installation.

System Updates
----------------

For editing different configurations, I tend to use *vim*. So we will
update our package cache and install vim.

.. code:: bash

    $ pacman -Syy
    $ pacman -S vim

Hard Drives
-----------

In my desktop, I have three hard drives, one 256 GB solid state drive
(SDD), one 1 TB HDD and another 3TB HDD. I set up my drives as follows: -
SDD for root(/), /boot, and /home partitions, 1st HDD for /data and
the 2nd HDD for /media partitions.

For UEFI machines, we need to use a GPT partition table and /boot
partition has to be a fat32 partition with a minimum size of 512 MB. We
will format rest other partitions with BTRFS. See this
`link <http://www.makeuseof.com/tag/ext4-btrfs-making-switch-linux/>`__
for benefits of using btrfs partitions.

First list your hard drives with the following:

.. code:: bash

    $ lsblk
    $ cat /proc/partitions

Assuming, my setup above, now create gpt partitions and format them.

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

Now we will format these partitions.

.. code:: bash

    $ mkfs.vfat -F32 /dev/sda1
    $ mkfs.btrfs -L arch /dev/sda2
    $ mkfs.btrfs -L data /dev/sdb1
    $ mkfs.btrfs -L media /dev/sdc1

Now, we will create btrfs subvolumes and mount them properly for
installation and final setup.

.. code:: bash

    $ mount /dev/sda2 /mnt
    $ btrfs subvolume create /mnt/ROOT
    $ btrfs subvolume create /mnt/home
    $ umount /mnt

    $ mount /dev/sdb1 /mnt
    $ btrfs subvolume create /mnt/data
    $ umount /mnt

    $ mount /dev/sdc1 /mnt
    $ btrfs subvolume create /mnt/media
    $ umount /mnt

Now, once the subvolumes have been created, we will mount them in
appropriate locations with optimal flags.

.. code:: bash

    $SSD_MOUNTS="rw,noatime,nodev,compress=lzo,ssd,discard,
        space_cache,autodefrag,inode_cache"
    $ HDD_MOUNTS="rw,nosuid,nodev,relatime,space_cache"
    $ EFI_MOUNTS="rw,noatime,discard,nodev,nosuid,noexec"
    $ mount -o $SSD_MOUNTS,subvol=ROOT /dev/sda2 /mnt
    $ mkdir -p /mnt/home
    $ mkdir -p /mnt/data
    $ mkdir -p /mnt/media
    $ mount -o $SSD_MOUNTS,nosuid,subvol=home /dev/sda2 /mnt/home
    $ mount -o $HDD_MOUNTS,subvol=data /dev/sdb1 /mnt/data
    $ mount -o $HDD_MOUNTS,subvol=media /dev/sdc1 /mnt/media

    $ mkdir -p /mnt/boot
    $ mount -o $EFI_MOUNTS /dev/sda1 /mnt/boot

Base Installation
=================

Now, we will do the actually installation of base packages.

.. code:: bash

    $ pacstrap /mnt base base-devel btrfs-progs
    $ genfstab -U -p /mnt >> /mnt/etc/fstab

Edit the /mnt/ect/fstab file to add following /tmp mounts.

.. code:: bash

    tmpfs /tmp tmpfs rw,nodev,nosuid 0 0
    tmpfs /dev/shm tmpfs rw,nodev,nosuid,noexec 0 0


.. note:: WIFI AT FIRST BOOT
    Copy our current wifi setup file into the new system. This will enable
    wifi at first boot. Next, chroot into our newly installed system:

    .. code:: bash

        $cp /etc/netctl/wl* /mnt/etc/netctl/


Finally  bind root for installation.

.. code:: bash

    $ arch-chroot /mnt /bin/bash

Basic Setup
------------

Here are some basic commands you need to run to get the installation started.

.. code:: bash

    $ pacman -Syy
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
    $ pacman -S dosfstools efibootmgr
    $ sed -i 's/^\(HOOKS=.*fsck\)\(.*$\)/\1 btrfs\2/g' /etc/mkinitcpio.conf
    $ mkinitcpio -p linux
    $ passwd

.. note:: WIFI PACKAGES
    We also need to install following packages for wifi to work at first boot:

    .. code:: bash

        $ pacman -S iw wpa_supplicant


We will also add *hostname* to our /etc/hosts file:

.. code:: bash

    $ vim /etc/hosts
    ...
    127.0.0.1       localhost.localdomain   localhost $HOSTNAME
    ::1             localhost.localdomain   localhost $HOSTNAME
    ...

Bootloader Setup
-----------------

systemd-boot, previously called gummiboot, is a simple UEFI boot manager
which executes configured EFI images. The default entry is selected by
a configured pattern (glob) or an on-screen menu.
It is included with the *systemd*, which is installed on an Arch systems by default.

Assuming /boot is your boot drive, first run the following command to get started:

.. code:: bash

    $ bootctl --path=/boot install

It will copy the systemd-boot binary to your EFI System Partition
(`/boot/EFI/systemd/systemd-bootx64.efi` and `/boot/EFI/Boot/BOOTX64.EFI`
- both of which are identical - on x64 systems) and add systemd-boot
itself as the default EFI application (default boot entry) loaded by
the EFI Boot Manager.

Finally to configure out boot loader, we will need the UUID of
out root drive (/dev/sda2). You can find that by:

.. code:: bash

    $ lsblk -no NAME,UUID /dev/sda2

Now, make sure that the following two files look as follows,
where $UUID is the value obtained from above command:

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
    options root=UUID=$UUID rw rootfstype=btrfs rootflags=subvol=ROOT
    ...

.. admonition:: Important

    Please  note that you will need manually run bootctl command everytime *systemd-boot* gets updated.

    .. code:: bash

        $ bootctl update


Network Setup
-------------

First setup hostname using systemd:

.. code:: bash

    $ hostnamectl set-hostname $HOSTNAME

 Check the "Ethernet controller" entry (or similar) from the
 `lspci -v` output. It should tell you which kernel module contains
 the driver for your network device. For example:

 .. code:: bash

    $ lspci -v
    $
    ...
    04:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 11)
            Subsystem: ASUSTeK Computer Inc. Device 859e
            Flags: bus master, fast devsel, latency 0, IRQ 29
            I/O ports at d000 [size=256]
            Memory at f7100000 (64-bit, non-prefetchable) [size=4K]
            Memory at f2100000 (64-bit, prefetchable) [size=16K]
            Capabilities: <access denied>
            Kernel driver in use: r8169
            Kernel modules: r8169
    ...
    $

Next, check that the driver was loaded via `dmesg | grep module_name`. For example:

.. code:: bash

    $ dmesg | grep r8169
    $
    ...
    [    3.215178] r8169 Gigabit Ethernet driver 2.3LK-NAPI loaded
    [    3.215185] r8169 0000:04:00.0: can't disable ASPM; OS doesn't have ASPM control
    [    3.220477] r8169 0000:04:00.0 eth0: RTL8168g/8111g at 0xffffc90000c74000, 78:24:af:d7:1d:3d, XID 0c000800 IRQ 29
    [    3.220481] r8169 0000:04:00.0 eth0: jumbo features [frames: 9200 bytes, tx checksumming: ko]
    [    3.226949] r8169 0000:04:00.0 enp4s0: renamed from eth0
    [    5.128713] r8169 0000:04:00.0 enp4s0: link down
    [    5.128713] r8169 0000:04:00.0 enp4s0: link down
    [    8.110869] r8169 0000:04:00.0 enp4s0: link up
    ...
    $

Proceed if the driver was loaded successfully. Otherwise,
you will need to know which module is needed for your particular model.
Please follow the
`Arch Wiki Networking <https://wiki.archlinux.org/index.php/Network_configuration>` _ guide
for further assitance.

Get current device names via `sysf`s or `ip link`. For example:

.. code:: bash

    $ ls /sys/class/net
    $
    ...
    enp4s0  lo  wlp3s0
    ...
    $
    $ ip link
    $
    ...
    2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
        link/ether 78:24:af:d7:1d:3d brd ff:ff:ff:ff:ff:ff
    ...
    $

Using this name of the device, we need to configure, enable following
two systemd services: *systemd-networkd.service*
and *systemd-resolved.service*.

For compatibility with resolv.conf, delete or rename the existing file and
create the following symbolic link:

.. code:: bash

    $ ln -s /usr/lib/systemd/resolv.conf /etc/resolv.conf

Network configurations are stored as \*.network in */etc/systemd/network*.
We need to create ours as follows.:

.. code:: bash

    $ vim /etc/systemd/network/wired.network
    $
    ...
    [Match]
    Name=enp4s0

    [Network]
    DHCP=ipv4

    ...

    $

Now enable these services:

.. code:: bash

    $ systemctl enable systemd-resolved.service
    $ systemctl enable systemd-networkd.service

Your network should be ready for first use!

First Boot
-----------

Now we are ready for the first boot!
Run the following command:

.. code:: bash

    $ exit
    $ umount -R /mnt
    $ reboot

Awesome! We are ready to play with our new system. Alas!
what you have is just a basic installation without any GUI.

Please see my next post for where to go next!
