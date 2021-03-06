# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import KeyChord, Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "st"                             # My terminal of choice
myConfig = "$HOME/.config/qtile/config.py"    # The Qtile config file location

keys = [
    # The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'
        ),
    Key([mod], "d",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc='Dmenu Run Launcher'
        ),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),
    Key([mod], "q",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),

    # Switch focus to specific monitor (out of three)
    Key([mod], "w",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),

    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    # Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),
    # Window controls
    Key([mod], "k",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "j",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod, "shift"], "m",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    Key(
        [mod], "f",
        lazy.window.toggle_fullscreen(),
    ),

    # Stack controls
    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),
    # Dmenu scripts launched with ALT + CTRL + KEY
    Key(["mod1", "control"], "e",
        lazy.spawn("./.dmenu/dmenu-edit-configs.sh"),
        desc='Dmenu script for editing config files'
        ),
    Key(["mod1", "control"], "m",
        lazy.spawn("./.dmenu/dmenu-sysmon.sh"),
        desc='Dmenu system monitor script'
        ),
    Key(["mod1", "control"], "p",
        lazy.spawn("passmenu"),
        desc='Passmenu'
        ),
    Key(["mod1", "control"], "r",
        desc='Dmenu reddio script'
        ),
    Key(["mod1", "control"], "s",
        lazy.spawn("./.dmenu/dmenu-surfraw.sh"),
        desc='Dmenu surfraw script'
        ),
    Key(["mod1", "control"], "t",
        lazy.spawn("./.dmenu/dmenu-trading.sh"),
        desc='Dmenu trading programs script'
        ),
    Key(["mod1", "control"], "i",
        lazy.spawn("./.dmenu/dmenu-scrot.sh"),
        desc='Dmenu scrot script'
        ),
    # My applications launched with SUPER + ALT + KEY
    Key([mod, "mod1"], "w",
        lazy.spawn("brave"),
        desc='brave browser'
        ),
    Key([mod, "mod1"], "v",
        lazy.spawn("vscodium"),
        desc='VScodium Code Editor'
        ),
    Key([mod, "mod1"], "r",
        lazy.spawn("$GFILE"),
        desc='GUI File Manager'
        ),
    Key([mod], "r",
        lazy.spawn("$TFILE"),
        desc='Terminal File Manager'
        ),
    Key([mod, "mod1"], "p",
        lazy.spawn("pamac-manager"),
        desc='GUI Package Manager'
        ),
    Key([mod, "mod1"], "e",
        lazy.spawn(myTerm+" -e neomutt"),
        desc='neomutt'
        ),
    Key([mod, "mod1"], "m",
        lazy.spawn(myTerm+" -e sh ./scripts/toot.sh"),
        desc='toot mastodon cli'
        ),
    Key([mod, "mod1"], "t",
        lazy.spawn(myTerm+" -e sh ./scripts/tig-script.sh"),
        desc='tig'
        ),
    Key([mod, "mod1"], "f",
        lazy.spawn(myTerm+" -e sh ./.config/vifm/scripts/vifmrun"),
        desc='vifm'
        ),
    Key([mod, "mod1"], "j",
        lazy.spawn(myTerm+" -e joplin"),
        desc='joplin'
        ),
    Key([mod, "mod1"], "c",
        lazy.spawn(myTerm+" -e cmus"),
        desc='cmus'
        ),
    Key([mod, "mod1"], "i",
        lazy.spawn(myTerm+" -e irssi"),
        desc='irssi'
        ),
    Key([mod, "mod1"], "y",
        lazy.spawn(myTerm+" -e youtube-viewer"),
        desc='youtube-viewer'
        ),
    Key([mod, "mod1"], "a",
        lazy.spawn(myTerm+" -e ncpamixer"),
        desc='ncpamixer'
        ),
]

group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'monadtall'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'monadtall'}),
               ("9", {'layout': 'monadtall'})
               ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.TreeTab(
    #     font="Ubuntu",
    #     fontsize=10,
    #     sections=["FIRST", "SECOND"],
    #     section_fontsize=11,
    #     bg_color="141414",
    #     active_bg="90C435",
    #     active_fg="000000",
    #     inactive_bg="384323",
    #     inactive_fg="a0a0a0",
    #     padding_y=5,
    #     section_top=10,
    #     panel_width=320
    # ),
    layout.Floating(**layout_theme)
]

