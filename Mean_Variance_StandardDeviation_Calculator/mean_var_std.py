import numpy as np

def calculate(list):
  if len(list)!=9:
      raise ValueError('List must contain nine numbers.') 
  lst=np.array(list).reshape(3,3)
  calculations={}
  calculations['mean']=[np.mean(lst,axis=0).tolist(),np.mean(lst,axis=1).tolist(),np.mean(lst).tolist()]
  calculations['variance']=[np.var(lst,axis=0).tolist(),np.var(lst,axis=1).tolist(),np.var(lst).tolist()]
  calculations['standard deviation']=[np.std(lst,axis=0).tolist(),np.std(lst,axis=1).tolist(),np.std(lst).tolist()]
  calculations['max']=[np.max(lst,axis=0).tolist(),np.max(lst,axis=1).tolist(),np.max(lst).tolist()]
  calculations['min']=[np.min(lst,axis=0).tolist(),np.min(lst,axis=1).tolist(),np.min(lst).tolist()]
  calculations['sum']=[np.sum(lst,axis=0).tolist(),np.sum(lst,axis=1).tolist(),np.sum(lst).tolist()]
  return calculations    

print(calculate([0,1,2,3,4,5,6,7,8]))