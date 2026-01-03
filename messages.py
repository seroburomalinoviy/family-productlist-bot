from abc import ABC, abstractmethod


from trigger_words import start_purchases


class BaseCommands(ABC):
    @abstractmethod
    async def start(self):
        pass

    @abstractmethod
    async def help(self):
        pass

    @abstractmethod
    async def cancel(self):
        pass


class ChannelCommands(BaseCommands):
    async def start(self):
        return "Привет, я твой личный секретарь в канале Мы!\nМоя задача составлять списки покупок."

    async def help(self):
        return f"Напиши в канал сообщение которое будет начинаться с {', '.join(start_purchases)}, на каждой новой строчке запиши продукт, отправсь это сообщение в канал и ты увидишь супер список!."

    async def cancel(self):
        pass

    async def mark_as_done(self):
        pass

    async def mark_as_undone(self):
        pass

    async def del_productlist(self):
        pass


class PersonalCommands(BaseCommands):
    async def start(self):
        return "Привет."

    async def help(self):
        return "Напиши мне @sergeevid"

    async def cancel(self):
        return "Отмена"


class BaseMessages(ABC):
    @abstractmethod
    async def edit(self, text: str) -> str:
        pass


class ChannelMessages(BaseMessages):
    def edit(self, text: str):
        txt = text.split("\n")[1:]
        template = """Нужно купить:\n\n"""
        for i in txt:
            template += f"- {i.capitalize()}\n"
        template += "\n#список_покупок"

        return template
