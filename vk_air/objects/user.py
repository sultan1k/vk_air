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
from .career import Career
from .city import City
from .connections import Connections
from .counters import UserCounters
from .country import Country
from .occupation import Occupation
from .photo import CropPhoto
from .education import Education
from .online import LastSeen
from .military import Military
from .personal import Personal

class User:
    """
    Объект пользователя.
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def first_name(self) -> str:
        return self.obj.get('first_name')
    
    @property
    def last_name(self) -> str:
        return self.obj.get('last_name')
    
    @property
    def deactivated(self) -> str:
        return self.obj.get('deactivated')
    
    @property
    def is_closed(self) -> bool:
        return self.obj.get('is_closed')
    
    @property
    def can_access_closed(self) -> bool:
        return self.obj.get('can_access_closed')
    
    @property
    def about(self) -> str:
        return self.obj.get('about')
    
    @property
    def activities(self) -> str:
        return self.obj.get('activities')
    
    @property
    def bdate(self) -> str:
        return self.obj.get('bdate')
    
    @property
    def books(self) -> str:
        return self.obj.get('books')
    
    @property
    def career(self) -> Career:
        return Career(self.obj.get('career')) if self.obj.get('career') else None
    
    @property
    def city(self) -> City:
        return City(self.obj.get('city')) if self.obj.get('city') else None
    
    @property
    def connections(self) -> Connections:
        return Connections(self.obj.get('connections')) if self.obj.get('connections') else None
    
    @property
    def home_phone(self) -> str:
        return self.obj['contacts'].get('home_phone') if self.obj.get('contacts') else None
    
    @property
    def counters(self) -> UserCounters:
        return UserCounters(self.obj.get('counters')) if self.obj.get('counters') else None
    
    @property
    def country(self) -> Country:
        return Country(self.obj.get('country')) if self.obj.get('country') else None
    
    @property
    def crop_photo(self) -> CropPhoto:
        return CropPhoto(self.obj.get('crop_photo')) if self.obj.get('crop_photo') else None
    
    @property
    def domain(self) -> str:
        return self.obj.get('domain')
    
    @property
    def education(self) -> Education:
        return Education(self.obj.get('education')) if self.obj.get('education') else None
    
    @property
    def exports(self) -> str:
        return self.obj.get('exports')
    
    def first_name_case(self, case) -> str:
        """
        Описание
        ----------

        Возвращает имя пользователя в заданном падеже.

        Параметры
        ----------

        * case - падеж.\n
        Возможные значения case:\n
        1. nom - именительный\n
        2. gen - родительный\n
        3. dat - дательный\n
        4. acc - винительный\n
        5. ins - творительный\n
        6. abl - предложный\n
        """
        return self.obj.get(f'first_name_{case}')
    
    def last_name_case(self, case) -> str:
        """
        Описание
        ----------

        Возвращает фамилию пользователя в заданном падеже.

        Параметры
        ----------

        * case - падеж.\n
        Возможные значения case:\n
        1. nom - именительный\n
        2. gen - родительный\n
        3. dat - дательный\n
        4. acc - винительный\n
        5. ins - творительный\n
        6. abl - предложный\n
        """
        return self.obj.get(f'last_name_{case}')
    
    @property
    def followers_count(self) -> int:
        return self.obj.get('followers_count')
    
    @property
    def games(self) -> str:
        return self.obj.get('games')
    
    @property
    def has_mobile(self) -> bool:
        return True if self.obj.get('has_mobile') == 1 else False
    
    @property
    def has_photo(self) -> bool:
        return True if self.obj.get('has_photo') == 1 else False
    
    @property
    def home_town(self) -> str:
        return self.obj.get('home_town')
    
    @property
    def interests(self) -> str:
        return self.obj.get('interests')
    
    @property
    def is_no_index(self) -> bool:
        return True if self.obj.get('is_no_index') == 1 else False
    
    @property
    def last_seen(self) -> LastSeen:
        return LastSeen(self.obj.get('last_seen')) if self.obj.get('last_seen') else None
    
    @property
    def maiden_name(self) -> str:
        return self.obj.get('maiden_name')
    
    @property
    def military(self) -> Military:
        return Military(self.obj.get('military')) if self.obj.get('military') else None

    @property
    def movies(self) -> str:
        return self.obj.get('movies')
    
    @property
    def music(self) -> str:
        return self.obj.get('music')
    
    @property
    def nickname(self) -> str:
        return self.obj.get('nickname')
    
    @property
    def occupation(self) -> Occupation:
        return Occupation(self.obj.get('occupation')) if self.obj.get('occupation') else None
    
    @property
    def online(self) -> bool:
        return True if self.obj.get('online') == 1 else False
    
    @property
    def personal(self) -> Personal:
        return Personal(self.obj.get('personal')) if self.obj.get('personal') else None
    
    @property
    def avatar_url(self) -> str:
        return self.obj.get('photo_max')
    
    @property
    def mention(self) -> str:
        return f'[id{self.id}|{self.domain}'