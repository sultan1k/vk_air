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
import asyncio
import sys
from asyncio.coroutines import iscoroutinefunction
from typing import List, Optional
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random
import base64
import string
from .longpoll import LongPoll
from .objects.group import Group
from .enums import EVENTS
from .bot_api import BotApi

class Client:
    """
    Объект основного бота.
    ------------

    Параметры
    ------------

    * prefix: :class:`str` - префикс бота.

    * debug: :class:`bool` - запустить
    бота в режиме отладки или нет. По умолчанию 
    запускается без режима отладки.
    """
    def __init__(self, *, prefix: str = '!', debug: bool = False) -> None:
        self.prefix = prefix
        self.debug = debug
        self.commands = {}
        self.events = EVENTS

    def event(
        self,
        *, 
        name: Optional[str] = None,
        users: Optional[List[int]] = None,
        cooldown: Optional[int] = None
    ) -> object:
        """
        Добавление события
        ---------------

        Функция позволяет добавить новое 
        событие. Перед запуском бота не забудьте 
        включить LongPoll в группе вк и включить передачу
        тех событий, которые хотите обрабатывать 
        с помощью бота.

        Параметры
        ---------------

        * name: :class:`str` - название события.

        * users: :class:`List[int]` - список пользователей,
        на которых будет реагировать бот (необязательно).

        * cooldown: :class:`int` - время (в секундах), 
        раз в которое пользователь сможет 
        влиять на событие (необязательно).
        """
        def wrap(func):
            if not iscoroutinefunction(func):
                print(f"\033[1m[\033[91mОШИБКА\033[97m] Функция {func.__name__} должна быть асинхронной\033[0m")
                sys.exit(1)
            _name = func.__name__ if not name else name
            if _name not in self.events:
                print(f"\033[1m[\033[91mОШИБКА\033[97m] События с названием \"{_name}\" не существует\033[0m")
                sys.exit(1)
            if func.__code__.co_argcount == 0 and func.__code__.co_kwonlycount == 0:
                print(f"\033[1m[\033[91mОШИБКА\033[97m] Функция {func.__name__} должна иметь как минимум один аргумент\033[0m")
                sys.exit(1)
            data = {'function': func}
            if users:
                data['users'] = users
            if cooldown:
                data['cooldown'] = cooldown
            self.events[_name].append(data)
            if self.debug:
                print(f"\033[1m[\033[92mУСПЕШНО\033[97m] Функция {func.__name__}, отвечающая за ивент {_name}, успешно зарегистрирована.\033[0m")
        return wrap
    
    def command(
        self, 
        *, 
        name: str = None, 
        aliases: List[str] = [],
        users: Optional[List[int]] = None,
        cooldown: Optional[int] = None
    ) -> object:
        """
        Добавление команды
        -------------------

        Функция позволяет добавить новую
        команду. Перед запуском бота не забудьте 
        включить LongPoll в группе вк и включить передачу
        события 'message_new'.

        Параметры
        -------------------

        * name: :class:`str` - название команды

        * aliases: :class:`List[str]` - названия, на которые
        команда тоже будет реагировать (необязательно).

        * users: :class:`List[int]` - список пользователей,
        которые смогут использовать команду (необязательно).

        * cooldown: :class:`int` - время (в секундах), раз
        в которое пользователь сможет вызывать
        команду (необязательно).
        """
        def wrap(func):
            if not iscoroutinefunction(func):
                print(f"\033[1m[\033[91mОШИБКА\033[97m] Функция {func.__name__} должна быть асинхронной\033[0m")
                sys.exit(1)
            _name = name if name else func.__name__
            if _name in self.commands:
                print(f"\033[1m[\033[91mОШИБКА\033[97m] Команда с именем {_name} уже существует\033[0m")
                sys.exit(1)
            data = {
                'function': func
            }
            if users:
                data['users'] = users
            if cooldown:
                data['cooldown'] = cooldown
            self.commands[_name] = data
            if self.debug:
                if self.debug:
                    print(f"\033[1m[\033[92mУСПЕШНО\033[97m] Функция {func.__name__}, отвечающая за команду {_name}, успешно зарегистрирована.\033[0m")
            for i in aliases:
                if i in self.commands:
                    print(
                        f"\033[1m[\033[91mОШИБКА\033[97m] Псевдоним команды с именем {i}, который вызывает оригинальную команду {func.__name__}, уже принадлежит другой функции.\033[0m")
                    sys.exit(1)
                self.commands[i] = data
        return wrap

    def login(self, *, token: str = None) -> None:
        """
        Запуск бота
        ------------

        Эта функция нужна для запуска бота. Её можно
        вызывать только в самом конце кода.

        Параметры
        ------------

        * token: :class:`str` - токен бота,
        полученный в настройках группы.
        """
        if not token:
            print("\033[1m[\033[91mОШИБКА\033[97m] Для запуска бота необходимо ввести токен\033[0m")
            sys.exit(1)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=32,
            salt=b'VKSALT',
            iterations=100000,
            backend=default_backend()
        )
        key_to_encrypt = base64.urlsafe_b64encode(kdf.derive(''.join(random.choices(string.ascii_uppercase + string.digits, k=10)).encode()))
        dangerous_f = Fernet(key_to_encrypt)
        encrypt_key = dangerous_f.encrypt(token.encode())
        self.api = BotApi(dangerous_f=dangerous_f, encrypt_key=encrypt_key, debug=self.debug)
        loop = asyncio.get_event_loop()
        self.group: Group = loop.run_until_complete(self.api.groupsGetById())[0]
        if self.group == []:
            print("\033[1m[\033[91mОШИБКА\033[97m] Введён неверный токен бота.\033[0m")
            sys.exit(1)
        if self.debug:
            print("\033[1m[\033[92mУСПЕШНО\033[97m] Бот успешно запущен.\033[0m")
        self.api.group_id = self.group.id
        self.longpoll: LongPoll = LongPoll(api=self.api, events=self.events, commands=self.commands, prefix=self.prefix)
        self.longpoll.connect()