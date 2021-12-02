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
from .button import Button
from .product import LinkProduct
from .photo import Photo


class GroupLink:
    """
    Информация о ссылке из блока ссылок.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def name(self) -> str:
        return self.obj.get('name')
    
    @property
    def desc(self) -> str:
        return self.obj.get('desc')
    
    @property
    def icon(self) -> str:
        return self.obj.get('photo_100')

class Link:
    """
    Объект ссылки.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def caption(self) -> Optional[str]:
        return self.obj.get('caption')
    
    @property
    def description(self) -> Optional[str]:
        return self.obj.get('description')
    
    @property
    def photo(self) -> Optional[Photo]:
        return Photo(self.obj.get('photo')) if self.obj.get('photo') else None
    
    @property
    def button(self) -> Optional[Button]:
        return Button(self.obj.get('button')) if self.obj.get('button') else None
    
    @property
    def product(self) -> Optional[LinkProduct]:
        return LinkProduct(self.obj.get('product')) if self.obj.get('product') else None
    
    @property
    def preview_page(self) -> Optional[str]:
        return self.obj.get('preview_page')
    
    @property
    def preview_url(self) -> Optional[str]:
        return self.obj.get('preview_url')