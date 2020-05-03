import hou

NODE = hou.pwd()
NODE_TYPES = ['matnet', 'geo', 'bone', 'null']
PREFIX = 'Spine'


def get_current_selected():
    current_selected = []
    sel = hou.selectedNodes()
    for node in sel:
        current_selected.append(node.name())
    if len(current_selected) < 1:
        print 'Nothing selected!'
    else:
        return current_selected


def get_all_children():
    child_nodes = []
    sel = hou.selectedNodes()
    for child in sel:
        child_node = child.children()
        for node in child_node:
            child_nodes.append(node.name())
        if len(child_nodes) < 1:
            print 'Nothing selected!'
        else:
            return child_nodes


def get_all_nodes_of_type(node_type=NODE_TYPES[3]):
    sel = hou.selectedNodes()
    nodes = []
    if len(sel) < 1:
        print 'Nothing selected!'
    else:
        for node in sel:
            child_nodes = node.children()
            for child in child_nodes:
                child_type = child.type()
                if child_type.name() == node_type:
                    nodes.append(child.name())
            return nodes


def get_all_nodes_of_prefix(prefix=PREFIX):
    sel = hou.selectedNodes()
    nodes = []
    if len(sel) < 1:
        print 'Nothing selected!'
    else:
        for child in sel:
            child_node = child.children()
            for node in child_node:
                if prefix in node.name():
                    nodes.append(node.name())
            return nodes


def select_file():
    hou.ui.selectFile(title='Select a File')


def display_message():
    hou.ui.displayMessage('Display Message')


