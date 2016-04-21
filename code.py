import web


urls = ("/", "begin",
        "/biaoding", "biaoding",
        "/renwuguanli", "renwuguanli",)
render = web.template.render('templates/')
app = web.application(urls, globals())

class begin:
    def GET(self):
        return render.index();


class biaoding:
    def GET(self):
        i = web.input(shujuji="default", picid="default")
        picurl = r"./static/data/1.jpg";
        output={};
        output['shujuji']=i.shujuji;
        output['picid'] = i.picid;
        output['picurl'] = picurl;
        return render.biaoding(output)

    def POST(self):
        id = 10;
        return "";


class renwuguanli:
    def GET(self):
        return 'Hello, world!'

if __name__ == "__main__":
    app.run()
