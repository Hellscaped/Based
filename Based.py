import json,os
class Based:
  
  def __init__(self,name):
    
    self.db = {}
    
    self.name = name
    
    if os.path.isfile(f"{self.name}.json"):
      
      self.db = json.loads(open(f"{self.name}.json","r").read())
      
  def internal_function_set_db_DONOTUSE(self,newDb):
    
    self.db = newDb
    
  def get(self, *key):
    
    if not key:
      
      return self.db
    
    else:
      return self.db[key]
    
  def write(self, key,value):
    
    self.db[key] = value
    
    return f"<DatabaseKey Object>"
  
  def save(self):
    
    open(f"{self.name}.json","w").write(json.dumps(self.db))
    
  def nuke(self):
    
    self.internal_function_set_db_DONOTUSE({})
    
    self.save()
    
    return f"BOOM! Database '{self.name}' has been nuked!"
  
  def delete(self,key):
    
    self.db[key] = None
  def __getitem__(self, key=None):
    if key == None:
      return self.db
    if key in self.db:
      return self.db[key]
    else:
      return None
  def __setitem__(self,key,value):
    self.db[key] = value
