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


class PhotoSize:
    """
    Копия изображения в разных размерах.
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def url(self) -> str:
        if not self.obj.get('url'):
            return self.obj.get('src')
        return self.obj.get('url')
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def height(self) -> int:
        return self.obj.get('height')

class Photo:
    """
    Объект фотографии.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api = api

    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def album_id(self) -> int:
        return self.obj.get('album_id')
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('owner_id')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def text(self) -> str:
        return self.obj.get('text')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def sizes(self) -> List[PhotoSize]:
        sizelist = []
        for i in self.obj.get('sizes'):
            sizelist.append(i)
        return sizelist
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def height(self) -> int:
        return self.obj.get('height')
    
    @property
    def access_key(self) -> Optional[str]:
        return self.obj.get('access_key')
    
    def to_attachment(self) -> str:
        if self.access_key:
            return f'photo{self.owner_id}_{self.id}_{self.access_key}'
        else:
            return f'photo{self.owner_id}_{self.id}'

class Crop:
    """
    Координаты вырезанной фотографии.
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def x(self) -> int:
        return self.obj.get('x')
    
    @property
    def y(self) -> int:
        return self.obj.get('y')
    
    @property
    def x2(self) -> int:
        return self.obj.get('x2')
    
    @property
    def y2(self) -> int:
        return self.obj.get('y2')

class Rect:
    """
    Миниатюрная квадратная фотография.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def x(self) -> int:
        return self.obj.get('x')
    
    @property
    def y(self) -> int:
        return self.obj.get('y')
    
    @property
    def x2(self) -> int:
        return self.obj.get('x2')
    
    @property
    def y2(self) -> int:
        return self.obj.get('y2')

class CropPhoto:
    """
    Профильная и миниатюрная фотографии.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def photo(self) -> Photo:
        return Photo(self.obj.get('photo')) if self.obj.get('photo') else None
    
    @property
    def crop(self) -> Crop:
        return Crop(self.obj.get('crop')) if self.obj.get('crop') else None
    
    @property
    def rect(self) -> Rect:
        return Rect(self.obj.get('rect')) if self.obj.get('rect') else None