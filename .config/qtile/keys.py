#!/usr/bin/env python3

from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension
from libqtile import layout, bar, widget, hook


import os

mod = "mod4"
alt = "mod1"
terminal = guess_terminal()

keys = [
Key([mod], "j", lazy.layout.down()),
Key([mod], "k", lazy.layout.up()),
Key([mod], "h", lazy.layout.left()),
Key([mod], "l", lazy.layout.right()),
Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
Key([mod, "control"], "j", lazy.layout.grow_down()),
Key([mod, "control"], "k", lazy.layout.grow_up()),
Key([mod, "control"], "h", lazy.layout.grow_left()),
Key([mod, "control"], "l", lazy.layout.grow_right()),
Key([mod], "Return", lazy.layout.toggle_split()),
Key([mod], "n", lazy.layout.normalize()),
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    Key([mod], "t", lazy.layout.toggle_split(),
        desc="Move focus up in stack pane"),
    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "Tab", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),

    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),

    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen"),

    # spawn programs

    Key([mod], "x", lazy.spawn("/home/drakula/.local/bin/fix_flick"),
        desc="toggle keyboard layout"),

    Key([mod], "g", lazy.spawn("alacritty -e toggle_keyboard"),
        desc="toggle keyboard layout"),

    # social app

    Key(
        [mod], "i",
        lazy.spawn('fix_flick'))
    ,
    Key(
        [mod, "shift"], "i",
        lazy.spawn("xset dpms force off")
    ),
    Key(
        [mod, "shift"], "f",
        lazy.window.toggle_floating()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),


]

run_programs = [
    Key([mod, "shift"], "b", lazy.spawn("brave"), desc="Spawn brave"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("emacsclient -create-frame --alternate-editor=\"\" "), desc="Spawn emacs"),
    Key([mod], "d", lazy.spawn("dmenu_run"), desc="Spawn dmenu"),
    Key([mod], "c", lazy.spawn("org-capture"), desc="Spawn org-capture"),

    Key([mod], "b", lazy.spawn("qutebrowser"), desc="Spawn qutebrowser"),

    Key([mod], "r", lazy.spawn("alacritty -e ranger"),
        desc="Spawn qutebrowser"),
]
spawn = [
    Key([], "f", lazy.spawn("ferdi"), desc="Spawn ferdi"),
    Key([], "b", lazy.spawn("brave"), desc="Spawn brave"),
    Key([], "d", lazy.spawn("discord"), desc="Spawn discord"),
    Key([], "p", lazy.spawn("pavucontrol"), desc="Spawn pavucontrol"),
    Key([], "t", lazy.spawn("teams"), desc="Spawn teams"),
    Key([], "c", lazy.spawn("kdeconnect"), desc="Spawn kde"),
    Key([], "v", lazy.spawn("viber"), desc="Spawn viber"),
]
kill = [
    Key([], "c", lazy.spawn("killall -KILL -r kdeconnect"), desc="Kill kdeconnect"),
    Key([], "s", lazy.spawn("killall -KILL -r shutter"), desc="Kill shutter"),
    Key([], "d", lazy.spawn("killall -KILL -r dropbox"), desc="Kill dropbox"),
]
shutter = [
    Key([], "f", lazy.spawn("shutter -f"), desc="Capture fullscreen"),
    Key([], "w", lazy.spawn("shutter -w"), desc="Capture window"),
    Key([], "a", lazy.spawn("shutter -a"), desc="Capture active window"),
    Key([], "s", lazy.spawn("shutter -s"), desc="Capture active window"),
]
power_m = [

    Key([], "s", lazy.spawn("shutdown now"), desc="Capture fullscreen"),
    Key([], "r", lazy.spawn("reboot"), desc="Capture fullscreen"),
]
xf86_keys = [
    KeyChord([mod], "s", spawn),
    KeyChord([mod], "k", kill),
    KeyChord([mod], "p", shutter),
    KeyChord([mod], "p", shutter),
    KeyChord([mod,"control"], "s", power_m),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pactl -- set-sink-volume 0 +5%"), desc="Increse volume"),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pactl -- set-sink-volume 0 -5%"), desc="Decrese volume"),
    Key([], "XF86AudioMute",
        lazy.spawn("pactl -- set-sink-mute 0 toggle"), desc="toggle mute"),

    Key(["shift"], "XF86AudioRaiseVolume",
        lazy.spawn("pactl -- set-source-volume alsa_input.pci-0000_05_00.6.analog-stereo +1%"),
        desc="Increse microfon boost"),
    Key(["shift"], "XF86AudioLowerVolume",
        lazy.spawn("pactl -- set-source-volume alsa_input.pci-0000_05_00.6.analog-stereo -1%"),
        desc="Decrese microfon boost"),

    Key(["shift"], "XF86AudioMute", lazy.spawn("mic_t_mute"),
        desc="toggle mute microfon"),


    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5"),
        desc="increse brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5"),
        desc="decrese brightness"),

    Key([], "XF86ScreenSaver", lazy.spawn("emacsclient -create-frame --alternate-editor=\"\" ")),
]
keys.extend(run_programs)
keys.extend(xf86_keys)
