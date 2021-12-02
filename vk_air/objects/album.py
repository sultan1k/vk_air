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
from .photo import Photo

class Album:
    """
    Объект альбома.
    """
    def __init__(self, obj: dict, api):
        self.obj = obj
        self.api = api

    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def thumb(self) -> Optional[Photo]:
        return Photo(self.obj.get('thumb')) if self.obj.get('thumb') else None
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('owner_id')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def description(self) -> Optional[str]:
        return self.obj.get('description')
    
    @property
    def created(self) -> int:
        return self.obj.get('created')
    
    @property
    def updated(self) -> int:
        return self.obj.get('updated')
    
    @property
    def size(self) -> int:
        return self.obj.get('size')

class MarketAlbum:
    """
    Подборка товаров.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('owner_id')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def is_main(self) -> bool:
        return self.obj.get('is_main')
    
    @property
    def is_hidden(self) -> bool:
        return self.obj.get('is_hidden')
    
    @property
    def photo(self) -> Optional[Photo]:
        return Photo(self.obj.get('photo')) if self.obj.get('photo') else None
    
    @property
    def count(self) -> int:
        return self.obj.get('count')