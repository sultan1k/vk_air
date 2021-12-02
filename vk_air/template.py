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
class TemplateButtons:
    """
    Объект кнопок карусели.
    """
    def __init__(self) -> None:
        self.fields = {
            'buttons': []
        }
    
    def add_text_button(self, *, label: str, color: str, payload: str) -> None:
        btn = {
            'color': color,
            'action': {
               'type': 'text',
               'label': label,
               'payload': {'command': payload}
           }
        }
        self.fields['buttons'].append(btn)
    
    def add_link_button(self, *, link: str, label: str) -> None:
        btn = {
            'action': {
                'type': 'open_link',
                'link': link,
                'label': label
            }
        }
        self.fields['buttons'].append(btn)
    
    def add_location_button(self, *, payload: str) -> None:
        btn = {
            'action': {
                'type': 'location',
                'payload': {'command': payload}
            }
        }
        self.fields['buttons'].append(btn)
    
    def add_vkpay_button(self, *, payload: str, hash: str) -> None:
        btn = {
            'action': {
                'type': 'vkpay',
                'hash': hash,
                'payload': {'command': payload}
            }
        }
        self.fields['buttons'].append(btn)
    
    def add_callback_button(self, *, label: str, payload: str, color: str) -> None:
        btn = {
            'color': color,
            'action': {
                'type': 'callback',
                'label': label,
                'payload': {'command': payload}
            }
        }
        self.fields['buttons'].append(btn)
    
    def remove_button(self, *, place: int) -> None:
        self.fields['buttons'].pop(place-1)

class TemplateAction:
    """
    Объект действия карусели.
    """
    def __init__(self, type: str, link: str = None) -> None:
        self.fields = {
            'type': type
        }
        if link:
            self.fields['link'] = link


class Template:
    """
    Объект карусели.
    """
    def __init__(self) -> None:
        self.fields = {
            'type': 'carousel',
            'elements': []
        }
    
    def add(
        self,
        *,
        title: str = None,
        description: str = None,
        photo_id: str = None,
        buttons: dict,
        action: dict = None
    ) -> None:
        data = {
            'buttons': buttons.fields['buttons']
        }
        if title:
            data['title'] = title
        if description:
            data['description'] = description
        if photo_id:
            data['photo_id'] = photo_id
        if action:
            data['action'] = action.fields
        self.fields['elements'].append(data)
    
    def remove(
        self,
        *,
        position: int
    ) -> None:
        self.fields['elements'].pop(position-1)