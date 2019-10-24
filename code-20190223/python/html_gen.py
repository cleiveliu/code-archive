# source:https://mozillazg.com/2016/03/let-us-build-a-template-engine-part1.html


# not wise version::
"""
HTML = '''
<div>
    <p>welcome, {name}</p>
    <ul>
        {info}
    </ul>
</div>
'''
def gen_html(person):
    name=person['name']
    info_list=[
        '<li>{0}: {1}</li>'.format(key,val)
        for key,val in person['info'].items()
    ]
    info='\n'.join(info_list)
    return HTML.format(name=name,info=info)

person={'name':"jack",'info':{'sex':'female'}}
print(gen_html(person))
"""
# modern version::
"""
HTML = '''
<div>
    <p>welcome, {{ person['name'] }}</p>
    <ul>
        {% for item, value in person['info'].items() %}
        <li>{{ item }}: {{ value }}</li>
        {% endfor %}
    </ul>
</div>
'''


def gen_html(person):
    return Template(HTML).render({'person': person})

"""


def render_function():
    result = []

    result.extend([
        '<div>\n',
        '<p>welcome, '
        str(person['name']),
        '</p>\n',
        '<ul>\n'
    ])
    for item, value in person['info'].items():
        result.extend([
            '<li>',
            str(item),
            ': ',
            str(value),
            '</li>\n'
        ])
    result.extend([
        '</ul>\n'
        '</div>\n'
    ])
    return ''.join(result)


class CodeBuilder:
    INDENT_STEP = 4     # 每次缩进的空格数

    def __init__(self, indent=0):
        self.indent = indent    # 当前缩进
        self.lines = []         # 保存一行一行生成的代码

    def forward(self):
        """缩进前进一步"""
        self.indent += self.INDENT_STEP

    def backward(self):
        """缩进后退一步"""
        self.indent -= self.INDENT_STEP

    def add(self, code):
        self.lines.append(code)

    def add_line(self, code):
        self.lines.append(' ' * self.indent + code)

    def __str__(self):
        """拼接所有代码行后的源码"""
        return '\n'.join(map(str, self.lines))

    def __repr__(self):
        """方便调试"""
        return str(self)
