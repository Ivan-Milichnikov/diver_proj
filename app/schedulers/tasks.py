from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

async def next_day(id,text):
    await bot.send_message(id,text)

async def next_two_weeks(id,text):
    await bot.send_message(id,text)

async def next_month(id,text):
    await bot.send_message(id,text)

async def next_two_months(id,text):
    await bot.send_message(id,text)

async def next_three_months(id,text):
    await bot.send_message(id,text)

async def next(id,text):
    await bot.send_message(id,text)



