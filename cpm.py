import networkx as nx
import matplotlib.pyplot as plt

class CPM(nx.DiGraph):

    def __init__(self):
        super().__init__()
        self._changed = True
        self._makespan = -1
        self._criticalPath = None

    def add_node(self, *args, **kwargs):
        self._changed = True
        super().add_node(*args, **kwargs)

    def add_nodes_from(self, *args, **kwargs):
        self._changed = True
        super().add_nodes_from(*args, **kwargs)

    def add_edge(self, *args):  
        self._changed = True
        super().add_edge(*args) 

    def add_edges_from(self, *args, **kwargs):
        self._changed = True
        super().add_edges_from(*args, **kwargs)

    def remove_node(self, *args, **kwargs):
        self._changed = True
        super().remove_node(*args, **kwargs)

    def remove_nodes_from(self, *args, **kwargs):
        self._changed = True
        super().remove_nodes_from(*args, **kwargs)

    def remove_edge(self, *args): 
        self._changed = True
        super().remove_edge(*args) 

    def remove_edges_from(self, *args, **kwargs):
        self._changed = True
        super().remove_edges_from(*args, **kwargs)

    def _forward(self):
        for n in nx.topological_sort(self):
            S = max([self.node[j]['C']
                     for j in self.predecessors(n)], default=0)
            self.add_node(n, S=S, C=S + self.node[n]['p'])

    def _backward(self):
        for n in nx.topological_sort(self, reverse=True):
            Cp = min([self.node[j]['Sp']
                      for j in self.successors(n)], default=self._makespan)
            self.add_node(n, Sp=Cp - self.node[n]['p'], Cp=Cp)

    def _computeCriticalPath(self):
        G = set()
        for n in self:
            if self.node[n]['C'] == self.node[n]['Cp']:
                G.add(n)
        self._criticalPath = self.subgraph(G)

    @property
    def makespan(self):
        if self._changed:
            self._update()
        return self._makespan

    @property
    def criticalPath(self):
        if self._changed:
            self._update()
        return self._criticalPath

    def _update(self):
        self._forward()
        self._makespan = max(nx.get_node_attributes(self, 'C').values())
        self._backward()
        self._computeCriticalPath()
        self._changed = False

    def drawGraph(self, filename):
        nx.draw_networkx(self._criticalPath, with_labels=True, font_weight='bold')
        if filename:
            plt.savefig(filename)
        else:
            plt.savefig('cp-graph.png')

