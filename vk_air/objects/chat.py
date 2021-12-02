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
from typing import Optional, List

from vk_air.bot_api import BotApi
from vk_air.keyboard import Keyboard
from vk_air.objects.message import DeliveredMessage, Message
from vk_air.template import Template
from .group import Group
from .user import User

class Chat:
    """
    Беседа.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api: BotApi = api
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def admin_id(self) -> int:
        return self.obj.get('admin_id')
    
    @property
    def users(self) -> Optional[List[int]]:
        return self.obj.get('users')
    
    @property
    def photo_50(self) -> Optional[str]:
        return self.obj.get('photo_50')
    
    @property
    def photo_100(self) -> Optional[str]:
        return self.obj.get('photo_100')
    
    @property
    def photo_200(self) -> Optional[str]:
        return self.obj.get('photo_200')
    
    @property
    def icon(self) -> Optional[str]:
        return self.obj.get('photo_100')
    
    @property
    def left(self) -> bool:
        return True if self.obj.get('left') else False
    
    @property
    def kicked(self) -> bool:
        return True if self.obj.get('kicked') else False

    async def rename(self, title: str) -> bool:
        r = await self.api.messagesEditChat(chat_id=self.id, title=title)
        return True if r == 1 else False

    async def ban_member(self, member_id: int) -> bool:
        r = await self.api.messagesRemoveChatUser(chat_id=self.id, member_id=member_id)
        return True if r == 1 else False

    async def get_invite(self, reset: int = 0) -> Optional[str]:
        r = await self.api.messagesGetInviteLink(peer_id=self.id, reset=reset)
        return r
    
    async def unpin_message(self) -> bool:
        r = await self.api.messagesUnpin(peer_id=self.id)
        return True if r == 1 else False

    async def pin_message(self, message_id: int) -> Optional[Message]:
        r = await self.api.messagesPin(peer_id=self.id, message_id=message_id)
        return r

    async def send_message(
        self,
        text: str = None,
        *,
        peer_id: int = None,
        peer_ids: List[int] = None,
        lat: int = None,
        long: int = None,
        attachment: str = None,
        reply_to: int = None,
        forward_messages: int = None,
        sticker_id: int = None,
        keyboard: Keyboard = None,
        template: Template = None,
        payload: dict | str = None,
        content_source: dict = None,
        dont_parse_links: int = None,
        disable_mentions: int = None,
        intent: str = None,
        subscribe_id: int = None
    ) -> int | List[DeliveredMessage]:
        r = await self.api.messagesSend(
            text=text,
            peer_id=peer_id,
            peer_ids=peer_ids,
            lat=lat,
            long=long,
            attachment=attachment,
            reply_to=reply_to,
            forward_messages=forward_messages,
            sticker_id=sticker_id,
            keyboard=keyboard,
            template=template,
            payload=payload,
            content_source=content_source,
            dont_parse_links=dont_parse_links,
            disable_mentions=disable_mentions,
            intent=intent,
            subscribe_id=subscribe_id
        )
        return r
    
    async def edit_message(
        self,
        text: str = None,
        *,
        message_id: int,
        peer_id: int = None,
        lat: int = None,
        long: int = None,
        attachment: str = None,
        keyboard: Keyboard = None,
        template: Template = None,
        dont_parse_links: int = None,
        disable_mentions: int = None,
        keep_forward_messages: int = 1,
        keep_snippets: int = 1
    ) -> int | List[DeliveredMessage]:
        r = await self.api.messagesEdit(
            text=text,
            peer_id=peer_id,
            lat=lat,
            long=long,
            attachment=attachment,
            keyboard=keyboard,
            template=template,
            dont_parse_links=dont_parse_links,
            disable_mentions=disable_mentions,
            keep_forward_messages=keep_forward_messages,
            keep_snippets=keep_snippets,
            message_id=message_id
        )
        return r
    
class ChatMember:
    """
    Объект участника беседы.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def member_id(self) -> int:
        return self.obj.get('member_id')
    
    @property
    def invited_by(self) -> int:
        return self.obj.get('invited_by')
    
    @property
    def join_date(self) -> int:
        return self.obj.get('join_date')
    
    @property
    def is_admin(self) -> bool:
        return self.obj.get('is_admin')
    
    @property
    def can_kick(self) -> bool:
        return self.obj.get('can_kick')

class ChatMembers:
    """
    Список участников беседы.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def count(self) -> int:
        return self.obj.get('count')
    
    @property
    def items(self) -> Optional[List[ChatMember]]:
        memberlist = []
        memberlist.append(ChatMember(i) for i in self.obj.get('items'))
        return memberlist
    
    @property
    def profiles(self) -> Optional[List[User]]:
        profilelist = []
        profilelist.append(User(i) for i in self.obj.get('profiles'))
        return profilelist
    
    @property
    def groups(self) -> Optional[List[Group]]:
        grouplist = []
        grouplist.append(Group(i) for i in self.obj.get('groups'))
        return grouplist