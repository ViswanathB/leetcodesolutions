from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.left_node = None
        self.right_node = None


class Tree:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

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


class SerializeDeserialize:
    def __init__(self):
        pass

    def deserialize(self, tree_string: str) -> Optional[Tree]:
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

        return tree_ref


if __name__ == "__main__":
    # test case 1
    print("Test case 1")
    serialized_tree = "a2c2b1e3f3i3"

    test_tree_1 = SerializeDeserialize().deserialize(serialized_tree)
    assert test_tree_1
    test_tree_1.printLevelWise()

    # test case 2
    print("Test case 2")
    serialized_tree = "a2c2b1e0f1i1g3h3j2k3l3"

    test_tree_1 = SerializeDeserialize().deserialize(serialized_tree)
    assert test_tree_1
    test_tree_1.printLevelWise()
