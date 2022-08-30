import numpy as np

def calculate(list):
  if len(list)==9:
    array=np.array(list)
    array=array.reshape(3,3)
    print(array)
    Dict=dict({
      'mean':[array.mean(axis=0).tolist(),array.mean(axis=1).tolist(),array.mean().tolist()],
      'variance':[array.var(axis=0).tolist(),array.var(axis=1).tolist(),array.var(axis=None).tolist()],
      'max':[np.amax(array,axis=0).tolist(),np.amax(array,axis=1).tolist(),np.amax(array).tolist()],
      'min':[np.amin(array,axis=0).tolist(),np.amin(array,axis=1).tolist(),np.amin(array).tolist()],
      'sum':[array.sum(axis=0).tolist(),array.sum(axis=1).tolist(),array.sum().tolist()]
    })
    return Dict
  else:
    raise ValueError("List must contain nine numbers.")


print(calculate([0,1,2,3,4,5,6,7,8]))

  




