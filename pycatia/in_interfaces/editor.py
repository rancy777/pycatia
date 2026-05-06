#! usr/bin/python3.9
"""
    Editor interface wrapper.

    The editor object is returned by ``Application.active_editor``. It exposes
    the active object and selection used by automation examples that call
    ``CATIA.ActiveEditor``.

"""

from pycatia.in_interfaces.selection import Selection
from pycatia.system_interfaces.any_object import AnyObject


class Editor(AnyObject):
    """
    Wrapper for the CATIA editor automation object.
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.editor = com_object

    @property
    def active_object(self) -> AnyObject:
        """
        Returns the active object in the editor.

        :rtype: AnyObject
        """

        return AnyObject(self.editor.ActiveObject)

    @property
    def selection(self) -> Selection:
        """
        Returns the editor selection.

        :rtype: Selection
        """

        return Selection(self.editor.Selection)
