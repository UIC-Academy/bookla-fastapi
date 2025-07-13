import asyncio


async def write_notification(email: str, message=""):
    await asyncio.sleep(3)
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)
