from scrapy.selector import Selector
from scrapy.http import HtmlResponse

def main():
    text = '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <h1>Hello Scrapy</h1>
        <b>Hello python</b>
        <ul>
            <li>C++</li>
            <li>Java</li>
            <li>Python</li>
        </ul>
    </body>
    </html>
    '''

    selector = Selector(text=text)
    print(selector)
    selector_list = selector.xpath('//h1')
    print(selector_list)

    # for sel in selector_list:
    #     print(sel.xpath('./text()'))
    selector_list_text = selector_list.xpath('./text()')
    print(selector_list_text)

    li_text = selector.xpath('.//ul').css('li').xpath('./text()')
    print(li_text)

    text = selector.css('ul').css('li').xpath('./text()')
    print(text)

    print(text.extract_first())
    print(text.extract())

if __name__ == '__main__':
    main()