import asyncio
from create_bot import bot, dp, scheduler
from handlers.start import start_router
# from asyncpg_lite import DatabaseManager

# from work_time.time_func import send_time_msg

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    # async with db_manager as manager:
    #     pass
    # db_manager = DatabaseManager(  db_url="postgresql://:@localhost:5432/bot_demo:1234/demo_telegram_bot", deletion_password="" )

if __name__ == "__main__":
    asyncio.run(main())