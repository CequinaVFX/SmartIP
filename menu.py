from os import path

import nuke


def open_SmartIP():
    nukescripts.clear_selection_recursive()
    
    allNodes = nuke.allNodes('Group')
    
    validNode = False

    for node in allNodes:
        if node.name().startswith('SmartIP'):
            validNode = True
            smartNode = node

    if validNode:
        smartNode.showControlPanel(forceFloat = True)

        allViewer = nuke.allNodes('Viewer')
        for viewer in allViewer:
            viewer['input_process_node'].setValue('SmartIP')
        return()

    else:
        dirPath = '/nbpt/remote/homes/luciano.cequinel/nuke_custom_settings/nukeTools/SmartIP' # Replace this path
        nodepath = '/'.join([dirPath, 'SmartIP.nk'])
        nuke.loadToolset(nodepath)
        time.sleep(1)

        node = nuke.toNode('SmartIP')
        node.setXYpos(nuke.activeViewer().node().xpos()+200, nuke.activeViewer().node().ypos())

        node.showControlPanel(forceFloat = True)

        allViewer = nuke.allNodes('Viewer')
        for viewer in allViewer:
            viewer['input_process_node'].setValue('SmartIP')
        return   

t = nuke.toolbar("EXTRA_TOOLS") # creates a new toolbar
t.addCommand("IP", 'open_SmartIP()', "F8", shortcutContext=2)
