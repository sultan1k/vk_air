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


class CallbackServer:
    """
    Объект сервера Callback.
    """
    def __init__(self, obj: dict):
        self.obj = obj
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def title(self) -> str:
        return self.obj.get('title')
    
    @property
    def creator_id(self) -> int:
        return self.obj.get('creator_id')
    
    @property
    def url(self) -> str:
        return self.obj.get('url')
    
    @property
    def secret_key(self) -> Optional[str]:
        return self.obj.get('secret_key')
    
    @property
    def status(self) -> Optional[str]:
        return self.obj.get('status')

class CallbackSettings:
    """
    Настройки Callback.
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def message_new(self) -> bool:
        return True if self.obj.get('message_new') == 1 else False
    
    @property
    def message_reply(self) -> bool:
        return True if self.obj.get('message_reply') == 1 else False
    
    @property
    def message_edit(self) -> bool:
        return True if self.obj.get('message_edit') == 1 else False
    
    @property
    def message_allow(self) -> bool:
        return True if self.obj.get('message_allow') == 1 else False
    
    @property
    def message_deny(self) -> bool:
        return True if self.obj.get('message_deny') == 1 else False
    
    @property
    def photo_new(self) -> bool:
        return True if self.obj.get('photo_new') == 1 else False
    
    @property
    def audio_new(self) -> bool:
        return True if self.obj.get('audio_new') == 1 else False
    
    @property
    def video_new(self) -> bool:
        return True if self.obj.get('video_new') == 1 else False
    
    @property
    def wall_reply_view(self) -> bool:
        return True if self.obj.get('wall_reply_view') == 1 else False
    
    @property
    def wall_reply_edit(self) -> bool:
        return True if self.obj.get('wall_reply_edit') == 1 else False
    
    @property
    def wall_reply_delete(self) -> bool:
        return True if self.obj.get('wall_reply_delete') == 1 else False
    
    @property
    def wall_post_new(self) -> bool:
        return True if self.obj.get('wall_post_new') == 1 else False
    
    @property
    def wall_repost(self) -> bool:
        return True if self.obj.get('wall_repost') == 1 else False
    
    @property
    def board_post_new(self) -> bool:
        return True if self.obj.get('board_post_new') == 1 else False
    
    @property
    def board_post_edit(self) -> bool:
        return True if self.obj.get('board_post_edit') == 1 else False
    
    @property
    def board_post_delete(self) -> bool:
        return True if self.obj.get('board_post_delete') == 1 else False
    
    @property
    def board_post_restore(self) -> bool:
        return True if self.obj.get('board_post_restore') == 1 else False
    
    @property
    def photo_comment_new(self) -> bool:
        return True if self.obj.get('photo_comment_new') == 1 else False

    @property
    def photo_comment_edit(self) -> bool:
        return True if self.obj.get('photo_comment_edit') == 1 else False
    
    @property
    def photo_comment_delete(self) -> bool:
        return True if self.obj.get('photo_comment_delete') == 1 else False
    
    @property
    def photo_comment_restore(self) -> bool:
        return True if self.obj.get('photo_comment_restore') == 1 else False
    
    @property
    def video_comment_new(self) -> bool:
        return True if self.obj.get('video_comment_new') == 1 else False
    
    @property
    def video_comment_edit(self) -> bool:
        return True if self.obj.get('video_comment_edit') == 1 else False
    
    @property
    def video_comment_delete(self) -> bool:
        return True if self.obj.get('video_comment_delete') == 1 else False
    
    @property
    def video_comment_restore(self) -> bool:
        return True if self.obj.get('video_comment_restore') == 1 else False
    
    @property
    def market_comment_new(self) -> bool:
        return True if self.obj.get('market_comment_new') == 1 else False
    
    @property
    def market_comment_edit(self) -> bool:
        return True if self.obj.get('market_comment_edit') == 1 else False
    
    @property
    def market_comment_delete(self) -> bool:
        return True if self.obj.get('market_comment_delete') == 1 else False
    
    @property
    def market_comment_restore(self) -> bool:
        return True if self.obj.get('market_comment_restore') == 1 else False
    
    @property
    def poll_vote_new(self) -> bool:
        return True if self.obj.get('poll_vote_new') == 1 else False
    
    @property
    def group_join(self) -> bool:
        return True if self.obj.get('group_join') == 1 else False
    
    @property
    def group_leave(self) -> bool:
        return True if self.obj.get('group_leave') == 1 else False
    
    @property
    def user_block(self) -> bool:
        return True if self.obj.get('user_block') == 1 else False
    
    @property
    def user_unblock(self) -> bool:
        return True if self.obj.get('user_unblock') == 1 else False
    
    @property
    def group_change_settings(self) -> bool:
        return True if self.obj.get('group_change_settings') == 1 else False
    
    @property
    def group_change_photo(self) -> bool:
        return True if self.obj.get('group_change_photo') == 1 else False
    
    @property
    def group_officers_edit(self) -> bool:
        return True if self.obj.get('group_officers_edit') == 1 else False
    
    @property
    def donut_subscription_create(self) -> bool:
        return True if self.obj.get('donut_subscription_create') == 1 else False
    
    @property
    def donut_subscription_prolonged(self) -> bool:
        return True if self.obj.get('donut_subscription_prolonged') == 1 else False
    
    @property
    def donut_subscription_expired(self) -> bool:
        return True if self.obj.get('donut_subscription_expired') == 1 else False
    
    @property
    def donut_subscription_cancelled(self) -> bool:
        return True if self.obj.get('donut_subscription_cancelled') == 1 else False
    
    @property
    def subscription_price_changed(self) -> bool:
        return True if self.obj.get('subscription_price_changed') == 1 else False
    
    @property
    def donut_money_withdraw(self) -> bool:
        return True if self.obj.get('donut_money_withdraw') == 1 else False
    
    @property
    def donut_money_withdraw_error(self) -> bool:
        return True if self.obj.get('donut_money_withdraw_error') == 1 else False