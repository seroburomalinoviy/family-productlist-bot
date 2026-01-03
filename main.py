from os import environ
import telegram.ext as tg_ext
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

from handlers import setup_handlers


def main():
    TOKEN = environ.get("TOKEN_BOT")

    logger.info('Start bot')

    app = tg_ext.ApplicationBuilder().token(TOKEN).build()

    setup_handlers(app)

    app.run_polling()


if __name__ == "__main__":
    main()
