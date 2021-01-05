#!/usr/bin/env python3

from libqtile import bar, layout, widget

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

            # [
            #     widget.CurrentLayout(),
            #     widget.GroupBox(disable_drag = True),
            #     widget.Prompt(),
            #     widget.WindowName(),
            #     widget.Chord(
            #         chords_colors={
            #             'launch': ("#ff0000", "#ffffff"),
            #         },
            #         name_transform=lambda name: name.upper(),
            #     ),
            #     widget.Systray(),
            #     widget.CPU(background=alt_color),
            #     widget.CPUGraph(),
            #     widget.ThermalSensor(background=alt_color),
            #     widget.Battery(),
            #     widget.Memory(background=alt_color),
            #     widget.MemoryGraph(background=alt_color),
            #     widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            #     widget.Pomodoro(background=alt_color),
            #     widget.KeyboardLayout(configured_keyboards=['us','hr'])
            # ],
widgets_list = [
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[6],
                        background = colors[0]
                        ),
               widget.GroupBox(font="Ubuntu Regular",
                               fontsize=11,
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
                        linewidth = 0,
                        padding = 40,
                        ),
               widget.WindowName(
                        foreground = colors[14],
                        background = colors[0],
                        padding = 0
                        ),
               widget.Systray(
                        foreground = colors[14],
                        background = colors[0],
                        padding = 0
               ),
               widget.TextBox(
                        text='',
                        background = colors[0],
                        foreground = colors[7],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                        text=" ",
                        padding = 0,
                        foreground=colors[0],
                        background=colors[7],
                        fontsize=12
                        ),
               widget.CPU(
                        format='CPU {freq_current}GHz {load_percent}%',
                        update_interval=1.0,
                        foreground=colors[0],
                        background=colors[7],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[7],
                        foreground = colors[10],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                        text=" 🌡",
                        padding = 2,
                        foreground=colors[0],
                        background=colors[10],
                        fontsize=11
                        ),
               widget.ThermalSensor(
                        foreground=colors[0],
                        background=colors[10],
                        padding = 5,
                        tag_sensor = "Tdie"
                        ),
               widget.TextBox(
                        text='',
                        background = colors[10],
                        foreground = colors[8],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                        text=" 🖬",
                        foreground=colors[0],
                        background=colors[8],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Memory(
                        foreground = colors[0],
                        background = colors[8],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[8],
                        foreground = colors[9],
                        padding=0,
                        fontsize=37
                        ),
               widget.Net(
                        interface = "enp2s0",
                        format = '{down} ↓↑ {up}',
                        foreground = colors[0],
                        background = colors[9],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[9],
                        foreground = colors[7],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                       text=" Vol:",
                        foreground=colors[0],
                        background=colors[7],
                        padding = 0
                        ),
               widget.Volume(
                        foreground = colors[0],
                        background = colors[7],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[7],
                        foreground = colors[10],
                        padding=0,
                        fontsize=37
                        ),
               widget.CurrentLayout(
                        foreground = colors[0],
                        background = colors[10],
                        padding = 5
                        ),

               widget.TextBox(
                        text='',
                        background = colors[10],
                        foreground = colors[9],
                        padding=0,
                        fontsize=37
                        ),
               widget.Battery(
                        background = colors[9],
                        foreground = colors[0],
                        padding = 5
               ),
               widget.TextBox(
                        text='',
                        background = colors[9],
                        foreground = colors[8],
                        padding=0,
                        fontsize=37
                        ),
               widget.Clock(
                        foreground = colors[0],
                        background = colors[8],
                        format="%A, %B %d  [ %I:%M %p ]"
                        ),
              ]
