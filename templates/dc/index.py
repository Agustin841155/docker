import web

render = web.template.render('dc/')
docker = web.template.render('dc/')
ubuntu = web.template.render('dc/')

class Index:
    def _init_(self):
        pass
    def GET(self):
        return render.index()
    
class Docker:
    def GET(self):
        return docker.docker()

class Ubuntu:
    def GET(self):
        return ubuntu.ubuntu()
