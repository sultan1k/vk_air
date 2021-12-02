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


class DonutWall:
    """
    Информация о записи для подписчиков Donut
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def is_donut(self) -> bool:
        return self.obj.get('is_donut')
    
    @property
    def paid_duration(self) -> Optional[int]:
        return self.obj.get('paid_duration')
    
    @property
    def can_publish_free_copy(self) -> Optional[bool]:
        return self.obj.get('can_publish_free_copy')
    
    @property
    def edit_mode(self) -> str:
        return self.obj.get('edit_mode')

class DonutSubscriptionCreate:
    """
    Объект оформления платной подписки.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def amount(self) -> int:
        return self.obj.get('amount')
    
    @property
    def amount_without_fee(self) -> float:
        return self.obj.get('amount_without_fee')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
 
class DonutSubscriptionProlonged:
    """
    Объект продления платной подписки.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def amount(self) -> int:
        return self.obj.get('amount')
    
    @property
    def amount_without_fee(self) -> float:
        return self.obj.get('amount_without_fee')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')

class DonutSubscriptionExpired:
    """
    Объект истечённой платной подписки.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')

class DonutSubscriptionCancelled:
    """
    Объект отменённой платной подписки.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')

class DonutSubscriptionPriceChanged:
    """
    Объект изменённой стоимости подписки.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def amount_old(self) -> int:
        return self.obj.get('amount_old')
    
    @property
    def amount_new(self) -> int:
        return self.obj.get('amount_new')
    
    @property
    def amount_diff(self) -> float:
        return self.obj.get('amount_diff')
    
    @property
    def amount_diff_without_fee(self) -> float:
        return self.obj.get('amount_diff_without_fee')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')

class DonutMoneyWithdraw:
    """
    Объект вывода денег.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def amount(self) -> float:
        return self.obj.get('amount')
    
    @property
    def amount_without_fee(self) -> float:
        return self.obj.get('amount_without_fee')

class DonutMoneyWithdrawError:
    """
    Объект ошибки вывода денег.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def reason(self) -> str:
        return self.obj.get('reason')