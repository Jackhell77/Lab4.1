#coding:utf-8
import sae  
  
from adoaccess import wsgi     
  
application = sae.create_wsgi_app(wsgi.application)
#change_two