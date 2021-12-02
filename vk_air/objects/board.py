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

from vk_air.bot_api import BotApi


class Board:
    """
    Объект обсуждения.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api: BotApi = api
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def created(self) -> int:
        return self.obj.get('created')
    
    @property
    def created_by(self) -> int:
        return self.obj.get('created_by')
    
    @property
    def updated(self) -> int:
        return self.obj.get('updated')
    
    @property
    def updated_by(self) -> int:
        return self.obj.get('updated_by')
    
    @property
    def is_closed(self) -> bool:
        return True if self.obj.get('is_closed') == 1 else False

    @property
    def is_fixed(self) -> bool:
        return True if self.obj.get('is_fixed') == 1 else False
    
    @property
    def comments(self) -> int:
        return self.obj.get('comments')
    
    @property
    def first_comment(self) -> Optional[str]:
        return self.obj.get('first_comment')
    
    @property
    def last_comment(self) -> Optional[str]:
        return self.obj.get('last_comment')

    async def deleteComment(self, comment_id: int) -> bool:
        r = await self.api.deleteBoardComment(topic_id=self.id, comment_id=comment_id)
        return True if r == 1 else False
    
    async def restoreComment(self, comment_id: int) -> bool:
        r = await self.api.restoreBoardComment(topic_id=self.id, comment_id=comment_id)
        return True if r == 1 else False    

class BoardComment:
    """
    Объект комментария в обсуждении.
    """
    def __init__(self, obj, api = None):
        self.obj = obj
        self.api: BotApi = api
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def from_id(self) -> int:
        return self.obj.get('from_id')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def text(self) -> str:
        return self.obj.get('text')
    
    @property
    def attachments(self) -> Optional[List]:
        attachment_list = []
        from enumsobj import ATTACHMENTS
        for i in self.obj.get('attachments'):
            cls = ATTACHMENTS[i['type']]
            attachment_list.append(cls(i))
        return attachment_list
    
    @property
    def likes(self) -> int:
        return self.obj['likes'].get('count') if self.obj.get('likes') else None
    
    @property
    def topic_id(self) -> Optional[int]:
        return self.obj.get('topic_id')
    
    @property
    def topic_owner_id(self) -> Optional[int]:
        return self.obj.get('topic_owner_id')

    async def delete(self) -> bool:
        r = await self.api.deleteBoardComment(topic_id=self.topic_id, comment_id=self.id)
        return True if r == 1 else False
    
    async def restore(self) -> bool:
        r = await self.api.restoreBoardComment(topic_id=self.topic_id, comment_id=self.id)
        return True if r == 1 else False

class DeletedBoardComment:
    """
    Объект удалённого комментария в обсуждениях.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api: BotApi = api
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def topic_id(self) -> int:
        return self.obj.get('topic_id')
    
    @property
    def topic_owner_id(self) -> int:
        return self.obj.get('topic_owner_id')

    async def restore(self) -> bool:
        r = await self.api.restoreBoardComment(topic_id=self.topic_id, comment_id=self.id)
        return True if r == 1 else False