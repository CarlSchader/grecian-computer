import pandas as pd
import numpy as np

def create_final_mat(plates):
  Z = np.zeros((12, 4), np.int32)
  for A in plates:
    Z = np.where(Z == 0, A, Z)
  return Z

def correct(Z):
  H = np.matmul(Z, np.ones((4), np.int32))
  for h in H:
    if h != 42:
      return False
  return True

def increment_indices(indices):
  for i in range(len(indices)):
    indices[i] = (indices[i] + 1) % 12
    if indices[i] != 0:
      break
  return indices

def rotate_plates(plates, shifts):
  new_plates = np.copy(plates)
  for i in range(len(shifts)):
    new_plates[i] = np.roll(new_plates[i], shifts[i], 0)
  return new_plates


indices = [0, 0, 0, 0]
plates = [pd.read_csv('plate{}.csv'.format(i)).values for i in range(5)]

for _ in range(12**4):
  if correct(create_final_mat(rotate_plates(plates, indices))):
    print('found')
    print(indices)
    print(create_final_mat(rotate_plates(plates, indices)))
    exit(0)
  increment_indices(indices)
print('no solution')
