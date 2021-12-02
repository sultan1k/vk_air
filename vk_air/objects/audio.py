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


class Audio:
    """
    Объект аудиозаписи.
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
    def artist(self) -> Optional[str]:
        return self.obj.get('artist')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def duration(self) -> int:
        return self.obj.get('duration')
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def lyrics_id(self) -> Optional[int]:
        return self.obj.get('lyrics_id')
    
    @property
    def album_id(self) -> Optional[int]:
        return self.obj.get('album_id')
    
    @property
    def genre_id(self) -> Optional[int]:
        return self.obj.get('genre_id')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def no_search(self) -> bool:
        return True if self.obj.get('no_search') else False
    
    @property
    def is_hq(self) -> bool:
        return True if self.obj.get('is_hq') else False
    
    def to_attachment(self) -> str:
        return f'audio{self.owner_id}_{self.id}'

class AudioMessage:
    """
    Аудиосообщение.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self):
        return 'audio_message'
    
    @property
    def id(self):
        return self.obj.get('id')
    
    @property
    def owner_id(self):
        return self.obj.get('owner_id')
    
    @property
    def duration(self):
        return self.obj.get('duration')
    
    @property
    def waveform(self):
        return self.obj.get('waveform')
    
    @property
    def link_ogg(self):
        return self.obj.get('link_ogg')
    
    @property
    def link_mp3(self):
        return self.obj.get('link_mp3')