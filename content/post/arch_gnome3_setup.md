---
title: "My Arch Linux Setup with GNOME 3"
slug: "CompleteSetupArchGnome"
date: 2018-11-25
tags:
    - "Linux"
    - "Arch Linux"
    - "Gnone 3"
categories:
    - "Computers"
link:
authors:
    - "Sadanand Singh"
description:
draft: true
disqus_identifier: "CompleteSetupArchGnome.sadanand"
---

If you have been following me on this space, you would have known by now, I am very particular about
my computers, its operating systems, looks, softwares etc. Before you start getting any wrong ideas,
my love for [Arch Linux] is still going strong. However, I have moved on to [Gnome 3] as my choice
desktop. This post is an update for the latest configuration of my machine. I have also update my
GPU to 1080 Ti to be able to run some computer vision models at reasonable speeds. I use this desktop
for some audio processing and some kaggle-level computer vision/deep learning.

<!-- more -->
{{< load-photoswipe >}}
{{< gallery >}}
{{< figure-thumb link="https://filedn.com/lSuvfdBS7StB1VENIoS8hjj/Blog-Static-Contents/images/gnome3/ApplicationMenu.png" caption="Applications Menu" >}}
{{< figure-thumb link="https://filedn.com/lSuvfdBS7StB1VENIoS8hjj/Blog-Static-Contents/images/gnome3/SystemInfo.png" caption="System Info" >}}
{{< figure-thumb link="https://filedn.com/lSuvfdBS7StB1VENIoS8hjj/Blog-Static-Contents/images/gnome3/workspaces.png" caption="Gnome 3 Workspaces" >}}
{{< figure-thumb link="https://filedn.com/lSuvfdBS7StB1VENIoS8hjj/Blog-Static-Contents/images/gnome3/Apps.png" caption="Apps" >}}
{{< figure-thumb link="https://filedn.com/lSuvfdBS7StB1VENIoS8hjj/Blog-Static-Contents/images/gnome3/editors.png" caption="Editors" >}}
{{< figure-thumb link="https://filedn.com/lSuvfdBS7StB1VENIoS8hjj/Blog-Static-Contents/images/gnome3/pcloud.png" caption="pCloud" >}}
{{< /gallery >}}

In this post, we will do a complete installation of Arch Linux with Gnome 3 as the desktop
environment. Our setup will also involve encryption of the root partition that will be formatted in
[btrfs]. This post is an updated version of my previous posts on
[Arch Linux]({{< relref "myarchsetup.md" >}}).


<br/>
{{< card primary "**IMPORTANT**" >}}

