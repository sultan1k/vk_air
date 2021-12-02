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

class Thread:
    """
    Вложенная ветка комментариев.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def count(self) -> int:
        return self.obj.get('count')
    
    @property
    def items(self) -> Optional[List[Comment]]:
        itemlist = []
        for i in self.obj.get('items'):
            itemlist.append(Comment(i))
        return itemlist
    
    @property
    def can_post(self) -> bool:
        return self.obj.get('can_post')
    
    @property
    def show_reply_button(self) -> bool:
        return self.obj.get('show_reply_button')
    
    @property
    def groups_can_post(self) -> bool:
        return self.obj.get('groups_can_post')

class Comment:
    """
    Объект комментария.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api = api
    
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
    def is_don(self) -> bool:
        return self.obj['donut'].get('is_don') if self.obj.get('donut') else False
    
    @property
    def reply_to_user(self) -> Optional[int]:
        return self.obj.get('reply_to_user')
    
    @property
    def reply_to_comment(self) -> Optional[int]:
        return self.obj.get('reply_to_comment')
    
    @property
    def attachments(self) -> Optional[List]:
        attachment_list = []
        import enumsobj
        for i in self.obj.get('attachments'):
            cls = enumsobj.ATTACHMENTS[i['type']]
            attachment_list.append(cls(i))
        return attachment_list
    
    @property
    def parents_stack(self) -> Optional[List[int]]:
        return self.obj.get('parents_stack')
    
    @property
    def thread(self) -> Optional[Thread]:
        return Thread(self.obj.get('thread')) if self.obj.get('thread') else None