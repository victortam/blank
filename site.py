import cherrypy
import os
import json
import socket

from queries import *

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
ip = socket.gethostbyname(socket.gethostname())

class Root(object):

    @cherrypy.expose
    def index(self):
        return open(os.path.join(STATIC_DIR, u'index.html'))

    @cherrypy.expose
    def back_end_function(self, name):

        #get data from front
        cherrypy.session['name'] = name

        #do some stuff to the frontend data with python! (ie the whole point of this)
        sentence = name + " sucks!"
               
        #send data to front
        data = json.dumps(dict(sentence = sentence))
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return data.encode('utf8') 

    @cherrypy.expose
    def query_data_warehouse(self, date):

        #get data from front
        cherrypy.session['date'] = date

        #do some stuff to the frontend data with python! (ie the whole point of this)
        trial_count = fetch_trials(date)

        #send data to front
        data = json.dumps(dict(trial_count = trial_count))
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return data.encode('utf8')   


cherrypy.config.update({

    'log.screen': True,
    #'server.socket_host': '127.0.0.1',
    'server.socket_host': ip,
    'tools.sessions.on': True,
    'tools.encode.on': True,
    'tools.encode.encoding': 'utf-8',
})

#**********************************************************#

config = {
            '/static':
            {'tools.staticdir.on': True,
            'tools.staticdir.dir': STATIC_DIR,
            }
}                                                                                                                                                                                

cherrypy.tree.mount(Root(), '/', config=config)
cherrypy.engine.start()
