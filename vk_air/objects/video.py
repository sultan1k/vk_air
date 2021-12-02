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


class VideoImage:
    """
    Изображение обложки.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def height(self) -> int:
        return self.obj.get('height')
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def with_padding(self) -> bool:
        return True if self.obj.get('with_padding') else False

class FirstFrame:
    """
    Изображение первого кадра.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def height(self) -> int:
        return self.obj.get('height')
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def width(self) -> int:
        return self.obj.get('width')

class VideoLikes:
    """
    Информация о лайках к видеозаписи.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def count(self) -> int:
        return self.obj.get('count')

class VideoReposts:
    """
    Информация о репостах к видеозаписи.
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def count(self) -> int:
        return self.obj.get('count')
    
    @property
    def wall_count(self) -> int:
        return self.obj.get('wall_count')
    
    @property
    def mail_count(self) -> int:
        return self.obj.get('main_count')
    
    @property
    def user_reposted(self) -> int:
        return self.obj.get('user_reposted')

class Video:
    """
    Объект видеозаписи.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api = api

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
    def description(self) -> str:
        return self.obj.get('description')
    
    @property
    def duration(self) -> int:
        return self.obj.get('duration')
    
    @property
    def image(self) -> List[VideoImage]:
        imagelist = []
        for i in self.obj.get('image'):
            imagelist.append(VideoImage(i))
        return imagelist
    
    @property
    def first_frame(self) -> List[FirstFrame]:
        framelist = []
        for i in self.obj.get('first_frame'):
            framelist.append(FirstFrame(i))
        return framelist
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def adding_date(self) -> int:
        return self.obj.get('adding_date')
    
    @property
    def views(self) -> int:
        return self.obj.get('views')
    
    @property
    def local_views(self) -> int:
        return self.obj.get('local_views')
    
    @property
    def comments(self) -> int:
        return self.obj.get('comments')
    
    @property
    def player(self) -> str:
        return self.obj.get('player')
    
    @property
    def platform(self) -> str:
        return self.obj.get('platform')
    
    @property
    def can_add(self) -> bool:
        return True if self.obj.get('can_add') == 1 else False
    
    @property
    def is_private(self) -> bool:
        return True if self.obj.get('is_private') else False
    
    @property
    def access_key(self) -> str:
        return self.obj.get('access_key')
    
    @property
    def processing(self) -> bool:
        return True if self.obj.get('processing') else False
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def height(self) -> int:
        return self.obj.get('height')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def converting(self) -> bool:
        return True if self.obj.get('converting') == 1 else False
    
    @property
    def repeat(self) -> int:
        return True if self.obj.get('repeat') else False
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def balance(self) -> int:
        return self.obj.get('balance')
    
    @property
    def live_status(self) -> str:
        return self.obj.get('live_status')
    
    @property
    def live(self) -> bool:
        return True if self.obj.get('live') else False
    
    @property
    def upcoming(self) -> bool:
        return True if self.obj.get('upcoming') else False
    
    @property
    def spectators(self) -> Optional[int]:
        return self.obj.get('spectators')
    
    @property
    def likes(self) -> VideoLikes:
        return VideoLikes(self.obj.get('likes')) if self.obj.get('likes') else None

    @property
    def reposts(self) -> VideoReposts:
        return VideoReposts(self.obj.get('reposts')) if self.obj.get('reposts') else None
    
    def to_attachment(self) -> str:
        if self.access_key:
            return f'video{self.owner_id}_{self.id}_{self.access_key}'
        else:
            return f'video{self.owner_id}_{self.id}'