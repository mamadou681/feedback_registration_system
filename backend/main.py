import asyncio
from forward_to_rabbitmq import forward_to_queue
import tornado.web


class AjaxHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        res = self.request.body
        data = tornado.escape.json_decode(res)
        self.write(data)
        print(data)
        forward_to_queue(res)


def make_app():
    return tornado.web.Application([
        (r"/", AjaxHandler)
    ])


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
