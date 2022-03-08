xrdb -merge ~/.Xresources
export XDG_SESSION_TYPE=x11
export GDK_BACKEND=x11
export DISPLAY=:0
#export QT_AUTO_SCREEN_SCALE_FACTOR=1
#export GDK_SCALE=1.25
#export GDK_DPI_SCALE=1.0

# Start DWM
#exec dwm

# Start BSPWM
exec bspwm

# Start Xmonad
#exec xmonad

# Start Qtile
#exec qtile

# Start Awesome
#exec awesome
