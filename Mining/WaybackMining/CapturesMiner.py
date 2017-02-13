def MineCaptures(website = None, numericStartDate = None, numericEndDate = None,limitPerRequest = None):
    import requests
    from Utilities.SaveHDf5 import saveAt
    from Utilities.reserved import replaceReservedCharacters as rp
    import json
    import h5py
    import numpy as np

    if website == None:
        website = 'http://www.huffingtonpost.com/'
    if numericStartDate == None:
        numericStartDate = '20150101010101'
    if numericEndDate == None:
        numericEndDate = '20160101010101'
    if limitPerRequest == None:
        limitPerRequest = '50'

    urlString = 'http://web.archive.org/cdx/search/cdx?url='+website+\
                '&output=json&fl=timestamp&filter=!statuscode:200&filter=!mimetype:text/html&from='+\
                str(numericStartDate)+'&to='+str(numericEndDate)+'&collapse=timestamp:8&limit=' + str(limitPerRequest)
    response = requests.get(urlString)
    data = response.json()
    stampList = []

    for id in range(1,len(data)):
        if(data[id] != 'timestamp'):
            strdat =str(data[id])
            stampList.append(int(strdat[2:-2]))

    path = '../TAdata/' + rp(website)

    saveAt(path,stampList,'testset')

    print(stampList)





