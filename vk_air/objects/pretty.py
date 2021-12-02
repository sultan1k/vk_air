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
from .button import Button

class PrettyCard:
    """
    Объект карточки.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def card_id(self) -> int:
        return self.obj.get('card_id')
    
    @property
    def link_url(self) -> str:
        return self.obj.get('link_url')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def images(self) -> Optional[List[PhotoSize]]:
        imagelist = []
        for i in self.obj.get('images'):
            imagelist.append(PhotoSize(i))
        return imagelist

    @property
    def button(self) -> Optional[Button]:
        return Button(self.obj.get('button')) if self.obj.get('button') else None

    @property
    def price(self) -> str:
        return self.obj.get('price')
    
    @property
    def price_old(self) -> Optional[str]:
        return self.obj.get('price_old')

class PrettyCards:
    """
    Массив элементов
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def cards(self) -> Optional[List[PrettyCard]]:
        cardlist = []
        for i in self.obj.get('cards'):
            cardlist.append(PrettyCard(i))
        return cardlist