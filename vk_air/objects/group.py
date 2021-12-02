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
from .city import City
from .contact import Contact
from typing import List, Optional
from .counters import GroupCounters
from .country import Country
from .cover import Cover
from .photo import CropPhoto
from .link import GroupLink
from .market import Market
from .place import Place

class GroupAddresses:
    """
    Информация об адресах сообщества.
    """
    def __init__(self, obj):
        self.obj  = obj
    
    @property
    def is_enabled(self) -> bool:
        return self.obj.get('is_enabled')
    
    @property
    def main_address_id(self) -> int:
        return self.obj.get('main_address_id')

class Group:
    """
    Объект группы.
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
    def screen_name(self) -> str:
        return self.obj.get('screen_name')
    
    @property
    def is_closed(self) -> int:
        return self.obj.get('is_closed')
    
    @property
    def deactivated(self) -> str:
        return self.obj.get('deactivated')
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def icon(self) -> str:
        return self.obj.get('photo_200')
    
    @property
    def small_icon(self) -> str:
        return self.obj.get('photo_100')
    
    @property
    def activity(self) -> str:
        return self.obj.get('activity')
    
    @property
    def addresses(self) -> GroupAddresses:
        return GroupAddresses(self.obj.get('addresses')) if self.obj.get('addresses') else None

    @property
    def age_limits(self) -> int:
        return self.obj.get('age_limits')
    
    @property
    def city(self) -> City:
        return City(self.obj.get('city')) if self.obj.get('city') else None
    
    @property
    def contacts(self) -> List[Contact]:
        contactlist = []
        for i in self.obj.get('contacts'):
            contactlist.append(Contact(i))
        return contactlist
    
    @property
    def counters(self) -> GroupCounters:
        return GroupCounters(self.obj.get('counters')) if self.obj.get('counters') else None
    
    @property
    def country(self) -> Country:
        return Country(self.obj.get('country')) if self.obj.get('country') else None
    
    @property
    def cover(self) -> Cover:
        return Cover(self.obj.get('cover')) if self.obj.get('cover') else None
    
    @property
    def crop_photo(self) -> CropPhoto:
        return CropPhoto(self.obj.get('crop_photo')) if self.obj.get('crop_photo') else None
    
    @property
    def description(self) -> str:
        return self.obj.get('description')
    
    @property
    def fixed_post(self) -> int:
        return self.obj.get('fixed_post')
    
    @property
    def has_photo(self) -> bool:
        return True if self.obj.get('has_photo') == 1 else False
    
    @property
    def links(self) -> List[GroupLink]:
        linklist = []
        for i in self.obj.get('links'):
            linklist.append(GroupLink(i))
        return linklist
    
    @property
    def main_album_id(self) -> int:
        return self.obj.get('main_album_id')
    
    @property
    def main_section(self) -> int:
        return self.obj.get('main_section')
    
    @property
    def market(self) -> Market:
        return Market(self.obj.get('market')) if self.obj.get('market') else None
    
    @property
    def members_count(self) -> int:
        return self.obj.get('members_count')
    
    @property
    def place(self) -> Place:
        return Place(self.obj.get('place')) if self.obj.get('place') else None

    @property
    def public_date_label(self) -> str:
        return self.obj.get('public_date_label')
    
    @property
    def site(self) -> str:
        return self.obj.get('site')
    
    @property
    def start_date(self) -> int:
        return self.obj.get('start_date')
    
    @property
    def finish_date(self) -> int:
        return self.obj.get('finish_date')
    
    @property
    def status(self) -> str:
        return self.obj.get('status')
    
    @property
    def trending(self) -> bool:
        return True if self.obj.get('trending') == 1 else False
    
    @property
    def verified(self) -> bool:
        return True if self.obj.get('verified') == 1 else False
    
    @property
    def wall(self) -> int:
        return self.obj.get('wall')
    
    @property
    def wiki_page(self) -> str:
        return self.obj.get('wiki_page')

class GroupIsMember:
    """
    Проверка, является ли пользователь участником группы.
    """
    def __init__(self, obj: dict):
        self.obj = obj
    
    @property
    def user_id(self) -> Optional[int]:
        return self.obj.get('user_id')
    
    @property
    def member(self) -> bool:
        return True if self.obj.get('member') == 1 else False

class GroupLeave:
    """
    Объект участника, которого забанили, либо он сам отписался от сообщества.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def _self(self) -> bool:
        return True if self.obj.get('self') == 1 else False

class GroupJoin:
    """
    Объект участника, который подписался на сообщество.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def join_type(self) -> str:
        return self.obj.get('join_type')
    
class UserBlock:
    """
    Объект участника, добавленного в чёрный список.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def admin_id(self) -> int:
        return self.obj.get('admin_id')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def unblock_date(self) -> int:
        return self.obj.get('unblock_date')
    
    @property
    def reason(self) -> int:
        return self.obj.get('reason')
    
    @property
    def comment(self) -> str:
        return self.obj.get('comment')

class UserUnblock:
    """
    Объект участника, убранного из чёрного списка.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def admin_id(self) -> int:
        return self.obj.get('admin_id')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def by_end_date(self) -> int:
        return self.obj.get('by_end_date')