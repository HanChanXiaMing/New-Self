#定制类__gettattr__
class Chain(object):
  
  def __init__(self, path=''):
    self._path = path
    
   def __getattr__(self, path):
     return Chain('%s%s' %(self._path,path))
     
    def __str__(self):
      return self._path
      
     __return__ = __str__
