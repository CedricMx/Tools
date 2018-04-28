# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

import tornado.web
import tornado.ioloop

# Local import
from handlers.url import urlpatterns

def make_app():
    app = tornado.web.Application(
        handlers=urlpatterns,
        # cookie_secret="MuG7xxacQdGPR7Svny1OfY6AymHPb0H/t02+I8rIHHE=",
        login_url="",
        expires_days=None,
        debug=True,
    )

    return app

def main():
    application = make_app()
    application.listen(8083)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
