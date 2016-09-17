def MinePage(urlString = 'https://web.archive.org/web/20140213040302/http://www.reddit.com/'):

    if urlString == '':
        print('missing url! turn back!')
    else:
        import requests
        import re
        import nltk
        from nltk import word_tokenize
        from bs4 import BeautifulSoup
        url = urlString
        values = {'s': 'basics',
                  'submit': 'search'}

        response = requests.get(urlString)
        data = response.text

        ## Beatiful Soup Method
        soup = BeautifulSoup(data,'html.parser')
        texts = soup.findAll(text=True)

        def visible(element):
            if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
                return False
            elif re.match('<!--.*-->', str(element)):
                return False
            return True

        visible_texts = ''.join(list(filter(visible, texts)))
        tokens = word_tokenize(visible_texts)
        text = nltk.Text(tokens)

        #print(tokens)
        print(text[:15])




        #return data


    '''
    This will mine the html from a given page
    :return:
    '''