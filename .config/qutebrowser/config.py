# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Require a confirmation before quitting the application.
# Type: ConfirmQuit
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a confirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ['multiple-tabs', 'downloads']

# Backend to use to display websites. qutebrowser supports two different
# web rendering engines / backends, QtWebEngine and QtWebKit (not
# recommended). QtWebEngine is Qt's official successor to QtWebKit, and
# both the default/recommended backend. It's based on a stripped-down
# Chromium and regularly updated with security fixes and new features by
# the Qt project: https://wiki.qt.io/QtWebEngine QtWebKit was
# qutebrowser's original backend when the project was started. However,
# support for QtWebKit was discontinued by the Qt project with Qt 5.6 in
# 2016. The development of QtWebKit was picked up in an official fork:
# https://github.com/qtwebkit/qtwebkit - however, the project seems to
# have stalled again. The latest release (5.212.0 Alpha 4) from March
# 2020 is based on a WebKit version from 2016, with many known security
# vulnerabilities. Additionally, there is no process isolation and
# sandboxing. Due to all those issues, while support for QtWebKit is
# still available in qutebrowser for now, using it is strongly
# discouraged.
# Type: String
# Valid values:
#   - webengine: Use QtWebEngine (based on Chromium - recommended).
#   - webkit: Use QtWebKit (based on WebKit, similar to Safari - many known security issues!).
c.backend = 'webengine'

# Turn on Qt HighDPI scaling. This is equivalent to setting
# QT_AUTO_SCREEN_SCALE_FACTOR=1 or QT_ENABLE_HIGHDPI_SCALING=1 (Qt >=
# 5.14) in the environment. It's off by default as it can cause issues
# with some bitmap fonts. As an alternative to this, it's possible to
# set font sizes and the `zoom.default` setting.
# Type: Bool
c.qt.highdpi = False

# Automatically start playing `<video>` elements.
# Type: Bool
c.content.autoplay = False

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
c.content.headers.accept_language = 'pt-BR;en-US,en;q=0.9'

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# When to send the Referer header. The Referer header tells websites
# from which website you were coming from when visiting them. No restart
# is needed with QtWebKit.
# Type: String
# Valid values:
#   - always: Always send the Referer.
#   - never: Never send the Referer. This is not recommended, as some sites may break.
#   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
c.content.headers.referer = 'same-domain'

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
c.content.images = True

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Allow JavaScript to open new tabs without user interaction.
# Type: Bool
c.content.javascript.can_open_tabs_automatically = True

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow websites to record audio.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.media.audio_capture', True, 'https://teams.microsoft.com')

# Allow websites to record video.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.media.video_capture', True, 'https://teams.microsoft.com')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', True, 'https://www.deezer.com')

# Enable plugins in Web pages.
# Type: Bool
c.content.plugins = True

# Allow websites to register protocol handlers via
# `navigator.registerProtocolHandler`.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')

# Editor (and arguments) to use for the `edit-*` commands. The following
# placeholders are defined:  * `{file}`: Filename of the file to be
# edited. * `{line}`: Line in which the caret is found in the text. *
# `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['kitty', '-e', 'nvim', '-f', '{}']

# CSS border value for hints.
# Type: String
c.hints.border = '1px solid #24292E'

# Leave insert mode when starting a new page load. Patterns may be
# unreliable on this setting, and they may match the url you are
# navigating to, or the URL you are navigating from.
# Type: Bool
c.input.insert_mode.leave_on_load = False

# Include hyperlinks in the keyboard focus chain when tabbing.
# Type: Bool
c.input.links_included_in_focus_chain = False

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = False

# Padding (in pixels) for the statusbar.
# Type: Padding
c.statusbar.padding = {'top': 6, 'right': 8, 'bottom': 6, 'left': 8}

# Open new tabs (middleclick/ctrl+click) in the background.
# Type: Bool
c.tabs.background = True

# Scaling factor for favicons in the tab bar. The tab size is unchanged,
# so big favicons also require extra `tabs.padding`.
# Type: Float
c.tabs.favicons.scale = 1.4

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {'top': 6, 'right': 8, 'bottom': 6, 'left': 8}

# Width (in pixels) of the progress indicator (0 to disable).
# Type: Int
c.tabs.indicator.width = 1

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
# multiple times.  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://www.google.com/search?&q={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://www.google.com.br/'

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#f8f8f2'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#24292E'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#24292E'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#f8f8f2'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#24292E'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#24292E'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#24292E'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#f8f8f2'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#555555'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#44475a'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#44475a'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#7DF059'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#f8f8f2'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#24292E'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#24292E'

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = '#2B5546'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#595959'

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'rgb'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#ff5555'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#24292E'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#00BFFF'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#24292E'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#FFFFFF'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#bd93f9'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#44475a'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#24292E'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#ff5555'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#24292E'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#24292E'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#ff5555'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#24292E'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#24292E'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#f9ebb0'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#24292E'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#24292E'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#8be9fd'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '1px solid #24292E'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#24292E'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#44475a'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#f8f8f2'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#24292E'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#ffffff'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#181920'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#ffb86c'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#24292E'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#e0e0e0'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#24292E'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#00FF7F'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#24292E'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#e0e0e0'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#24292E'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#ffb86c'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#24292E'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#ffb86c'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#24292E'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#24292E'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#f8f8f2'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#ff5555'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#8be9fd'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#50fa7b'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#50fa7b'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#f1fa8c'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#24292E'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#ffb86c'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#50fa7b'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#ff5555'

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#f8f8f2'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#24292E'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#f8f8f2'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#24292E'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#f8f8f2'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#4B7251'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#f8f8f2'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#4B7251'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '12pt FiraCode Nerd Font'

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = '12pt FiraCode Nerd Font'

# Font used for the debugging console.
# Type: Font
c.fonts.debug_console = '10pt monospace'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '10pt FiraCode Nerd Font'

# Font used for the hints.
# Type: Font
c.fonts.hints = '12pt FiraCode Nerd Font'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '10pt FiraCode Nerd Font'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '10pt FiraCode Nerd Font'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '10pt FiraCode Nerd Font'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '10pt monospace'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '12pt FiraCode Nerd Font'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '12pt FiraCode Nerd Font'

# Font used for selected tabs.
# Type: Font
c.fonts.tabs.selected = '12pt FiraCode Nerd Font'

# Font used for unselected tabs.
# Type: Font
c.fonts.tabs.unselected = '12pt FiraCode Nerd Font'

# Font family for standard fonts.
# Type: FontFamily
c.fonts.web.family.standard = ''

# Font family for fixed fonts.
# Type: FontFamily
c.fonts.web.family.fixed = ''

# Font family for serif fonts.
# Type: FontFamily
c.fonts.web.family.serif = ''

# Font family for sans-serif fonts.
# Type: FontFamily
c.fonts.web.family.sans_serif = ''

# Font family for cursive fonts.
# Type: FontFamily
c.fonts.web.family.cursive = ''

# Font family for fantasy fonts.
# Type: FontFamily
c.fonts.web.family.fantasy = ''

# Default font size (in pixels) for regular text.
# Type: Int
c.fonts.web.size.default = 16

# Default font size (in pixels) for fixed-pitch text.
# Type: Int
c.fonts.web.size.default_fixed = 13

# Hard minimum font size (in pixels).
# Type: Int
c.fonts.web.size.minimum = 0

# Minimum logical font size (in pixels) that is applied when zooming
# out.
# Type: Int
c.fonts.web.size.minimum_logical = 6

# Bindings for normal mode
config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('m', 'spawn mpv {url}')
