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
from .background import Background

class PollAnswer:
    """
    Объект варианта ответа.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def text(self) -> str:
        return self.obj.get('text')
    
    @property
    def votes(self) -> int:
        return self.obj.get('votes')
    
    @property
    def rate(self) -> int:
        return self.obj.get('rate')

class Poll:
    """
    Объект опроса.
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
    def created(self) -> int:
        return self.obj.get('created')
    
    @property
    def question(self) -> str:
        return self.obj.get('question')
    
    @property
    def votes(self) -> int:
        return self.obj.get('votes')
    
    @property
    def answers(self) -> List[PollAnswer]:
        answerlist = []
        for i in self.obj.get('answers'):
            answerlist.append(PollAnswer(i))
        return answerlist
    
    @property
    def anonymous(self) -> bool:
        return self.obj.get('anonymous')
    
    @property
    def multiple(self) -> bool:
        return self.obj.get('multiple')
    
    @property
    def end_date(self) -> int:
        return self.obj.get('end_date')
    
    @property
    def closed(self) -> bool:
        return self.obj.get('closed')
    
    @property
    def is_board(self) -> bool:
        return self.obj.get('is_board')
    
    @property
    def can_edit(self) -> bool:
        return self.obj.get('can_edit')
    
    @property
    def can_vote(self) -> bool:
        return self.obj.get('can_vote')
    
    @property
    def can_report(self) -> bool:
        return self.obj.get('can_report')
    
    @property
    def can_share(self) -> bool:
        return self.obj.get('can_share')
    
    @property
    def author_id(self) -> int:
        return self.obj.get('author_id')
    
    @property
    def photo(self) -> Optional[Photo]:
        return Photo(self.obj.get('photo')) if self.obj.get('photo') else None
    
    @property
    def background(self) -> Optional[Background]:
        return Background(self.obj.get('background')) if self.obj.get('background') else None
    
    @property
    def friends(self) -> Optional[List[int]]:
        return self.obj.get('friends')
    
    @property
    def access_key(self) -> Optional[str]:
        return self.obj.get('access_key')
    
    def to_attachment(self) -> str:
        if self.access_key:
            return f'poll{self.owner_id}_{self.id}_{self.access_key}'
        else:
            return f'poll{self.owner_id}_{self.id}'

class PollVote:
    """
    Объект нового голоса в опросе.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('owner_id')
    
    @property
    def poll_id(self) -> int:
        return self.obj.get('poll_id')
    
    @property
    def option_id(self) -> int:
        return self.obj.get('option_id')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')