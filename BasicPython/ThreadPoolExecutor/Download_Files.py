from os import makedirs
from os.path import basename
from os.path import join
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

def download_url(url):
    try:
        with urlopen(url, timeout=3) as connection:
            return (connection.read(), url)
    except:
        return (None, url)

def save_file(url, data, path):
    filename = basename(url)
    outpath = join(path, filename)
    with open(outpath, 'wb') as file:
        file.write(data)
    return outpath

def download_docs(urls, path):
    makedirs(path, exist_ok=True)
    n_threads = len(urls)
    with ThreadPoolExecutor(n_threads) as executor:
        futures = [executor.submit(download_url, url) for url in urls]
        for future in as_completed(futures):
            data, url = future.result()
            if data is None:
                print(f'Error download {url}')
                continue
            outpath = save_file(url, data, path)
            print(f'Save {url} to {outpath}')

URLS = ['https://docs.python.org/3/library/concurrency.html',
'https://docs.python.org/3/library/concurrent.html',
'https://docs.python.org/3/library/concurrent.futures.html',
'https://docs.python.org/3/library/threading.html',
'https://docs.python.org/3/library/multiprocessing.html',
'https://docs.python.org/3/library/multiprocessing.shared_memory.html',
'https://docs.python.org/3/library/subprocess.html',
'https://docs.python.org/3/library/queue.html',
'https://docs.python.org/3/library/sched.html',
'https://docs.python.org/3/library/contextvars.html']
# local path for saving the files
PATH = 'docs'
# download all docs
download_docs(URLS, PATH)