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
from .objects.message import UploadedMessagePhoto
from .objects.server import MessagesUploadServer
from .bot_api import BotApi
import os
import asyncio
from typing import List
import json

class File:
    def __init__(
        self,
        *,
        file: TextIOWrapper,
        peer_id: int = None,
        title: str = None,
        tags: str = None
    ):
        self.file = file
        self.peer_id = peer_id
        self.title = title
        self.tags = tags
    
class Attachment:
    def __init__(self, *, api: BotApi):
        self.api = api


    async def get_servers(self, *, files):
        code = ''
        rdict = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h',
            8: 't',
            9: 'q',
            10: 'z'
        }
        for i in range(0, len(files)):
            if os.path.splitext(files[i].file.name)[1] in ['.jpg', '.png', '.gif', '.jpeg']:
                code = code + f'\nvar {rdict[i]} = API.photos.getMessagesUploadServer({json.dumps({"group_id": self.api.group_id})});'
            elif os.path.splitext(files[i].file.name)[1] in ['.ogg', '.opus']:
                code = code + f'\nvar {rdict[i]} = API.docs.getMessagesUploadServer({json.dumps({"type": "audio_message", "peer_id": files[i].peer_id})});'
            else:
                code = code + f'\nvar {rdict[i]} = API.docs.getMessagesUploadServer({json.dumps({"type": "doc", "peer_id": files[i].peer_id})});'
        code = code + f'\nreturn [{",".join(rdict[i] for i in range(0, len(files)))}];'
        servers = await self.api.execute(
            code=code
        )
        servlist = []
        for i in range(0, len(files)):
            if os.path.splitext(files[i].file.name)[1] in ['.jpg', '.png', '.gif', '.jpeg']:
                servlist.append(MessagesUploadServer(servers[i]))
            else:
                servlist.append(servers[i]['upload_url'])
        return servlist


    async def save_files(self, *, savedfiles, files):
        code = ''
        rdict = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h',
            8: 't',
            9: 'q',
            10: 'z'
        }
        for i in range(0, len(savedfiles)):
            if (type(savedfiles[i])) == UploadedMessagePhoto:
                code = code + f'\nvar {rdict[i]} = API.photos.saveMessagesPhoto({json.dumps({"photo": savedfiles[i].photo, "server": savedfiles[i].server, "hash": savedfiles[i].hash})})[0];'
                code = code + f'\nvar {rdict[i]} = "photo" + {rdict[i]}["owner_id"] + "_" + {rdict[i]}["id"];'
            else:
                code = code + f'\nvar {rdict[i]} = API.docs.save({json.dumps({"file": savedfiles[i], "title": files[i].title, "tags": files[i].tags})});'
                code = code + f'\nvar {rdict[i]}_type = {rdict[i]}["type"];'
                code = code + f'\nvar {rdict[i]} = {rdict[i]}_type + {rdict[i]}[{rdict[i]}_type]["owner_id"] + "_" + {rdict[i]}[{rdict[i]}_type]["id"];'
        code = code + f'\nreturn [{",".join(rdict[i] for i in range(0, len(files)))}];'
        saved = await self.api.execute(
            code=code
        )
        return saved


    async def upload_several_files_to_message(
        self,
        *,
        files: List[File]
    ):
        servers = []
        uploads = []
        savedfiles = []
        supersavedfiles = []
        loop = asyncio.get_event_loop()
        servers = await self.get_servers(files=files)
        for i in range(0, len(files)):
            uploads.append(loop.create_task(self.api.upload_messages_photo_to_server(upload_url=servers[i].upload_url, photo=files[i].file)) if files[i].file.name.lower().endswith(('.jpg', '.png', '.gif', '.jpeg')) 
            else loop.create_task(self.api.upload_doc_to_server(upload_url=servers[i], file=files[i].file)))
        savedfiles = await asyncio.gather(*uploads)
        supersavedfiles = await self.save_files(savedfiles=savedfiles, files=files)
        return ",".join(supersavedfiles)


    def check_type(self, files): 
        return type(files)
    
    async def upload(
        self,
        *,
        files: File
    ):
        if self.check_type(files) == list:
            return await self.upload_several_files_to_message(files=files)
        if files.file.name.lower().endswith(('.jpg', '.png', '.gif', '.jpeg')):
            upload = await self.api.photos_get_messages_upload_server()
            uploaded = await self.api.upload_messages_photo_to_server(
                upload_url=upload.upload_url,
                photo=files.file
            )
            saved = await self.api.photos_save_messages_photo(
                photo=uploaded.photo,
                server=uploaded.server,
                hash=uploaded.hash 
            )
            return f'photo{saved.owner_id}_{saved.id}'
        else: 
            if files.file.name.lower().endswith(('.ogg', '.opus')):
                type = 'audio_message'
            else:
                type = 'doc'
            upload_url = await self.api.get_docs_dm_upload_server(
                type=type, peer_id=files.peer_id
            )
            uploaded = await self.api.upload_doc_to_server(
                upload_url=upload_url,
                file=files.file
            )
            saved = await self.api.docs_save(
                file=uploaded,
                title=files.title,
                tags=files.tags
            )
            return f'{type}{saved.owner_id}_{saved.id}'