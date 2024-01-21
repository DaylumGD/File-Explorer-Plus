import requests
import bs4

class FileData:
    def GetFileData(filesuffix) -> dict:
        httpreq = requests.get(f'https://fileinfo.com/extension/{filesuffix}').content
        icon = str(bs4.BeautifulSoup(httpreq, 'html5lib').find_all('div', 'entryIcon')[0])
        title = str(bs4.BeautifulSoup(httpreq, 'html5lib').find_all('h2')[0])
        
        icon = str.removeprefix(icon, '<div class="entryIcon" data-bg="').split('"', 1)[0]
        title = str.removeprefix(title, '<h2 class="title">').split('<', 1)[0]
        
        config = {
            "icon": icon,
            "title": title
        }
        return config