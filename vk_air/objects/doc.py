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
from __future__ import annotations
from typing import List, Optional
from .photo import PhotoSize

class DocPhoto:
    """
    Изображение для предпросмотра документа.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def sizes(self) -> Optional[List[PhotoSize]]:
        sizelist = []
        for i in self.obj.get('sizes'):
            sizelist.append(PhotoSize(i))
        return sizelist

class DocGraffiti:
    """
    Граффити для предпросмотра документа.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def src(self) -> str:
        return self.obj.get('src')
    
    @property
    def width(self) -> int:
        return self.obj.get('width')
    
    @property
    def height(self) -> int:
        return self.obj.get('height')

class DocAudioMessage:
    """
    Объект аудиосообщения.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def duration(self) -> int:
        return self.obj.get('duration')
    
    @property
    def waveform(self) -> List[int]:
        return self.obj.get('waveform')
    
    @property
    def link_ogg(self) -> str:
        return self.obj.get('link_ogg')
    
    @property
    def link_mp3(self) -> str:
        return self.obj.get('link_mp3')
    
    @property
    def link(self) -> str:
        return self.obj.get('link_mp3')

class DocPreview:
    """
    Информация для предварительного просмотра документа.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def photo(self) -> Optional[DocPhoto]:
        return DocPhoto(self.obj.get('photo')) if self.obj.get('photo') else None
    
    @property
    def graffiti(self) -> Optional[DocGraffiti]:
        return DocGraffiti(self.obj.get('graffiti')) if self.obj.get('graffiti') else None
    
    @property
    def audio_message(self) -> Optional[DocAudioMessage]:
        return DocAudioMessage(self.obj.get('audio_message')) if self.obj.get('audio_message') else None

class Doc:
    """
    Объект документа.
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
    def size(self) -> int:
        return self.obj.get('size')
    
    @property
    def ext(self) -> Optional[str]:
        return self.obj.get('ext')
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def date(self) -> int:
        return self.obj.get('date')
    
    @property
    def type(self) -> int:
        return self.obj.get('type')
    
    @property
    def preview(self) -> Optional[DocPreview]:
        return DocPreview(self.obj.get('preview')) if self.obj.get('preview') else None
    
    @property
    def access_key(self) -> Optional[str]:
        return self.obj.get('access_key')
    
    def to_attachment(self) -> str:
        if self.access_key:
            return f'doc{self.owner_id}_{self.id}_{self.access_key}'
        else:
            return f'doc{self.owner_id}_{self.id}'