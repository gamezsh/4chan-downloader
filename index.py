import os
import sys
import getopt
import urllib.request
import requests
import threading
from bs4 import BeautifulSoup

class Downloader():
    def _download_media(_id, board):
        allowed_formats = ['jpeg', 'png', 'webm', 'mp4', 'jpg']

        base_url = "https://boards.4chan.org/%s/thread/%s" % (board, _id)

        req = requests.get(base_url)

        if req.status_code != 200:
            print("\033[91m page %s not found " % _id)
            return
        
        print("\033[92m page %s exists! " % _id)
        
        soup = BeautifulSoup(req.content, 'html.parser')
        elements = soup.find_all(attrs={ "href" : True })
        for element in elements:
            if any(x in element["href"] for x in allowed_formats):
                _filename = element["href"].split('/')[4]
                _dirname = os.path.join(save_path, _filename)
                if os.path.exists(_dirname) is False:
                    resource = urllib.request.urlopen("https:" + element["href"])
                    output = open(_dirname, "wb")
                    output.write(resource.read())
                    output.close()
                    print("\033[96m media %s saved!" % _filename)

        return


if __name__ == "__main__":

    chan_threads = []
    chan_board = ''
    save_path = ''

    argv = sys.argv[1:]
    optlist, args = getopt.getopt(argv, 'f:t:b:', ['folder=', 'threads=', 'board='])
    
    for flag, arg in optlist:
        print(flag, arg)
        if flag == '-f' or flag == '--folder':
            save_path = arg
        if flag == '-b' or flag == '--board':
            chan_board = arg
        if flag == '-t' or flag == '--threads':
            chan_threads = arg.split(' ')

    threads = []

    for _id in chan_threads:
        t = threading.Thread(target=Downloader._download_media, args=[_id, chan_board])
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()