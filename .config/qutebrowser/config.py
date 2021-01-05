import dracula.draw

# Load existing settings made via :set
# config.load_autoconfig()

# Font
c.fonts.default_family = 'BreezeSans'
c.fonts.default_size = '9pt'

# Improved find
# config.bind('f', 'hint links spawn urlhandler {hint-url}')
# config.bind('F', 'hint links spawn urlhandler -t {hint-url}')

# Load theme
dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})

# config.set("colors.webpage.darkmode.enabled", True)

# config.set("statusbar.show", "never")

config.bind(";;", 'hint links spawn mpv {hint-url}')
config.bind("xb", 'config-cycle statusbar.show always never')



c.url.searchengines = {
        'DEFAULT' :    'https://google.com/search?q={}',
        'd'       :    'https://duckduckgo.com/?q={}',
        'gh'      :    'https://github.com/search?q={}',
        'yt'      :    'https://youtube.com/results?search_query={}',
        're'      :    'https://www.reddit.com/search/?q={}',
        'aw'      :    'https://wiki.archlinux.org/index.php/{}',
        'tpb'     :    'https://thepiratebay.org/index.php?q=b{}',
        '4'       :    'https://boards.4chan.org/{}/',
        'tr'      :    'https://translate.google.com/#en/sr/{}',
        'sh'      :    'https://sci-hub.tw/{}',
        'r'       :    'https://www.reddit.com/r/{}',
        'wa'      :    'https://www.wolframalpha.com/input/?i={}',
        'w'       :    'http://wttr.in/{}',
        'tw'      :    'https://www.thinkwiki.org/wiki/{}',
}

config.unbind('d')
config.unbind('m')

config.unbind('K')
config.unbind('J')


config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('ge', 'open https://mail.google.com/mail/u/0/#inbox')
config.bind('gm', 'open https://www.facebook.com/messages/t/')
config.bind('gi', 'open https://www.instagram.com/?hl=en')
config.bind('gd', 'open https://drive.google.com/drive/my-drive')
config.bind('gw', 'open https://web.whatsapp.com/')
config.bind('gy', 'open https://www.youtube.com/')
config.bind('gK', 'open https://kissanime.ru/')
config.bind('gh', 'open https://github.com/Drakula44')


config.bind('1', 'tab-focus 1')
config.bind('2', 'tab-focus 2')
config.bind('3', 'tab-focus 3')
config.bind('4', 'tab-focus 4')
config.bind('5', 'tab-focus 5')
config.bind('6', 'tab-focus 6')
config.bind('7', 'tab-focus 7')
config.bind('8', 'tab-focus 8')
config.bind('9', 'tab-focus 9')
config.bind('0', 'tab-focus -1')

c.content.host_blocking.lists.append( str(config.configdir) + "/blockedHosts")
