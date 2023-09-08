from abc import ABC, abstractmethod

import telegram as tg
import telegram.ext as tg_ext
import logging

import messages

logger = logging.getLogger(__name__)

class BaseHandler(ABC):
    def __init__(self):
        self.user = None
        self.message = None

    async def __call__(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        self.user = update.effective_user
        self.message = messages.ChannelMessages()
        await self.handle(update, context)

    @abstractmethod
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE):
        pass


class StartHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("привет чудик")


class ChannelMessageHandler_products(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE):
        markup = tg.InlineKeyboardMarkup([[tg.InlineKeyboardButton('markall', callback_data='markall')]])
        message = update.channel_post.edit_text(self.message.edit(update.channel_post.text), parse_mode='MarkdownV2', reply_markup=markup)
        await message


class ChannelMessageHandler_markall_button(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE):
        await update.callback_query.answer()
        await update.callback_query.delete_message()

def setup_handlers(app):
    app.add_handler(tg_ext.CommandHandler("start", StartHandler()))
    app.add_handler(tg_ext.MessageHandler(tg_ext.filters.Regex('^п|Продукты') & ~tg_ext.filters.COMMAND, ChannelMessageHandler_products()))
    app.add_handler(tg.ext.CallbackQueryHandler(ChannelMessageHandler_markall_button(), pattern='markall'))