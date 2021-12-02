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
class PhotoAttachment:
    """
    Вложенная фотография.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def photo(self) -> Optional[Photo]:
        return Photo(self.obj.get('photo')) if self.obj.get('photo') else None
    
from .postedphoto import PostedPhoto
class PostedPhotoAttachment:
    """
    Вложенная фотография, загруженная напрямую. LegacySupport.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def posted_photo(self) -> Optional[PostedPhoto]:
        return PostedPhoto(self.obj.get('posted_photo')) if self.obj.get('posted_photo') else None
    
from .video import Video
class VideoAttachment:
    """
    Вложенная видеозапись.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def video(self) -> Optional[Video]:
        return Video(self.obj.get('video')) if self.obj.get('video') else None
    
from .audio import Audio
class AudioAttachment:
    """
    Вложенная аудиозапись.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def audio(self) -> Optional[Audio]:
        return Audio(self.obj.get('audio')) if self.obj.get('audio') else None

from .doc import Doc 
class DocAttachment:
    """
    Вложенный документ.
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def doc(self) -> Optional[Doc]:
        return Doc(self.obj.get('doc')) if self.obj.get('doc') else None
    
class GraffitiAttachment:
    """
    Вложенный граффити.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('graffiti')
    
    @property
    def graffiti(self) -> Optional[PostedPhoto]:
        return PostedPhoto(self.obj.get('graffiti')) if self.obj.get('graffiti') else None

from .link import Link
class LinkAttachment:
    """
    Вложенная ссылка.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def link(self) -> Optional[Link]:
        return Link(self.obj.get('link')) if self.obj.get('link') else None
    
from .note import Note
class NoteAttachment:
    """
    Вложенная заметка.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def note(self) -> Optional[Note]:
        return Note(self.obj.get('note')) if self.obj.get('note') else None
    
class AppAttachment:
    """
    Вложенный контент приложения.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def app(self) -> Optional[PostedPhoto]:
        return PostedPhoto(self.obj.get('app')) if self.obj.get('app') else None

from .poll import Poll
class PollAttachment:
    """
    Вложенный опрос.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def poll(self) -> Optional[Poll]:
        return Poll(self.obj.get('poll')) if self.obj.get('poll') else None

from .page import Page
class PageAttachment:
    """
    Вложенная вики-страница.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def page(self) -> Optional[Page]:
        return Page(self.obj.get('page')) if self.obj.get('page') else None

from .album import Album  
class AlbumAttachment:
    """
    Вложенный альбом.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def album(self) -> Optional[Album]:
        return Album(self.obj.get('album')) if self.obj.get('album') else None

class PhotosListAttachment:
    """
    Вложенный список фотографий.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def photos_list(self) -> Optional[List[int]]:
        return self.obj.get('photos_list')

from .market import Market   
class MarketAttachment:
    """
    Вложенный товар.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def market(self) -> Optional[Market]:
        return Market(self.obj.get('market')) if self.obj.get('market') else None

from .album import MarketAlbum
class MarketAlbumAttachment:
    """
    Вложенная подборка товаров.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def market_album(self) -> Optional[MarketAlbum]:
        return MarketAlbum(self.obj.get('market_album')) if self.obj.get('market_album') else None

from .sticker import Sticker
class StickerAttachment:
    """
    Вложенный стикер.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def sticker(self) -> Optional[Sticker]:
        return Sticker(self.obj.get('sticker')) if self.obj.get('sticker') else None

from .pretty import PrettyCard
from .pretty import PrettyCards
class PrettyCardsAttachment:
    """
    Вложенный массив элементов-карточек.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def pretty_cards(self) -> Optional[PrettyCards]:
        return PrettyCards(self.obj.get('pretty_cards')) if self.obj.get('pretty_cards') else None

from .eventobj import Event
class EventAttachment:
    """
    Вложенная встреча.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def event(self) -> Optional[Event]:
        return Event(self.obj.get('event')) if self.obj.get('event') else None

class WallObj:
    """
    Вложенная запись на стене.
    """
    from .wall import Wall
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def wall(self) -> Optional[Wall]:
        from .wall import Wall
        return Wall(self.obj.get('wall')) if self.obj.get('wall') else None
    
from .comment import Comment
class WallReplyObj:
    """
    Вложенный комментарий на стене.
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def wall_reply(self) -> Optional[Comment]:
        return Comment(self.obj.get('wall_reply')) if self.obj.get('wall_reply') else None
    
from .gift import Gift
class GiftObj:
    """
    Вложенный подарок.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def type(self) -> str:
        return self.obj.get('type')
    
    @property
    def gift(self) -> Optional[Gift]:
        return Gift(self.obj.get('gift')) if self.obj.get('gift') else None


ATTACHMENTS = {
    'photo': PhotoAttachment,
    'posted_photo': PostedPhotoAttachment,
    'video': VideoAttachment,
    'audio': AudioAttachment,
    'doc': DocAttachment,
    'graffiti': PostedPhotoAttachment,
    'link': LinkAttachment,
    'note': NoteAttachment,
    'app': AppAttachment,
    'poll': PollAttachment,
    'page': PageAttachment,
    'album': AlbumAttachment,
    'photos_list': PhotosListAttachment,
    'market': MarketAttachment,
    'market_album': MarketAlbumAttachment,
    'sticker': StickerAttachment,
    'pretty_cards': PrettyCardsAttachment,
    'event': EventAttachment
}
