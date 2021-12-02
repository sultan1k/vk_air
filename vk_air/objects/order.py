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
from .delivery import Delivery
from .product import LinkProductPrice, Product
from .recipient import Recipient
from .variant import Variant


class Order:
    """
    Объект заказа.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api = api
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def group_id(self) -> int:
        return self.obj.get('group_id')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def variants_grouping_id(self) -> int:
        return self.obj.get('variants_grouping_id')
    
    @property
    def is_main_variant(self) -> bool:
        return self.obj.get('is_main_variant')
    
    @property
    def property_values(self) -> Optional[List[Variant]]:
        variant_list = []
        for i in self.obj.get('property_values'):
            variant_list.append(Variant(i))
        return variant_list
    
    @property
    def cart_quantity(self) -> int:
        return self.obj.get('cart_quantity')
    
    @property
    def status(self) -> int:
        return self.obj.get('status')
    
    @property
    def items_count(self) -> int:
        return self.obj.get('items_count')
    
    @property
    def total_price(self) -> Optional[LinkProductPrice]:
        return LinkProductPrice(self.obj.get('total_price')) if self.obj.get('total_price') else None
    
    @property
    def display_order_id(self) -> str:
        return self.obj.get('display_order_id')
    
    @property
    def comment(self) -> Optional[str]:
        return self.obj.get('comment')
    
    @property
    def preview_order_items(self) -> Optional[List[Product]]:
        product_list = []
        for i in self.obj.get('preview_order_items'):
            product_list.append(Product(i))
        return product_list
    
    @property
    def delivery(self) -> Optional[Delivery]:
        return Delivery(self.obj.get('delivery')) if self.obj.get('delivery') else None
    
    @property
    def recipient(self) -> Optional[Recipient]:
        return Recipient(self.obj.get('recipient')) if self.obj.get('recipient') else None