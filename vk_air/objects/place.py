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


class Place:
    """
    Объект места.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def latitude(self) -> int:
        return self.obj.get('latitude')
    
    @property
    def longitude(self) -> int:
        return self.obj.get('longitude')
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def country(self) -> int:
        return self.obj.get('country')
    
    @property
    def city(self) -> int:
        return self.obj.get('city')
    
    @property
    def address(self) -> str:
        return self.obj.get('address')
    
    @property
    def icon(self) -> Optional[str]:
        return self.obj.get('icon')
    
    @property
    def checkins(self) -> Optional[int]:
        return self.obj.get('checkins')
    
    @property
    def updated(self) -> Optional[int]:
        return self.obj.get('updated')