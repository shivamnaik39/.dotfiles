#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then







    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then







    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

#Policy kit daemon
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#Bind keys
sxhkd &

#dwm status
#/home/$USER/.config/dwm-status/dwm-status.sh &

#dwm blocks
dwmblocks &

#slstatus
#slstatus &

#keyboard layout
#setxkbmap us &

#Display Resolution
xrandr --output eDP  --mode 1366x768 & 

#Compositor
picom -f &

#wallpaper
nitrogen --restore &

# screen locker
xautolock -time 5 -locker "betterlockscreen -l dim --off 5" -detectsleep &

#Execute DWM
exec dwm
