
from tryalgo.Sequence import *  
from abc import ABC
from typing import Set, List, Dict, Optional, Union

class Node(ABC):

    def __init__(self, ID=None):
        self.parent = None
        self.full_counter = 0
        self.ID = ID
        self.is_terminal = False
        self.neighbors = None

    def is_full(self) -> bool:
        """
        Check if the element is full. Return True or False.
        """
        return self.full_counter >= len(self.neighbors) - 1

    def is_partial(self):
        """
        Check if the element is full. Return True or False.
        """
        return self.full_counter and not self.is_full()

    def signal_full(self):
        pass

    def clean(self):
        pass

    def attach(self, new):
        pass

    def detach(self, old):
        """
        Removes a neighbor.
        """
        if self.parent is old:
            self.parent = None
        self.neighbors.remove(old)


    def detach_bilateral(self, to_detach):
        """
        Deletes the link between this node and all given neighbors
        """
        for x in to_detach:
            x.detach(self)
            self.detach(x)

    def attach_neighbors(self) -> None:
        pass

    def represent_parent(self, show_parent: bool) -> List[Optional[int]]:
        pass


class Leaf(Node):
    def __init__(self, ID):
        super().__init__(ID)
        self.full = False

    def is_full(self):
        """
        Check if the element is full. Return True or False.
        """
        return self.full

    def clean(self):
        pass

    def to_signal(self):
        pass

    def detach(self, old):
        """
        Removes the link between an element and the parent.
        """
        assert self.parent is old
        self.parent = None

    def attach(self, new):
        pass

    def frontier(self, trace: List[int], enter: Node):
        pass



class P_node(Node):
    def __init__(self, neighbors: Set[Node] = set()):
        super().__init__()
        self.neighbors = neighbors
        self.full_neighbors: Set[Node] = set()
        self.attach_neighbors()

    def clean(self):
        pass

    def _splittable(self, left_terminal, right_terminal) -> None:
        """
        Verifies if we can split the node.
        Raises an exception if not.
        """
        pass            # P-nodes are always splittable

    def split(self):
        """
        Create a new full node that contains all the full neighbors 
        of this element, and it becomes an empty node.
        """
        self.detach_bilateral(self.full_neighbors)
        return P_node(neighbors=self.full_neighbors)

    def signal_full(self, full_neighbor):
        pass

    def to_signal(self):
        pass

    def represent(self, show_parent=False):
        pass
    
    def frontier(self, trace: List[int], enter: Node):
        pass

    def _simplify(self):
        pass
        


class C_node(Node):
    def __init__(self, neighbors: List[Node] = []):
        super().__init__()
        self.neighbors = Sequence(neighbors)
        self.first_full = None  
        self.attach_neighbors()

    def clean(self):
        pass

    def flip(self):
        pass

    def _splittable(self, left_terminal :Optional[Node], right_terminal :Optional[Node]) -> None:
        pass

    def split(self):
        """
        Splits a C node.
        Returns a new C-node with all full neighbors.
        """
        assert self.is_partial()        # will be called only for partial nodes

        L = [] # will contain the nodes of the full interval
        x = self.first_full
        while x.is_full():
            L.append(x)
            x = self.neighbors.successor(x)


        self.detach_bilateral(L)

        self.neighbors._first = id(x)

        split_off = C_node(L)
        split_off.neighbors._first = id(self.first_full)
        return split_off

    def signal_full(self, fullNeighbor):
        pass

    def to_signal(self):
        pass

    def represent(self, show_parent=False):
        pass
    
    def frontier(self, trace: List[int], enter: Node):
        pass

    def _simplify(self):
        pass
    
    def detach(self, old):
        """
        Removes a neighbor.
        """
        self.neighbors._first = id(self.neighbors.successor(old))
        super().detach(old)



class Infeasible(Exception):
    def __init__(self, reason):
        super().__init__("Impossible restriction because : " + reason)


Inner_node = Union[P_node, C_node]

class PC_tree:
    def __init__(self, nb_leaves: int):
        assert nb_leaves >= 3
        self.leaves = [Leaf(i) for i in range(nb_leaves)]
        P_node(set(self.leaves))    # initially the tree is a star

    def restrict(self, restriction):
        pass

    def _label(self, restriction):
        pass

    def _terminal_path(self, partial_nodes: Dict[int, Node]):
        pass
                            
    def _splittable(self, path :List[Inner_node]) -> None:
        pass

    def _split(self, path):
        pass

    def _simplify(self, path):
        pass

    def _remodel(self, path):
        pass

    def represent(self, show_parent=False):
        pass
    
    def frontier(self) -> List[int]:
        pass

        
    def print_dot(self):
        pass

