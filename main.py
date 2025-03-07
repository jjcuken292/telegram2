from telethon import TelegramClient, errors
import asyncio
import os
import time

# Налаштування змінних середовища
API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
PHONE_NUMBER = os.environ['PHONE_NUMBER']

# Список груп
GROUPS = ['@Crypto_Affiliate_eng', '@fortraffic', '@LeadsAreUs', '@affmktcity', '@affiliate_marketing_hub', '@blackhat_forever', '@wiseaffiliate', '@delta_fx_crypto_board', '@trafficforyou', '@enalltrafficgroupchat', '@looking_for_offers', '@dark_side_affiliate_offers', '@affhub_collab', '@affcommunity']

# Текст повідомлення
MESSAGE = """🚀 WHO NEEDS HIGH-QUALITY LIVE LEADS? 🚀
💰 Looking for fresh, real-time leads that actually convert? I’ve got top-tier traffic across multiple geos and flexible deals to match your needs. Whether you're after exclusive leads or high-intent traffic, I’ve got you covered! 💯

📌 Top countries I work with:

🇩🇪 Germany
🇫🇷 France
🇮🇹 Italy
🇪🇸 Spain
🇳🇱 Netherlands
🇸🇪 Sweden
🇳🇴 Norway
🇩🇰 Denmark
🇨🇭 Switzerland
🇬🇧 United Kingdom
🇧🇪 Belgium
🇦🇹 Austria
🇫🇮 Finland
🇵🇱 Poland
🇨🇿 Czech Republic
🇵🇹 Portugal
🇮🇪 Ireland
🇬🇷 Greece
🇸🇰 Slovakia
🇨🇦 Canada
🇦🇺 Australia

🔥 Let’s get started—DM me now for details! 📩💸"""  # Ваш текст

async def send_messages():
    client = TelegramClient('session_name', API_ID, API_HASH)
    try:
        # Авторизація через файл сесії
        await client.connect()
        
        if not await client.is_user_authorized():
            print("❌ Помилка: файл сесії не працює")
            return

        # Розсилка повідомлень
        for group in GROUPS:
            try:
                await client.send_message(group, MESSAGE)
                print(f"✅ Відправлено в {group}")
                await asyncio.sleep(10)
            except errors.FloodWaitError as e:
                print(f"⏳ Зачекайте {e.seconds} секунд...")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"🚨 Помилка: {str(e)}")

    except Exception as e:
        print(f"🔥 Критична помилка: {str(e)}")
    finally:
        await client.disconnect()

async def main():
    while True:
        await send_messages()
        print("⏳ Наступна розсилка через 1 годину...")
        await asyncio.sleep(3602)

if __name__ == '__main__':
    print("🚀 Запуск розсильника...")
    asyncio.run(main())
