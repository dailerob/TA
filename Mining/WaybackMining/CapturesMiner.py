def MineCaptures():
    import requests,json

    website = 'http://www.huffingtonpost.com/'
    numericStartDate = '20150101010101'
    numericEndDate = '20160101010101'
    limitPerRequest = '50'
    urlString = 'http://web.archive.org/cdx/search/cdx?url='+website+\
                '&output=json&fl=timestamp&filter=!statuscode:200&filter=!mimetype:text/html&from='+\
                str(numericStartDate)+'&to='+str(numericEndDate)+'&collapse=timestamp:8&limit=' + str(limitPerRequest)
    response = requests.get(urlString)
    data = response.json()
    for id in data:
        if(id != 'timestamp'):
            print(id)




