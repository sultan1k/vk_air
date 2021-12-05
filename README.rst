vk_air
-------------

Фреймворк для VK API.

С помощью этого фреймворка можно написать бота для группы ВКонтакте. Фреймворк был сделан недавно, документация появится чуть позже.

Фреймворк устанавливается с помощью команды
.. code:: sh
      
    pip install vk_air

или

.. code:: sh
    
    pip install git+https://github.com/sultan1k/vk_air

Пару примеров с кодом:

.. code:: python
    
    from vk_air import Client
    from vk_air.utils import Utils
    
    bot = Client(prefix='!', debug=False)
    
    @bot.command(name='hi')
    async def hi(ctx):
      await ctx.send('Привет')
    
    @bot.event(name='chat_invite_user')
    async def add_me(ctx):
      if ctx.action.member_id == -bot.group.id:
        await ctx.send('Вы добавили меня в беседу!')
    
    @bot.command(name='whois')
    async def whois(ctx, user, *, reason):
      user = Utils().mention_to_id(user) # достаём из упоминания айди
      await ctx.send(f'Айди пользователя - {user}\nПричина вызова команды: {reason}')
      
    bot.login(token='TOKEN')
