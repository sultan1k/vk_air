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
from io import TextIOWrapper
import random
from typing import List, Optional
from aiohttp import ClientSession
import json
from .objects.stories import Stories
from .objects.cover import SavedCoverPhoto, UploadedCoverPhoto
from .objects.storage import Storage
from .keyboard import Keyboard
from .objects.chat import Chat, ChatMembers
from .objects.conversation import Conversation, Conversations
from .objects.history import HistoryAttachments
from .objects.message import DeletedMessages, DeliveredMessage, Message, SavedMessagePhoto, UploadServer, UploadedMessagePhoto
from .objects.product import Product
from .template import Template
from .objects.callback import CallbackServer, CallbackSettings
from .objects.lp import LP
from .objects.online import GroupOnline
from .objects.tags import GroupTag
from .objects.audio import AudioMessage
from .objects.enumsobj import DocAttachment
from .objects.group import Group, GroupIsMember
from .objects.user import User
from .objects.app import AppImages
from .objects.doc import Doc
from .objects.ban import BanInfo
from .objects.order import Order
from .enums import BoolToInt, DeleteChatPhotoResponse

BASE = 'https://api.vk.com/method/'
VERSION = '5.131'

class BotApi:
    def __init__(
        self,
        *,
        dangerous_f, 
        encrypt_key,
        debug
    ) -> None:
        self.DANGEROUS_f = dangerous_f
        self._DANGEROUS_3nCR3pT_k3Y = encrypt_key
        self.group_id = None
        self.debug = debug

    async def request(self, method, url, params) -> dict:
        async with ClientSession() as session:
            methods = {
                'get': session.get,
                'post': session.post
            }
            method = methods[method]
            if method == session.get:
                async with method(url, params=params) as r:
                    r: dict = await r.json()
                await session.close()
            elif method == session.post:
                async with method(url, data=params) as r:
                    r: dict = await r.json()
                await session.close()
        return r
    
    # widgets management

    async def getAppImages(
        self,
        *,
        offset: Optional[int] = None,
        count: int,
        image_type: int
    ) -> Optional[AppImages]:
        fields = {
            'count': count,
            'image_type': image_type,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id
        }
        if offset:
            fields['offset'] = offset
        url = BASE + 'appWidgets.getAppImages?'
        r = await self.request('get', url, fields)
        return AppImages(r.get('response')) if r.get('response') else None
    
    async def getAppImagesById(
        self,
        *,
        images: List[str]
    ) -> Optional[AppImages]:
        fields = {
            'images': ','.join(i for i in images),
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id
        }
        url = BASE + 'appWidgets.getImagesById?'
        r = await self.request('get', url, fields)
        return AppImages(r.get('response')) if r.get('response') else None
    
    async def updateWidget(
        self,
        *,
        code: str,
        type: str
    ) -> int:
        fields = {
            'code': code,
            'type': type,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id
        }
        url = BASE + 'appWidgets.update?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    
    # board management
    
    async def deleteBoardComment(
        self,
        *,
        topic_id: int,
        comment_id: int
    ) -> int:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'topic_id': topic_id,
            'comment_id': comment_id
        }
        url = BASE + 'board.deleteComment?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def restoreBoardComment(
        self,
        *,
        topic_id: int,
        comment_id: int
    ) -> int:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'topic_id': topic_id,
            'comment_id': comment_id
        }
        url = BASE + 'board.restoreComment?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    # docs management
    
    async def docsGetById(
        self,
        *,
        docs: List[str],
        return_tags: int = 1
    ) -> Optional[List[Doc]]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'docs': ','.join(i for i in docs),
            'return_tags': return_tags
        }
        url = BASE + 'docs.getById?'
        docs_list = []
        r = await self.request('get', url, fields)
        for i in r.get('response'):
            docs_list.append(Doc(i))
        return docs_list
    
    async def getDocsMessagesUploadServer(
        self,
        *,
        type: str,
        peer_id: int
    ) -> str:
        fields = {
            'type': type,
            'peer_id': peer_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id
        }
        url = BASE + 'docs.getMessagesUploadServer?'
        r = await self.request('get', url, fields)
        return r['response'].get('upload_url') if r.get('response') else None
    
    async def getDocsWallUploadServer(self) -> str:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id
        }
        url = BASE + 'docs.getWallUploadServer?'
        r = await self.request('get', url, fields)
        return r['response'].get('upload_url') if r.get('response') else None
    
    async def docsSave(
        self,
        *,
        file: str,
        title: str = None,
        tags: str = None,
        return_tags: int = 1
    ) -> DocAttachment | AudioMessage | None:
        fields = {
            'file': file,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'return_tags': return_tags
        }
        if title:
            fields['title'] = title
        if tags:
            fields['tags'] = tags
        url = BASE + 'docs.save?'
        r = await self.request('post', url, fields)
        if r.get('response'):
            if r['response']['type'] == 'doc':
                return DocAttachment(r)
            elif r['response']['type'] == 'audio_message':
                return AudioMessage(r)
        else: return
    
    async def docsSearch(
        self,
        *,
        q: str,
        search_own: int = 0,
        count: int = 20,
        offset: int = 0,
        return_tags: int = 1
    ) -> Optional[List[Doc]]:
        fields = {
            'q': q,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'search_own': search_own,
            'count': count,
            'offset': offset,
            'return_tags': return_tags
        }
        url = BASE + 'docs.search?'
        r = await self.request('get', url, fields)
        doc_list = []
        for i in r['response']['items']:
            doc_list.append(Doc(i))
        return doc_list
    
    async def execute(
        self,
        *,
        code: str,
        func_v: int = None
    ) -> Optional[dict]:
        fields = {
            'code': code,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id
        }
        if func_v:
            fields['func_v'] = func_v
        url = BASE + 'execute?'
        r = await self.request('post', url, fields)
        return r.get('response')
    
    # group management

    async def groupsAddAddress(
        self,
        *,
        title: str,
        address: str,
        additional_address: Optional[str] = None,
        country_id: int,
        city_id: int,
        metro_id: int = None,
        latitude: float,
        longitude: float,
        phone: str = None,
        work_info_status: str = None,
        timetable: dict = None,
        is_main_address: int = 0
    ) -> Optional[dict]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'title': title,
            'address': address,
            'country_id': country_id,
            'city_id': city_id,
            'latitude': latitude,
            'longitude': longitude,
            'is_main_address': is_main_address
        }
        if additional_address:
            fields['additional_address'] = additional_address
        if metro_id:
            fields['metro_id'] = metro_id
        if phone:
            fields['phone'] = phone
        if work_info_status:
            fields['work_info_status'] = work_info_status
        if timetable:
            fields['timetable'] = timetable
        url = BASE + 'groups.addAddress?'
        r = await self.request('post', url, fields)
        return r.get('response')
    
    async def groupsAddCallbackServer(
        self,
        *,
        url: str,
        title: str,
        secret_key: Optional[str] = None
    ) -> Optional[int]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'url': url,
            'title': title
        }
        if secret_key:
            fields['secret_key'] = secret_key
        url = BASE + 'groups.addCallbackServer?'
        r = await self.request('post', url, fields)
        return r['response'].get('server_id') if r.get('response') else None
    
    async def groupsDeleteAddress(self, *, address_id: int) -> int:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'address_id': address_id
        }
        url = BASE + 'groups.deleteAddress?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsDeleteCallbackServer(self, *, server_id: int) -> int:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'server_id': server_id
        }
        url = BASE + 'groups.deleteCallbackServer?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsDisableOnline(self) -> int:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id
        }
        url = BASE + 'groups.disableOnline?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsEdit(
        self,
        *,
        title: str = None,
        description: str = None,
        screen_name: str = None,
        access: int = None,
        website: str = None,
        subject: str = None,
        email: str = None,
        phone: str = None,
        public_date: str = None,
        wall: int = None,
        topics: int = None,
        photos: int = None,
        video: int = None,
        audio: int = None,
        links: int = None,
        events: int = None,
        places: int = None,
        contacts: int = None,
        docs: int = None,
        wiki: int = None,
        messages: int = None,
        articles: int = None,
        addresses: int = None,
        age_limits: int = None,
        market: int = None,
        market_comments: int = None,
        market_country: str = None,
        market_city: str = None,
        market_currency: int = None,
        market_contact: int = None,
        market_wiki: int = None,
        obscene_filter: int = None,
        obscene_stopwords: int = None,
        obscene_words: str = None,
        main_section: int = None,
        secondary_section: int = None,
        country: int = None,
        city: int = None
    ) -> int:
        url = BASE + 'groups.edit?'
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id
        }
        if title:
            fields['title'] = title
        if description:
            fields['description'] = description
        if screen_name:
            fields['screen_name'] = screen_name
        if access:
            fields['access'] = access
        if website:
            fields['website'] = website
        if subject:
            fields['subject'] = subject
        if email:
            fields['email'] = email
        if phone:
            fields['phone'] = phone
        if public_date:
            fields['public_date'] = public_date
        if wall:
            fields['wall'] = wall
        if topics:
            fields['topics'] = topics
        if photos:
            fields['photos'] = photos
        if video:
            fields['video'] = video
        if audio:
            fields['audio'] = audio
        if links:
            fields['links'] = links
        if events:
            fields['events'] = events
        if places:
            fields['places'] = places
        if contacts:
            fields['contacts'] = contacts
        if docs:
            fields['docs'] = docs
        if wiki:
            fields['wiki'] = wiki
        if messages:
            fields['messages'] = messages
        if articles:
            fields['articles'] = articles
        if addresses:
            fields['addresses'] = addresses
        if age_limits:
            fields['age_limits'] = age_limits
        if market:
            fields['market'] = market
        if market_comments:
            fields['market_comments'] = market_comments
        if market_country:
            fields['market_country'] = market_country
        if market_city:
            fields['market_city'] = market_city
        if market_currency:
            fields['market_currency'] = market_currency
        if market_contact:
            fields['market_contact'] = market_contact
        if market_wiki:
            fields['market_wiki'] = market_wiki
        if obscene_filter:
            fields['obscene_filter'] = obscene_filter
        if obscene_stopwords:
            fields['obscene_stopwords'] = obscene_stopwords
        if obscene_words:
            fields['obscene_words'] = obscene_words
        if main_section:
            fields['main_section'] = main_section
        if secondary_section:
            fields['secondary_section'] = secondary_section
        if country:
            fields['country'] = country
        if city:
            fields['city'] = city
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsEditAddress(
        self,
        *,
        address_id: int,
        title: str = None,
        address: str = None,
        additional_address: str = None,
        country_id: int = None,
        city_id: int = None,
        metro_id: int = None,
        latitude: float = None,
        longitude: float = None,
        phone: str = None,
        work_info_status: str = None,
        timetable: dict = None,
        is_main_address: int = None
    ) -> Optional[dict]:
        fields = {
            'address_id': address_id,
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if title:
            fields['title'] = title
        if address:
            fields['address'] = address
        if additional_address:
            fields['additional_address'] = additional_address
        if country_id:
            fields['country_id'] = country_id
        if city_id:
            fields['city_id'] = city_id
        if metro_id:
            fields['metro_id'] = metro_id
        if latitude:
            fields['latitude'] = latitude
        if longitude:
            fields['longitude'] = longitude
        if phone:
            fields['phone'] = phone
        if work_info_status:
            fields['work_info_status'] = work_info_status
        if timetable:
            fields['timetable'] = timetable.obj
        if is_main_address:
            fields['is_main_address'] = is_main_address
        url = BASE + 'groups.editAddress?'
        r = await self.request('post', url, fields)
        return r

    async def groupsEditCallbackServer(
        self,
        *,
        server_id: int,
        url: str,
        title: str,
        secret_key: str = None
    ) -> int:
        fields = {
            'group_id': self.group_id,
            'server_id': server_id,
            'url': url,
            'title': title,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if secret_key:
            fields['secret_key'] = secret_key
        url = BASE + 'groups.editCallbackServer?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsEnableOnline(self) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        url = BASE + 'groups.enableOnline?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsGetBanned(
        self,
        *,
        offset: int = 0,
        count: int = 20,
        owner_id: Optional[int] = None
    ) -> Optional[List]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'count': count,
            'offset': offset
        }
        if owner_id:
            fields['owner_id'] = owner_id
        url = BASE + 'groups.getBanned?'
        r = await self.request('get', url, fields)
        banned_list = []
        baninfo_list = []
        try:
            r = r['response']['items']
            for i in r:
                if i['type'] == 'group':
                    banned_list.append(Group(i['group']))
                else:
                    banned_list.append(User(i['profile']))
                baninfo_list.append(BanInfo(i['ban_info']))
        except KeyError: pass
        return [banned_list, baninfo_list]

    async def groupsGetById(
        self,
        *,
        group_id: int = None,
        group_ids: List[int] = None
    ) -> Optional[List[Group]]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if group_id:
            fields['group_id'] = str(group_id)
        if group_ids:
            fields['group_ids'] = ','.join(group_ids)
        url = BASE + 'groups.getById?'
        r = await self.request('get', url, fields)
        group_list = []
        try:
            for i in r['response']:
                group_list.append(Group(i))
        except KeyError:
            pass
        return group_list
    
    async def groupsGetConfirmCode(self) -> Optional[int]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        url = BASE + 'groups.getCallbackConfirmationCode?'
        r = await self.request('get', url, fields)
        return r['response'].get('code') if r.get('response') else None
    
    async def groupsGetCallbackServers(self, *, server_ids: List[int] = None) -> Optional[List[CallbackServer]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if server_ids:
            fields['server_ids'] = ','.join(server_ids)
        url = BASE + 'groups.getCallbackServers?'
        r = await self.request('get', url, fields)
        server_list = []
        for i in r['response']['items']:
            server_list.append(CallbackServer(i))
        return server_list

    async def groupsGetCallbackSettings(self, *, server_id: int = None) -> Optional[CallbackSettings]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if server_id:
            fields['server_id'] = server_id
        url = BASE + 'groups.getCallbackSettings?'
        r = await self.request('get', url, fields)
        return CallbackSettings(r['response']['events']) if r.get('response') else None

    async def groupsGetLongPollServer(self) -> Optional[LP]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        url = BASE + 'groups.getLongPollServer?'
        r = await self.request('get', url, fields)
        return LP(r['response']) if r.get('response') else None
    
    async def groupsGetLongPollSettings(self) -> Optional[CallbackSettings]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        url = BASE + 'groups.getLongPollSettings?'
        r = await self.request('get', url, fields)
        return CallbackSettings(r['response']['events']) if r.get('response') else None

    async def groupsGetMembers(
        self,
        *,
        sort: str = 'id_asc',
        offset: int = 0,
        count: int = 1000,
        filter: str = None
    ) -> Optional[List[int]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'sort': sort,
            'offset': offset,
            'count': count
        }
        if filter:
            fields['filter'] = filter
        url = BASE + 'groups.getMembers?'
        r = await self.request('get', url, fields)
        return r['response']['items'] if r.get('response') else None
    
    async def groupsGetOnlineStatus(self) -> Optional[GroupOnline]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        url = BASE + 'groups.getOnlineStatus?'
        r = await self.request('get', url, fields)
        return GroupOnline(r['response']) if r.get('response') else None
    
    async def groupsGetTagList(self) -> Optional[List[GroupTag]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        url = BASE + 'groups.getTagList?'
        r = await self.request('get', url, fields)
        taglist = []
        for i in r['response']:
            taglist.append(GroupTag(i))
        return taglist
    
    async def groupsIsMember(self, *, user_ids: List[int]) -> Optional[List[GroupIsMember]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'user_ids': ','.join(user_ids)
        }
        url = BASE + 'groups.isMember?'
        r = await self.request('get', url, fields)
        userlist = []
        if type(r['response']) == list:
            for i in r['response']:
                userlist.append(GroupIsMember(i))
        elif type(r['response']) == dict:
            userlist.append(GroupIsMember(r['response']))
        return userlist
    
    async def groupsSetCallbackSettings(self, **kwargs) -> int:
        for i in kwargs:
            kwargs[i] = BoolToInt[kwargs[i]]
        kwargs['group_id'] = self.group_id
        kwargs['access_token'] = self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
        kwargs['v'] = VERSION
        url = BASE + 'groups.setCallbackSettings?'
        r = await self.request('post', url, kwargs)
        return 1 if r.get('response') else 0
    
    async def groupsSetLongPollSettings(self, **kwargs) -> int:
        for i in kwargs:
            kwargs[i] = BoolToInt[kwargs[i]]
        kwargs['group_id'] = self.group_id
        kwargs['access_token'] = self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
        kwargs['v'] = VERSION
        url = BASE + 'groups.setLongPollSettings?'
        r = await self.request('post', url, kwargs)
        return 1 if r.get('response') else 0
    
    async def groupsSetSettings(self, **kwargs) -> int:
        for i in kwargs:
            kwargs[i] = BoolToInt[kwargs[i]]
        kwargs['group_id'] = self.group_id
        kwargs['access_token'] = self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
        kwargs['v'] = VERSION
        url = BASE + 'groups.setSettings?'
        r = await self.request('post', url, kwargs)
        return 1 if r.get('response') else 0
    
    async def groupsSetUserNote(self, *, user_id: int, note: str) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'user_id': user_id,
            'note': note
        }
        url = BASE + 'groups.setUserNote?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsAddTag(self, *, name: str, color: str) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'tag_name': name,
            'tag_color': color
        }
        url = BASE + 'groups.tagAdd?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsBindTag(self, *, tag_id: int, user_id: int, act: str) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'tag_id': tag_id,
            'user_id': user_id,
            'act': act
        }
        url = BASE + 'groups.tagBind?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsDeleteTag(self, *, tag_id: int) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'tag_id': tag_id
        }
        url = BASE + 'groups.tagDelete?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def groupsUpdateTag(self, *, tag_id: int, tag_name: str) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'tag_id': tag_id,
            'tag_name': tag_name
        }
        url = BASE + 'groups.tagUpdate?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    # market management

    async def marketEditOrder(
        self,
        *,
        user_id: int,
        order_id: int,
        merchant_comment: str = None,
        status: int = None,
        track_number: str = None,
        payment_status: str = None,
        delivery_price: int = None,
        width: int = None,
        length: int = None,
        height: int = None,
        weight: int = None,
        comment_for_user: str = None, # будет доступно с версии 5.139
        receipt_link: str = None # будет доступно с версии 5.159
    ) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'user_id': user_id,
            'order_id': order_id
        }
        if merchant_comment:
            fields['merchant_comment'] = merchant_comment
        if status:
            fields['status'] = status
        if track_number:
            fields['track_number'] = track_number
        if payment_status:
            fields['payment_status'] = payment_status
        if delivery_price:
            fields['delivery_price'] = delivery_price
        if width:
            fields['width'] = width
        if length:
            fields['length'] = length
        if height:
            fields['height'] = height
        if weight:
            fields['weight'] = weight
        if comment_for_user:
            fields['comment_for_user'] = comment_for_user
        if receipt_link:
            fields['receipt_link'] = receipt_link
        url = BASE + 'market.editOrder?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def marketGetOrders(self, *, offset: int = 0, count: int = 10) -> Optional[List[Order]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'offset': offset,
            'count': count
        }
        url = BASE + 'market.getGroupOrders?'
        r = await self.request('get', url, fields)
        orderlist = []
        for i in r['response']['items']:
            orderlist.append(Order(i))
        return orderlist
    
    async def marketGetOrder(self, *, order_id: int, user_id: int = None, extended: int = None) -> Optional[Order]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'order_id': order_id
        }
        if user_id:
            fields['user_id'] = user_id
        if extended:
            fields['extended'] = extended
        url = BASE + 'market.getOrtderById?'
        r = await self.request('get', url, fields)
        return Order(r['response']) if r.get('response') else None
    
    async def marketGetOrderItems(self, *, order_id: int, user_id: int = None, offset: int = 0, count: int = 50) -> Optional[List[Product]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'order_id': order_id,
            'offset': offset,
            'count': count
        }
        if user_id:
            fields['user_id'] = user_id
        url = BASE + 'market.getOrderItems?'
        r = await self.request('get', url, fields)
        items = []
        for i in r['response']['items']:
            items.append(Product(i))
        return items
    
    # messages management

    async def messagesCreateChat(self, *, title: str) -> Optional[int]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'title': title
        }
        url = BASE + 'messages.createChat?'
        r = await self.request('post', url, fields)
        return r.get('response')
    
    async def messagesDelete(self, *, message_ids: List[int] = None, delete_for_all: int = 1, peer_id: int, conversation_message_ids: List[int] = None) -> Optional[DeletedMessages]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'delete_for_all': delete_for_all,
            'peer_id': peer_id
        }
        if conversation_message_ids:
            fields['conversation_message_ids'] = ','.join(conversation_message_ids)
        if message_ids:
            fields['message_ids'] = ','.join(message_ids)
        url = BASE + 'messages.delete?'
        r = await self.request('post', url, fields)
        return DeletedMessages(r['response']) if r.get('response') else None
    
    async def messagesDeleteChatPhoto(self, *, chat_id: int) -> Optional[DeleteChatPhotoResponse]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'chat_id': chat_id
        }
        url = BASE + 'messages.deleteChatPhoto?'
        r = await self.request('post', url, fields)
        return DeleteChatPhotoResponse(r['response']) if r.get('response') else None
    
    async def messagesDeleteChat(self, *, user_id: int = None, peer_id: int = None) -> Optional[int]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if not user_id and not peer_id:
            return
        if user_id:
            fields['user_id'] = user_id
        if peer_id:
            fields['peer_id'] = peer_id
        url = BASE + 'messages.deleteConversation?'
        r = await self.request('post', url, fields)
        return r['response']['last_deleted_id'] if r.get('response') else None
    
    async def messagesEdit(
        self,
        *,
        peer_id: int,
        text: str = None,
        lat: float = None,
        long: float = None,
        attachment: str = None,
        keep_forward_messages: int = 1,
        keep_snippets: int = 1,
        dont_parse_links: int = 0,
        disable_mentions: int = 0,
        message_id: int = None,
        conversation_message_id: int = None,
        keyboard: Keyboard = None,
        template: Template = None
    ) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id,
            'keep_forward_messages': keep_forward_messages,
            'keep_snippets': keep_snippets,
            'dont_parse_links': dont_parse_links,
            'disable_mentions': disable_mentions
        }
        if text:
            fields['message'] = text
        if lat:
            fields['lat'] = lat
        if long:
            fields['long'] = long
        if attachment:
            fields['attachment'] = attachment
        if keyboard:
            fields['keyboard'] = keyboard.fields
        if template:
            fields['template'] = template.fields
        if dont_parse_links:
            fields['dont_parse_links'] = dont_parse_links
        if disable_mentions:
            fields['disable_mentions'] = disable_mentions
        if keep_forward_messages:
            fields['keep_forward_messages'] = keep_forward_messages
        if keep_snippets:
            fields['keep_snippets'] = keep_snippets
        if message_id:
            fields['message_id'] = message_id
        if conversation_message_id:
            fields['conversation_message_id'] = conversation_message_id
        url = BASE + 'messages.edit?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0

    async def messagesEditChat(self, *, chat_id: int, title: str) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'chat_id': chat_id,
            'title': title
        }
        url = BASE + 'messages.editChat?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def messagesGetByConversationMessageId(self, *, peer_id: int, conversation_message_ids: List[int], extended: int = 0) -> Optional[List[Message]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id,
            'conversation_message_ids': ','.join(conversation_message_ids),
            'extended': extended
        }
        url = BASE + 'messages.getByConversationMessageId?'
        r = await self.request('get', url, fields)
        messagelist = []
        for i in r['response']['items']:
            messagelist.append(Message(i, self))
        return messagelist
    
    async def messagesGetById(self, *, message_ids: List[int], preview_length: int = 0, extended: int = 0) -> Optional[List[Message]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'message_ids': ','.join(message_ids),
            'preview_length': preview_length,
            'extended': extended
        }
        url = BASE + 'messages.getById?'
        r = await self.request('get', url, fields)
        messagelist = []
        for i in r['response']['items']:
            messagelist.append(Message(i, self))
        return messagelist
    
    async def messagesGetConversationMembers(self, *, peer_id: int) -> Optional[ChatMembers]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id
        }
        url = BASE + 'messages.getConversationMembers?'
        r = await self.request('get', url, fields)
        return ChatMembers(r['response']) if r.get('response') else None
    
    async def messagesGetConversations(self) -> Optional[Conversations]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        url = BASE + 'messages.getConversations?'
        r = await self.request('get', url, fields)
        return Conversations(r['response']) if r.get('response') else None
    
    async def messagesGetConversationsById(self, *, peer_ids: List[int], extended: int = 0) -> Optional[List[Conversation]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_ids': ','.join(peer_ids),
            'extended': extended
        }
        url = BASE + 'messages.getConversationsById?'
        r = await self.request('get', url, fields)
        conversationlist = []
        for i in r['response']['items']:
            conversationlist.append(Conversation(i))
        return conversationlist
    
    async def messagesGetHistory(
        self,
        *,
        offset: int = 0,
        count: int = 20,
        user_id: int = None,
        peer_id: int = None,
        start_message_id: int = None,
        rev: int = 0,
        extended: int = 0
    ) -> Optional[List[Message]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'offset': offset,
            'count': count,
            'rev': rev,
            'extended': extended
        }
        url = BASE + 'messages.getHistory?'
        if user_id:
            fields['user_id'] = user_id
        if peer_id:
            fields['peer_id'] = peer_id
        if start_message_id:
            fields['start_message_id'] = start_message_id
        r = await self.request('get', url, fields)
        history = []
        for i in r['response']['items']:
            history.append(Message(i, self))
        return history
    
    async def messagesGetHistoryAttachments(
        self,
        *,
        peer_id: int,
        media_type: str = 'photo',
        start_from: str = None,
        count: int = 30,
        photo_sizes: int = 0,
        preserve_order: int = 1,
        max_forwards_level: int = 45
    ) -> Optional[HistoryAttachments]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id,
            'media_type': media_type,
            'count': count,
            'photo_sizes': photo_sizes,
            'preserve_order': preserve_order,
            'max_forwards_level': max_forwards_level
        }
        if start_from:
            fields['start_from'] = start_from
        url = BASE + 'messages.getHistoryAttachments?'
        r = await self.request('get', url, fields)
        return HistoryAttachments(r['response']) if r.get('response') else None
    
    async def messagesGetImportantMessages(
        self,
        *,
        offset: int = 0,
        count: int = 20,
        start_message_id: int = None,
        extended: int = 0,
        preview_length: int = 0
    ) -> Optional[List[Message]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'offset': offset,
            'count': count,
            'extended': extended,
            'preview_length': preview_length
        }
        if start_message_id:
            fields['start_message_id'] = start_message_id
        url = BASE + 'messages.getImportantMessages?'
        r = await self.request('get', url, fields)
        important = []
        for i in r['response']['items']:
            important.append(Message(i, self))
        return important
    
    async def messagesGetInviteLink(self, *, peer_id: int, reset: int = 0) -> Optional[str]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id,
            'reset': reset
        }
        url = BASE + 'messages.getInviteLink?'
        r = await self.request('get', url, fields)
        return r['response'].get('link') if r.get('response') else None
    
    async def messagesGetLongPollHistory(
        self,
        *,
        ts: int,
        pts: int,
        preview_length: int = 0,
        onlines: int = 0,
        events_limit: int = 1000,
        msgs_limit: int = 200,
        max_msg_id: int = None,
        lp_version: int = 3,
        last_n: int = 0,
        credentials: int = 0
    ) -> Optional[List[Message]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'ts': ts,
            'pts': pts,
            'preview_length': preview_length,
            'onlines': onlines,
            'events_limit': events_limit,
            'msgs_limit': msgs_limit,
            'lp_version': lp_version,
            'last_n': last_n,
            'credentials': credentials
        }
        if max_msg_id:
            fields['max_msg_id'] = max_msg_id
        url = BASE + 'messages.getLongPollHistory?'
        r = await self.request('get', url, fields)
        messagelist = []
        for i in r['response']['messages']['items']:
            messagelist.append(Message(i, self))
        return messagelist
    
    async def messagesGetLongPollServer(self) -> Optional[LP]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'need_pts': 1,
            'lp_version': 3
        }
        url = BASE + 'messages.getLongPollServer?'
        r = await self.request('get', url, fields)
        return LP(r['response']) if r.get('response') else None
    
    async def messagesIsMessagesFromGroupAllowed(self, *, user_id: int) -> bool:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'user_id': user_id
        }
        url = BASE + 'messages.isMessagesFromGroupAllowed?'
        r = await self.request('get', url, fields)
        return r['response']['is_allowed'] if r.get('response') else None
    
    async def messagesMarkAsAnsweredConversation(self, *, peer_id: int, answered: int = 1) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id,
            'answered': answered
        }
        url = BASE + 'messages.markAsAnsweredConversation?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def messagesMarkAsImportantConversation(self, *, peer_id: int, important: int = 1) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id,
            'important': important
        }
        url = BASE + 'messages.markAsImportantConversation?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def messagesMarkAsRead(self, *, peer_id: int, start_message_id: int = None, mark_conversation_as_read: int = 1) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id,
            'mark_conversation_as_read': mark_conversation_as_read
        }
        if start_message_id:
            fields['start_message_id'] = start_message_id
        url = BASE + 'messages.markAsRead?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def messagesPin(self, *, peer_id: int, message_id: int = None, conversation_message_id: int = None) -> Optional[Message]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id
        }
        if message_id:
            fields['message_id'] = message_id
        if conversation_message_id:
            fields['conversation_message_id'] = conversation_message_id
        url = BASE + 'messages.pin?'
        r = await self.request('post', url, fields)
        return Message(r['response'], self) if r.get('response') else None
    
    async def messagesRemoveChatUser(self, *, chat_id: int, member_id: int) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'chat_id': chat_id,
            'member_id': member_id
        }
        url = BASE + 'messages.removeChatUser?'
        r = await self.request('post', url, fields)
        return 1 if r.get("response") else 0
    
    async def messagesRestore(self, *, message_id: int) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'message_id': message_id
        }
        url = BASE + 'messages.restore?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def messagesSearch(
        self,
        *,
        q: str = None,
        peer_id: int = None,
        date: int = None,
        preview_length: int = 0,
        offset: int = 0,
        count: int = 20,
        extended: int = 0
    ) -> Optional[List[Message]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'preview_length': preview_length,
            'offset': offset,
            'count': count,
            'extended': extended
        }
        if q:
            fields['q'] = q
        if peer_id:
            fields['peer_id'] = peer_id
        if date:
            fields['date'] = date
        if offset:
            fields['offset'] = offset
        url = BASE + 'messages.search?'
        r = await self.request('get', url, fields)
        qlist = []
        for i in r['response']['items']:
            qlist.append(Message(i, self))
        return qlist
    
    async def messagesSearchConversations(self, *, q: str, count: int = 20, extended: int = 0) -> Optional[List[Conversation]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'count': count,
            'extended': extended,
            'q': q
        }
        url = BASE + 'messages.searchConversations?'
        r = await self.request('get', url, fields)
        qlist = []
        for i in r['response']['items']:
            qlist.append(Conversation(i))
        return qlist
    
    async def messagesSend(
        self,
        text: str = None,
        *,
        peer_id: int = None,
        peer_ids: List[int] = None,
        lat: int = None,
        long: int = None,
        attachment: str = None,
        reply_to: int = None,
        forward_messages: int = None,
        sticker_id: int = None,
        keyboard: Keyboard = None,
        template: Template = None,
        payload: dict | str = None,
        content_source: dict = None,
        dont_parse_links: int = None,
        disable_mentions: int = None,
        intent: str = None,
        subscribe_id: int = None
    ) -> int | List[DeliveredMessage]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'random_id': random.randint(0, 5000)
        }
        if peer_id:
            fields['peer_id'] = peer_id
        if peer_ids:
            fields['peer_ids'] = peer_ids
        if text:
            fields['message'] = text
        if lat:
            fields['lat'] = lat
        if long:
            fields['long'] = long
        if attachment:
            fields['attachment'] = attachment
        if reply_to:
            fields['reply_to'] = reply_to
        if keyboard:
            fields['keyboard'] = json.dumps(keyboard.fields)
        if forward_messages:
            fields['forward_messages'] = forward_messages
        if sticker_id:
            fields['sticker_id'] = sticker_id
        if template:
            fields['template'] = json.dumps(template.fields)
        if payload:
            if type(payload) == str:
                fields['payload'] = {'command': payload}
            elif type(payload) == dict:
                fields['payload'] = payload
        if content_source:
            fields['content_source'] = content_source
        if dont_parse_links:
            fields['dont_parse_links'] = dont_parse_links
        if disable_mentions:
            fields['disable_mentions'] = disable_mentions
        if intent:
            fields['intent'] = intent
        if subscribe_id:
            fields['subscribe_id'] = subscribe_id
        url = BASE + 'messages.send?'
        r = await self.request('post', url, fields)
        if peer_id:
            return 1 if r.get('response') else 0
        elif peer_ids:
            msglist = []
            for i in r['response']:
                msglist.append(DeliveredMessage(i))
            return msglist
        else:
            return 0
    
    async def messagesSendEventAnswer(self, *, event_id: str, user_id: int, peer_id: int, event_data: dict) -> int:
        fields = {
            'event_id': event_id,
            'user_id': user_id,
            'peer_id': peer_id,
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'event_data': event_data
        }
        url = BASE + 'messages.sendMessageEventAnswer?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def messagesSetActivity(self, *, type: str, peer_id: int) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'type': type,
            'peer_id': peer_id
        }
        url = BASE + 'messages.setActivity?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def messagesSetChatPhoto(self, *, file: str) -> Optional[Chat]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'file': file
        }
        url = BASE + 'messages.setChatPhoto?'
        r = await self.request('post', url, fields)
        return Chat(r['response']['chat']) if r.get('response') else None
    
    async def messagesUnpin(self, *, peer_id: int) -> int:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'peer_id': peer_id
        }
        url = BASE + 'messages.unpin?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    # photo management

    async def photosGetChatUploadServer(self, *, chat_id: int, crop_x: int = None, crop_y: int = None, crop_width: int = None) -> Optional[str]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'chat_id': chat_id
        }
        if crop_width:
            fields['crop_width'] = crop_width
        if crop_x:
            fields['crop_x'] = crop_x
        if crop_y:
            fields['crop_y'] = crop_y
        url = BASE + 'photos.getChatUploadServer?'
        r = await self.request('get', url, fields)
        return r['response']['upload_url'] if r.get('response') else None
    
    async def photosGetMessagesUploadServer(self) -> Optional[UploadServer]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        url = BASE + 'photos.getMessagesUploadServer?'
        r = await self.request('get', url, fields)
        return UploadServer(r['response']) if r.get('response') else None
    
    async def photosGetCoverUploadServer(self, *, crop_x: int = 0, crop_y: int = 0, crop_x2: int = 795, crop_y2: int = 200) -> Optional[str]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'crop_x': crop_x,
            'crop_y': crop_y,
            'crop_x2': crop_x2,
            'crop_y2': crop_y2
        }
        url = BASE + 'photos.getOwnerCoverPhotoUploadServer?'
        r = await self.request('get', url, fields)
        return r['response']['upload_url'] if r.get('response') else None
    
    async def photosSaveMessagesPhoto(self, *, photo: str, server: int, hash: str) -> Optional[SavedMessagePhoto]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'photo': photo,
            'server': server,
            'hash': hash
        }
        url = BASE + 'photos.saveMessagesPhoto?'
        r = await self.request('post', url, fields)
        return SavedMessagePhoto(r['response'][0]) if r.get('response') else None
    
    async def photosSaveCover(self, *, hash: str, photo: str) -> Optional[List[SavedCoverPhoto]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'hash': hash,
            'photo': photo
        }
        url = BASE + 'photos.saveOwnerCoverPhoto?'
        r = await self.request('post', url, fields)
        coverlist = []
        for i in r['response']['images']:
            coverlist.append(SavedCoverPhoto(i))
        return coverlist
    
    # uploading files to server

    async def uploadMessagesPhoto(self, *, upload_url: str, photo: TextIOWrapper) -> UploadedMessagePhoto:
        fields = {
            'photo': photo
        }
        async with ClientSession() as session:
            async with session.post(upload_url, data=fields) as r:
                r = await r.json()
            await session.close()
        return UploadedMessagePhoto(r)
    
    async def uploadMessagesAudio(self, *, upload_url: str, file: TextIOWrapper) -> Optional[str]:
        fields = {
            'file': file
        }
        async with ClientSession() as session:
            async with session.post(upload_url, data=fields) as r:
                r = await r.json()
            await session.close()
        return r.get('file')
    
    async def uploadStories(self, *, type: str, file: TextIOWrapper, upload_url: str) -> Optional[str]:
        fields = {}
        if type == 'photo':
            fields['file'] = file
        else:
            fields['video_file'] = file
        async with ClientSession() as session:
            async with session.post(upload_url, data=fields) as r:
                r = await r.json()
            await session.close()
        return r.get('upload_result')
    
    async def uploadChatPhoto(self, *, upload_url: str, file: TextIOWrapper) -> Optional[str]:
        fields = {
            'file': file
        }
        async with ClientSession() as session:
            async with session.post(upload_url, data=fields) as r:
                r = await r.json()
            await session.close()
        return r.get('response')
    
    async def uploadDoc(self, *, upload_url: str, file: TextIOWrapper) -> Optional[str]:
        fields = {
            'file': file
        }
        async with ClientSession() as session:
            async with session.post(upload_url, data=fields) as r:
                r = await r.json()
            await session.close()
        return r.get('file')
    
    async def uploadCover(self, *, upload_url: str, photo: TextIOWrapper) -> UploadedCoverPhoto:
        fields = {
            'photo': photo
        }
        async with ClientSession() as session:
            async with session.post(upload_url, data=fields) as r:
                r = await r.json()
            await session.close()
        return UploadedCoverPhoto(r)

    # podcast management

    async def podcastSearch(self, *, search_string: str, offset: int = 0, count: int = 20) -> dict:
        fields = {
            'search_string': search_string,
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'offset': offset,
            'count': count
        }
        url = BASE + 'podcasts.searchPodcast?'
        return await self.request('get', url, fields)

    # storage management

    async def storageGet(self, *, key: str = None, keys: List[str] = None) -> Optional[List[Storage]]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if key:
            fields['key'] = key
        if keys:
            fields['keys'] = ','.join(keys)
        url = BASE + 'storage.get?'
        r = await self.request('get', url, fields)
        storagelist = []
        for i in r['response']:
            storagelist.append(Storage(i))
        return storagelist
    
    async def storageGetKeys(self, *, offset: int = 0, count: int = 100) -> Optional[dict]:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'offset': offset,
            'count': count
        }
        url = BASE + 'storage.getKeys?'
        r = await self.request('get', url, fields)
        return r.get('response')

    async def storageSet(self, *, key: str, value: Optional[str] = '', user_id: int = None) -> bool:
        fields = {
            'group_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'key': key,
            'value': value
        }
        url = BASE + 'storage.set?'
        if user_id:
            fields['user_id'] = user_id
        r = await self.request('post', url, fields)
        return True if r.get('response') else False
    
    # stories management

    async def storiesDelete(self, *, story_id: Optional[int] = None, stories: Optional[List[int]] = None) -> bool:
        fields = {
            'owner_id': self.group_id,
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if story_id:
            fields['story_id'] = story_id
        if stories:
            fields['stories'] = ','.join(stories)
        url = BASE + 'stories.delete?'
        r = await self.request('post', url, fields)
        return True if r.get('response') else False
    
    async def storiesGet(self, *, owner_id: Optional[int] = None) -> Optional[List[Stories]]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION
        }
        if owner_id:
            fields['owner_id'] = owner_id
        url = BASE + 'stories.get?'
        r = await self.request('get', url, fields)
        stories = []
        for i in r['response']['items']['stories']:
            stories.append(Stories(i))
        return stories
    
    async def storiesGetById(self, *, stories: str) -> Optional[List[Stories]]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'stories': stories
        }
        url = BASE + 'stories.getById?'
        r = await self.request('get', url, fields)
        stories: list = []
        for i in r['response']['items']:
            stories.append(Stories(i))
        return stories
    
    async def storiesGetPhotoUploadServer(
        self,
        *,
        add_to_news: int = 1,
        user_ids: Optional[List[int]] = None,
        reply_to_story: Optional[str] = None,
        link_text: Optional[str] = None,
        link_url: Optional[str] = None     
    ) -> Optional[str]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'group_id': self.group_id,
            'add_to_news': add_to_news
        }
        if user_ids:
            fields['user_ids'] = ','.join(user_ids)
        if reply_to_story:
            fields['reply_to_story'] = reply_to_story
        if link_text:
            fields['link_text'] = link_text
        if link_url:
            fields['link_url'] = link_url
        url = BASE + 'stories.getPhotoUploadServer?'
        r = await self.request('get', url, fields)
        return r['response'].get('upload_result') if r.get('response') else None
    
    async def storiesGetReplies(self, *, owner_id: int, story_id: int, access_key: Optional[str] = None) -> Optional[List[Stories]]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'owner_id': owner_id,
            'story_id': story_id
        }
        if access_key:
            fields['access_key'] = access_key
        url = BASE + 'stories.getReplies?'
        r = await self.request('get', url, fields)
        stories = []
        for i in r['response']['items']['stories']:
            stories.append(Stories(i))
        return stories

    # users management

    async def usersGet(self, *, user_ids: List[int], fields: str = None, name_case: str = 'nom') -> Optional[List[User]]:
        _fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'user_ids': ','.join(str(i) for i in user_ids),
            'name_case': name_case
        }
        if fields:
            _fields['fields'] = fields
        url = BASE + 'users.get?'
        r = await self.request('get', url, _fields)
        users = []
        for i in r['response']:
            users.append(User(i))
        return users

    # wall management

    async def wallCloseComments(self, *, owner_id: int, post_id: int) -> int:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'owner_id': owner_id,
            'post_id': post_id
        }
        url = BASE + 'wall.closeComments?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def wallOpenComments(self, *, owner_id: int, post_id: int) -> int:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'owner_id': owner_id,
            'post_id': post_id
        }
        url = BASE + 'wall.openComments?'
        r = await self.request('post', url, fields)
        return 1 if r.get('response') else 0
    
    async def wallCreateComment(
        self, 
        *, 
        owner_id: int, 
        post_id: int, 
        from_group: int = 0, 
        message: str = None,
        reply_to_comment: int = None,
        attachments: str = None,
        sticker_id: int = None,
        guid: str = None
    ) -> Optional[int]:
        fields = {
            'access_token': self.DANGEROUS_f.decrypt(self._DANGEROUS_3nCR3pT_k3Y).decode('utf-8'),
            'v': VERSION,
            'owner_id': owner_id,
            'post_id': post_id,
            'from_group': from_group
        }
        if message:
            fields['message'] = message
        if reply_to_comment:
            fields['reply_to_comment'] = reply_to_comment
        if attachments:
            fields['attachments'] = attachments
        if sticker_id:
            fields['sticker_id'] = sticker_id
        if guid:
            fields['guid'] = guid
        url = BASE + 'wall.createComment?'
        r = await self.request('post', url, fields)
        return r['response']['comment_id'] if r.get('response') else None