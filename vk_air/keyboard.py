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
class ButtonColor:
    """
    Выбор цвета кнопки.
    """
    blue = 'primary'
    white = 'secondary'
    red = 'negative'
    green = 'positive'


class Keyboard:
    """
    Объект клавиатуры.
    """
    def __init__(
        self,
        *,
        inline: bool = False,
        one_time: bool = True
    ):
        self.fields = {'buttons': [[]]}
        self.position = 0
        if inline:
            one_time = None
        self.fields['inline'] = inline
        if one_time:
            self.fields['one_time'] = one_time
    
    def add_text_button(self, *, label: str, color: str, payload: str):
        btn = {
            'color': color,
            'action': {
               'type': 'text',
               'label': label,
               'payload': {'command': payload}
           }
        }
        self.fields['buttons'][self.position].append(btn)
    
    def add_link_button(self, *, link: str, label: str):
        btn = {
            'action': {
                'type': 'open_link',
                'link': link,
                'label': label
            }
        }
        self.fields['buttons'][self.position].append(btn)
    
    def add_location_button(self, *, payload: str):
        btn = {
            'action': {
                'type': 'location',
                'payload': {'command': payload}
            }
        }
        self.fields['buttons'][self.position].append(btn)
    
    def add_vkpay_button(self, *, payload: str, hash: str):
        btn = {
            'action': {
                'type': 'vkpay',
                'hash': hash,
                'payload': {'command': payload}
            }
        }
        self.fields['buttons'][self.position].append(btn)
    
    def add_callback_button(self, *, label: str, color: str, payload: str):
        btn = {
            'color': color,
            'action': {
                'type': 'callback',
                'label': label,
                'payload': {'command': payload}
            }
        }
        self.fields['buttons'][self.position].append(btn)
    
    def add_raw(self):
        self.fields['buttons'].append([])
        self.position += 1
    
    @property
    def raws(self):
        return self.position + 1
    
    def remove_button(self, *, raw: int, place: int):
        self.fields['buttons'][raw-1].pop(place-1)
    
    def remove_raw(self, *, raw: int):
        self.fields['buttons'].pop(raw-1)

class EmptyKeyboard:
    """
    Объект пустой клавиатуры.
    """
    def __init__(self):
        self.fields = {
            'one_time': True,
            'buttons': []
        }