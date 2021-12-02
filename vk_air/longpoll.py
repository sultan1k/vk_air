"""
MIT License

Copyright (c) 2021 sultan1k

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from types import NoneType
from .bot_api import BotApi
import asyncio
import sys
from aiohttp import ClientSession
from .enums import CLASSES

class LongPoll:
    """
    Объект LongPoll
    ---------------

    LongPoll позволяет получать данные о новых событиях 
    с помощью «длинных запросов». 
    Сервер получает запрос, но отправляет ответ на него не 
    сразу, а лишь тогда, когда произойдет какое-либо событие 
    (например, придёт новое сообщение), либо истечет заданное 
    время ожидания.

    Параметры
    ----------------

    * ts: :class:`int` - значение ts, которое 
    обновляется с каждым новым событием.

    * key: :class:`str` - ключ LongPoll.

    * server: :class:`str` - адрес LongPoll сервера.

    * events: :class:`dict` - словарь, содержащий 
    события.

    * commands: :class:`dict` - словарь, содержащий 
    команды.

    * collector: :class:`List[dict]` - список, 
    содержащий словари с событиями, которые
    ожидаются ботом.

    * worker: :class:`bool` - флаг, необходимый для
    выключения/включения отслеживания событий.
    """
    def __init__(self, *, api, events, commands, prefix) -> None:
        self.api: BotApi = api
        self.events = events
        self.commands = commands
        self.ts = None
        self.key = None
        self.server = None
        self.worker = True
        self.collector = []
        self.prefix = prefix

    async def update(self) -> None:
        r = await self.api.groupsGetLongPollServer()
        if type(r) == NoneType:
            print("\033[1m[\033[94mОШИБКА LONGPOLL\033[97m] Не удалось получить данные для подключения к LongPoll.\033[0m")
            sys.exit(1)
        self.ts = r.ts
        self.key = r.key
        self.server = r.server

    async def collecting(self, updates):
        for update in updates:
            for collection in self.collector:
                if update['type'] == 'message_new' and update['type'] == collection['event']:
                    compare1 = set(collection['object'].keys())
                    compare2 = set(update['object']['message'].keys())
                    shared = compare1.intersection(compare2)
                    if len(set(i for i in shared if collection['object'][i] == update['object']['message'][i])) == len(collection['object']):
                        future = collection['future']
                        _update = await self.to_class(update['type'], update)
                        future.set_result(_update)
                        self.collector.remove(collection)
                elif update['type'] == collection['event']:
                    compare1 = set(collection['object'].keys())
                    compare2 = set(update['object'].keys())
                    shared = compare1.intersection(compare2)
                    if len(set(i for i in shared if collection['object'][i] == update['object'][i])) == len(collection['object']):
                        future = collection['future']
                        _update = await self.to_class(update['type'], update)
                        future.set_result(_update)
                        self.collector.remove(collection)
    
    async def post(self, *, name, object):
        cls = CLASSES[name]
        cls = cls(object, self.api)
        loop = asyncio.get_event_loop()
        for obj in self.events[name]:
            func = obj['function']
            loop.create_task(func(cls))
        if name == 'message_new':
            if cls.text.startswith(self.prefix):
                command = cls.text[len(self.prefix):]
                text = command.split(' ', 1)
                command = text[0]
                if command in self.commands:
                    func = self.commands[command]['function']
                    if func.__code__.co_argcount == 0:
                        loop.create_task(func(cls))
                    else:
                        args = text[1:][0].split()
                        kwargs = {}
                        loop = asyncio.get_event_loop()
                        names = func.__code__.co_varnames
                        if func.__code__.co_kwonlyargcount == 0:
                            loop.create_task(func(cls, *args))
                        else:
                            ln = args[func.__code__.co_argcount-func.__code__.co_kwonlyargcount:]
                            _kw = ' '.join(ln)
                            args = args[:-(len(ln))]
                            kwargs[names[(func.__code__.co_argcount+func.__code__.co_kwonlyargcount)-1]] = _kw
                            loop.create_task(func(cls, *args, **kwargs))

    async def load(self, update):
        if update['type'] == 'message_new':
            if update['object']['message'].get('action'):
                await self.post(name=update['object']['message']['action']['type'], object=update['object']['message'])
            else:
                await self.post(name=update['type'], object=update['object']['message'])
        else:
            await self.post(name=update['type'], object=update['object'])
    
    async def check(self) -> None:
        fields = {
            'act': 'a_check',
            'key': self.key,
            'ts': self.ts,
            'wait': 25
        }
        async with ClientSession() as session:
            async with session.get(url=self.server, params=fields) as r:
                r = await r.json()
            await session.close()
        try:
            self.ts = r['ts']
            updates = r['updates']
            if self.api.debug:
                print(f"\033[1m[\033[93mLONGPOLL\033[97m] Получен ответ от LongPoll.\033[0m")
            loop = asyncio.get_event_loop()
            loop.create_task(self.collecting(updates))
            for update in updates:
                loop.create_task(self.load(update))
        except KeyError:
            print(f"\033[1m[\033[94mОШИБКА LONGPOLL\033[97m] Сервер прислал ответ: \"{r}\"\033[0m")
            await asyncio.sleep(0.1)
            print(f"\033[1m[\033[93mLONGPOLL\033[97m] Пытаюсь переподключиться к серверу...\033[0m")
            await self.update()
            print(f"\033[1m[\033[93mLONGPOLL\033[97m] Подключение восстановлено.\033[0m")
    
    def connect(self) -> None:
        loop = asyncio.get_event_loop()
        if self.api.debug:
            print(f"\033[1m[\033[93mLONGPOLL\033[97m] Пытаюсь переподключиться к серверу...\033[0m")
        r = loop.run_until_complete(self.api.groupsGetLongPollServer())
        if type(r) == NoneType:
            print("\033[1m[\033[94mОШИБКА LONGPOLL\033[97m] Не удалось получить данные для подключения к LongPoll.\033[0m")
            sys.exit(1)
        if self.api.debug:
            print(f"\033[1m[\033[93mLONGPOLL\033[97m] Подключение прошло успешно.\033[0m")
        self.ts = r.ts
        self.key = r.key
        self.server = r.server
        while self.worker:
            if self.api.debug:
                print(f"\033[1m[\033[93mLONGPOLL\033[97m] Слушаю LongPoll...\033[0m")
            loop.run_until_complete(self.check())
    
    def stop(self) -> None:
        self.worker = False

    
