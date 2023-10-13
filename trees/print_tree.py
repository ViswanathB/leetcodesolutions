from typing import Optional, Any
from queue import Queue


class TreeNode:
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.left_node = None
        self.right_node = None


class Tree:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root

    def _height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return max(self._height(root.left_node), self._height(root.right_node)) + 1

    def printLevelWise(self):
        queue_bfs = Queue()

        queue_bfs.put(self.root)
        level = 0
        len_q = 1
        while not queue_bfs.empty():
            local_len_q = 0
            print(f"level : {level}")
            while len_q:
                f_ele_q = queue_bfs.get()
                print(f_ele_q.val)

                if f_ele_q.left_node != None:
                    queue_bfs.put(f_ele_q.left_node)
                    local_len_q += 1

                if f_ele_q.right_node != None:
                    queue_bfs.put(f_ele_q.right_node)
                    local_len_q += 1

                len_q -= 1

            level += 1
            len_q = local_len_q
            print()

    def getHeight(self):
        return self._height(self.root)

    def prettyPrint(self):
        node_q = Queue()

        height = self.getHeight()
        level = 1
        count = 1
        node_q.put(self.root)
        space = " "
        forward_slashes = []
        backward_slashes = []
        while level <= height:
            count = node_q._qsize()

            initial_space = pow(2, height - level) - 1
            middle_space = pow(2, height - level + 1) - 1
            print(f"{space*initial_space}", end="")
            cur_pos = initial_space
            while count:
                count -= 1
                next_ele = node_q.get()
                if next_ele != None:
                    if next_ele.val == 999999:
                        print(f"{space}{space*middle_space}", end="")
                        cur_pos += 1 + middle_space
                        if level < height:
                            node_q.put(TreeNode(999999))
                            node_q.put(TreeNode(999999))
                        continue
                    else:
                        print(f"{next_ele.val}{space*middle_space}", end="")
                        if next_ele.left_node != None:
                            node_q.put(next_ele.left_node)
                            forward_slashes.append(cur_pos - 1)
                        else:
                            node_q.put(TreeNode(999999))
                        if next_ele.right_node != None:
                            node_q.put(next_ele.right_node)
                            backward_slashes.append(cur_pos + 1)
                        else:
                            node_q.put(TreeNode(999999))

                        cur_pos += 1 + middle_space

            if level + 1 > height:
                break

            print()
            next_level = level + 1
            next_level_initial_space = pow(2, height - next_level) - 1
            for i in range(initial_space, next_level_initial_space + 1, -1):
                cur_pos = 0
                last_pos = backward_slashes[-1]
                for j in range(cur_pos, last_pos + 1):
                    if j == forward_slashes[0]:
                        print("/", end="")
                        forward_slashes.pop(0)
                        forward_slashes.append(j - 1)
                    elif j == backward_slashes[0]:
                        print("\\", end="")
                        backward_slashes.pop(0)
                        backward_slashes.append(j + 1)
                    else:
                        print(" ", end="")
                print()

            forward_slashes.clear()
            backward_slashes.clear()
            level += 1
        print()

    def construct(self, tree_string: str) -> Optional[Any]:
        if tree_string == "":
            return None

        root_node = TreeNode()
        tree_ref = Tree(root_node)

        deserialize_q = Queue()
        deserialize_q.put(root_node)
        str_index = 0
        while str_index < len(tree_string):
            current_node = tree_string[str_index : (str_index + 2)]

            q_node = deserialize_q.get()
            q_node.val = current_node[0]

            match int(current_node[1]):
                case 0:
                    q_node.left_node = TreeNode()
                    deserialize_q.put(q_node.left_node)
                case 1:
                    q_node.right_node = TreeNode()
                    deserialize_q.put(q_node.right_node)
                case 2:
                    q_node.left_node = TreeNode()
                    deserialize_q.put(q_node.left_node)

                    q_node.right_node = TreeNode()
                    deserialize_q.put(q_node.right_node)
                case 3:
                    pass

            str_index += 2

        self.root = tree_ref
        return tree_ref


"""
Test case 1
               a                               
              / \
             /   \
            /     \
           /       \
          /         \
         /           \
        /             \
       c               b               
      / \               \
     /   \               \
    /     \               \
   e       f               i       
  /         \               \
 g           h               j   
                            k l 
Test case 2
               a                               
              / \
             /   \
            /     \
           /       \
          /         \
         /           \
        /             \
       c               b               
      / \               \
     /   \               \
    /     \               \
   e       f               i       
  / \                       \
 g   k                       n   
l m                           o 
Test case 3
               a                               
              / \
             /   \
            /     \
           /       \
          /         \
         /           \
        /             \
       c               b               
      / \               \
     /   \               \
    /     \               \
   e       f               i       
  / \       \             / \
 g   k       1           2   n   
l m           3         4     o
"""
if __name__ == "__main__":
    print("Test case 1")
    serialized_tree_1 = "a2c2b1e0f1i1g3h3j2k3l3"

    test_tree_1 = Tree().construct(serialized_tree_1)
    assert test_tree_1
    # test_tree_1.printLevelWise()
    test_tree_1.prettyPrint()

    print("Test case 2")
    serialized_tree_2 = "a2c2b1e2f3i1g2k3n1l3m3o3"

    test_tree_2 = Tree().construct(serialized_tree_2)
    assert test_tree_2
    # test_tree_1.printLevelWise()
    test_tree_2.prettyPrint()

    print("Test case 3")
    serialized_tree_3 = "a2c2b1e2f1i2g2k31120n1l3m33343o3"

    test_tree_3 = Tree().construct(serialized_tree_3)
    assert test_tree_3
    # test_tree_1.printLevelWise()
    test_tree_3.prettyPrint()
