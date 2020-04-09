from userbot.utils import register

@register(outgoing=True, pattern="^.me$")

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("I AM OUWNER OF EYE GANG /n/n IF ANY YOUR CHANNEL SO MAKE ME ADMIN IN POST PREMIUM ACCOUNT /n/n MY RULES /n/n * NO SEELING /n * NO PROMOTION /n * AND MORE RULES")
