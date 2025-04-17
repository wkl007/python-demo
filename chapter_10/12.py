from urllib import request
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)



class WeatherHandler:
    def __init__(self):
        self.result = {
            'city': '',
            'weather': {
                'condition': '',
                'temperature': 0.0,
                'wind': 0.0
            }
        }
        self.current_element = ''

    def start_element(self, name, attrs):
        self.current_element = name

    def end_element(self, name):
        self.current_element = ''

    def char_data(self, data):
        data = data.strip()
        if not data:
            return
        if self.current_element == 'name' and not self.result['city']:
            self.result['city'] = data
        elif self.current_element == 'text':
            self.result['weather']['condition'] = data
        elif self.current_element == 'temp_c':
            self.result['weather']['temperature'] = float(data)
        elif self.current_element == 'wind_kph':
            self.result['weather']['wind'] = float(data)


def parseXml(xml_str):
    handler = WeatherHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return handler.result


# 测试:
URL = 'https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))

# 输出 & 测试断言
print(result)
assert result['city'] == 'Beijing'
print('ok')
