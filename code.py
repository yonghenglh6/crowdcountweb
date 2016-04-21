#!/usr/bin/env python
# coding: utf-8
import web
import pickle
import os
import string

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
        i = web.input(subpage="0", pagenum="1",taskid="-1")
        if(i.taskid=="-1"):
            return "NO this Task";
        pagenum=string.atoi(i.pagenum);
        mtask=TaskManager.get(string.atoi(i.taskid));
        traindir=mtask['traindir'];
        print 'static/data/'+traindir
        if os.path.exists('static/data/'+traindir):
            files=os.listdir('static/data/'+traindir);
            print len(files)
            print files
            picurl = 'static/data/'+traindir+"/"+files[pagenum];
            print picurl;
            output = {};
            output['IImagePath'] = picurl;
            output['taskid'] = i.taskid;
            output['pagenum'] = i.pagenum;
            output['sumpage'] = len(files);
            output['subpage'] = i.subpage;
            return render.biaoding(output)
        else:
            return "任务配置错误";


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
