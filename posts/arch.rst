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

Wifi
----

To setup wifi simply run:

.. code:: bash

    $ wifi-menu

This is a pretty straight forward tool and will setup wifi for you for
this installation session.

This will also create a file at */etc/netctl/*. We will use this file
later to enable wifi at the first session after installation.

For editing different configurations, I tend to use *vim*. So we will
update our package cache and install vim.

.. code:: bash

    $ pacman -Syy
    $ pacman -S vim

Hard Drives
-----------

In my desktop, I have two hard drives, one 256 GB solid state drive
(SDD) and another 1TB hard drive (HDD). I set up my drives as follows: -
SDD for root(/), /boot, /opt and /home partitions - HDD for /var and
/media partitions.

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

Repeat the above procedure for */dev/sdb*, but create just one partition
with all values as default. At the end we will have three partitions:
/dev/sda1, /dev/sda2 and /dev/sdb1

Now we will format these partitions.

.. code:: bash

    $ mkfs.vfat -F32 /dev/sda1
    $ mkfs.btrfs -L arch /dev/sda2
    $ mkfs.btrfs -L data /dev/sdb1

Now, we will create btrfs subvolumes and mount them properly for
installation and final setup.

.. code:: bash

    $ mount /dev/sda2 /mnt
    $ btrfs subvolume create /mnt/ROOT
    $ btrfs subvolume create /mnt/opt
    $ btrfs subvolume create /mnt/home
    $ umount /mnt

    $ mount /dev/sdb1 /mnt
    $ btrfs subvolume create /mnt/var
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
    $ mkdir -p /mnt/opt
    $ mkdir -p /mnt/home
    $ mkdir -p /mnt/var
    $ mkdir -p /mnt/media
    $ mount -o $SSD_MOUNTS,nosuid,subvol=opt /dev/sda2 /mnt/opt
    $ mount -o $SSD_MOUNTS,nosuid,subvol=home /dev/sda2 /mnt/home
    $ mount -o $HDD_MOUNTS,subvol=var /dev/sdb1 /mnt/var
    $ mount -o $HDD_MOUNTS,subvol=media /dev/sdb1 /mnt/media

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

Copy our current wifi setup file into the new system. This will enable
wifi at first boot. Next, chroot into our newly installed system:

.. code:: bash

    $ cp /etc/netctl/wl* /mnt/etc/netctl/
    $ arch-chroot /mnt /bin/bash

Some basic setup:

.. code:: bash

    $ pacman -Syy
    $ pacman -S sudo vim
    $ vim /etc/locale.gen

    ...
    $en_SG ISO-8859-1
    en_US.UTF-8 UTF-8
    $en_US ISO-8859-1
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
    $ gummiboot install
    $ passwd

We also need to install following packages for wifi to work at first
boot:

.. code:: bash

    $ pacman -S iw wpa_supplicant

We will also add *hostname* to our /etc/hosts file:

.. code:: bash

    $ vim /etc/hosts
    ...
    127.0.0.1       localhost.localdomain   localhost $HOSTNAME
    ::1             localhost.localdomain   localhost $HOSTNAME
    ...

We will do the final setup now, that should enable us to login into our
newly installed system. Make sure following two files look as follows:

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
    options root=UUID=1c27fa42-ca19-482f-b49a-3b8366eb7783 rw rootfstype=btrfs rootflags=subvol=ROOT
    ...
    $ exit
    $ umount -R /mnt
    $ reboot

Awesome! We are ready to play with our new system. Please see my next
post for more.
