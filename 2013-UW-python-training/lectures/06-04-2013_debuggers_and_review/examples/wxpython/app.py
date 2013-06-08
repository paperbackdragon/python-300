import wx
from wx.lib.wordwrap import wordwrap

class MyApp(wx.App):
   def __init__(self, redirect=False, filename=None):
       wx.App.__init__(self, redirect, filename)
       self.frame = wx.Frame(None, wx.ID_ANY, title='My Title')

       self.panel = wx.Panel(self.frame, wx.ID_ANY)

       # copy the code for the AboutBox

       # change the button's parent to refer to my panel
       b = wx.Button(self.panel, -1, "Show a wx.AboutBox", (50,50))
       self.Bind(wx.EVT_BUTTON, self.OnButton, b)

       self.frame.Show()

   def OnButton(self, evt):
       # First we create and fill the info object
       info = wx.AboutDialogInfo()
       info.Name = "Hello World"
       info.Version = "1.2.3"
       info.Copyright = "(C) 2006 Programmers and Coders Everywhere"
       info.Description = wordwrap(
           "A \"hello world\" program is a software program that prints out "
           "\"Hello world!\" on a display device. It is used in many introductory "
           "tutorials for teaching a programming language."
                     "\n\nSuch a program is typically one of the simplest programs possible "
           "in a computer language. A \"hello world\" program can be a useful "
           "sanity test to make sure that a language's compiler, development "
           "environment, and run-time environment are correctly installed.",
           # change the wx.ClientDC to use self.panel instead of self
           350, wx.ClientDC(self.panel))
       info.WebSite = ("http://en.wikipedia.org/wiki/Hello_world", "Hello World home page")
       info.Developers = [ "Joe Programmer",
                           "Jane Coder",
                           "Vippy the Mascot" ]

       # change the wx.ClientDC to use self.panel instead of self
       info.License = wordwrap(licenseText, 500, wx.ClientDC(self.panel))

       # Then we call wx.AboutBox giving it that info object
       wx.AboutBox(info)

overview = """<html><body>
<h2><center>wx.AboutBox</center></h2>

This function shows the native standard about dialog containing the
information specified in info. If the current platform has a native
about dialog which is capable of showing all the fields in info, the
native dialog is used, otherwise the function falls back to the
generic wxWidgets version of the dialog.

</body></html>
"""


licenseText = "blah " * 250 + "\n\n" +"yadda " * 100

if __name__ == '__main__':
   app = MyApp()
   app.MainLoop()
