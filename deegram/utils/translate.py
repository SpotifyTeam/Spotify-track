VERSION = "5.0.0"
CREATOR = "@masterolic"
BOT_NAME = "Spotify Downloa"
DONATE = "https://t.me/spotify_downloa"
WELCOME_MSG = (
    f"🎶🎵 Welcome to {BOT_NAME} 🎵🎶\n\n"
    "I can help you search 🔍, listen 🎧 and download 📱 songs easily using Spotify URLs and custom queries! You can directly send Spotify URLs of tracks, playlists and albums to download them.\n---\n\nUse Help to know about command usage.."
)
INFO_MSG = (
    f"👤 Creator: {CREATOR}\n"
    f"ℹ Version: {VERSION}\n"
    f"🍩 Donate: {DONATE}"
)
STATS_MSG = (
    "**Bot Uptime:** {}\n"
    "**Total Disk Space:** {}\n"
    "**Used:** {} "
    "**Free:** {}\n\n"
    "📊Data Usage📊\n**Upload:** {}\n"
    "**Download:** {}\n\n"
    "**CPU:** {}\n"
    "**RAM:** {}\n"
    "**DISK:** {}"
)
HELP_MSG = (
    "Search by Album or Track or just send me a Deezer Track or Album link and I will download it for you 🙂\n\n"
    "**List of all commands:**\n"
    "/start - Get the welcome message\n"
    "/help - Get this message\n"
    "/settings - Change your preferences\n"
    "/info - Get some useful information about the Bot\n"
    "/stats - Get some statistics about the Bot\n"
)
DOWNLOAD_MSG = "⏳"
UPLOAD_MSG = "⏳"
END_MSG = "Finished."
ALBUM_MSG = (
    "💽 Album: {}\n"
    "👤 Artist: {}\n"
    "📅 Date: {}\n"
    "🎧 Total tracks: {}"
)
TRACK_MSG = (
    "🎧 Track: {}\n"
    "👤 Artist: {}\n"
    "💽 Album: {}\n"
    "📅 Date: {}"
)
CHOOSE = "Choose:"
SEARCH_ALBUM = "Search Album 💽"
SEARCH_TRACK = "Search Track 🎧"
Start_inline_search_buttons = (
    [Button.url("OWNER", url_owner),
    [Button.url("OWNER", url_channe)]
    [Button.switch_inline(translate.SEARCH_TRACK),
     Button.switch_inline(translate.SEARCH_ALBUM, query=".a ")],
    [Button.inline('❌')])
