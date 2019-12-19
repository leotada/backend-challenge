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
    if url.endswith('/'):
        url = url[:len(url)-1]

    print('Running crawler')
    result = await simple_crawler(
        root_url=url, concurrency=30, timeout=5*60,
        save_urls=False, verbose=False)
    if result is not None:
        return json(result)
    return json({'message': 'Timeout reached!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
