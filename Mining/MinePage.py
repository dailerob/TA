def MinePage(urlString = 'http://www.nature.com/srep/2013/130425/srep01684/full/srep01684.html#f2'):
    if urlString == '':
        print('missing url! turn back!')
    else:
        import urllib.request
        import urllib.parse
        import re

        url = urlString
        values = {'s': 'basics',
                  'submit': 'search'}

        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        paragraphs = re.findall(r'<p>(.*?)<p>', str(respData))
        print(paragraphs)


    print('this is a test a test a test')

    '''
    This will mine the html from a given page
    :return:
    '''