import numpy as np


 
vec_a = np.array([23, 34, 27])
vec_b = np.array([-54, 1, 46])
vec_c = np.array([46, 68, 54])

#сонаправленость векторов, если угол 0 -соноправлены, 180 - противопложно напр

сos_theta_ab = np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))
сos_theta_ac = np.dot(vec_a, vec_c) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_c))
сos_theta_bc = np.dot(vec_b, vec_c) / (np.linalg.norm(vec_b) * np.linalg.norm(vec_c))

#дистанция между векторами
distance_ab = np.linalg.norm(vec_a - vec_b)
distance_ac = np.linalg.norm(vec_a - vec_c)
distance_bc = np.linalg.norm(vec_b - vec_c)

#ортогоналность векторов

print(np.dot(vec_a, vec_b), np.dot(vec_a, vec_c), np.dot(vec_b, vec_c))
