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


class Page:
    """
    Объект вики-страницы.
    """
    def __init__(self, obj: dict):
        self.obj = obj

    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def group_id(self) -> int:
        return self.obj.get('group_id')
    
    @property
    def creator_id(self) -> int:
        return self.obj.get('creator_id')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def who_can_view(self) -> int:
        return self.obj.get('who_can_view')
    
    @property
    def who_can_edit(self) -> int:
        return self.obj.get('who_can_edit')
    
    @property
    def edited(self) -> int:
        return self.obj.get('edited')
    
    @property
    def created(self) -> int:
        return self.obj.get('created')
    
    @property
    def editor_id(self) -> int:
        return self.obj.get('editor_id')
    
    @property
    def views(self) -> int:
        return self.obj.get('views')
    
    @property
    def parent(self) -> Optional[str]:
        return self.obj.get('parent')
    
    @property
    def parent2(self) -> Optional[str]:
        return self.obj.get('parent2')
    
    @property
    def source(self) -> Optional[str]:
        return self.obj.get('source')
    
    @property
    def html(self) -> Optional[str]:
        return self.obj.get('html')
    
    @property
    def view_url(self) -> Optional[str]:
        return self.obj.get('view_url')