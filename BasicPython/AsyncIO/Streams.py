import asyncio
from urllib.parse import urlsplit

async def get_status(url):
    url_parsed = urlsplit(url)
    if url_parsed.scheme == 'https':
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 80)
    query = f'GET {url_parsed.path} HTTP/1.1\r\nHost: {url_parsed.hostname}\r\n\r\n'
    writer.write(query.encode())
    await writer.drain()
    response = await reader.readline()
    writer.close()
    status = response.decode().strip()
    return status

async def main():
    sites = ['https://www.google.com/',
    'https://www.youtube.com/',
    'https://www.facebook.com/',
    'https://twitter.com/',
    'https://www.instagram.com/',
    'https://www.wikipedia.org/',
    'https://yandex.ru/',
    'https://yahoo.com/',
    'https://www.whatsapp.com/']
    # check the status of all websites
    for url in sites:
        status = await get_status(url)
        print(f'{url:30}:\t{status}')

asyncio.run(main())