I do not wish to repeat [Arch Installation Guide](https://wiki.archlinux.org/index.php/installation_guide) here.

Do not forget about [Arch Wiki], the best documentation in the world! Most of the content
in this post has been compiled from the [Arch wiki].
[Arch wiki]: https://wiki.archlinux.org/
{{< /card >}}
<br/>

<!--toc-->

[Arch Linux]: https://www.archlinux.org
[Gnome 3]: https://www.gnome.org/gnome-3/
[btrfs]: https://en.wikipedia.org/wiki/Btrfs


System Details
==============

For reference, my installation system is a slightly upgraded form of
[my original desktop]({{< relref "newdesktop.md" >}}):

-   i7 4790 3.6 GHz (Haswell)
-   ASRock Z97 Extreme6 LGA 1150 Intel Z97 HDMI SATA USB 3.0
-   ADATA XPG V1.0 DDR3 1866 4x4 GB RAM
-   OCZ Vertex 460A Series 2.5" 240 GB
-   WD Blue 1TB 3.5" 7200 RPM, 64MB Cache
-   WD Blue 3TB 3.5" 7200 RPM, 64MB Cache
-   Ultra LSP V2 650 Watt PSU
-   Cooler Master - MasterCase Pro 5
-   Asus BW-12B1ST/BLK/G/AS Blue Ray Burner
-   Samsung U28E590D 28-Inch UHD LED-Lit 4K Monitor
-   Nvidia GeForce GTX 1080 Ti GPU

Base Installation
=================

Before beginning this guide, I would assume that you have a bootable USB of the latest Arch Linux
Installer. If not, please follow the
[Arch wiki guide](https://wiki.archlinux.org/index.php/USB_flash_installation_media).
Once you login into the installer USB, You will be logged in as the root user, and presented with
a *zsh* shell. I will assume you have an __Ethernet__ connection and hence will be connected to
Internet by default. If you have to rely on wifi, please refer to the
[Wireless Network Configuration](https://wiki.archlinux.org/index.php/Wireless_network_configuration)
wiki page for the detailed setup. **You must have Internet connection at this stage before
proceeding any further.**

You should boot into _UEFI_ mode if you have a UEFI motherboard and UEFI mode enabled. To verify
thatyou have booted in UEFI mode, please run:

```bash
efivar -l
```

This should print all set UEFI variables. Please look at the
[Arch Installation Guide](https://wiki.archlinux.org/index.php/installation_guide) in case you do
not get any list of UEFI variables.

If you have a 4k (high resolution) monitor like me, you will need to run following to increase fonts
to a readable size:

```bash
pacman -Sy
pacman -S terminus-font
setfont ter-132n
```

We are all set to get started with the actual installation process.

Partitioning Hard Drives
-------------------------

First find the hard drive that you will be using as the main/root disk.

```bash
cat /proc/partitions

  OUTPUT eg.
  major minor  #blocks  name

  8        0  268435456 sda
  9        0  268435456 sdb
  19       0  268435456 sdc
  11       0     759808 sr0
  7        0     328616 loop0
```

Say, we will be using */dev/sda* as the main disk and */dev/sdb* as */data* and */dev/sdc*
as */media* .

Because we are creating an encrypted file system it’s a good idea to first overwrite it with
random data.

We’ll use **badblocks** for this. Another method is to use *dd if=/dev/urandom of=/dev/xxx*, the
*dd* method is probably the best method, but is a lot slower.
**The following step should take about 20 minutes on a 240 GB SSD.**

```bash
badblocks -c 10240 -s -w -t random -v /dev/sda
```

Next, we will create GPT partitions on all disks using _gdisk_ command. Let us first randomize
the first few blocks to corrupt any existing GPT.

```bash
dd if=/dev/zero of=/dev/sda bs=1M count=5000
gdisk /dev/sda
Found invalid MBR and corrupt GPT. What do you want to do? (Using the
GPT MAY permit recovery of GPT data.)
 1 - Use current GPT
 2 - Create blank GPT
 ```

Then press 2 to create a blank GPT and start fresh

```bash
ZAP:
press x - to go to extended menu
press z - to zap
press Y - to confirm
press Y - to delete MBR
```

It might now kick us out of _gdisk_, so get back into it:

```bash
gdisk /dev/sda

Command (? for help): m
Command (? for help): n

Partition number (1-128, default 1):
First sector (34-500118158, default = 2048) or {+-}size{KMGTP}:
Last sector (2048-500118, default = 500118) or {+-}size{KMGTP}: 512M
Current type is 'Linux filesystem'
Hex code or GUID (L to show codes, Enter = 8300): ef00
Changed type of partition to 'EFI System'

Partition number (2-128, default 2):
First sector (34-500118, default = 16779264) or {+-}size{KMGTP}:
Last sector (16779264-500118, default = 500118) or {+-}size{KMGTP}:
Current type is 'Linux filesystem'
Hex code or GUID (L to show codes, Enter = 8300):
Changed type of partition to 'Linux filesystem'

Command (? for help): p
Press w to write to disk
Press Y to confirm
```

Repeat the above procedure for */dev/sdb* and */dev/sdc*, but create
just one partition with all values as default. At the end we will have
three partitions: */dev/sda1*, */dev/sda2*, */dev/sdb1* and */dev/sdc1*.

Setup Disk Encryption
---------------------

Our /boot partition will be on */dev/sda1*, while the main installation
will be on */dev/sda2*. In this setup, we will be enabling full
encryption on */dev/sda2* only.

In order to enable disk encryption, we will first create a root luks
volume, open it and then format it.

```bash
# first, we need to prepare the encrypted (outer) volume
cryptsetup --cipher aes-xts-plain64 --hash sha512 --use-random --verify-passphrase luksFormat /dev/sda2

# I really hope I don't have to lecture you on NOT LOSING this
# password, lest all of your data will be forever inaccessible,
# right?

# then, we actually open it as a block device, and format the
# inner volume later
cryptsetup luksOpen /dev/sda2 root
```

{{< card success "**Automatic Key Login from an USB/SD Card**" >}}

If you want to automatically login the encrypted disk password from an
externally attached USB or SD card, you will first need to create a key
file.

```bash
dd bs=512 count=4 if=/dev/urandom of=KEYFILE
```

Then, add this key to the luks container, so that it can be later used
to open the encrypted drive.

```bash
cryptsetup luksAddKey /dev/sda2 KEYFILE
```

{{< emph warning >}} Note that the KEYFILE here should be kept on a
separate USB drive or SD card. {{< /emph >}} The recommended way of
using such a disk would be as follows:

```bash
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
```

We will be later using this KEYFILE in boot loader setup.

{{< /card >}}

Format HDDs
-----------

At this point, we have following drives ready for format: */dev/sda1*,
*/dev/mapper/root*, */dev/sdb1* and */dev/sdc1*.

These can be format as follows:

```bash
mkfs.vfat -F32 /dev/sda1
mkfs.btrfs -L arch /dev/mapper/root
mkfs.btrfs -L data /dev/sdb1
mkfs.btrfs -L media /dev/sdc1
```

Now, we will create _btrfs_ subvolumes and mount them properly for
installation and final setup.

```bash
mount /dev/mapper/root /mnt
btrfs subvolume create /mnt/ROOT
btrfs subvolume create /mnt/home
umount /mnt

mount /dev/sdb1 /mnt
btrfs subvolume create /mnt/data
umount /mnt

mount /dev/sdc1 /mnt
btrfs subvolume create /mnt/media
umount /mnt
```

Now, once the sub-volumes have been created, we will mount them in
appropriate locations with optimal flags.

```bash
SSD_MOUNTS="rw,noatime,nodev,compress=lzo,ssd,discard,
    space_cache,autodefrag,inode_cache"
HDD_MOUNTS="rw,nosuid,nodev,relatime,space_cache"
EFI_MOUNTS="rw,noatime,discard,nodev,nosuid,noexec"
mount -o $SSD_MOUNTS,subvol=ROOT /dev/mapper/root /mnt
mkdir -p /mnt/home
mkdir -p /mnt/data
mkdir -p /mnt/media
mount -o $SSD_MOUNTS,nosuid,subvol=home /dev/mapper/root /mnt/home
mount -o $HDD_MOUNTS,subvol=data /dev/sdb1 /mnt/data
mount -o $HDD_MOUNTS,subvol=media /dev/sdc1 /mnt/media

mkdir -p /mnt/boot
mount -o $EFI_MOUNTS /dev/sda1 /mnt/boot
```

{{< marker cyan >}} Save the current <i>/etc/resolv.conf</i> file for future
use! {{< /marker >}}

```bash
cp /etc/resolv.conf /mnt/etc/resolv.conf
```

Base System Installation
------------------------

Now, we will do the actually installation of base packages.

```bash
pacstrap /mnt base base-devel btrfs-progs
genfstab -U -p /mnt >> /mnt/etc/fstab
```

Initial System Setup
--------------------

Edit the _/mnt/ect/fstab_ file to add following _/tmp_ mounts.

```bash
tmpfs /tmp tmpfs rw,nodev,nosuid 0 0
tmpfs /dev/shm tmpfs rw,nodev,nosuid,noexec 0 0
```

Finally bind root for installation.

```bash
arch-chroot /mnt "bash"
pacman -Syy
pacman -Syu
pacman -S sudo vim
vim /etc/locale.gen

...
# en_SG ISO-8859-1
en_US.UTF-8 UTF-8
# en_US ISO-8859-1
...

locale-gen
echo LANG=en_US.UTF-8 > /etc/locale.conf
export LANG=en_US.UTF-8
ls -l /usr/share/zoneinfo
ln -sf /usr/share/zoneinfo/Zone/SubZone /etc/localtime
hwclock --systohc --utc
sed -i "s/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/" /etc/sudoers
HOSTNAME=euler
echo $HOSTNAME > /etc/hostname
passwd
```

We will also add *hostname* to our `/etc/hosts` file:

```bash
vim /etc/hosts
...
127.0.0.1       localhost.localdomain   localhost
::1             localhost.localdomain   localhost
127.0.0.1       $HOSTNAME.localdomain   $HOSTNAME
...
```

We also need to fix the `mkinitcpio.conf` to contain what we actually
need.

```bash
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
```

Boot Manager Setup
------------------

*systemd-boot*, previously called *gummiboot*, is a simple UEFI boot
manager which executes configured EFI images. The default entry is
selected by a configured pattern (glob) or an on-screen menu. It is
included with the *systemd*, which is installed on an Arch systems by
default.

Assuming */boot* is your boot drive, first run the following command to
get started:

```bash
bootctl --path=/boot install
```

It will copy the systemd-boot binary to your EFI System Partition (
`/boot/EFI/systemd/systemd-bootx64.efi` and `/boot/EFI/Boot/BOOTX64.EFI` -
both of which are identical - on __x64__ systems ) and add *systemd-boot*
itself as the default EFI application (default boot entry) loaded by the
EFI Boot Manager.

Finally to configure out boot loader, we will need the UUID of some of
our hard drives. These can be easily done using the *blkid* command.

```bash
blkid /dev/sda1 > /boot/loader/entries/arch.conf
blkid /dev/sda2 >> /boot/loader/entries/arch.conf
blkid /dev/mapper/root >> /boot/loader/entries/arch.conf
blkid /dev/sdd1 >> /boot/loader/entries/arch.conf

# for this example, I'm going to mark them like this:
# /dev/sda1 LABEL="EFI"                 UUID=11111111-1111-1111-1111-111111111111
# /dev/sda2 LABEL="arch"      UUID=33333333-3333-3333-3333-333333333333
# /dev/mapper/root LABEL="Arch Linux"   UUID=44444444-4444-4444-4444-444444444444
# /dev/sdd1 LABEL="USB"     UUID=0000-0000  # this is the drive where KEYFILE exists
```

Now, make sure that the following two files look as follows, where UUIDs
is the value obtained from above commands.

{{< marker warning >}} Do not forget to modify UUIDs and KEYFIL entries!
{{< /marker >}}

```bash
vim /boot/loader/loader.conf
...
timeout 3
default arch
...
vim /boot/loader/entries/arch.conf
...

title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
options ro cryptdevice=UUID=33333333-3333-3333-3333-333333333333:luks-33333333-3333-3333-3333-333333333333 root=UUID=44444444-4444-4444-4444-444444444444 rootfstype=btrfs rootflags=subvol=ROOT cryptkey=UUID=0000-0000:vfat:KEYFILE
...
```

Network Setup
-------------

At first we will need to figure out the Ethernet controller on which
cable is connected.

```bash
networkctl
#
# IDX LINK             TYPE               OPERATIONAL SETUP
#   1 lo               loopback           carrier     unmanaged
#   2 enp3s0           ether              no-carrier  unmanaged
#   3 wlp6s0           wlan               no-carrier  unmanaged
#   4 enp0s25          ether              routable    configured
#
```

In my case, the name of the device is *enp0s25*.

Using this name of the device, we need to configure, and enable the
*systemd-networkd.service* service.

Note that we will using the *resolv.conf* that we saved from this
session.

Network configurations are stored as \*.network in
`/etc/systemd/network`. We need to create ours as follows.:

```bash
vim /etc/systemd/network/50-wired.network

...
[Match]
Name=enp0s25

[Network]
DHCP=ipv4

...


```

Now enable the `networkd` services:

```bash
systemctl enable systemd-networkd.service
```

Your network should be ready for the first use!

Sync time automatically using the *systemd* service:

```bash
vim /etc/systemd/timesyncd.conf

...
[Time]
NTP=0.arch.pool.ntp.org 1.arch.pool.ntp.org 2.arch.pool.ntp.org 3.arch.pool.ntp.org
FallbackNTP=0.pool.ntp.org 1.pool.ntp.org 0.fr.pool.ntp.org
...

timedatectl set-ntp true
timedatectl status

...
      Local time: Tue 2016-09-20 16:40:44 PDT
  Universal time: Tue 2016-09-20 23:40:44 UTC
        RTC time: Tue 2016-09-20 23:40:44
       Time zone: US/Pacific (PDT, -0700)
 Network time on: yes
NTP synchronized: yes
 RTC in local TZ: no
 ...

```

[Avahi](https://wiki.archlinux.org/index.php/avahi) is a tool that
allows programs to publish and discover services and hosts running on a
local network with no specific configuration. For example you can plug
into a network and instantly find printers to print to, files to look at
and people to talk to.

We can easily set it up it as follows:

```bash
pacman -S avahi nss-mdns
systemctl enable avahi-daemon.service
```

We will also install `terminus-font` on our system to work with proper
fonts on first boot.

```bash
pacman -S terminus-font
```

First Boot Installations
========================

Now we are ready for the first boot! Run the following command:

```bash
exit
umount -R /mnt
reboot
```

After your new system boots, Network should be setup at the start. Check
the status of network using:

```bash
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
```

If you do not get this output, please follow the troubleshooting links
at Arch Wiki on [setting up
network](https://wiki.archlinux.org/index.php/systemd-networkd).

Adding New User
---------------

Choose `$USERNAME` per your liking. I chose *ssingh*, so in future
commands whenever you see *ssingh* please replace it with your
`$USERNAME`.

```bash
pacman -S zsh
useradd -m -G wheel -s usr/bin/zsh $USERNAME
chfn --full-name "$FULL_NAME" $USERNAME
passwd $USERNAME
```

GUI Installation with nvidia
----------------------------

I will be assuming you have an `NVIDIA` card for graphics installation.

To setup a graphical desktop, first we need to install some basic X
related packages, and some *essential* packages (including fonts):

```bash
pacman -S xorg-server nvidia nvidia-libgl nvidia-settings mesa
```

To avoid the possibility of forgetting to update your *initramfs* after
an *nvidia* upgrade, you have to use a *pacman* hook like this:

```bash
vim /etc/pacman.d/hooks/nvidia.hook

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

```

Nvidia has a daemon that is to be run at boot. To start the _persistence_
daemon at boot, enable the `nvidia-persistenced.service`.

```bash
systemctl enable nvidia-persistenced.service
systemctl start nvidia-persistenced.service
```

{{< card warning "**How to Avoid Screen Tearing**" >}}

Tearing can be avoided by forcing a full composition pipeline,
regardless of the compositor you are using.

In order to make this change permanent, We will need to edit nvidia
configuration file. Since, by default there aren't any, we will first
need to create one.

```bash
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
```

{{< /card >}}

Specific for Plasma 5, we will also create the following file to avoid
any tearing in Plasma.

```bash
vim /etc/profile.d/kwin.sh

...
export KWIN_TRIPLE_BUFFER=1
...
```

{{< card warning "**How to Enable Better Resolution During Boot**" >}}

The kernel compiled in *efifb* module supports high-resolution nvidia
console on EFI systems. This can enabled by enabling the DRM kernel mode
setting.

First, we will need to add following to MODULES section of the
*mkinitcpio.conf* file:

-  *nvidia*
-  *nvidia_modeset*
-  *nvidia_uvm*
-  *nvidia_drm*

We will also need to pass the *nvidia-drm.modeset=1* kernel parameter during the boot.

```bash
vim /etc/mkinitcpio.conf

...
MODULES="vfat aes_x86_64 crc32c-intel nvidia nvidia_modeset nvidia_uvm nvidia_drm"
...

vim /boot/loader/entries/arch.conf

...
options ro cryptdevice=UUID=:luks- root=UUID= rootfstype=btrfs rootflags=subvol=ROOT cryptkey=UUID=:vfat:deepmind20170602 nvidia-drm.modeset=1
...

mkinitcpio -p linux
```

{{< /card >}}

Plasma 5 Installation and Setup
-------------------------------

We can now proceed with the installation of Plasma 5. In the process, we
will also install some useful fonts.

```bash
pacman -S ttf-hack ttf-anonymous-pro
pacman -S ttf-dejavu ttf-freefont ttf-liberation
pacman -S plasma-meta dolphin kdialog kfind
pacman -S konsole gwenview okular spectacle kio-extras
pacman -S kompare dolphin-plugins kwallet kwalletmanager
pacman -S ark yakuake flite
```

We will also need to select proper themes for the Plasma 5 display
manager *sddm* and then enable its *systemd* service.

```bash
vim /etc/sddm.conf

....
[Theme]
# Current theme name
Current=breeze

# Cursor theme used in the greeter
CursorTheme=breeze_cursors
...

systemctl enable sddm
reboot
```

Once, we boot into the new system, we should have a basic Plasma 5
desktop waiting for you. In the following section, we will be do
installation and modifications to the system that I prefer.

Post Installation Setup
=======================

Plasma 5 provides a handy network manager applet. However, in order to
use it properly we will need the NetworkManager service to be enabled.
This applet allows user specific enabling of *wifi*, *ethernet* or even
*VPN* connections.

```bash
sudo pacman -S networkmanager
systemctl enable NetworkManager.service
systemctl start NetworkManager.service
```

We can also automate the *hostname* setup using the following *systemd*
command:

```bash
hostnamectl set-hostname $HOSTNAME
```

Selecting pacman Mirrors
------------------------

The *pacman* package provides a "bash" script, */usr/bin/rankmirrors*,
which can be used to rank the mirrors according to their connection and
opening speeds to take advantage of using the fastest local mirror.

We will do this only on the US based mirrors. First make a copy of the
mirrors list file and then delete all non-US mirrors. We will then
*rankmirrors* script on the modified list to get the top 6 mirrors for
our regular use.

```bash
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.us
vim /etc/pacman.d/mirrorlist.us
....
# Delete all non-US servers
....
rankmirrors -n 6 /etc/pacman.d/mirrorlist.us > /etc/pacman.d/mirrorlist
```

Setup AUR
---------

[AUR](https://aur.archlinux.org/) is a community-driven repository for
Arch users. This allows you to install many popular packages that are
otherwise not available through core repositories.

In order to make all types of installations uniform, I use
[pacaur](https://github.com/rmarquis/pacaur) as the preferred tool for
installing all packages. One the biggest advantages of *pacaur* is that
is uses exactly the same options that regular *pacman* uses.

In order to install *pacuar*, first install dependencies.

```bash
sudo pacman -S expac yajl curl gnupg --noconfirm
```

Create a temp directory for building packages:

```bash
mkdir ~/temp
cp ~ temp
```

Install *cower* first and then *pacaur*:

```bash
gpg --recv-keys --keyserver hkp://pgp.mit.edu 1EB2638FF56C0C53
curl -o PKGBUILD https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=cower
makepkg -i PKGBUILD --noconfirm

curl -o PKGBUILD https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=pacaur
makepkg -i PKGBUILD --noconfirm

# Finally cleanup and remove the temp directory
cd ~
rm -r ~/temp
```

Audio Setup
-----------

This is pretty simple. Install following packages and you should be
done:

```bash
sudo pacaur -S alsa-utils pulseaudio pulseaudio-alsa mpv
sudo pacaur -S libcanberra-pulse libcanberra-gstreamer
sudo pacaur -S vlc-qt5
```

Now start the *pulseaudio* service.

```bash
systemctl --user enable pulseaudio.socket
```

Web Browsers
------------

My preferred choice of browsers is *google chrome*. However, it is also
good to have the KDE native *qupzilla*.

```bash
sudo pacaur -S google-chrome qupzilla
```

*Profile-sync-daemon (psd)* is a tiny pseudo-daemon designed to manage
browser profile(s) in *tmpfs* and to periodically sync back to the
physical disc (HDD/SSD). This is accomplished by an innovative use of
*rsync* to maintain synchronization between a *tmpfs* copy and
media-bound backup of the browser profile(s). These features of *psd*
leads to following benefits:

-   Transparent user experience
-   Reduced wear to physical drives, and
-   Speed

To setup. first install the *profile-sync-daemon* package.

```bash
sudo pacaur -S profile-sync-daemon
```

Run *psd* the first time which will create a configuration file at
\$XDG\_CONFIG\_HOME/psd/psd.conf which contains all settings.

```bash
psd
# First time running psd so please edit
# /home/$USERNAME/.config/psd/psd.conf to your liking and run again.
```

In the config file change the BROWSERS variables to *google-chrome
qupzilla*. Also, enable the use of *overlayfs* to improve sync speed
and to use a smaller memory footprint. Do this in the
*USE\_OVERLAYFS="yes"* variable.

{{< marker warning >}} Note: USE_OVERLAYFS feature requires a Linux
kernel version of 3.18.0 or greater to work. {{< /marker >}}

In order to use the OVERLAYFS feature, you will also need to give *sudo*
permissions to psd-helper as follows (replace `$USERNAME` accordingly):

```bash
vim /etc/sudoers
...
$USERNAME ALL=(ALL) NOPASSWD: /usr/bin/psd-overlay-helper
...
```

Verify the working of configuration using the preview mode of psd:

```bash
psd p
```

*Google Chrome* by default uses *kdewallet* to manage passwords, where
as *Qupzilla* does not. You can change that in its settings.

git Setup
---------

Install git and setup some global options as below:

```bash
sudo pacaur -S git

vim ~/.gitconfig
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

```

ssh Setup
---------

To get started first install the *openssh* package.

```bash
sudo pacaur -S openssh
```

The ssh server can be started using the *systemd* service. Before
starting the service, however, we want to generate ssh keys and setup
the server for login based only on keys.

```bash
ssh-keygen -t ed25519

# Create a .ssh/config file for rmate usage in sublime text
vim ~/.ssh/config
...
RemoteForward 52698 localhost:52698
...

# Create ~/.ssh/authorized_keys file with list of machines that
# are allowed to login to this machine.
touch ~/.ssh/authorized_keys

# Finally edit the /etc/ssh/sshd_config
# file to disable Password based logins
sudo vim /etc/ssh/sshd_config
...
PasswordAuthentication no
...
```

Furthermore, before enabling the *sshd* service, please also ensure to
copy your keys to all your relevant other servers and places like
github.

We can now use *systemd* to start the ssh service.

```bash
systemctl enable sshd.socket
systemctl start sshd.socket
```

zsh Setup
---------

During the user creation, we already installed the *zsh* shell. We have
also activated a basic setup at first login by the user.

In this section, we will be installing my variation of
[zprezto](https://github.com/sorin-ionescu/prezto) package to manage
*zsh* configurations.

First install the main zprezto package:

```bash
git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"

setopt EXTENDED_GLOB
for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N);
do
    ln -sf "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"
done

```

Now, We will add my version of prezto to the same git repo.

```bash
cd ~/.zprezto
git remote add personal git@github.com:sadanand-singh/My-Zprezto.git
git pull personal arch
git checkout arch
git merge master
```

And we are all setup for using *zsh*!

gpg Setup
---------

We have already installed the *gnupg* package during the *pacaur*
installation. We will first either import our already existing private
keys(s) or create one.

Once We have our keys setup, edit keys to change trust level.

Once all keys are setup, we need to gpg-agent configuration file:

```bash
vim ~/.gnupg/gpg-agent.conf
..
enable-ssh-support
default-cache-ttl-ssh 10800
default-cache-ttl 10800
max-cache-ttl-ssh 10800
...

```

Also, add following to your *.zshrc* or *."bash"rc* file. If you are using
my zprezto setup, you already have this!

```bash
vim ~/.zshrc
...
# set GPG TTY
export GPG_TTY=$(tty)

# Refresh gpg-agent tty in case user switches into an X Session
gpg-connect-agent updatestartuptty /bye >/dev/null

# Set SSH to use gpg-agent
unset SSH_AGENT_PID
if [ "${gnupg_SSH_AUTH_SOCK_by:-0}" -ne $]; then
  export SSH_AUTH_SOCK="/run/user/$UID/gnupg/S.gpg-agent.ssh"
fi
...

```

Now, simply start the following systemd sockets as user:

```bash
systemctl --user enable gpg-agent.socket
systemctl --user enable gpg-agent-ssh.socket
systemctl --user enable dirmngr.socket
systemctl --user enable gpg-agent-browser.socket

systemctl --user start gpg-agent.socket
systemctl --user start gpg-agent-ssh.socket
systemctl --user start dirmngr.socket
systemctl --user start gpg-agent-browser.socket
```

Finally add your ssh key to ssh agent.

```bash
ssh-add ~/.ssh/id_ed25519
```

User Wallpapers
---------------

You can store your own wallpapers at the following location. A good
place to get some good wallpapers are [KaOS
Wallpapers](https://github.com/KaOSx/kaos-wallpapers).

```bash
mkdir -p $HOME/.local/wallpapers
cp SOME_JPEG $HOME/.local/wallpapers/
```


Software Installations
----------------------

Here is a running list of other common softwares that I install.

```bash
paci spotify tmux tree dropbox thesilver_searcher
paci digikam imagemagick
```

I also add the following repository to install the [Sublime
Text](https://www.sublimetext.com/) editor. Refer to
my previous post <sublimetext> for details on setting up Sublime
Text.

```bash
curl -O https://download.sublimetext.com/sublimehq-pub.gpg
sudo pacman-key --add sublimehq-pub.gpg
sudo pacman-key --lsign-key 8A8F901A
rm sublimehq-pub.gpg

echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/dev/x86_64" | sudo tee -a /etc/pacman.conf
```

Now we can install *sublime-text* as:

```bash
paci sublime-text/sublime-text
```

This brings us to the conclusion of this installation guide. Hope many
of you find it useful. Please drop your comments below if you have any
suggestions for improvements etc.