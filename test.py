
import telegram
import asyncio

async def main(): #실행시킬 함수명 임의지정
    chat_id = 5925375596
    token = "6651535891:AAH8gDDZUjAMGVyw5ivhW58WW8FztZBsrbw"
    bot = telegram.Bot(token = token)
    await bot.send_message(chat_id,'드디어 성공했구나 오태식이!!!')

asyncio.run(main()) 