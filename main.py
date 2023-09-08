import telegram.ext as tg_ext
import tomllib

from handlers import setup_handlers


def main():
    with open("config.toml", "rb") as f:
        TOKEN = tomllib.load(f)["bot"]["token"]

    app = tg_ext.ApplicationBuilder().token(TOKEN).build()

    setup_handlers(app)

    app.run_polling()


if __name__ == "__main__":
    main()
