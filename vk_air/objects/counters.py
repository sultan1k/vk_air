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
class UserCounters:
    """
    Счётчики пользователя.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def albums(self) -> int:
        return self.obj.get('albums')
    
    @property
    def videos(self) -> int:
        return self.obj.get('videos')
    
    @property
    def audios(self) -> int:
        return self.obj.get('audios')
    
    @property
    def photos(self) -> int:
        return self.obj.get('photos')
    
    @property
    def notes(self) -> int:
        return self.obj.get('notes')
    
    @property
    def friends(self) -> int:
        return self.obj.get('friends')
    
    @property
    def groups(self) -> int:
        return self.obj.get('groups')
    
    @property
    def online_friends(self) -> int:
        return self.obj.get('online_friends')
    
    @property
    def mutual_friends(self) -> int:
        return self.obj.get('mutual_friends')
    
    @property
    def user_videos(self) -> int:
        return self.obj.get('user_videos')
    
    @property
    def followers(self) -> int:
        return self.obj.get('followers')
    
    @property
    def pages(self) -> int:
        return self.obj.get('pages')

class GroupCounters:
    """
    Счётчики группы.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def photos(self) -> int:
        return self.obj.get('photos')
    
    @property
    def albums(self) -> int:
        return self.obj.get('albums')
    
    @property
    def audios(self) -> int:
        return self.obj.get('audios')
    
    @property
    def videos(self) -> int:
        return self.obj.get('videos')
    
    @property
    def topics(self) -> int:
        return self.obj.get('topics')
    
    @property
    def docs(self) -> int:
        return self.obj.get('docs')