if [[ "$(tty)" = "/dev/tty1" ]]; then
	pgrep 'tmux|startx' || startx 
fi

export PATH="/home/shivam/.local/share/solana/install/active_release/bin:$PATH"
