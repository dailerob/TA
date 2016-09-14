def MinePage(urlString = ''):
    if urlString == '':
        print('missing url! turn back!')
        return ''
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
        return paragraphs

    '''
    This will mine the html from a given page
    :return:
    '''