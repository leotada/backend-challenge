import re

from sanic import Sanic
from sanic.response import json
from sanic.response import HTTPResponse

from gecko import simple_crawler

app = Sanic()


@app.route("/crawler/<url:path>", methods=['GET'])
async def crawler(request, url: str) -> HTTPResponse:
    """
    Endpoint to run crawler to a url parameter determined.
    Return JSON with result.
    """
    print('Received URL:', url)
    if re.search(r'([\w-]+\.)+(\w+)', url) is None:
        return json({'message': 'This is not a valid url'})

    if not url.startswith('https://') or not url.startswith('http://'):
        url = 'https://' + url

    if url.endswith('/'):
        url = url[:len(url)-1]

    print('Running crawler on', url)
    result = await simple_crawler(
        root_url=url, concurrency=30, timeout=5*60,
        save_urls=False, verbose=False)
    print('Done')
    if result is not None:
        return json(result)
    return json({'message': 'Timeout reached!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, access_log=True)
