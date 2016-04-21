#!/usr/bin/env python
# coding: utf-8
import web
import pickle
import os
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
        return render.setting(TaskManager.get())
    def POST(self):
        i = web.input(action="none", traindir="", predictdir="", background_picture="", rows="", columns="");
        if i.action=="newtask":
            ntask={"traindir":i.traindir, "predictdir":i.predictdir, "background_picture":i.background_picture, "rows":i.rows, "columns":i.columns};
            TaskManager.add(ntask);
        return render.setting(TaskManager.get());

class MTaskManager:
    def __init__(self):
        self.filename="tasks.list";
        if not os.path.exists(self.filename):
            self.tasks=[];
            with open(self.filename, 'w') as f:
                pickle.dump(self.tasks, f)
        else:
            with open(self.filename,'r') as f:
                self.tasks=pickle.load(f);
    def add(self,ntask):
        self.tasks.append(ntask);
        with open(self.filename, 'w') as f:
            pickle.dump(self.tasks, f)
    def get(self,id=-1):
        if id==-1:
            return self.tasks;
        else:
            return self.tasks[id]
TaskManager= MTaskManager();
if __name__ == "__main__":
    app.run()
