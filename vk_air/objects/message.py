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
from __future__ import annotations
from typing import List, Optional
import json
from .geo import Geo

class MessageAction:
    """
    Сервисное действие с чатом.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def member_id(self) -> Optional[int]:
        return self.obj.get('member_id')
    
    @property
    def text(self) -> Optional[str]:
        return self.obj.get('text')
    
    @property
    def email(self) -> Optional[str]:
        return self.obj.get('email')
    
    @property
    def icon(self) -> Optional[str]:
        return self.obj['photo'].get('photo_200') if self.obj.get('photo') else None
    
class Message:
    """
    Объект личного сообщения.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api = api
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def peer_id(self) -> int:
        return self.obj.get('peer_id')
    
    @property
    def from_id(self) -> int:
        return self.obj.get('from_id')
    
    @property
    def text(self) -> str:
        return self.obj.get('text')
    
    @property
    def random_id(self) -> Optional[int]:
        return self.obj.get('random_id')
    
    @property
    def ref(self) -> Optional[str]:
        return self.obj.get('ref')
    
    @property
    def ref_source(self) -> Optional[str]:
        return self.obj.get('ref_source')
    
    @property
    def attachments(self) -> Optional[List]:
        attachment_list = []
        from enumsobj import ATTACHMENTS
        for i in self.obj.get('attachments'):
            cls = ATTACHMENTS[i['type']]
            attachment_list.append(cls(i))
        return attachment_list

    @property
    def important(self) -> bool:
        return self.obj.get('important')
    
    @property
    def geo(self) -> Optional[Geo]:
        return Geo(self.obj.get('geo')) if self.obj.get('geo') else None
    
    @property
    def payload(self) -> Optional[dict]:
        try:
            json.loads(self.obj.get('payload'))
        except:
            return None
        
    @property
    def fwd_messages(self) -> Optional[List[Message]]:
        fwdlist = []
        for i in self.obj.get('fwd_messages'):
            fwdlist.append(Message(i))
        return fwdlist
    
    @property
    def reply_message(self) -> Optional[Message]:
        return Message(self.obj.get('reply_message')) if self.obj.get('reply_message') else None

    @property
    def action(self) -> Optional[MessageAction]:
        return MessageAction(self.obj.get('action')) if self.obj.get('action') else None

    @property
    def admin_author_id(self) -> Optional[int]:
        return self.obj.get('admin_author_id')
    
    @property
    def conversation_message_id(self) -> Optional[int]:
        return self.obj.get('conversation_message_id')
    
    @property
    def is_cropped(self) -> bool:
        return self.obj.get('is_cropped')
    
    @property
    def memberscount(self) -> Optional[int]:
        return self.obj.get('members_count')
    
    @property
    def update_time(self) -> Optional[int]:
        return self.obj.get('update_time')
    
    @property
    def was_listened(self) -> bool:
        return self.obj.get('was_listened')
    
    @property
    def pinned_at(self) -> Optional[int]:
        return self.obj.get('pinned_at')
    
    @property
    def message_tag(self) -> Optional[str]:
        return self.obj.get('message_tag')
    
    # ниже только для бесед

    @property
    def chat_id(self) -> Optional[int]:
        return self.obj.get('chat_id')
    
    @property
    def chat_active(self) -> Optional[List[int]]:
        return self.obj.get('chat_active')
    
    @property
    def users_count(self) -> Optional[int]:
        return self.obj.get('users_count')
    
    @property
    def admin_id(self) -> Optional[int]:
        return self.obj.get('admin_id')
    
    @property
    def icon(self) -> Optional[str]:
        return self.obj.get('photo_200')
    
    async def unpin(self) -> bool:
        r = await self.api.messagesUnpin(peer_id=self.peer_id)
        return True if r == 1 else False

    async def pin(self) -> Optional[Message]:
        r = await self.api.messagesPin(peer_id=self.peer_id, message_id=self.id)
        return r

    async def send(
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
        keyboard = None,
        template = None,
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
    
    async def edit(
        self,
        text: str = None,
        *,
        lat: int = None,
        long: int = None,
        attachment: str = None,
        keyboard = None,
        template = None,
        dont_parse_links: int = None,
        disable_mentions: int = None,
        keep_forward_messages: int = 1,
        keep_snippets: int = 1
    ) -> int | List[DeliveredMessage]:
        r = await self.api.messagesEdit(
            text=text,
            peer_id=self.peer_id,
            lat=lat,
            long=long,
            attachment=attachment,
            keyboard=keyboard,
            template=template,
            dont_parse_links=dont_parse_links,
            disable_mentions=disable_mentions,
            keep_forward_messages=keep_forward_messages,
            keep_snippets=keep_snippets,
            message_id=self.id
        )
        return r

class DeletedMessages:
    """
    Объект удалённых сообщений.
    """
    def __init__(self, obj: dict):
        self.obj = obj
    
    def status(self, id: int) -> Optional[int]:
        """
        Посмотреть статус удалённого сообщения по его айди.
        """
        return self.obj.get(str(id))

class DeliveredMessage:
    """
    Объект отправленного сообщения. 

    Возвращается только при отправке сообщений
    с указанием peer_ids (т.е. нескольких
    отправителей).
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def peer_id(self) -> int:
        return self.obj.get('peer_id')
    
    @property
    def message_id(self) -> int:
        return self.obj.get('message_id')
    
    @property
    def conversation_message_id(self) -> Optional[int]:
        return self.obj.get('conversation_message_id')
    
    @property
    def error(self) -> Optional[str]:
        return self.obj.get('error')

class MessageEvent:
    """
    Объект нового ивента в сообщениях.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def peer_id(self) -> int:
        return self.obj.get('peer_id')
    
    @property
    def event_id(self) -> str:
        return self.obj.get('event_id')
    
    @property
    def payload(self) -> Optional[str | dict]:
        return self.obj['payload']['command'] if self.obj.get('payload') and self.obj['payload'].get('command') else self.obj.get('payload')
    
    async def show_snackbar(self, *, text: str) -> int:
        """
        Отображает всплывающее сообщение 
        у пользователя сверху (Android, iOS)
        или в левом нижнем углу (Desktop).
        """
        data = {
            'type': 'show_snackbar',
            'text': text
        }
        r = await self.api.messagesSendEventAnswer(
            event_id=self.event_id,
            user_id=self.user_id,
            peer_id=self.peer_id,
            event_data=data
        )
        return r
    
    async def open_link(self, *, link: str) -> int:
        """
        Открывает у пользователя сайт, ссылку
        на который вы отправили в этом методе.
        """
        data = {
            'type': 'open_link',
            'link': link
        }
        r = await self.api.messagesSendEventAnswer(
            event_id=self.event_id,
            user_id=self.user_id,
            peer_id=self.peer_id,
            event_data=data
        )
        return r
    
    async def open_app(self, *, app_id: int, owner_id: int = None, hash: str) -> int:
        """
        Открывает у пользователя приложение. 
        """
        data = {
            'type': 'open_app',
            'app_id': app_id,
            'hash': hash
        }
        if owner_id:
            data['owner_id'] = owner_id
        r = await self.api.messagesSendEventAnswer(
            event_id=self.event_id,
            user_id=self.user_id,
            peer_id=self.peer_id,
            event_data=data
        )
        return r
    
class UploadServer:
    """
    Объект данных для отправки вложения в ЛС.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def upload_url(self) -> str:
        return self.obj.get('upload_url')
    
    @property
    def album_id(self) -> Optional[int]:
        return self.obj.get('album_id')
    
    @property
    def group_id(self) -> Optional[int]:
        return self.obj.get('group_id')

class SavedMessagePhoto:
    """
    Объект загруженной фотографии.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def pid(self) -> int:
        return self.obj.get('pid')
    
    @property
    def aid(self) -> int:
        return self.obj.get('aid')
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('owner_id')
    
    @property
    def src(self) -> str:
        return self.obj.get('src')
    
    @property
    def src_big(self) -> Optional[str]:
        return self.obj.get('src_big')
    
    @property
    def src_small(self) -> Optional[str]:
        return self.obj.get('src_small')
    
    @property
    def created(self) -> int:
        return self.obj.get('created')
    
    @property
    def src_xbig(self) -> Optional[str]:
        return self.obj.get('src_xbig')
    
    @property
    def src_xxbig(self) -> Optional[str]:
        return self.obj.get('src_xxbig')

class UploadedMessagePhoto:
    """
    Объект фотографии, загруженной на сервер.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def server(self) -> int:
        return self.obj.get('server')
    
    @property
    def photo(self) -> str:
        return self.obj.get('photo')
    
    @property
    def hash(self) -> str:
        return self.obj.get('hash')