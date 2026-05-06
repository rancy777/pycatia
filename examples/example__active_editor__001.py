"""

    Example - Active Editor - 001

    Description:
        Get the active editor, active object and selection.

    Requirements:
        - CATIA running.
        - A session that exposes CATIA.ActiveEditor.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.in_interfaces.editor import Editor

application = catia()

editor: Editor = application.active_editor
active_object = editor.active_object
selection = editor.selection

print(active_object.name)
print(selection.count)
