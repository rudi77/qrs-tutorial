import os
import urllib.request

from tqdm import tqdm
from bs4 import BeautifulSoup as BSoup

def download_mitdb():
    """ All """
    extensions = ['atr', 'dat', 'hea']
    the_path = 'https://www.physionet.org/physiobank/database/mitdb/'

    # Save to proper data/ directory
    savedir = 'data/mitdb'
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    # With this format
    savename = savedir + '/{}.{}'

    # Find all interesting files on that site:
    soup = BSoup(urllib.request.urlopen(the_path).read())

    # Find all links pointing to .dat files
    hrefs = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        # Download datafiles with markers given
        if href[-4::] == '.dat':
            hrefs.append(href[:-4])

    # Path to the file on the internet
    down_path = the_path + '{}.{}'

    for data_id in hrefs:
        for ext in extensions:
            webpath = down_path.format(data_id, ext)
            datafile = urllib.request.urlopen(webpath)

            # Save locally
            filepath = savename.format(data_id, ext)
            with open(filepath, 'wb') as out:
                out.write(datafile.read())

    print('Downloaded {} data files'.format(len(hrefs)))

if __name__ == '__main__':
    download_mitdb()
