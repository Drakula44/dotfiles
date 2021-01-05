#!/usr/bin/env bash
set -euo pipefail


feh --bg-scale ~/home/images/bg/dracula.jpg &
picom &
syndaemon -K -i 0.5 -R -d &
/usr/lib/kdeconnectd & /usr/bin/kdeconnect-indicator &
~/.dropbox-dist/dropboxd &
shutter --min_at_startup &
