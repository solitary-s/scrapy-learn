from scrapy.http import HtmlResponse

def main():
    body = '''
    <html> 
    <head> 
        <base href='http://example.com/'/>
         <title>Example website</title> 
    </head>
    <body> 
        <div id='images'>
            <a href='image1.html'>Name: Image 1 <br/><img src='image1.jpg'/></a> 
            <a href='image2.html'>Name: Image 2 <br/><img src='image2.jpg'/></a>
            <a href='image3.html'>Name: Image 3 <br/><img src='image3.jpg'/></a>
            <a href='image4.html'>Name: Image 4 <br/><img src='image4.jpg'/></a>
            <a href='image5.html'>Name: Image 5 <br/><img src='image5.jpg'/></a> 
        </div>
    </body>
    </html>
    '''

    response = HtmlResponse(url='http://www.example.com', body=body.encode('utf-8'))

    sel = response.xpath('//a')[0]
    print(sel.xpath('.//img'))
    print(sel.xpath('//img/..'))
    print(response.xpath('//a[3]'))
    print(response.xpath('//a[last()]'))
    print(response.xpath('//a[position()<=3]'))
    print(response.xpath('//div[@id]'))

    # print(response.xpath('/html'))
    # print(response.xpath('/html/head'))
    # print(response.xpath('/html/body/div/a'))
    # print(response.xpath('//a'))
    # print(response.xpath('/html/body//img'))
    # print(response.xpath('//a/text()'))
    # print(response.xpath('/html/*'))
    # print(response.xpath('/html/body/div//*'))
    # print(response.xpath('//div/*/img'))
    # print(response.xpath('//img/@src'))
    # print(response.xpath('//@href'))


if __name__ == '__main__':
    main()