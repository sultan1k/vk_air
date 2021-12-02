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
from typing import Optional


class Note:
    """
    Объект заметки.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('id')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def text(self) -> Optional[str]:
        return self.obj.get('text')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def comments(self) -> int:
        return self.obj.get('comments')
    
    @property
    def read_comments(self) -> Optional[int]:
        return self.obj.get('read_comments')
    
    @property
    def view_url(self) -> str:
        return self.obj.get('view_url')
    
    @property
    def privacy_view(self) -> str:
        return self.obj.get('privacy_view')
    
    @property
    def privacy_comment(self) -> str:
        return self.obj.get('privacy_comment')
    
    @property
    def can_comment(self) -> bool:
        return True if self.obj.get('can_comment') == 1 else False
    
    @property
    def text_wiki(self) -> Optional[str]:
        return self.obj.get('text_wiki')