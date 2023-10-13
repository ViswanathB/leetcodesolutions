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
        while level <= height:
            count = node_q._qsize()

            initial_space = pow(2, height - level) - 1
            middle_space = pow(2, height - level + 1) - 1
            print()
            print(f"{space*initial_space}", end="")
            while count:
                count -= 1
                next_ele = node_q.get()
                if next_ele != None:
                    if next_ele.val == 999999:
                        print(f"{space}{space*middle_space}", end="")

                        if level < height:
                            node_q.put(TreeNode(999999))
                            node_q.put(TreeNode(999999))
                        continue
                    else:
                        print(f"{next_ele.val}{space*middle_space}", end="")
                        if next_ele.left_node != None:
                            node_q.put(next_ele.left_node)
                        else:
                            node_q.put(TreeNode(999999))
                        if next_ele.right_node != None:
                            node_q.put(next_ele.right_node)
                        else:
                            node_q.put(TreeNode(999999))

            level += 1
        print()


class SerializeDeserialize:
    def __init__(self):
        pass

    def serialize(self, root: Optional[Tree]) -> Optional[str]:
        if root:
            node_q = Queue()
            node_q.put(root.root)

            result = ""
            while not node_q.empty():
                next_node = node_q.get()
                result += next_node.val

                left_child = next_node.left_node
                right_child = next_node.right_node

                if left_child != None and right_child != None:
                    result += "2"
                elif left_child != None:
                    result += "0"
                elif right_child != None:
                    result += "1"
                else:
                    result += "3"

                if left_child != None:
                    node_q.put(left_child)

                if right_child != None:
                    node_q.put(right_child)

            return result

        return None

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
    # # test case 1
    # print("Test case 1")
    # serialized_tree = "a2c2b1e3f3i3"

    # test_tree_1 = SerializeDeserialize().deserialize(serialized_tree)
    # assert test_tree_1
    # # test_tree_1.printLevelWise()

    # # test case 2
    # print("Test case 2")
    # serialized_tree = "a2c2b1e0f1i1g3h3j2k3l3"

    # test_tree_2 = SerializeDeserialize().deserialize(serialized_tree)
    # assert test_tree_2
    # # test_tree_2.printLevelWise()

    # test case 3
    print("Test case 3")
    serialized_tree_3 = "a2c2b1e0f1i1g3h3j2k3l3"

    test_tree_3 = SerializeDeserialize().deserialize(serialized_tree_3)
    assert test_tree_3
    test_tree_3.printLevelWise()
    test_tree_3.prettyPrint()

    test_tree_3_serialize = SerializeDeserialize().serialize(test_tree_3)
    assert serialized_tree_3 == test_tree_3_serialize
