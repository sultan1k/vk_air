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
from typing import List


class Personal:
    """
    Информация из раздела "жизненная позиция".
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def political(self) -> int:
        return self.obj.get('political')
    
    @property
    def langs(self) -> List:
        return self.obj.get('langs')
    
    @property
    def religion(self) -> str:
        return self.obj.get('religion')
    
    @property
    def inspired_by(self) -> str:
        return self.obj.get('inspired_by')
    
    @property
    def people_main(self) -> int:
        return self.obj.get('people_main')
    
    @property
    def life_main(self) -> int:
        return self.obj.get('life_main')
    
    @property
    def smoking(self) -> int:
        return self.obj.get('smoking')
    
    @property
    def alcohol(self) -> int:
        return self.obj.get('alcohol')