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
from typing import List, Optional
from .group import Group
from .user import User
from .message import Message

class ConversationPeer:
    """
    Информация о собеседнике.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def local_id(self) -> int:
        return self.obj.get('local_id')
    
class ConversationPermissions:
    """
    Может ли пользователь писать в диалог.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def allowed(self) -> bool:
        return self.obj.get('allowed')
    
    @property
    def reason(self) -> Optional[int]:
        return self.obj.get('reason')
    
class ConversationSessings:
    """
    Настройки диалога.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def members_count(self) -> Optional[int]:
        return self.obj.get('members_count')
    
    @property
    def title(self) -> Optional[str]:
        return self.obj.get('title')
    
    @property
    def pinned_message(self) -> Optional[Message]:
        return Message(self.obj.get('pinned_message')) if self.obj.get('pinned_message') else None
    
    @property
    def state(self) -> Optional[str]:
        return self.obj.get('state')
    
    @property
    def icon(self) -> Optional[str]:
        return self.obj['photo'].get('photo_200') if self.obj.get('photo') else None
    
    @property
    def active_ids(self) -> Optional[List[int]]:
        return self.obj.get('active_ids')
    
    @property
    def is_group_channel(self) -> Optional[bool]:
        return self.obj.get('is_group_channel')

class Conversation:
    """
    Объект диалога.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def peer(self) -> Optional[ConversationPeer]:
        return ConversationPeer(self.obj.get('peer')) if self.obj.get('peer') else None
    
    @property
    def in_read(self) -> int:
        return self.obj.get('in_read')
    
    @property
    def out_read(self) -> int:
        return self.obj.get('out_read')
    
    @property
    def unread_count(self) -> int:
        return self.obj.get('unread_count')
    
    @property
    def important(self) -> bool:
        return self.obj.get('important')
    
    @property
    def unanswered(self) -> bool:
        return self.obj.get('unanswered')
    
    @property
    def can_write(self) -> Optional[ConversationPermissions]:
        return ConversationPermissions(self.obj.get('can_write')) if self.obj.get('can_write') else None
    
    @property
    def chat_settings(self) -> Optional[ConversationSessings]:
        return ConversationSessings(self.obj.get('chat_settings')) if self.obj.get('chat_settings') else None

class ConversationItem:
    """
    Отображаемый объект диалога.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def conversation(self) -> Optional[Conversation]:
        return Conversation(self.obj.get('conversation')) if self.obj.get('conversation') else None
    
    @property
    def last_message(self) -> Optional[Message]:
        return Message(self.obj.get('last_message')) if self.obj.get('last_message') else None

class Conversations:
    """
    Все диалоги.
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def count(self) -> int:
        return self.obj.get('count')
    
    @property
    def items(self) -> Optional[List[ConversationItem]]:
        itemlist = []
        itemlist.append(ConversationItem(i) for i in self.obj.get('items'))
        return itemlist
    
    @property
    def unread_count(self) -> int:
        return self.obj.get('unread_count')
    
    @property
    def profiles(self) -> Optional[List[User]]:
        profilelist = []
        profilelist.append(User(i) for i in self.obj.get('profiles'))
        return profilelist
    
    @property
    def groups(self) -> Optional[List[Group]]:
        grouplist = []
        grouplist.append(Group(i) for i in self.obj.get('groups'))