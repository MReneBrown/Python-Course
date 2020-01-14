class Html:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        raise NotImplementedError('Subclass must implement render method')

class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'

class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'

tags = [
        Div('Some content'),
        Heading('Some big heading'),
        Div('Another div')
        ]

for tag in tags:
#     print(str(tag) + ': ' + tag.render())

# <__main__.Div object at 0x00000215AB347880>: <div>Some content</div>
# <__main__.Heading object at 0x00000215AB369B80>: <h1>Some big heading</h1>
# <__main__.Div object at 0x00000215AD4C24C0>: <div>Another div</div>

    print(tag.render())

<div>Some content</div>
<h1>Some big heading</h1>
<div>Another div</div>
