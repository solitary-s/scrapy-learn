from scrapy.http import HtmlResponse

def main():
    body = '''
        <html> 
        <head> 
            <base href='http://example.com/'/>
            <title>Example website</title> 
        </head>
        <body> 
            <div id='images-1' style="width: 1230px;">  
                <a href='image1.html'>Name: Image 1 <br/><img src='image1.jpg'/></a>
                <a href='image2.html'>Name: Image 2 <br/><img src='image2.jpg'/></a>
                <a href='image3.html'>Name: Image 3 <br/><img src='image3.jpg'/></a>
            </div>
            
            <div id='images-2' class='small'>  
                <a href='image4.html'>Name: Image 4 <br/><img src='image4.jpg'/></a>  
                <a href='image5.html'>Name: Image 5 <br/><img src='image5.jpg'/></a> 
            </div>
        </body>
        </html>
    '''
    response = HtmlResponse(url='http://www.example.com', body=body.encode('utf-8'))
    print(response.css('img'))
    print(response.css('base, title'))
    print(response.css('div img'))
    print(response.css('body>div'))
    print(response.css('[style]'))
    print(response.css('[id=images-1]'))
    print(response.css('div>a:nth-child(1)'))

if __name__ == '__main__':
    main()