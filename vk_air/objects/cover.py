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
from typing import List


class CoverImage:
    """
    Копия изображения обложки.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def height(self) -> int:
        return self.obj.get('height')

class Cover:
    """
    Обложка сообщества.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def enabled(self) -> bool:
        return True if self.obj.get('enabled') == 1 else False
    
    @property
    def images(self) -> List[CoverImage]:
        coverlist = []
        for i in self.obj.get('images'):
            coverlist.append(CoverImage(i))
        return coverlist

class SavedCoverPhoto:
    """
    Объект сохранённой обложки.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def height(self) -> int:
        return self.obj.get('height')

class UploadedCoverPhoto:
    """
    Объект обложки, загруженной на сервер.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def hash(self) -> str:
        return self.obj.get('hash')
    
    @property
    def photo(self) -> str:
        return self.obj.get('photo')