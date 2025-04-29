import asyncio
import asyncpg 
from create_bot import bot, dp, scheduler
from handlers.start import start_router
from decouple import config
# from asyncpg_lite import DatabaseManager

# from work_time.time_func import send_time_msg

async def main():
    
    host = config('HOST')
    port = config('PORT')
    user = config('USER')
    password = config('PASSWORD')
    database = config('DB_NAME')
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    # await conn = asyncpg.connect(user=config("USER"), password=config("PASSWORD"),
    #                              database=config("DATABASE"), host=config("HOST"), port=config("port"), timeout=120)

if __name__ == "__main__":
    asyncio.run(main())