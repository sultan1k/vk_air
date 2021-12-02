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
from typing import Optional
from .photo import Photo
from .video import Video

class StoriesLink:
    """
    Объект ссылки из истории.
    """
    def __init__(self, obj: dict) -> None:
        self.obj = obj
    
    @property
    def text(self) -> str:
        return self.obj.get('text')
    
    @property
    def url(self) -> str:
        return self.obj.get('url')

class Stories:
    """
    Объект истории.
    """
    def __init__(self, obj: dict) -> None:
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('owner_id')
    
    @property
    def date(self) -> Optional[int]:
        return self.obj.get('date')
    
    @property
    def expires_at(self) -> Optional[int]:
        return self.obj.get('expires_at')
    
    @property
    def is_expired(self) -> Optional[bool]:
        return self.obj.get('is_expired')
    
    @property
    def is_deleted(self) -> bool:
        return self.obj.get('is_deleted')
    
    @property
    def can_see(self) -> Optional[bool]:
        return True if self.obj.get('can_see') == 1 else False
    
    @property
    def seen(self) -> bool:
        return bool(self.obj.get('seen'))
    
    @property
    def type(self) -> Optional[str]:
        return self.obj.get('type')
    
    @property
    def photo(self) -> Optional[Photo]:
        return self.obj.get('photo')
    
    @property
    def video(self) -> Optional[Video]:
        return self.obj.get('video')
    
    @property
    def link(self) -> Optional[StoriesLink]:
        return StoriesLink(self.obj.get('link')) if self.obj.get('link') else None
    
    @property
    def parent_story_owner_id(self) -> Optional[int]:
        return self.obj.get('parent_story_owner_id')
    
    @property
    def parent_story_id(self) -> Optional[int]:
        return self.obj.get('parent_story_id')
    
    @property
    def parent_story(self) -> Optional[Stories]:
        return self.obj.get('parent_story')
    
    @property
    def replies(self) -> Optional[int]:
        return self.obj['replies'].get('count') if self.obj.get('replies') else None
    
    @property
    def views(self) -> int:
        return self.obj.get('views')
    
    @property
    def access_key(self) -> Optional[str]:
        return self.obj.get('access_key')