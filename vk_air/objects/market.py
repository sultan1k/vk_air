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
class MarketCurrency:
    """
    Информация о валюте.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def name(self) -> str:
        return self.obj.get('name')

class Market:
    """
    Информация о магазине.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def enabled(self) -> bool:
        return True if self.obj.get('enabled') == 1 else None
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def price_min(self) -> int:
        return self.obj.get('price_min')
    
    @property
    def price_max(self) -> int:
        return self.obj.get('price_max')
    
    @property
    def main_album_id(self) -> int:
        return self.obj.get('main_album_id')
    
    @property
    def contact_id(self) -> int:
        return self.obj.get('contact_id')
    
    @property
    def currency(self) -> MarketCurrency:
        return MarketCurrency(self.obj.get('currency')) if self.obj.get('currency') else None
    
    @property
    def currency_text(self) -> str:
        return self.obj.get('currency_text')