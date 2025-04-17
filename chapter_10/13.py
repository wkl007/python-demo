from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_event_time = False
        self.in_event_name = False
        self.in_event_location = False
        self.events = []
        self.current = {}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'time':
            self.in_event_time = True
        elif tag == 'a' and attrs_dict.get('class') == 'event-title':
            self.in_event_name = True
        elif tag == 'span' and attrs_dict.get('class') == 'event-location':
            self.in_event_location = True

    def handle_endtag(self, tag):
        if tag == 'time':
            self.in_event_time = False
        elif tag == 'a':
            self.in_event_name = False
        elif tag == 'span':
            self.in_event_location = False

    def handle_data(self, data):
        data = data.strip()
        if not data:
            return
        if self.in_event_time:
            self.current['time'] = data
        elif self.in_event_name:
            self.current['name'] = data
        elif self.in_event_location:
            self.current['location'] = data
            self.events.append(self.current)
            self.current = {}


# 示例：你需要把这里替换为你复制的HTML字符串
html = '''
<section class="event-widget">
  <ul>
    <li>
      <time datetime="2025-01-15">Jan. 15, 2025</time>
      <a class="event-title" href="/events/python-events/123/">Python Conference 2025</a>
      <span class="event-location">Amsterdam, Netherlands</span>
    </li>
    <li>
      <time datetime="2025-02-10">Feb. 10, 2025</time>
      <a class="event-title" href="/events/python-events/124/">PyData Global 2025</a>
      <span class="event-location">San Francisco, USA</span>
    </li>
  </ul>
</section>
'''

parser = MyHTMLParser()
parser.feed(html)

# 打印结果
for event in parser.events:
    print(f"时间：{event['time']}")
    print(f"名称：{event['name']}")
    print(f"地点：{event['location']}")
    print('---')
