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
from .objects.changes import ChangePhoto
from .objects.comment import Comment
from .objects.message import Message, MessageEvent
from .objects.chat import Chat
from .objects.photo import Photo
from .objects.audio import Audio
from .objects.video import Video
from .objects.wall import Wall
from .objects.board import BoardComment, DeletedBoardComment
from .objects.order import Order
from .objects.group import GroupLeave, GroupJoin, UserBlock, UserUnblock
from .objects.poll import PollVote
from .objects.officer import Officer
from .objects.settings import ChangeSettings
from .objects.vkpay import Transaction
from .objects.app import AppPayload
from .objects.donut import (
    DonutSubscriptionProlonged,
    DonutSubscriptionCreate,
    DonutMoneyWithdraw,
    DonutMoneyWithdrawError,
    DonutSubscriptionCancelled,
    DonutSubscriptionExpired,
    DonutSubscriptionPriceChanged
)

EVENTS = {
    'message_new': [],
    'message_reply': [],
    'message_edit': [],
    'message_allow': [],
    'message_deny': [],
    'message_typing_state': [],
    'message_event': [],
    'photo_new': [],
    'photo_comment_new': [],
    'photo_comment_edit': [],
    'photo_comment_restore': [],
    'photo_comment_delete': [],
    'audio_new': [],
    'video_new': [],
    'video_comment_new': [],
    'video_comment_edit': [],
    'video_comment_restore': [],
    'video_comment_delete': [],
    'wall_post_new': [],
    'wall_repost': [],
    'wall_reply_new': [],
    'wall_reply_edit': [],
    'wall_reply_restore': [],
    'wall_reply_delete': [],
    'like_add': [],
    'like_remove': [],
    'board_post_new': [],
    'board_post_edit': [],
    'board_post_restore': [],
    'board_post_delete': [],
    'market_comment_new': [],
    'market_comment_edit': [],
    'market_comment_restore': [],
    'market_comment_delete': [],
    'market_order_new': [],
    'market_order_edit': [],
    'group_leave': [],
    'group_join': [],
    'user_block': [],
    'user_unblock': [],
    'poll_vote_new': [],
    'group_officers_edit': [],
    'group_change_settings': [],
    'group_change_photo': [],
    'vkpay_transaction': [],
    'app_payload': [],
    'donut_subscription_create': [],
    'donut_subscription_prolonged': [],
    'donut_subscription_expired': [],
    'donut_subscription_cancelled': [],
    'donut_subscription_price_changed': [],
    'donut_money_withdraw': [],
    'donut_money_withdraw_error': [],
    'ready': [],
    'chat_photo_update': [],
    'chat_photo_remove': [],
    'chat_create': [],
    'chat_title_update': [],
    'chat_invite_user': [],
    'chat_kick_user': [],
    'chat_pin_message': [],
    'chat_unpin_message': [],
    'chat_invite_user_by_link': []
}

BoolToInt = {
    True: 1,
    False: 0
}

class DeleteChatPhotoResponse:
    """
    Объект для метода messages.deleteChatPhoto
    """
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def message_id(self) -> int:
        return self.obj.get('message_id')
    
    @property
    def chat(self) -> Optional[Chat]:
        return Chat(self.obj.get('chat')) if self.obj.get('chat') else None

class MessageAllow:
    """
    Объект подписки на сообщения от сообщества.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def key(self) -> str:
        return self.obj.get('key')

class MessageDeny:
    """
    Объект запрета сообщений от сообщества.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')

class MessageTypingState:
    """
    Объект статуса набора сообщения.
    """
    def __init__(self, obj, api):
        self.obj = obj
        self.api = api
    
    @property
    def state(self) -> str:
        return self.obj.get('state')
    
    @property
    def from_id(self) -> int:
        return self.obj.get('from_id')
    
    @property
    def to_id(self) -> int:
        return self.obj.get('to_id')

class DeletedComment:
    """
    Объект удалённого комментария.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api = api
    
    @property
    def owner_id(self) -> int:
        return self.obj.get('owner_id')
    
    @property
    def id(self) -> int:
        return self.obj.get('id')
    
    @property
    def user_id(self) -> int:
        return self.obj.get('user_id')
    
    @property
    def deleter_id(self) -> int:
        return self.obj.get('deleter_id')

class Like:
    """
    Объект лайка.
    """
    def __init__(self, obj, api=None):
        self.obj = obj
        self.api = api
    
    @property
    def liker_id(self) -> int:
        return self.obj.get('liker_id')
    
    @property
    def object_type(self) -> str:
        return self.obj.get('object_type')
    
    @property
    def object_owner_id(self) -> int:
        return self.obj.get('object_owner_id')
    
    @property
    def object_id(self) -> int:
        return self.obj.get('object_id')
    
    @property
    def thread_reply_id(self) -> Optional[int]:
        return self.obj.get('thread_reply_id')
    
    @property
    def post_id(self) -> int:
        return self.obj.get('post_id')

CLASSES = {
    'message_new': Message,
    'message_reply': Message,
    'message_allow': MessageAllow,
    'message_deny': MessageDeny,
    'message_typing_state': MessageTypingState,
    'message_event': MessageEvent,
    'photo_new': Photo,
    'photo_comment_new': Comment,
    'photo_comment_edit': Comment,
    'photo_comment_restore': Comment,
    'photo_comment_delete': DeletedComment,
    'audio_new': Audio,
    'video_new': Video,
    'video_comment_new': Comment,
    'video_comment_edit': Comment,
    'video_comment_restore': Comment,
    'video_comment_delete': DeletedComment,
    'wall_post_new': Wall,
    'wall_repost': Wall,
    'wall_reply_new': Comment,
    'wall_reply_edit': Comment,
    'wall_reply_restore': Comment,
    'wall_reply_delete': DeletedComment,
    'like_add': Like,
    'like_remove': Like,
    'board_post_new': BoardComment,
    'board_post_edit': BoardComment,
    'board_post_restore': BoardComment,
    'board_post_delete': DeletedBoardComment,
    'market_comment_new': Comment,
    'market_comment_edit': Comment,
    'market_comment_restore': Comment,
    'market_comment_delete': DeletedComment,
    'market_order_new': Order,
    'market_order_edit': Order,
    'group_leave': GroupLeave,
    'group_join': GroupJoin,
    'user_block': UserBlock,
    'user_unblock': UserUnblock,
    'poll_vote_new': PollVote,
    'group_officers_edit': Officer,
    'group_change_settings': ChangeSettings,
    'group_change_photo': ChangePhoto,
    'vkpay_transaction': Transaction,
    'app_payload': AppPayload,
    'donut_subscription_create': DonutSubscriptionCreate,
    'donut_subscription_prolonged': DonutSubscriptionProlonged,
    'donut_subscription_expired': DonutSubscriptionExpired,
    'donut_subscription_cancelled': DonutSubscriptionCancelled,
    'donut_subscription_price_changed': DonutSubscriptionPriceChanged,
    'donut_money_withdraw': DonutMoneyWithdraw,
    'donut_money_withdraw_error': DonutMoneyWithdrawError,
    'chat_photo_update': Message,
    'chat_photo_remove': Message,
    'chat_create': Message,
    'chat_title_update': Message,
    'chat_invite_user': Message,
    'chat_kick_user': Message,
    'chat_pin_message': Message,
    'chat_unpin_message': Message,
    'chat_invite_user_by_link': Message
}