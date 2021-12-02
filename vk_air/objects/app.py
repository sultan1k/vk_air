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
from .photo import Photo

class App:
    """
    Объект приложения.
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
    def icon_278(self) -> Optional[str]:
        return self.obj.get('icon_278')
    
    @property
    def icon_139(self) -> Optional[str]:
        return self.obj.get('icon_139')
    
    @property
    def icon_150(self) -> Optional[str]:
        return self.obj.get('icon_150')
    
    @property
    def icon_75(self) -> Optional[str]:
        return self.obj.get('icon_75')
    
    @property
    def icon(self) -> Optional[str]:
        return self.obj.get('icon_150')
    
    @property
    def banner_560(self) -> Optional[str]:
        return self.obj.get('banner_560')
    
    @property
    def banner_1120(self) -> Optional[str]:
        return self.obj.get('banner_1120')
    
    @property
    def banner(self) -> Optional[str]:
        return self.obj.get('banner_560')
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def section(self) -> Optional[str]:
        return self.obj.get('section')
    
    @property
    def author_url(self) -> Optional[str]:
        return self.obj.get('author_url')
    
    @property
    def author_id(self) -> Optional[int]:
        return self.obj.get('author_id')

    @property
    def author_group(self) -> Optional[int]:
        return self.obj.get('author_group')
    
    @property
    def memberscount(self) -> int:
        return self.obj.get('memberscount')
    
    @property
    def published_date(self) -> int:
        return self.obj.get('published_date')
    
    @property
    def catalog_position(self) -> Optional[int]:
        return self.obj.get('caatalog_position')
    
    @property
    def international(self) -> bool:
        return True if self.obj.get('international') == 1 else False
    
    @property
    def leaderboard_type(self) -> Optional[int]:
        return self.obj.get('leaderboard_type')
    
    @property
    def genre_id(self) -> Optional[int]:
        return self.obj.get('genre_id')
    
    @property
    def genre(self) -> Optional[str]:
        return self.obj.get('genre')
    
    @property
    def platform_id(self) -> Optional[str]:
        return self.obj.get('platform_id')
    
    @property
    def is_html5_app(self) -> bool:
        return True if self.obj.get('is_html5_app') else False
    
    @property
    def screen_orientation(self) -> int:
        return self.obj.get('screen_orientation')
    
    @property
    def mobile_controls_type(self) -> int:
        return self.obj.get('mobile_controls_type')
    
    @property
    def mobile_view_support_type(self) -> int:
        return self.obj.get('mobile_view_support_type')
    
    # при extended=1

    @property
    def description(self) -> Optional[str]:
        return self.obj.get('description')
    
    @property
    def screen_name(self) -> Optional[str]:
        return self.obj.get('screen_name')
    
    @property
    def icon_16(self) -> Optional[str]:
        return self.obj.get('icon_16')
    
    @property
    def screenshots(self) -> Optional[List[Photo]]:
        screenlist = []
        for i in self.obj.get('screenshots'):
            screenlist.append(Photo(i))
        return screenlist

class AppImage:
    """
    Изображение виджета.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def height(self) -> int:
        return self.obj.get('height')

class AppItem:
    """
    Виджет приложения.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> str:
        return self.obj.get('id')
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def images(self) -> Optional[List[AppImage]]:
        image_list = []
        for i in self.obj.get('images'):
            image_list.append(AppImage(i))
        return image_list

class AppImages:
    """
    Массив виджетов.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def count(self) -> int:
        return self.obj.get('count')
    
    @property
    def items(self) -> Optional[List[AppItem]]:
        item_list = []
        for i in self.obj.get('items'):
            item_list.append(AppItem(i))
        return item_list

class AppPayload:
    """
    Объект события в VK Mini Apps.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def app_id(self) -> int:
        return self.obj.get('app_id')
    
    @property
    def payload(self) -> dict:
        return self.obj.get('payload')
    
    @property
    def group_id(self) -> int:
        return self.obj.get('group_id')