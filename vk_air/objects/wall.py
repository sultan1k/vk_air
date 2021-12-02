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

from ..bot_api import BotApi
from .geo import Geo
from .donut import DonutWall

class WallCopyright:
    """
    Информация об источнике материала.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def link(self) -> str:
        return self.obj.get('link')
    
    @property
    def name(self) -> str:
        return self.obj.get('name')
    
    @property
    def type(self) -> str:
        return self.obj.get('type')

class WallLikes:
    """
    Информация о лайках к записи.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def count(self) -> int:
        return self.obj.get('count')
    
    @property
    def user_likes(self) -> bool:
        return True if self.obj.get('user_likes') == 1 else False
    
    @property
    def can_like(self) -> bool:
        return True if self.obj.get('can_like') == 1 else False
    
    @property
    def can_publish(self) -> bool:
        return True if self.obj.get('can_publish') == 1 else False

class WallReposts:
    """
    Информация о репостах записи.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def count(self) -> int:
        return self.obj.get('count')

class WallViews:
    """
    Информация о просмотрах записи.
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def count(self) -> int:
        return self.obj.get('count')

class WallComments:
    """
    Информация о комментариях к записи.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def count(self) -> int:
        return self.obj.get('count')
    
    @property
    def can_post(self) -> bool:
        return True if self.obj.get('can_post') == 1 else False
    
    @property
    def groups_can_post(self) -> bool:
        return True if self.obj.get('groups_can_post') == 1 else False

    @property
    def can_close(self) -> bool:
        return self.obj.get('can_close')
    
    @property
    def can_open(self) -> bool:
        return self.obj.get('can_open')

class Wall:
    """
    Объект поста на стене пользователя/сообщества.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api: BotApi = api
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('owner_id')
    
    @property
    def from_id(self) -> int:
        return self.obj.get('from_id')
    
    @property
    def created_by(self) -> int:
        return self.obj.get('created_by')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def text(self) -> str:
        return self.obj.get('text')
    
    @property
    def reply_owner_id(self) -> int:
        return self.obj.get('reply_owner_id')
    
    @property
    def reply_post_id(self) -> int:
        return self.obj.get('reply_post_id')
    
    @property
    def friends_only(self) -> bool:
        return True if self.obj.get('friends_only') else False
    
    @property
    def comments(self) -> WallComments:
        return WallComments(self.obj.get('comments')) if self.obj.get('comments') else None

    @property
    def copyright(self) -> WallCopyright:
        return WallCopyright(self.obj.get('copyright')) if self.obj.get('copyright') else None
    
    @property
    def likes(self) -> WallLikes:
        return WallLikes(self.obj.get('likes')) if self.obj.get('likes') else None
    
    @property
    def reposts(self) -> WallReposts:
        return WallReposts(self.obj.get('reposts')) if self.obj.get('reposts') else None
    
    @property
    def views(self) -> WallViews:
        return WallViews(self.obj.get('views')) if self.obj.get('views') else None
    
    @property
    def post_type(self) -> str:
        return self.obj.get('post_type')
    
    @property
    def attachments(self) -> Optional[List]:
        attachment_list = []
        import enumsobj
        for i in self.obj.get('attachments'):
            cls = enumsobj.ATTACHMENTS[i['type']]
            attachment_list.append(cls(i))
        return attachment_list
    
    @property
    def geo(self) -> Optional[Geo]:
        return Geo(self.obj.get('geo')) if self.obj.get('geo') else None
    
    @property
    def signer_id(self) -> Optional[int]:
        return self.obj.get('signer_id')
    
    @property
    def copy_history(self) -> Optional[List[Wall]]:
        copylist = []
        for i in self.obj.get('copy_history'):
            copylist.append(Wall(i))
        return copylist
    
    @property
    def can_pin(self) -> bool:
        return True if self.obj.get('can_pin') == 1 else False
    
    @property
    def can_delete(self) -> bool:
        return True if self.obj.get('can_delete') == 1 else False

    @property
    def can_edit(self) -> bool:
        return True if self.obj.get('can_edit') == 1 else False
    
    @property
    def is_pinned(self) -> bool:
        return True if self.obj.get('is_pinned') else False
    
    @property
    def ad(self) -> bool:
        return True if self.obj.get('marked_as_ads') == 1 else False
    
    @property
    def donut(self) -> Optional[DonutWall]:
        return DonutWall(self.obj.get('donut')) if self.obj.get('donut') else None
    
    @property
    def postponed_id(self) -> Optional[int]:
        return self.obj.get('postponed_id')
    
    @property
    def access_key(self) -> Optional[str]:
        return self.obj.get('access_key')
    
    def to_attachment(self) -> str:
        if self.access_key:
            return f'wall{self.owner_id}_{self.id}_{self.access_key}'
        else:
            return f'wall{self.owner_id}_{self.id}'

    async def close_comments(self) -> bool:
        r = await self.api.wallCloseComments(owner_id=self.owner_id, post_id=self.id)
        return True if r == 1 else False
    
    async def open_comments(self) -> bool:
        r = await self.api.wallOpenComments(owner_id=self.owner_id, post_id=self.id)
        return True if r == 1 else False
    
    async def create_comment(
        self, 
        *, 
        owner_id: int, 
        post_id: int, 
        from_group: int = 0, 
        message: str = None,
        reply_to_comment: int = None,
        attachments: str = None,
        sticker_id: int = None,
        guid: str = None
    ) -> Optional[int]:
        r = await self.api.wallCreateComment(
            owner_id=owner_id,
            post_id=post_id,
            from_group=from_group,
            message=message,
            reply_to_comment=reply_to_comment,
            attachments=attachments,
            sticker_id=sticker_id,
            guid=guid
        )
        return r