from typing import List, Union
import numpy as np
from collections import Counter
from spinqit.algorithm import VQE, TorchOptimizer
from spinqit.primitive import generate_hamitonian_matrix
from spinqit import X,Ry, Cx, CZ, CSWAP



class TSPSolver:
  def __init__(self, vertex_num: int, weighted_adjacency: Union[List, np.ndarray], penalty: float):
    """
    :param vertex_num: 顶点数量
    :param weighted_adjacency: 权重邻接矩阵
    :param penalty: 惩罚系数
    """
    self.vertex_num = vertex_num
    self.weighted_adjacency = np.array(weighted_adjacency)
    self.penalty = penalty

  def tsp_graph_to_hamitonian(self) -> List:
    hamitonian_list = []
    qubit_num = (self.vertex_num - 1) ** 2 # 由于特定情况下不一定是完全图，量子比特所需数量一般与边数相关
    # 我们需要为vertex_num-1个点的路径选择分配量子比特
    for i in range(self.vertex_num - 1):
      for j in range(self.vertex_num - 1):
        if i != j:
           l_ij = self.weighted_adjacency[i][j]

           for t in range(self.vertex_num - 2):
              pauli_list_1 = ['I'] * qubit_num
              pauli_list_2 = ['I'] * qubit_num
              pauli_list_3 = ['I'] * qubit_num
              pauli_list_4 = ['I'] * qubit_num

              

  
