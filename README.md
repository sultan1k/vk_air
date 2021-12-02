# vk_air
Фреймворк для VK API.

С помощью этого фреймворка можно написать бота для группы во ВКонтакте.
Фреймворк был сделан недавно, документация появится чуть позже.

Фреймворк устанавливается с помощью команды
```
pip install vk-air
```
или
```
pip install git+https://github.com/sultan1k/vk_air
```

Пару примеров с кодом:

```python
from vk_air import Client
from vk_air.utils import Utils

bot = Client(prefix='!', debug=False)

@bot.command(name='hi')
async def hi(ctx):
  await ctx.send('Привет')
 
@bot.event(name='chat_invite_user')
async def add_me(ctx):
  if ctx.action.member_id == bot.group.id:
    await ctx.send('Вы добавили меня в беседу!')
    
@bot.command(name='whois')
async def kill(ctx, user, *, reason):
  utils = Utils()
  user = utils.mention_to_id(user) # достаём из упоминания айди
  await ctx.send(f'Айди пользователя - {user}\nПричина вызова команды: {reason}')
  
bot.login(token='TOKEN')
```