# colors = [["#292d3e", "#292d3e"],  # panel background
#           ["#434758", "#434758"],  # background for current screen tab
#           ["#ffffff", "#ffffff"],  # font color for group names
#           ["#ff5555", "#ff5555"],  # border line color for current tab
#           ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
#           ["#668bd7", "#668bd7"],  # color for the even widgets
#           ["#e1acff", "#e1acff"]]  # window name

# Nord Color Theme
colors = [["#2e3440", "#2e3440"],  # nord0
          ["#3b4252", "#3b4252"],  # nord1
          ["#434c5e", "#434c5e"],  # nord2
          ["#4c566a", "#4c566a"],  # nord3
          ["#d8dee9", "#d8dee9"],  # nord4
          ["#e5e9f0", "#e5e9f0"],  # nord5
          ["#eceff4", "#eceff4"],  # nord6
          ["#8fbcbb", "#8fbcbb"],  # nord7
          ["#88c0d0", "#88c0d0"],  # nord8
          ["#81a1c1", "#81a1c1"],  # nord9
          ["#5e81ac", "#5e81ac"],  # nord10
          ["#bf616a", "#bf616a"],  # nord11
          ["#d08770", "#d08770"],  # nord12
          ["#ebcb8b", "#ebcb8b"],  # nord13
          ["#a3be8c", "#a3be8c"],  # nord14
          ["#b48ead", "#b48ead"]]  # nord15


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=14,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [

        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[6],
            background=colors[0]
        ),
        widget.GroupBox(font="JetBrains Mono",
                        fontsize=14,
                        margin_y=3,
                        margin_x=0,
                        padding_y=5,
                        padding_x=5,
                        borderwidth=3,
                        active=colors[6],
                        inactive=colors[6],
                        rounded=False,
                        highlight_color=colors[3],
                        highlight_method="block",
                        this_current_screen_border=colors[3],
                        this_screen_border=colors[0],
                        other_current_screen_border=colors[0],
                        other_screen_border=colors[0],
                        foreground=colors[6],
                        background=colors[0]
                        ),
        widget.Sep(
            linewidth=0,
            padding=190,
        ),
        
        widget.TextBox(
            text='',
            background=colors[0],
            foreground=colors[7],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" ",
            padding=0,
            foreground=colors[0],
            background=colors[7],
            fontsize=12
        ),
        widget.CPU(
            format='{load_percent}%',
            update_interval=1.0,
            foreground=colors[0],
            background=colors[7],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[7],
            foreground=colors[10],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=colors[0],
            background=colors[10],
            fontsize=11
        ),
        widget.ThermalSensor(
            foreground=colors[0],
            background=colors[10],
            padding=5,
            tag_sensor="tdie"
        ),
        widget.TextBox(
            text='',
            background=colors[10],
            foreground=colors[8],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" 🖬",
            foreground=colors[0],
            background=colors[8],
            padding=0,
            fontsize=14
        ),
        widget.Memory(
            foreground=colors[0],
            background=colors[8],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[8],
            foreground=colors[9],
            padding=0,
            fontsize=37
        ),
        widget.Net(
            interface="wlp2s0",
            format='{down} ↓↑ {up}',
            foreground=colors[0],
            background=colors[9],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[9],
            foreground=colors[7],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" Vol:",
            foreground=colors[0],
            background=colors[7],
            padding=0
        ),
        widget.Volume(
            foreground=colors[0],
            background=colors[7],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[7],
            foreground=colors[10],
            padding=0,
            fontsize=37
        ),
        widget.CurrentLayout(
            foreground=colors[0],
            background=colors[10],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[10],
            foreground=colors[8],
            padding=0,
            fontsize=37
        ),
        widget.Clock(
            foreground=colors[0],
            background=colors[8],
            format="%A, %B %d  [ %I:%M %p ]"
        ),

    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # Slicing removes unwanted widgets on Monitors 1,3
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # Monitor 2 will display all widgets in widgets_list
    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# @hook.subscribe.startup_once
# def start_once():
#     home = os.path.expanduser('~')
#     subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
