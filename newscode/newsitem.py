from newscode.mediaoutlet import MediaOutlet

class NewsItem:
    def __init__(self, date, headline, text, media_outlet):
        self.date = date
        self.headline = headline
        self.text = text
        self.media_outlet = media_outlet
        self.is_read = False
        self.tags = []
        
    def add_tag(self, tag):
        self.tags.append(tag)

    def to_dict(self):
        return{
            'date': self.date,
            'headline': self.headline,
            'text': self.text,
            'media_outlet': self.media_outlet.name,
            'is_read': self.is_read
        }
