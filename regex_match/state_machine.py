"""
Regex match. if there is * it can match any character

*, aab    -> match
*a, aab  -> mismatch
a*, aab  -> match
a*b*,ab   -> match
a*b*, cacb -> mismatch
"""

import uuid
from queue import Queue

class StateMachineNode:
    def __init__(self, node_name: str) -> None:
        self.name = node_name
        self.neighbors = {}
        self.loop = False
        self.terminal_node = False

class StateMachine:
    def __init__(self) -> None:
        self.root_node = StateMachineNode("S0")
 
    def print(self) -> None:
        print("""
            PRINTING GRAPH
        """)
        q = Queue()
        q.put(self.root_node)

        while not q.empty():
            node = q.get()

            output_string = node.name
            if node.loop:
                output_string += "  (self loop)"
            if node.terminal_node:
                output_string += "   (terminal)"
            
            print(output_string)

            for k,v in node.neighbors.items():
                print(f"Going to {k}")
                q.put(v)

    def build(self, pattern: str) -> None:
        prev_node = self.root_node

        for item in pattern:
            if item == "*":
                prev_node.loop = True
            else:
                prev_node.neighbors[item] = StateMachineNode("S" + item + "_" + str(uuid.uuid4()))
                prev_node = prev_node.neighbors[item]

        prev_node.terminal_node = True

    def traverse(self, string:str) -> bool:
        q = Queue()
        q.put(self.root_node)

        for item in string:
            #print(f"matching {item}")
            count = q.qsize()

            if count == 0:
                return False

            while count:  
                node = q.get()
                if node.loop == True:
                    q.put(node)
                if item in node.neighbors:
                    q.put(node.neighbors[item])

                count -=1 

        while not q.empty():
            node = q.get()
            if node.terminal_node:
                return True
        
        return False

def regex_match(pattern: str, string: str):
    state_machine = StateMachine()
    state_machine.build(pattern)
    state_machine.print()
    return state_machine.traverse(string)

def test_cases():
    pattern = ["*", "a*", "a*b", "a*b", "a*b*", "a*b*", "a*b*", "a*b*c"]
    string = ["aab", "aab", "aab", "aa", "ab", "abaaa", "axasbsdsddb", "axasbsdsddb"]
    result = [True, True, True, False, True, True, True, False]

    for i in range(0, len(pattern)):
        print(f"""--------------------------TEST CASE MATCHING {pattern[i]} for {string[i]}------------""")
        if regex_match(pattern[i], string[i]) != result[i]:
            print(f"""---------------------------NOT MATCHING: {pattern[i]} -> {string[i]}---------------""")
        else:
            print(f"""---------------------------MATCH FOUND---------------------------------------""")


test_cases()