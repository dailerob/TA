def replaceReservedCharacters(unedited):
    if 'https:' in unedited or 'http:' in unedited:
        unedited = unedited[unedited.index(':')+3:len(unedited)]
    unedited = unedited.replace('<', ' LN')
    unedited = unedited.replace('>', ' GN')
    unedited = unedited.replace(':', ' C')
    unedited = unedited.replace('\"', ' DQ')
    unedited = unedited.replace('/', ' FS')
    unedited = unedited.replace('\\\\', ' BH')
    unedited = unedited.replace('\\|', ' VR')
    unedited = unedited.replace('\\?', ' QK')
    unedited = unedited.replace('\\*', ' A')

    return unedited

def addReservedCharacters(unedited):
    unedited = unedited.replace(' LN', '<')
    unedited = unedited.replace(' GN', '>')
    unedited = unedited.replace(' C', ':')
    unedited = unedited.replace(' DQ', '\"')
    unedited = unedited.replace(' FS', '/')
    unedited = unedited.replace(' BH', '\\\\')
    unedited = unedited.replace(' VR', '\\|')
    unedited = unedited.replace(' QK', '\\?')
    unedited = unedited.replace(' A', '\\*')

    return unedited