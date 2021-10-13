#!/bin/bash

function run() {
  if ! pgrep $1; then
    $@ &
  fi
}
#run xrandr --output VGA-1 --primary --mode 1360x768 --pos 0x0 --rotate normal
#run xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off
run $HOME/.screenlayout/monitor.sh
#autorandr horizontal
run dunst
run nm-applet
run blueberry-tray
run /usr/bin/lxpolkit 
run nitrogen --restore
run parcellite

killall redshift
redshift -P -O 6500
redshift &

run xautolock -time 5 -locker 'betterlockscreen -l dim --off 60'

#you can set wallpapers in themes as well
#run applications from startup
