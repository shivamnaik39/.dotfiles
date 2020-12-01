if [[ "$(tty)" = "/dev/tty1" ]]; then
	pgrep 'tmux|startx' || startx 
fi

