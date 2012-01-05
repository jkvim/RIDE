#  Copyright 2008-2012 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import wx


class Label(wx.StaticText):

    def __init__(self, parent, id=-1, label='', **args):
        wx.StaticText.__init__(self, parent=parent, id=id, label=label.replace('&', '&&'), **args)

    def SetLabel(self, label):
        wx.StaticText.SetLabel(self, label.replace('&', '&&'))


class HeaderLabel(wx.StaticText):

    def __init__(self, parent, text):
        wx.StaticText.__init__(self, parent, -1, text)
        self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
