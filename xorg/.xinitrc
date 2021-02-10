
# Find out your monitor name with xrandr or arandr (save and you get this line)
$HOME/.screenlayout/monitor.sh &

# Launch Polybar
#$HOME/.config/polybar/launch.sh &

# change your keyboard if you need it
#setxkbmap -layout be

# Set wallpaper
nitrogen --restore &

# run simple X hot key daemon (sxhkd) bind keys
#sxhkd &

# run compositor
picom --experimental-backends &

#Policy kit daemon
/usr/bin/lxpolkit &

#dwm status
#/home/$USER/.config/dwm-status/dwm-status.sh &

#dwm blocks
#dwmblocks &

#slstatus
#slstatus &

#dunst notification daemon
dunst &

# flameshot screen shot tool
#flameshot &

# netwoek manager applet
#nm-applet &

# blue light filter (redshift)
redshift &

$HOME/.test &

# screen locker
xautolock -time 5 -locker "betterlockscreen -l dim --off 60" &

# fix cursor (bspwm)
xsetroot -cursor_name left_ptr & 

#xmodmap ~/.Xmodmap &

# Start DWM
#exec dwm

# Start BSPWM
exec bspwm

# Start Xmonad
#exec xmonad

# Start Qtile
#exec qtile
