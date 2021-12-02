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
from .currency import Currency
from .photo import Photo

class LinkProductPrice:
    """
    Объект, описывающий цену товара.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def amount(self) -> int:
        return self.obj.get('amount')
    
    @property
    def currency(self) -> Optional[Currency]:
        return Currency(self.obj.get('currency')) if self.obj.get('currency') else None
    
    @property
    def text(self) -> str:
        return self.obj.get('text')
    
    @property
    def old_amount(self) -> Optional[str]:
        return self.obj.get('old_amount')

class LinkProduct:
    """
    Информация о продукте.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def price(self) -> Optional[LinkProductPrice]:
        return LinkProductPrice(self.obj.get('price')) if self.obj.get('price') else None

class ProductDimensions:
    """
    Габариты товара.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def height(self) -> int:
        return self.obj.get('height')
    
    @property
    def length(self) -> int:
        return self.obj.get('length')

class ProductCategorySection:
    """
    Секция товара.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def name(self) -> str:
        return self.obj.get('name')

class ProductCategory:
    """
    Категория товара.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def name(self) -> str:
        return self.obj.get('name')
    
    @property
    def section(self) -> Optional[ProductCategorySection]:
        return ProductCategorySection(self.obj.get('section')) if self.obj.get('section') else None

class Product:
    """
    Объект товара.
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
    def description(self) -> Optional[str]:
        return self.obj.get('description')
    
    @property
    def price(self) -> Optional[LinkProductPrice]:
        return LinkProductPrice(self.obj.get('price')) if self.obj.get('price') else None
    
    @property
    def dimensions(self) -> Optional[ProductDimensions]:
        return ProductDimensions(self.obj.get('dimensions')) if self.obj.get('dimensions') else None

    @property
    def weight(self) -> int:
        return self.obj.get('weight')
    
    @property
    def category(self) -> Optional[ProductCategory]:
        return ProductCategory(self.obj.get('category')) if self.obj.get('category') else None
    
    @property
    def thumb_photo(self) -> str:
        return self.obj.get('thumb_photo')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def availability(self) -> int:
        return self.obj.get('availability')
    
    @property
    def sku(self) -> str:
        return self.obj.get('sku')
    
    @property
    def photos(self) -> Optional[List[Photo]]:
        photolist = []
        for i in self.obj.get('photos'):
            photolist.append(Photo(i))
        return photolist
    
    @property
    def likescount(self) -> Optional[int]:
        return self.obj['likes'].get('count') if self.obj.get('likes') else None
    
    @property
    def url(self) -> Optional[str]:
        return self.obj.get('url')
    
    @property
    def button_title(self) -> Optional[str]:
        return self.obj.get('button_title')
    
    def to_attachment(self) -> str:
        return f'market{self.owner_id}_{self.id}'