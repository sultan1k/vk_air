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
from .photo import PhotoSize


class Sticker:
    """
    Объект стикера.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def product_id(self) -> int:
        return self.obj.get('product_id')
    
    @property
    def sticker_id(self) -> int:
        return self.obj.get('sticker_id')
    
    @property
    def images(self) -> Optional[List[PhotoSize]]:
        imagelist = []
        for i in self.obj.get('images'):
            imagelist.append(PhotoSize(i))
        
    @property
    def images_with_background(self) -> Optional[List[PhotoSize]]:
        bglist = []
        for i in self.obj.get('images_with_background'):
            bglist.append(PhotoSize(i))
        return bglist
    
    @property
    def animation_url(self) -> Optional[str]:
        return self.obj.get('animation_url')
    
    @property
    def is_allowed(self) -> bool:
        return self.obj.get('is_allowed')