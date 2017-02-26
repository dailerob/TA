def MineCaptures(website = None, numericStartDate = None, numericEndDate = None,limitPerRequest = None):
    import requests
    from Utilities.SaveHDf5 import saveAt
    from Utilities.reserved import replaceReservedCharacters as rp


    if website == None:
        website = 'http://www.huffingtonpost.com/'
    if numericStartDate == None:
        numericStartDate = '20150101010101'
    if numericEndDate == None:
        numericEndDate = '20160101010101'
    if limitPerRequest == None:
        limitPerRequest = '50'

    returnSize = int(limitPerRequest) #so that the check for return is the same size as requested return

    stampList = []  #list to contain all time stamps for a given website



    while int(numericEndDate) > int(numericStartDate) and returnSize == int(limitPerRequest):
        urlString = 'http://web.archive.org/cdx/search/cdx?url='+website+\
                    '&output=json&fl=timestamp&filter=!statuscode:200&filter=!mimetype:text/html&from='+\
                    str(numericStartDate)+'&to='+str(numericEndDate)+'&collapse=timestamp:8&limit=' + str(limitPerRequest)
        response = requests.get(urlString)
        data = response.json()

        for id in range(0,len(data)):
            if(str(data[id])[2:-2] != 'timestamp'):
                strdat =str(data[id])
                stampList.append(int(strdat[2:-2]))

        print(stampList[-1]) #just prints the last return from each search
        returnSize = (len(data)-1) #used to check if the endDate has been reached (-1 is for the first element('timestamp')
        numericStartDate = int(stampList[-1]) + 1  #sets the startdate to end of the previous returns

    path = '../TAdata/CapturesAvailible/' + rp(website)
    saveAt(path, stampList, 'testset')




