#!/usr/bin/env python
# coding: utf-8
import web

urls = ("/", "index",
        "/biaoding\.html", "biaoding",
        "/help\.html", "help",
        "/hotmap\.html", "hotmap",
        "/setting\.html", "setting",)
render = web.template.render('templates/')
app = web.application(urls, globals())


class index:
    def GET(self):
        return render.index();


class biaoding:
    def GET(self):
        i = web.input(shujuji="default", picid="default")
        picurl = r"./static/data/1.jpg";
        output = {};
        output['shujuji'] = i.shujuji;
        output['picid'] = i.picid;
        output['picurl'] = picurl;
        return render.biaoding(output)

    def POST(self):
        id = 10;
        return "";


class help:
    def GET(self):
        return render.help()


class hotmap:
    def GET(self):
        return render.hotmap()

class setting:
    def GET(self):
        return render.setting()


if __name__ == "__main__":
    app.run()
