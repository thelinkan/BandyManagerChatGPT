from newscode.mediaoutlet import MediaOutlet

class NewsItem:
    def __init__(self, date, headline, text, media_outlet):
        self.date = date
        self.headline = headline
        self.text = text
        self.media_outlet = media_outlet
        self.tags = []
        
    def add_tag(self, tag):
        self.tags.append(tag)

