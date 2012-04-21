import cherrypy
import csv
import json

class NHTG(object):
    def index(self, **params):
        reader = csv.reader(open("exams.csv"))
        data = []
        for row in reader: data.append(row)
        return json.dumps({'aaData': data})
    index.exposed = True

config = {'/static': {'tools.staticdir.on': True, 'tools.staticdir.dir': '/home/harry/nhtg12/static', 'tools.staticdir.debug': True, 'log.screen': True}}

cherrypy.tree.mount(NHTG(), "/", config=config)
cherrypy.engine.start()
cherrypy.engine.block()
