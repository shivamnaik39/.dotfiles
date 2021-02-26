set fish_greeting                                 # Supresses fish's intro message
set TERM "xterm-256color"                         # Sets the terminal type

### SET EITHER DEFAULT EMACS MODE OR VI MODE ###
function fish_user_key_bindings
  # fish_default_key_bindings
  fish_vi_key_bindings
end
### END OF VI MODE ###

### SET MANPAGER
### "bat" as manpager
set -x MANPAGER "sh -c 'col -bx | bat -l man -p'" 


### AUTOCOMPLETE AND HIGHLIGHT COLORS ###
set fish_color_normal '#A3BE8C'
set fish_color_autosuggestion '#7d7d7d'
set fish_color_command '#A3BE8C'
set fish_color_error '#BF616A'
set fish_color_param '#A3BE8C'

# Aliases
source ~/.config/fish/fish_aliases

starship init fish | source
