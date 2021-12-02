class MessagesUploadServer:
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def upload_url(self):
        return self.obj.get('upload_url')
    
    @property
    def album_id(self):
        return self.obj.get('album_id')
    
    @property
    def group_id(self):
        return self.obj.get('group_id')