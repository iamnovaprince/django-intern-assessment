
def  group_by_owners(dictObj):
    groupedDict = {}
    for file in dictObj:
        if dictObj[file] in groupedDict.keys():
            groupedDict[dictObj[file]].append(file)
        else:
            groupedDict[dictObj[file]] = [file]

    return groupedDict
    
    

if __name__ == '__main__':
    ungroupedDict = {'Input.txt': 'Randy','Code.py': 'Stan','Output.txt': 'Randy'}
    groupedDict = group_by_owners(ungroupedDict)
    print("Before grouping : " + str(ungroupedDict))
    print("After grouping : " + str(groupedDict))