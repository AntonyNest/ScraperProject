from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from itscraperbot.config import TOKEN
from itscraperbot.scraper.work_ua import scrape_work_ua
import itscraperbot.database as db

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db.init_db()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to ITScraperBot! Use /search <keyword> to find IT jobs.")

@dp.message_handler(commands=['search'])
async def search_jobs(message: types.Message):
    keyword = message.get_args()
    if not keyword:
        await message.reply("Please provide a keyword for searching.")
        return

    await message.reply(f"Searching for jobs with keyword: {keyword}...")
    jobs = scrape_work_ua(keyword)
    response = "\n\n".join([f"{job['title']}\n{job['salary']}\n{job['location']}\n{job['link']}" for job in jobs])

    for job in jobs:
        conn = sqlite3.connect("jobs.db")
    conn = db.init_db()

    await message.reply(response if response else "No jobs found.")

if __name__ == '__main__':