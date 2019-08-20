import collections


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        serialized_tree = []
        starting_depth = 1
        nodes_to_process = collections.deque([(root, starting_depth)])
        while nodes_to_process:
            curr, curr_depth = nodes_to_process.popleft()
            val = curr.val if curr else None
            serialized_tree.append("{0} {1}".format(val, curr_depth))
            if curr:
                nodes_to_process.append((curr.left, curr_depth+1))
                nodes_to_process.append((curr.right, curr_depth+1))
        return ','.join(serialized_tree)

    def deserialize(self, data):
        nodes_to_process = data.split(',')
        nodes_to_process.reverse()
        last_level = 0
        attach_index = 0
        this_level_nodes = []
        root = None
        while nodes_to_process:
            val, depth = nodes_to_process.pop().split()
            depth = int(depth)

            if depth != last_level:
                last_level = depth
                last_level_nodes = this_level_nodes[:]
                this_level_nodes = []
                attach_index = 0

            if val == "None":
                attach_index += 1
                continue
            val = int(val)
            node = TreeNode(val)
            if depth == 1:
                root = node
            this_level_nodes.append(node)

            if last_level_nodes:
                node_to_attach = last_level_nodes[attach_index//2]
                if attach_index & 1:
                    node_to_attach.right = node
                else:
                    node_to_attach.left = node
                attach_index += 1
        return root
