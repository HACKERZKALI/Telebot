from userbot.utils import register

@register(outgoing=True, pattern="^.group$")

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("This is my community.\n\n[Netflix Commix](http://t.me/netflix_coomix)\n\n[Eonarmy](http://t.me/eonarmy)\n\n[Eonarmy Bins](https://t.me/eonarmy_bins)\n\n[Eonarmy Network](http://t.me/eonarmy_network)")
