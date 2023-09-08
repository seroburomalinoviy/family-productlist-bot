import telegram.ext as tg_ext
import tomllib
import logging

logging.basicConfig(filename='bot.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

from handlers import setup_handlers


def main():
    with open("config.toml", "rb") as f:
        TOKEN = tomllib.load(f)["bot"]["token"]

    logger.info('Start bot')

    app = tg_ext.ApplicationBuilder().token(TOKEN).build()

    setup_handlers(app)

    app.run_polling()


if __name__ == "__main__":
    main()
