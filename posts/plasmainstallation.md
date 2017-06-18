title: Plasma 5 Installation on Arch Linux
slug: plasmaInstall
date: 2015-06-21 11:20:11 UTC-07:00
tags: Linux, Arch Linux, Plasma 5, KDE
category: Computers
link:
disqus_identifier: plasmaInstall.sadanand
description:
type: text
author: Sadanand Singh

In my last post on
{{% doc %}}Arch Installation Guide <archInstall>{{% /doc %}}, We
installed the base system and we can now login into our new system as
root using the password that we set.

<!--more-->

**Table of Content**

[TOC]

{{% figure http://imgur.com/IjJYMR0.jpg alt="Plasma 5 Looks" align=center %}}

Now, we will proceed further to install the Plasma 5 desktop.

Add New User
============

Choose `$USERNAME` per your liking. I chose `ssingh`, so in future commands
whenever you see `ssingh` please replace it with your `$USERNAME`.

{{% code-block code=bash %}}
$ useradd -m -G wheel -s /bin/bash $USERNAME
$ chfn --full-name "$FULL_NAME" $USERNAME
$ passwd $USERNAME
{{% /code-block %}}

Plasma 5 Desktop
================

Network should be setup at the start. Check the status of network using:

{{% code-block code=bash %}}
$ ping google.com -c 2
$
$ PING google.com (10.38.24.84) 56(84) bytes of data.
$ 64 bytes from google.com (10.38.24.84): icmp_seq=1 ttl=64 time=0.022 ms
$ 64 bytes from google.com (10.38.24.84): icmp_seq=2 ttl=64 time=0.023 ms
$
$ --- google.com ping statistics ---
$ 2 packets transmitted, 2 received, 0% packet loss, time 999ms
$ rtt min/avg/max/mdev = 0.022/0.022/0.023/0.004 ms
$
{{% /code-block %}}

If you do not get this output, please follow the troubleshooting links
at [arch wiki](https://wiki.archlinux.org/index.php/systemd-networkd) on
setting up network.

I will be assuming you have an NVIDIA card for graphics installation.

To setup a graphical desktop, first we need to install some basic X
related packages, and some *essential* packages (including fonts):

{{% code-block code=bash %}}
$ pacman -S xorg-server xorg-server-utils nvidia nvidia-libgl
{{% /code-block %}}

To avoid the possibility of forgetting to update your _initramfs_ after an
_nvidia_ upgrade, you have to use a _pacman_ hook like this:

{{% code-block code=bash %}}
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
{{% /code-block %}}

Nvidia has a daemon that is to be run at boot. To start the persistence
daemon at boot, enable the `nvidia-persistenced.service`.

{{% code-block code=bash %}}
$ systemctl enable nvidia-persistenced.service
$ systemctl start nvidia-persistenced.service
{{% /code-block %}}


{{% panel info "**KWIN FLICKERING ISSUE**" %}}

To avoid screen tearing in KDE (KWin), add following:

{{% code-block code=bash %}}
$ vim /etc/profile.d/kwin.sh
$
...
export __GL_YIELD="USLEEP"
...
{{% /code-block %}}

If this does not help please try adding the following instead -

{{% code-block code=bash %}}
$ vim /etc/profile.d/kwin.sh
$
...
export KWIN_TRIPLE_BUFFER=1
...
{{% /code-block %}}

{{% emph danger %}}
__Do not have both of the above enabled at the same
time. Please look at [Arch
Wiki](https://wiki.archlinux.org/index.php/NVIDIA/Troubleshooting) for
additional details.__
{{% /emph %}}

{{% /panel %}}

Now continue installing remaining important packages for the GUI.

{{% code-block code=bash %}}
$ pacman -S mesa ttf-hack ttf-anonymous-pro
$ pacman -S tlp tlp-rdw acpi_call bash-completion git meld
$ pacman -S ttf-dejavu ttf-freefont ttf-liberation
{{% /code-block %}}

Now, we will install the packages related to Plasma 5:

{{% code-block code=bash %}}
$ pacman -S plasma-meta kf5 kdebase kdeutils kde-applications
$ pacman -S kdegraphics gwenview
{{% /code-block %}}

Now we have to setup a display manager. I chose recommended SDDM for
plasma 5.

{{% code-block code=bash %}}
$ pacman -S sddm sddm-kcm
$ vim /etc/sddm.conf

...
[Theme]
# Current theme name
Current=breeze

# Cursor theme
CursorTheme=breeze_cursors
...

$ systemctl enable sddm
{{% /code-block %}}

Also make sure that network manager starts at boot:

{{% code-block code=bash %}}
$ systemctl disable dhcpcd.service
$ systemctl enable NetworkManager
{{% /code-block %}}

Audio Setup
===========

This is pretty simple. Install following packages and you should be
done:

{{% code-block code=bash %}}
$ pacman -S alsa-utils pulseaudio pulseaudio-alsa libcanberra-pulse
$ pacman -S libcanberra-gstreamer jack2-dbus kmix
$ pacman -S mpv mplayer
{{% /code-block %}}

Useful Tips
===========

This part is optional and you can choose as per your taste. Sync time
using the `systemd` service:

{{% code-block code=bash %}}
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
{{% /code-block %}}

On Plasma 5, It is recommended to enable no-bitmaps to improve the font
rendering:

{{% code-block code=bash %}}
$ sudo ln -s /etc/fonts/conf.avail/70-no-bitmaps.conf
   /etc/fonts/conf.d
   {{% /code-block %}}

If you use vim as your primary editor, you may find
this [vimrc](https://github.com/amix/vimrc) quite useful.

That's It. You are done. Start playing your new beautiful desktop.
Please leave your comments with suggestions or any word of appreciation
if this has been of any help to you.

Follow this page for any additional suggestions or improvements in this
guide.
