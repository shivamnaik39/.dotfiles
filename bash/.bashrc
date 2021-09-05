#neofetch

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# ---Powerline Prompt---
#function _update_ps1() {
#    PS1=$(powerline-shell $?)
#}

#if [[ $TERM != linux && ! $PROMPT_COMMAND =~ _update_ps1 ]]; then
#    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
#fi

# ----------------------

# PS1 Prompt
#export PS1="\[\e[33m\][\[\e[m\]\[\e[31m\]\u\[\e[m\]@\[\e[36m\]\h\[\e[m\]:\[\e[35m\]\w\[\e[m\]\[\e[33m\]]\[\e[m\] (\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)) \$ "

#export PROMPT_COMMAND="notify-send 'Important Notice' 'ARCH LINUX IS THE BEST DISTRO'"

set -o vi

# Source configs
for f in ~/.config/shellconfig/*; do source "$f"; done
#source /home/brodie/.config/broot/launcher/bash/br

bind -x '"\C-l": clear'


export QSYS_ROOTDIR="/home/shivam/.cache/yay/quartus-free/pkg/quartus-free-quartus/opt/intelFPGA/20.1/quartus/sopc_builder/bin"
source /home/shivam/.config/broot/launcher/bash/br
