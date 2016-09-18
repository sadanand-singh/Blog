.. title: Plasma 5 Installation on Arch Linux
.. slug: plasmaInstall
.. date: 2015-06-21 11:20:11 UTC-07:00
.. tags: Linux
.. category: Linux
.. link:
.. description:
.. type: text
.. author: Sadanand Singh

In my last post on :doc:`Arch Installation Guide <archInstall>` , We installed the base system and
we can now login into our new system as root using the password that we
set.

.. TEASER_END

.. figure:: http://imgur.com/IjJYMR0.jpg
   :alt: Plasma 5 Looks

   Plasma 5 Looks

Now, we will proceed further to install the Plasma 5 desktop.

Add New User
------------

Choose $USER per your liking. I chose ssingh, so in future commands
whenever you see *ssingh* please replace it with your $USER.

.. code:: bash

    $ useradd -m -G wheel -s /bin/bash $USERNAME
    $ chfn --full-name "$FULL_NAME" $USERNAME
    $ passwd $USERNAME

Plasma 5 Desktop
----------------

To install anything new, we first need to enable wifi for this session.
To do this I will use the wl\* file that we saved from the initial
installation setup at /etc/netctl.

.. code:: bash

    $ netctl start /etc/netctl/wl*

To setup a graphical desktop, first we need to install some basic X
related packages, and some *essential* packages (including fonts):

.. code:: bash

    $ pacman -S intel-dri xf86-video-intel xorg-server xorg-server-utils
    $ pacman -S intel xorg xorg-xinit xorg-twm xorg-xclock xterm mesa
    $ pacman -S tlp tlp-rdw acpi_call bash-completion git meld
    $ pacman -S firefox flashplugin
    $ pacman -S ttf-dejavu ttf-freefont ttf-liberation ttf-anonymous-pro
    $ pacman -S adobe-source-code-pro-fonts

Now, we will install the packages related to Plasma 5:

.. code:: bash

    $ pacman -S kf5 kf5-aids
    $ pacman -S plasma kdebase kdeutils-kwalletmanager
    $ pacman -S kdegraphics-ksnapshot gwenview
    $ pacman -R plasma-mediacenter
    $ pacman -S networkmanager plasma-nm

Now we have to setup a display manager. I chose recommended SDDM for
plasma 5.

.. code:: bash

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

Also make sure that networkmanager starts at boot:

.. code:: bash

    $ systemctl disable dhcpcd.service
    $ systemctl enable NetworkManager

Audio Setup
-----------

This is pretty simple. Install following packages and you should be
done:

.. code:: bash

    $ pacman -S alsa-utils pulseaudio pulseaudio-alsa libcanberra-pulse
    $ pacman -S libcanberra-gstreamer jack2-dbus kmix
    $ pacman -S vlc mplayer

Useful Tips
-----------

This part is optional and you can choose as per your taste. Sync time:

.. code:: bash

    $ pacman -S ntp
    $ systemctl enable ntpd

On Plasma 5, It is recommended to enable no-bitmaps to improve the font
rendering:

.. code:: bash

    $ sudo ln -s /etc/fonts/conf.avail/70-no-bitmaps.conf /etc/fonts/conf.d

I prefer to use zsh over bash. I also use the awesome
`prezto <https://github.com/sorin-ionescu/prezto>`__ for zsh
configuration. However, I ran into an issue with sddm, where use of
their configurations will lead sddm to freeze. To fix these you need to
do the following before you reboot/logout your system.

.. code:: bash

    $ vim /usr/share/sddm/scripts/Xsession
    ...
    */zsh)
        [ -z "$ZSH_NAME" ] && exec $SHELL $0 "$@"
        emulate -R sh
        [ -d /etc/zsh ] && zdir=/etc/zsh || zdir=/etc
        zhome=${ZDOTDIR:-$HOME}
        # zshenv is always sourced automatically.
        [ -f $zdir/zprofile ] && . $zdir/zprofile
        [ -f $zhome/.zprofile ] && . $zhome/.zprofile
        [ -f $zdir/zlogin ] && . $zdir/zlogin
        [ -f $zhome/.zlogin ] && . $zhome/.zlogin
        ;;
    ...

    Should be changed to:
    ...
    */zsh)
        [ -z "$ZSH_NAME" ] && exec $SHELL $0 "$@"
        [ -d /etc/zsh ] && zdir=/etc/zsh || zdir=/etc
        zhome=${ZDOTDIR:-$HOME}
        # zshenv is always sourced automatically.
        [ -f $zdir/zprofile ] && . $zdir/zprofile
        [ -f $zhome/.zprofile ] && . $zhome/.zprofile
        [ -f $zdir/zlogin ] && . $zdir/zlogin
        [ -f $zhome/.zlogin ] && . $zhome/.zlogin
        emulate -R sh
        ;;
    ...

If you use vim as your primary editor, you may find
`this <https://github.com/amix/vimrc>`__ vimrc quite useful.

That's It. You are done. Start playing your new beautiful desktop.
Please leave your comments with suggestions or any word of appreciation
if this has been of any help to you.

Follow my blog for any further suggestions or improvements in this
guide.
