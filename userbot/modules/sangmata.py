from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError


@register(outgoing=True, pattern=r"^\.sa(?: |$)(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```Mohon Balas Ke Pesan Pengguna.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("```Balas Ke Pesan Pengguna Yang Sebenarnya.```")
        return
    await steal.edit("```𝑪𝒆𝒏𝒃𝒐𝒚 𝒃𝒖𝒌𝒂 𝒌𝒂𝒓𝒕𝒖 𝒂𝒏𝒂𝒌 𝒃𝒂𝒃𝒊 𝒊𝒏𝒊,𝒔𝒖𝒓𝒖𝒉 𝒔𝒊𝒂𝒑𝒂 𝒈𝒂𝒌 𝒔𝒆𝒑𝒊𝒍 𝒔𝒆𝒏𝒅𝒊𝒓𝒊😡..```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Mohon Unblock @sangmatainfo_bot Dan Coba Lagi```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit("```𝑪𝒆𝒏𝒃𝒐𝒚 𝒕𝒊𝒅𝒂𝒌 𝒅𝒂𝒑𝒂𝒕 𝒎𝒆𝒏𝒆𝒎𝒖𝒌𝒂𝒏 𝒔𝒆𝒑𝒊𝒍𝒂𝒏,𝒂𝒏𝒂𝒌 𝒃𝒂𝒃𝒊 𝒈𝒂 𝒑𝒆𝒓𝒏𝒂𝒉 𝒈𝒂𝒏𝒕𝒊 𝒏𝒂𝒎𝒂😡```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`𝑪𝒆𝒏𝒃𝒐𝒚 𝒔𝒆𝒅𝒂𝒏𝒈 𝒕𝒊𝒅𝒂𝒌 𝒃𝒊𝒔𝒂 𝒏𝒚𝒆𝒑𝒊𝒍 𝒏𝒂𝒎𝒂(𝒆𝒓𝒓𝒐𝒓❜)🥵`")


CMD_HELP.update({
    "sangmata":
        "`.sa`\
          \nUsage: Mendapatkan Riwayat Nama Pengguna."
})
