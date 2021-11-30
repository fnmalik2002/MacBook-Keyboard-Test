# -*- coding: utf-8 -*-
# Python GUI code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/

import wx
from wx.lib.mixins import listctrl


class kb_test(wx.Frame):
    bg_clr = wx.Colour(250, 250, 250)
    fr_clr = wx.Colour(76, 76, 76)

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Full Keyboard Test Utility", pos=wx.DefaultPosition,
                          size=wx.Size(1100, 370), style=wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        # attach the key bind event to accelerator table (to use cmd+q keys to close app)
        randomId = wx.NewIdRef(count=1)
        self.Bind(wx.EVT_MENU, self.onkeycombo, id=randomId)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('q'), randomId)])
        self.SetAcceleratorTable(accel_tbl)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)


        self.m_staticText_empty1 = wx.StaticText(self.m_panel1, wx.ID_ANY,
                                                 u"",
                                                 wx.DefaultPosition, wx.DefaultSize,
                                                 )
        self.m_button_reset = wx.Button(self.m_panel1, wx.ID_ANY, u"Reset", wx.DefaultPosition,
                                          wx.DefaultSize, 0)

        # self.m_staticText.SetFont(
        #     wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        self.m_staticText_empty2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize,
                                                 )
        bSizer3.Add(self.m_staticText_empty1, 10, wx.ALIGN_CENTER_VERTICAL, 5)
        bSizer3.Add(self.m_button_reset, 1, wx.ALL | wx.EXPAND, 5)
        bSizer3.Add(self.m_staticText_empty2, 10, wx.ALL, 5)

        bSizer2.Add(bSizer3, 0, wx.ALL, 10)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline1 = wx.StaticLine(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        self.m_staticline1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizer4.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 0)
        # self.m_staticText_empty = wx.StaticText(self.m_panel1, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize,
        #                                 )
        # bSizer4.Add(self.m_staticText_empty, 0, wx.ALL, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_esc = wx.StaticText(self.m_panel1, wx.ID_ANY, u"esc", wx.DefaultPosition, wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_esc.Wrap(-1)

        self.m_staticText_esc.SetForegroundColour(self.fr_clr)
        self.m_staticText_esc.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_esc, 0, wx.ALL, 5)

        self.m_staticText_f1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f1.Wrap(-1)

        self.m_staticText_f1.SetForegroundColour(self.fr_clr)
        self.m_staticText_f1.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f1, 0, wx.ALL, 5)

        self.m_staticText_f2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F2", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f2.Wrap(-1)

        self.m_staticText_f2.SetForegroundColour(self.fr_clr)
        self.m_staticText_f2.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f2, 0, wx.ALL, 5)

        self.m_staticText_f3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F3", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f3.Wrap(-1)

        self.m_staticText_f3.SetForegroundColour(self.fr_clr)
        self.m_staticText_f3.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f3, 0, wx.ALL, 5)

        self.m_staticText_f4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F4", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f4.Wrap(-1)

        self.m_staticText_f4.SetForegroundColour(self.fr_clr)
        self.m_staticText_f4.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f4, 0, wx.ALL, 5)

        self.m_staticText_f5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F5", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f5.Wrap(-1)

        self.m_staticText_f5.SetForegroundColour(self.fr_clr)
        self.m_staticText_f5.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f5, 0, wx.ALL, 5)

        self.m_staticText_f6 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F6", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f6.Wrap(-1)

        self.m_staticText_f6.SetForegroundColour(self.fr_clr)
        self.m_staticText_f6.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f6, 0, wx.ALL, 5)

        self.m_staticText_f7 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F7", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f7.Wrap(-1)

        self.m_staticText_f7.SetForegroundColour(self.fr_clr)
        self.m_staticText_f7.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f7, 0, wx.ALL, 5)

        self.m_staticText_f8 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F8", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f8.Wrap(-1)

        self.m_staticText_f8.SetForegroundColour(self.fr_clr)
        self.m_staticText_f8.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f8, 0, wx.ALL, 5)

        self.m_staticText_f9 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F9", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f9.Wrap(-1)

        self.m_staticText_f9.SetForegroundColour(self.fr_clr)
        self.m_staticText_f9.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f9, 0, wx.ALL, 5)

        self.m_staticText_f10 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F10", wx.DefaultPosition, wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f10.Wrap(-1)

        self.m_staticText_f10.SetForegroundColour(self.fr_clr)
        self.m_staticText_f10.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f10, 0, wx.ALL, 5)

        self.m_staticText_f11 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F11", wx.DefaultPosition, wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f11.Wrap(-1)

        self.m_staticText_f11.SetForegroundColour(self.fr_clr)
        self.m_staticText_f11.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f11, 0, wx.ALL, 5)

        self.m_staticText_f12 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F12", wx.DefaultPosition, wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f12.Wrap(-1)

        self.m_staticText_f12.SetForegroundColour(self.fr_clr)
        self.m_staticText_f12.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_f12, 0, wx.ALL, 5)

        self.m_staticText_eject = wx.StaticText(self.m_panel1, wx.ID_ANY, u'\u23CF', wx.DefaultPosition,
                                                wx.Size(40, 20),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_eject.Wrap(-1)

        self.m_staticText_eject.SetForegroundColour(self.fr_clr)
        self.m_staticText_eject.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_eject, 0, wx.ALL, 5)

        """------------First row extended --------"""
        self.m_staticText_empty = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                              wx.Size(10, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty.Wrap(-1)
        bSizer5.Add(self.m_staticText_empty, 0, wx.ALL, 5)

        self.m_staticText_F13 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'F13', wx.DefaultPosition,
                                                wx.Size(40, 20),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_F13.Wrap(-1)

        self.m_staticText_F13.SetForegroundColour(self.fr_clr)
        self.m_staticText_F13.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_F13, 0, wx.ALL, 5)

        self.m_staticText_F14 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'F13', wx.DefaultPosition,
                                              wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_F14.Wrap(-1)

        self.m_staticText_F14.SetForegroundColour(self.fr_clr)
        self.m_staticText_F14.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_F14, 0, wx.ALL, 5)

        self.m_staticText_F15 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'F13', wx.DefaultPosition,
                                              wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_F15.Wrap(-1)

        self.m_staticText_F15.SetForegroundColour(self.fr_clr)
        self.m_staticText_F15.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_F15, 0, wx.ALL, 5)

        self.m_staticText_empty11 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                wx.Size(10, 20),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty.Wrap(-1)
        bSizer5.Add(self.m_staticText_empty11, 0, wx.ALL, 5)

        self.m_staticText_F16 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'F16', wx.DefaultPosition,
                                              wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_F16.Wrap(-1)

        self.m_staticText_F16.SetForegroundColour(self.fr_clr)
        self.m_staticText_F16.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_F16, 0, wx.ALL, 5)

        self.m_staticText_F17 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'F17', wx.DefaultPosition,
                                              wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_F17.Wrap(-1)

        self.m_staticText_F17.SetForegroundColour(self.fr_clr)
        self.m_staticText_F17.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_F17, 0, wx.ALL, 5)

        self.m_staticText_F18 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'F18', wx.DefaultPosition,
                                              wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_F18.Wrap(-1)

        self.m_staticText_F18.SetForegroundColour(self.fr_clr)
        self.m_staticText_F18.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_F18, 0, wx.ALL, 5)

        self.m_staticText_F19 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'F19', wx.DefaultPosition,
                                              wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_F19.Wrap(-1)

        self.m_staticText_F19.SetForegroundColour(self.fr_clr)
        self.m_staticText_F19.SetBackgroundColour(self.bg_clr)

        bSizer5.Add(self.m_staticText_F19, 0, wx.ALL, 5)
        """--------- end of line 1 -----------"""







        bSizer4.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_tilde = wx.StaticText(self.m_panel1, wx.ID_ANY, u"~\n`", wx.DefaultPosition, wx.Size(38, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_tilde.Wrap(-1)

        self.m_staticText_tilde.SetForegroundColour(self.fr_clr)
        self.m_staticText_tilde.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_tilde, 0, wx.ALL, 5)

        self.m_staticText_1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"!\n1", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_1.Wrap(-1)

        self.m_staticText_1.SetForegroundColour(self.fr_clr)
        self.m_staticText_1.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_1, 0, wx.ALL, 5)

        self.m_staticText_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"@\n2", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_2.Wrap(-1)

        self.m_staticText_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_2.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_2, 0, wx.ALL, 5)

        self.m_staticText_3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"#\n3", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_3.Wrap(-1)

        self.m_staticText_3.SetForegroundColour(self.fr_clr)
        self.m_staticText_3.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_3, 0, wx.ALL, 5)

        self.m_staticText_4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"$\n4", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_4.Wrap(-1)

        self.m_staticText_4.SetForegroundColour(self.fr_clr)
        self.m_staticText_4.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_4, 0, wx.ALL, 5)

        self.m_staticText_5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"%\n5", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_5.Wrap(-1)

        self.m_staticText_5.SetForegroundColour(self.fr_clr)
        self.m_staticText_5.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_5, 0, wx.ALL, 5)

        self.m_staticText_6 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"^\n6", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_6.Wrap(-1)

        self.m_staticText_6.SetForegroundColour(self.fr_clr)
        self.m_staticText_6.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_6, 0, wx.ALL, 5)

        self.m_staticText_7 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"&&\n7", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_7.Wrap(-1)

        self.m_staticText_7.SetForegroundColour(self.fr_clr)
        self.m_staticText_7.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_7, 0, wx.ALL, 5)

        self.m_staticText_8 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"*\n8", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_8.Wrap(-1)

        self.m_staticText_8.SetForegroundColour(self.fr_clr)
        self.m_staticText_8.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_8, 0, wx.ALL, 5)

        self.m_staticText_9 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"(\n9", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_9.Wrap(-1)

        self.m_staticText_9.SetForegroundColour(self.fr_clr)
        self.m_staticText_9.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_9, 0, wx.ALL, 5)

        self.m_staticText_0 = wx.StaticText(self.m_panel1, wx.ID_ANY, u")\n0", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_0.Wrap(-1)

        self.m_staticText_0.SetForegroundColour(self.fr_clr)
        self.m_staticText_0.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_0, 0, wx.ALL, 5)

        self.m_staticText_minus = wx.StaticText(self.m_panel1, wx.ID_ANY, u"_\n-", wx.DefaultPosition, wx.Size(38, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_minus.Wrap(-1)

        self.m_staticText_minus.SetForegroundColour(self.fr_clr)
        self.m_staticText_minus.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_minus, 0, wx.ALL, 5)

        self.m_staticText_plus = wx.StaticText(self.m_panel1, wx.ID_ANY, u"+\n=", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_plus.Wrap(-1)

        self.m_staticText_plus.SetForegroundColour(self.fr_clr)
        self.m_staticText_plus.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_plus, 0, wx.ALL, 5)

        self.m_staticText_delete = wx.StaticText(self.m_panel1, wx.ID_ANY, u"delete", wx.DefaultPosition,
                                                 wx.Size(67, 38),
                                                 wx.ALIGN_RIGHT)
        self.m_staticText_delete.Wrap(-1)

        self.m_staticText_delete.SetForegroundColour(self.fr_clr)
        self.m_staticText_delete.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_delete, 0, wx.ALL, 5)

        """-----------  2nd line extended -----------"""
        self.m_staticText_empty = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                wx.Size(10, 20),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty.Wrap(-1)
        bSizer6.Add(self.m_staticText_empty, 0, wx.ALL, 5)

        self.m_staticText_fn = wx.StaticText(self.m_panel1, wx.ID_ANY, u'fn', wx.DefaultPosition,
                                              wx.Size(40, 38),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_fn.Wrap(-1)

        self.m_staticText_fn.SetForegroundColour(self.fr_clr)
        self.m_staticText_fn.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_fn, 0, wx.ALL, 5)

        self.m_staticText_home = wx.StaticText(self.m_panel1, wx.ID_ANY, u'home', wx.DefaultPosition,
                                              wx.Size(40, 38),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_home.Wrap(-1)

        self.m_staticText_home.SetForegroundColour(self.fr_clr)
        self.m_staticText_home.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_home, 0, wx.ALL, 5)

        self.m_staticText_pgup = wx.StaticText(self.m_panel1, wx.ID_ANY, u'page\nup', wx.DefaultPosition,
                                              wx.Size(40, 38),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_pgup.Wrap(-1)

        self.m_staticText_pgup.SetForegroundColour(self.fr_clr)
        self.m_staticText_pgup.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_pgup, 0, wx.ALL, 5)

        self.m_staticText_empty11 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                  wx.Size(10, 38),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty.Wrap(-1)
        bSizer6.Add(self.m_staticText_empty11, 0, wx.ALL, 5)

        self.m_staticText_clear = wx.StaticText(self.m_panel1, wx.ID_ANY, u'clear', wx.DefaultPosition,
                                              wx.Size(40, 38),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_clear.Wrap(-1)

        self.m_staticText_clear.SetForegroundColour(self.fr_clr)
        self.m_staticText_clear.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_clear, 0, wx.ALL, 5)

        self.m_staticText_equal2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'=', wx.DefaultPosition,
                                              wx.Size(40, 38),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_equal2.Wrap(-1)

        self.m_staticText_equal2.SetForegroundColour(self.fr_clr)
        self.m_staticText_equal2.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_equal2, 0, wx.ALL, 5)

        self.m_staticText_fslah = wx.StaticText(self.m_panel1, wx.ID_ANY, u'/', wx.DefaultPosition,
                                              wx.Size(40, 38),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_fslah.Wrap(-1)

        self.m_staticText_fslah.SetForegroundColour(self.fr_clr)
        self.m_staticText_fslah.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_fslah, 0, wx.ALL, 5)

        self.m_staticText_esteric = wx.StaticText(self.m_panel1, wx.ID_ANY, u'*', wx.DefaultPosition,
                                              wx.Size(40, 38),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_esteric.Wrap(-1)

        self.m_staticText_esteric.SetForegroundColour(self.fr_clr)
        self.m_staticText_esteric.SetBackgroundColour(self.bg_clr)

        bSizer6.Add(self.m_staticText_esteric, 0, wx.ALL, 5)
        """--------- end of line 2 -----------"""














        bSizer4.Add(bSizer6, 0, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_tab = wx.StaticText(self.m_panel1, wx.ID_ANY, u"tab", wx.DefaultPosition, wx.Size(67, 38), 0)
        self.m_staticText_tab.Wrap(-1)

        self.m_staticText_tab.SetForegroundColour(self.fr_clr)
        self.m_staticText_tab.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_tab, 0, wx.ALL, 5)

        self.m_staticText_q = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Q", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_q.Wrap(-1)

        self.m_staticText_q.SetForegroundColour(self.fr_clr)
        self.m_staticText_q.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_q, 0, wx.ALL, 5)

        self.m_staticText_w = wx.StaticText(self.m_panel1, wx.ID_ANY, u"W", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_w.Wrap(-1)

        self.m_staticText_w.SetForegroundColour(self.fr_clr)
        self.m_staticText_w.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_w, 0, wx.ALL, 5)

        self.m_staticText_e = wx.StaticText(self.m_panel1, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_e.Wrap(-1)

        self.m_staticText_e.SetForegroundColour(self.fr_clr)
        self.m_staticText_e.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_e, 0, wx.ALL, 5)

        self.m_staticText_r = wx.StaticText(self.m_panel1, wx.ID_ANY, u"R", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_r.Wrap(-1)

        self.m_staticText_r.SetForegroundColour(self.fr_clr)
        self.m_staticText_r.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_r, 0, wx.ALL, 5)

        self.m_staticText_t = wx.StaticText(self.m_panel1, wx.ID_ANY, u"T", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_t.Wrap(-1)

        self.m_staticText_t.SetForegroundColour(self.fr_clr)
        self.m_staticText_t.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_t, 0, wx.ALL, 5)

        self.m_staticText_y = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_y.Wrap(-1)

        self.m_staticText_y.SetForegroundColour(self.fr_clr)
        self.m_staticText_y.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_y, 0, wx.ALL, 5)

        self.m_staticText_u = wx.StaticText(self.m_panel1, wx.ID_ANY, u"U", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_u.Wrap(-1)

        self.m_staticText_u.SetForegroundColour(self.fr_clr)
        self.m_staticText_u.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_u, 0, wx.ALL, 5)

        self.m_staticText_i = wx.StaticText(self.m_panel1, wx.ID_ANY, u"I", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_i.Wrap(-1)

        self.m_staticText_i.SetForegroundColour(self.fr_clr)
        self.m_staticText_i.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_i, 0, wx.ALL, 5)

        self.m_staticText_o = wx.StaticText(self.m_panel1, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_o.Wrap(-1)

        self.m_staticText_o.SetForegroundColour(self.fr_clr)
        self.m_staticText_o.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_o, 0, wx.ALL, 5)

        self.m_staticText_p = wx.StaticText(self.m_panel1, wx.ID_ANY, u"P", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_p.Wrap(-1)

        self.m_staticText_p.SetForegroundColour(self.fr_clr)
        self.m_staticText_p.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_p, 0, wx.ALL, 5)

        self.m_staticText_curly_left = wx.StaticText(self.m_panel1, wx.ID_ANY, u"{\n[", wx.DefaultPosition,
                                                     wx.Size(38, 38),
                                                     wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_curly_left.Wrap(-1)

        self.m_staticText_curly_left.SetForegroundColour(self.fr_clr)
        self.m_staticText_curly_left.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_curly_left, 0, wx.ALL, 5)

        self.m_staticText_curly_right = wx.StaticText(self.m_panel1, wx.ID_ANY, u"}\n]", wx.DefaultPosition,
                                                      wx.Size(38, 38),
                                                      wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_curly_right.Wrap(-1)

        self.m_staticText_curly_right.SetForegroundColour(self.fr_clr)
        self.m_staticText_curly_right.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_curly_right, 0, wx.ALL, 5)

        self.m_staticText_pipe = wx.StaticText(self.m_panel1, wx.ID_ANY, u"|\n\\", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_pipe.Wrap(-1)

        self.m_staticText_pipe.SetForegroundColour(self.fr_clr)
        self.m_staticText_pipe.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_pipe, 0, wx.ALL, 5)

        """-----------  2nd line extended -----------"""
        self.m_staticText_empty = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                wx.Size(10, 20),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty.Wrap(-1)
        bSizer7.Add(self.m_staticText_empty, 0, wx.ALL, 5)

        self.m_staticText_del2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'delete', wx.DefaultPosition,
                                             wx.Size(40, 38),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_del2.Wrap(-1)

        self.m_staticText_del2.SetForegroundColour(self.fr_clr)
        self.m_staticText_del2.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_del2, 0, wx.ALL, 5)

        self.m_staticText_end = wx.StaticText(self.m_panel1, wx.ID_ANY, u'end', wx.DefaultPosition,
                                               wx.Size(40, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_end.Wrap(-1)

        self.m_staticText_end.SetForegroundColour(self.fr_clr)
        self.m_staticText_end.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_end, 0, wx.ALL, 5)

        self.m_staticText_pgdn = wx.StaticText(self.m_panel1, wx.ID_ANY, u'page\ndown', wx.DefaultPosition,
                                               wx.Size(40, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_pgdn.Wrap(-1)

        self.m_staticText_pgdn.SetForegroundColour(self.fr_clr)
        self.m_staticText_pgdn.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_pgdn, 0, wx.ALL, 5)

        self.m_staticText_empty111 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                  wx.Size(10, 20),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty111.Wrap(-1)
        bSizer7.Add(self.m_staticText_empty111, 0, wx.ALL, 5)

        self.m_staticText_7_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'7', wx.DefaultPosition,
                                                wx.Size(40, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_7_2.Wrap(-1)

        self.m_staticText_7_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_7_2.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_7_2, 0, wx.ALL, 5)

        self.m_staticText_8_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'8', wx.DefaultPosition,
                                                 wx.Size(40, 38),
                                                 wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_8_2.Wrap(-1)

        self.m_staticText_8_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_8_2.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_8_2, 0, wx.ALL, 5)

        self.m_staticText_9_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'9', wx.DefaultPosition,
                                                wx.Size(40, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_9_2.Wrap(-1)

        self.m_staticText_9_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_9_2.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_9_2, 0, wx.ALL, 5)

        self.m_staticText_minus_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'-', wx.DefaultPosition,
                                                  wx.Size(40, 38),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_minus_2.Wrap(-1)

        self.m_staticText_minus_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_minus_2.SetBackgroundColour(self.bg_clr)

        bSizer7.Add(self.m_staticText_minus_2, 0, wx.ALL, 5)
        """--------- end of line 3 -----------"""




        bSizer4.Add(bSizer7, 0, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_caps = wx.StaticText(self.m_panel1, wx.ID_ANY, u"caps lock", wx.DefaultPosition,
                                               wx.Size(77, 38), wx.ALIGN_LEFT)
        self.m_staticText_caps.Wrap(-1)

        self.m_staticText_caps.SetForegroundColour(self.fr_clr)
        self.m_staticText_caps.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_caps, 0, wx.ALL, 5)

        self.m_staticText_a = wx.StaticText(self.m_panel1, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_a.Wrap(-1)

        self.m_staticText_a.SetForegroundColour(self.fr_clr)
        self.m_staticText_a.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_a, 0, wx.ALL, 5)

        self.m_staticText_s = wx.StaticText(self.m_panel1, wx.ID_ANY, u"S", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_s.Wrap(-1)

        self.m_staticText_s.SetForegroundColour(self.fr_clr)
        self.m_staticText_s.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_s, 0, wx.ALL, 5)

        self.m_staticText_d = wx.StaticText(self.m_panel1, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_d.Wrap(-1)

        self.m_staticText_d.SetForegroundColour(self.fr_clr)
        self.m_staticText_d.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_d, 0, wx.ALL, 5)

        self.m_staticText_f = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f.Wrap(-1)

        self.m_staticText_f.SetForegroundColour(self.fr_clr)
        self.m_staticText_f.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_f, 0, wx.ALL, 5)

        self.m_staticText_g = wx.StaticText(self.m_panel1, wx.ID_ANY, u"G", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_g.Wrap(-1)

        self.m_staticText_g.SetForegroundColour(self.fr_clr)
        self.m_staticText_g.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_g, 0, wx.ALL, 5)

        self.m_staticText_h = wx.StaticText(self.m_panel1, wx.ID_ANY, u"H", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_h.Wrap(-1)

        self.m_staticText_h.SetForegroundColour(self.fr_clr)
        self.m_staticText_h.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_h, 0, wx.ALL, 5)

        self.m_staticText_j = wx.StaticText(self.m_panel1, wx.ID_ANY, u"J", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_j.Wrap(-1)

        self.m_staticText_j.SetForegroundColour(self.fr_clr)
        self.m_staticText_j.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_j, 0, wx.ALL, 5)

        self.m_staticText_k = wx.StaticText(self.m_panel1, wx.ID_ANY, u"K", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_k.Wrap(-1)

        self.m_staticText_k.SetForegroundColour(self.fr_clr)
        self.m_staticText_k.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_k, 0, wx.ALL, 5)

        self.m_staticText_l = wx.StaticText(self.m_panel1, wx.ID_ANY, u"L", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_l.Wrap(-1)

        self.m_staticText_l.SetForegroundColour(self.fr_clr)
        self.m_staticText_l.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_l, 0, wx.ALL, 5)

        self.m_staticText_colon = wx.StaticText(self.m_panel1, wx.ID_ANY, u":\n;", wx.DefaultPosition, wx.Size(38, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_colon.Wrap(-1)

        self.m_staticText_colon.SetForegroundColour(self.fr_clr)
        self.m_staticText_colon.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_colon, 0, wx.ALL, 5)

        self.m_staticText_quote = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\"\n'", wx.DefaultPosition, wx.Size(38, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_quote.Wrap(-1)

        self.m_staticText_quote.SetForegroundColour(self.fr_clr)
        self.m_staticText_quote.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_quote, 0, wx.ALL, 5)

        self.m_staticText_enter = wx.StaticText(self.m_panel1, wx.ID_ANY, u"enter\nreturn", wx.DefaultPosition,
                                                wx.Size(77, 38), wx.ALIGN_RIGHT)
        self.m_staticText_enter.Wrap(-1)

        self.m_staticText_enter.SetForegroundColour(self.fr_clr)
        self.m_staticText_enter.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_enter, 0, wx.ALL, 5)
        """-------------- line 4 --------------"""
        """-----------  4th line extended -----------"""
        self.m_staticText_empty4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                wx.Size(10, 20),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty4.Wrap(-1)
        bSizer8.Add(self.m_staticText_empty4, 0, wx.ALL, 5)

        self.m_staticText_empty41 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                             wx.Size(40, 38),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty41.Wrap(-1)

        # self.m_staticText_empty41.SetForegroundColour(self.fr_clr)
        # self.m_staticText_empty41.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_empty41, 0, wx.ALL, 5)

        self.m_staticText_42 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                               wx.Size(40, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_42.Wrap(-1)

        # self.m_staticText_42.SetForegroundColour(self.fr_clr)
        # self.m_staticText_42.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_42, 0, wx.ALL, 5)

        self.m_staticText_43 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                               wx.Size(40, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_43.Wrap(-1)

        # self.m_staticText_43.SetForegroundColour(self.fr_clr)
        # self.m_staticText_43.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_43, 0, wx.ALL, 5)

        self.m_staticText_empty44 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                  wx.Size(10, 20),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty44.Wrap(-1)
        bSizer8.Add(self.m_staticText_empty44, 0, wx.ALL, 5)

        self.m_staticText_4_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'4', wx.DefaultPosition,
                                                wx.Size(40, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_4_2.Wrap(-1)

        self.m_staticText_4_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_4_2.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_4_2, 0, wx.ALL, 5)

        self.m_staticText_5_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'5', wx.DefaultPosition,
                                                 wx.Size(40, 38),
                                                 wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_5_2.Wrap(-1)

        self.m_staticText_5_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_5_2.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_5_2, 0, wx.ALL, 5)

        self.m_staticText_6_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'6', wx.DefaultPosition,
                                                wx.Size(40, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_6_2.Wrap(-1)

        self.m_staticText_6_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_6_2.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_6_2, 0, wx.ALL, 5)

        self.m_staticText_plus_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'+', wx.DefaultPosition,
                                                  wx.Size(40, 38),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_plus_2.Wrap(-1)

        self.m_staticText_plus_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_plus_2.SetBackgroundColour(self.bg_clr)

        bSizer8.Add(self.m_staticText_plus_2, 0, wx.ALL, 5)
        """--------- end of line 4 -----------"""









        bSizer4.Add(bSizer8, 0, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_left_shift = wx.StaticText(self.m_panel1, wx.ID_ANY, u"shift", wx.DefaultPosition,
                                                     wx.Size(101, 38),
                                                     0)
        self.m_staticText_left_shift.Wrap(-1)

        self.m_staticText_left_shift.SetForegroundColour(self.fr_clr)
        self.m_staticText_left_shift.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_left_shift, 0, wx.ALL, 5)

        self.m_staticText_z = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Z", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_z.Wrap(-1)

        self.m_staticText_z.SetForegroundColour(self.fr_clr)
        self.m_staticText_z.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_z, 0, wx.ALL, 5)

        self.m_staticText_x = wx.StaticText(self.m_panel1, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_x.Wrap(-1)

        self.m_staticText_x.SetForegroundColour(self.fr_clr)
        self.m_staticText_x.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_x, 0, wx.ALL, 5)

        self.m_staticText_c = wx.StaticText(self.m_panel1, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_c.Wrap(-1)

        self.m_staticText_c.SetForegroundColour(self.fr_clr)
        self.m_staticText_c.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_c, 0, wx.ALL, 5)

        self.m_staticText_v = wx.StaticText(self.m_panel1, wx.ID_ANY, u"V", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_v.Wrap(-1)

        self.m_staticText_v.SetForegroundColour(self.fr_clr)
        self.m_staticText_v.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_v, 0, wx.ALL, 5)

        self.m_staticText_b = wx.StaticText(self.m_panel1, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_b.Wrap(-1)

        self.m_staticText_b.SetForegroundColour(self.fr_clr)
        self.m_staticText_b.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_b, 0, wx.ALL, 5)

        self.m_staticText_n = wx.StaticText(self.m_panel1, wx.ID_ANY, u"N", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_n.Wrap(-1)

        self.m_staticText_n.SetForegroundColour(self.fr_clr)
        self.m_staticText_n.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_n, 0, wx.ALL, 5)

        self.m_staticText_m = wx.StaticText(self.m_panel1, wx.ID_ANY, u"M", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_m.Wrap(-1)

        self.m_staticText_m.SetForegroundColour(self.fr_clr)
        self.m_staticText_m.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_m, 0, wx.ALL, 5)

        self.m_staticText_less = wx.StaticText(self.m_panel1, wx.ID_ANY, u"<\n,", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_less.Wrap(-1)

        self.m_staticText_less.SetForegroundColour(self.fr_clr)
        self.m_staticText_less.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_less, 0, wx.ALL, 5)

        self.m_staticText_more = wx.StaticText(self.m_panel1, wx.ID_ANY, u">\n.", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_more.Wrap(-1)

        self.m_staticText_more.SetForegroundColour(self.fr_clr)
        self.m_staticText_more.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_more, 0, wx.ALL, 5)

        self.m_staticText_question = wx.StaticText(self.m_panel1, wx.ID_ANY, u"?\n/", wx.DefaultPosition,
                                                   wx.Size(38, 38),
                                                   wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_question.Wrap(-1)

        self.m_staticText_question.SetForegroundColour(self.fr_clr)
        self.m_staticText_question.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_question, 0, wx.ALL, 5)

        self.m_staticText_right_shift = wx.StaticText(self.m_panel1, wx.ID_ANY, u"shift", wx.DefaultPosition,
                                                      wx.Size(101, 38),
                                                      wx.ALIGN_RIGHT)
        self.m_staticText_right_shift.Wrap(-1)

        self.m_staticText_right_shift.SetForegroundColour(self.fr_clr)
        self.m_staticText_right_shift.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_right_shift, 0, wx.ALL, 5)

        """--------------- extended line 5 started --------------------"""

        self.m_staticText_empty45 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                wx.Size(10, 20),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty45.Wrap(-1)
        bSizer9.Add(self.m_staticText_empty45, 0, wx.ALL, 5)

        self.m_staticText_empty451 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                             wx.Size(40, 38),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty451.Wrap(-1)

        # self.m_staticText_empty41.SetForegroundColour(self.fr_clr)
        # self.m_staticText_empty41.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_empty451, 0, wx.ALL, 5)

        self.m_staticText_top_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u'\u2191', wx.DefaultPosition,
                                               wx.Size(40, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_top_arrow.Wrap(-1)

        self.m_staticText_top_arrow.SetForegroundColour(self.fr_clr)
        self.m_staticText_top_arrow.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_top_arrow, 0, wx.ALL, 5)

        self.m_staticText_453 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                               wx.Size(40, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_453.Wrap(-1)

        # self.m_staticText_433.SetForegroundColour(self.fr_clr)
        # self.m_staticText_433.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_453, 0, wx.ALL, 5)

        self.m_staticText_empty444 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                  wx.Size(10, 20),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty444.Wrap(-1)
        bSizer9.Add(self.m_staticText_empty444, 0, wx.ALL, 5)

        self.m_staticText_1_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'1', wx.DefaultPosition,
                                                wx.Size(40, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_1_2.Wrap(-1)

        self.m_staticText_1_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_1_2.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_1_2, 0, wx.ALL, 5)

        self.m_staticText_2_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'2', wx.DefaultPosition,
                                                 wx.Size(40, 38),
                                                 wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_2_2.Wrap(-1)

        self.m_staticText_2_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_2_2.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_2_2, 0, wx.ALL, 5)

        self.m_staticText_3_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'3', wx.DefaultPosition,
                                                wx.Size(40, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_3_2.Wrap(-1)

        self.m_staticText_3_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_3_2.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_3_2, 0, wx.ALL, 5)

        self.m_staticText_empt = wx.StaticText(self.m_panel1, wx.ID_ANY, u' ', wx.DefaultPosition,
                                                  wx.Size(40, 38),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empt.Wrap(-1)

        self.m_staticText_empt.SetForegroundColour(self.fr_clr)
        self.m_staticText_empt.SetBackgroundColour(self.bg_clr)

        bSizer9.Add(self.m_staticText_empt, 0, wx.ALL, 5)
        """--------- end of line 5 -----------"""





        bSizer4.Add(bSizer9, 0, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        # self.m_staticText_fn0 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(38, 38),
        #                                      wx.ALIGN_LEFT)
        # self.m_staticText_fn0.Wrap(-1)
        #
        # self.m_staticText_fn0.SetForegroundColour(self.fr_clr)
        # self.m_staticText_fn0.SetBackgroundColour(self.bg_clr)
        #
        # bSizer10.Add(self.m_staticText_fn0, 0, wx.ALL, 5)

        self.m_staticText_ctrl = wx.StaticText(self.m_panel1, wx.ID_ANY, u"control", wx.DefaultPosition, wx.Size(70, 38),
                                               wx.ALIGN_LEFT)
        self.m_staticText_ctrl.Wrap(-1)

        self.m_staticText_ctrl.SetForegroundColour(self.fr_clr)
        self.m_staticText_ctrl.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_ctrl, 0, wx.ALL, 5)

        self.m_staticText_left_option = wx.StaticText(self.m_panel1, wx.ID_ANY, u"option", wx.DefaultPosition,
                                                      wx.Size(50, 38), 0)
        self.m_staticText_left_option.Wrap(-1)

        self.m_staticText_left_option.SetForegroundColour(self.fr_clr)
        self.m_staticText_left_option.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_left_option, 0, wx.ALL, 5)

        self.m_staticText_left_command = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2318", wx.DefaultPosition,
                                                       wx.Size(58, 38), 0)
        self.m_staticText_left_command.Wrap(-1)

        self.m_staticText_left_command.SetForegroundColour(self.fr_clr)
        self.m_staticText_left_command.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_left_command, 0, wx.ALL, 5)

        self.m_staticText_spacebar = wx.StaticText(self.m_panel1, wx.ID_ANY, u" ", wx.DefaultPosition,
                                                   wx.Size(278, 38), 0)
        self.m_staticText_spacebar.Wrap(-1)

        self.m_staticText_spacebar.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_spacebar, 0, wx.ALL, 5)

        self.m_staticText_right_command = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2318", wx.DefaultPosition,
                                                        wx.Size(60, 38), 0)
        self.m_staticText_right_command.Wrap(-1)

        self.m_staticText_right_command.SetForegroundColour(self.fr_clr)
        self.m_staticText_right_command.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_right_command, 0, wx.ALL, 5)

        self.m_staticText_right_option = wx.StaticText(self.m_panel1, wx.ID_ANY, u"option", wx.DefaultPosition,
                                                       wx.Size(48, 38), 0)
        self.m_staticText_right_option.Wrap(-1)

        self.m_staticText_right_option.SetForegroundColour(self.fr_clr)
        self.m_staticText_right_option.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_right_option, 0, wx.ALL, 5)

        self.m_staticText_right_control = wx.StaticText(self.m_panel1, wx.ID_ANY, u"control", wx.DefaultPosition,
                                                       wx.Size(68, 38), 0)
        self.m_staticText_right_control.Wrap(-1)

        self.m_staticText_right_control.SetForegroundColour(self.fr_clr)
        self.m_staticText_right_control.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_right_control, 0, wx.ALL, 5)

        self.m_staticText_empty6 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                  wx.Size(10, 20),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty6.Wrap(-1)
        bSizer10.Add(self.m_staticText_empty6, 0, wx.ALL, 5)



        self.m_staticText_let_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2190", wx.DefaultPosition,
                                                    wx.Size(40, 38),
                                                    wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_let_arrow.Wrap(-1)

        self.m_staticText_let_arrow.SetForegroundColour(self.fr_clr)
        self.m_staticText_let_arrow.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_let_arrow, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        # self.m_staticText_top_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2191", wx.DefaultPosition,
        #                                             wx.Size(38, 38),
        #                                             wx.ALIGN_CENTER_HORIZONTAL)
        # self.m_staticText_top_arrow.Wrap(-1)
        #
        # self.m_staticText_top_arrow.SetForegroundColour(self.fr_clr)
        # self.m_staticText_top_arrow.SetBackgroundColour(self.bg_clr)
        #
        # bSizer11.Add(self.m_staticText_top_arrow, 0, wx.ALL, 1)

        self.m_staticText_down_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2193", wx.DefaultPosition,
                                                     wx.Size(40, 38),
                                                     wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_down_arrow.Wrap(-1)

        self.m_staticText_down_arrow.SetForegroundColour(self.fr_clr)
        self.m_staticText_down_arrow.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_down_arrow, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        bSizer10.Add(bSizer11, 0, wx.EXPAND, 5)

        self.m_staticText_right_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2192", wx.DefaultPosition,
                                                      wx.Size(40, 38),
                                                      wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_right_arrow.Wrap(-1)

        self.m_staticText_right_arrow.SetForegroundColour(self.fr_clr)
        self.m_staticText_right_arrow.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_right_arrow, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.m_staticText_empty62 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'', wx.DefaultPosition,
                                                  wx.Size(10, 20),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_empty62.Wrap(-1)
        bSizer10.Add(self.m_staticText_empty62, 0, wx.ALL, 5)

        self.m_staticText_0_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'0', wx.DefaultPosition,
                                                 wx.Size(90, 38),
                                                 wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_0_2.Wrap(-1)

        self.m_staticText_0_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_0_2.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_0_2, 0, wx.ALL, 5)

        self.m_staticText_dot_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'.', wx.DefaultPosition,
                                                wx.Size(40, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_dot_2.Wrap(-1)

        self.m_staticText_dot_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_dot_2.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_dot_2, 0, wx.ALL, 5)

        self.m_staticText_enter_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u'enter', wx.DefaultPosition,
                                                  wx.Size(40, 38),
                                                  wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_enter_2.Wrap(-1)

        self.m_staticText_enter_2.SetForegroundColour(self.fr_clr)
        self.m_staticText_enter_2.SetBackgroundColour(self.bg_clr)

        bSizer10.Add(self.m_staticText_enter_2, 0, wx.ALL, 5)
        bSizer4.Add(bSizer10, 0, wx.EXPAND, 5)



        bSizer2.Add(bSizer4, 0, wx.EXPAND, 10)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticline12 = wx.StaticLine(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        self.m_staticline12.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizer5.Add(self.m_staticline12, 0, wx.EXPAND | wx.ALL, 0)



        bSizer2.Add(bSizer5, 0, wx.EXPAND, 10)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_panel1.Bind(wx.EVT_KEY_DOWN, self.onTextKeyEvent)
        self.m_button_reset.Bind(wx.EVT_BUTTON, self.onReset)
        self.Show()

    def __del__(self):
        pass

    def getWidgets(parent, event):
        """
        Return a list of all the child widgets
        """
        items = [parent]
        for item in parent.GetChildren():
            items.append(item)
            if hasattr(item, "GetChildren"):
                for child in item.GetChildren():
                    items.append(child)
        print(items)
        return items

    def onReset(self, event):
        widgets = self.getWidgets(None)
        # print(widgets)
        panel = widgets[0]
        for widget in widgets:
            # print(widget)
            if isinstance(widget, wx.StaticText):
                print(widget)

                print(widget.GetLabel())
                if widget.GetLabel() == wx.EmptyString:
                    print("Empty StaticText item")
                else:

                    widget.SetBackgroundColour(self.bg_clr)
                    widget.SetForegroundColour(self.fr_clr)
        self.Refresh()



    grn = wx.Colour(114, 166, 113)
    blu = wx.Colour(34, 174, 240)
    org = wx.Colour(237, 183, 33)

    def onkeycombo(self, event):
        # print "You pressed CTRL+Q!"
        self.Destroy()

    def ch_color(self, wgt, color):
        if wgt.GetBackgroundColour() != color:
            wgt.SetBackgroundColour(color)
        else:
            wgt.SetForegroundColour(self.bg_clr)

    def onTextKeyEvent(self, event):
        print(event.GetKeyCode())
        keycode = event.GetKeyCode()
        self.m_panel1.SetFocus()

        if keycode == 127:
            self.ch_color(self.m_staticText_del2, self.blu)
            print("keypressed = delete")
        if keycode == 312:
            print("keypressed = end")
            self.ch_color(self.m_staticText_end, self.blu)
        if keycode == 367:
            print("keypressed = pg dwn")
            self.ch_color(self.m_staticText_pgdn, self.blu)
        if keycode == 313:
            print("keypressed = home")
            self.ch_color(self.m_staticText_home, self.blu)
        if keycode == 366:
            print("keypressed = pg up")
            self.ch_color(self.m_staticText_pgup, self.blu)
        if keycode == 352:
            print("keypressed = f13")
            self.ch_color(self.m_staticText_F13, self.org)
        if keycode == 353:
            print("keypressed = f14")
            self.ch_color(self.m_staticText_F14, self.org)
        if keycode == 354:
            print("keypressed = f15")
            self.ch_color(self.m_staticText_F15, self.org)
        if keycode == 355:
            print("keypressed = f16")
            self.ch_color(self.m_staticText_F16, self.org)
        if keycode == 356:
            print("keypressed = f17")
            self.ch_color(self.m_staticText_F17, self.org)
        if keycode == 357:
            print("keypressed = f18")
            self.ch_color(self.m_staticText_F18, self.org)
        if keycode == 358:
            print("keypressed = f19")
            self.ch_color(self.m_staticText_F19, self.org)
        if keycode == 305:
            print("keypressed = clear")
            self.ch_color(self.m_staticText_clear, self.blu)
        if keycode == 61:
            print("keypressed = =")
            self.ch_color(self.m_staticText_equal2, self.blu)
        if keycode == 392:
            print("keypressed = /")
            self.ch_color(self.m_staticText_fslah, self.blu)
        if keycode == 387:
            print("keypressed = *")
            self.ch_color(self.m_staticText_esteric, self.blu)
        if keycode == 331:
            print("keypressed = 7")
            self.ch_color(self.m_staticText_7_2, self.grn)
        if keycode == 332:
            print("keypressed = 8")
            self.ch_color(self.m_staticText_8_2, self.grn)
        if keycode == 333:
            print("keypressed = 9")
            self.ch_color(self.m_staticText_9_2, self.grn)
        if keycode == 390:
            print("keypressed = -")
            self.ch_color(self.m_staticText_minus_2, self.blu)
        if keycode == 328:
            print("keypressed = 4")
            self.ch_color(self.m_staticText_4_2, self.grn)
        if keycode == 329:
            print("keypressed = 5")
            self.ch_color(self.m_staticText_5_2, self.grn)
        if keycode == 330:
            print("keypressed = 6")
            self.ch_color(self.m_staticText_6_2, self.grn)
        if keycode == 388:
            print("keypressed = +")
            self.ch_color(self.m_staticText_plus_2, self.blu)
        if keycode == 325:
            print("keypressed = 1")
            self.ch_color(self.m_staticText_1_2, self.grn)
        if keycode == 326:
            print("keypressed = 2")
            self.ch_color(self.m_staticText_2_2, self.grn)
        if keycode == 327:
            print("keypressed = 3")
            self.ch_color(self.m_staticText_3_2, self.grn)
        if keycode == 324:
            print("keypressed = 0")
            self.ch_color(self.m_staticText_0_2, self.grn)
        if keycode == 391:
            print("keypressed = .")
            self.ch_color(self.m_staticText_dot_2, self.grn)
        if keycode == 370:
            print("keypressed = ENT")
            self.ch_color(self.m_staticText_enter_2, self.blu)
            self.ch_color(self.m_staticText_empt, self.blu)

        if keycode == 396:
            self.ch_color(self.m_staticText_right_control, self.grn)
            self.ch_color(self.m_staticText_ctrl, self.grn)
        if keycode == 307:
            self.ch_color(self.m_staticText_left_option, self.grn)
            self.ch_color(self.m_staticText_right_option, self.grn)
        if keycode == 308:
            self.ch_color(self.m_staticText_left_command, self.grn)
            self.ch_color(self.m_staticText_right_command, self.grn)
        if keycode == 314:
            self.ch_color(self.m_staticText_let_arrow, self.grn)
        if keycode == 13:
            self.ch_color(self.m_staticText_enter, self.grn)
        if keycode == 311:
            self.ch_color(self.m_staticText_caps, self.grn)
        if keycode == 306:
            self.ch_color(self.m_staticText_left_shift, self.grn)
            self.ch_color(self.m_staticText_right_shift, self.grn)
        if keycode == 350:
            self.ch_color(self.m_staticText_f11, self.org)
        if keycode == 27:
            self.ch_color(self.m_staticText_esc, self.org)
        if keycode == 340:
            self.ch_color(self.m_staticText_f1, self.org)
        if keycode == 341:
            self.ch_color(self.m_staticText_f2, self.org)
        if keycode == 342:
            self.ch_color(self.m_staticText_f3, self.org)
        if keycode == 343:
            self.ch_color(self.m_staticText_f4, self.org)
        if keycode == 344:
            self.ch_color(self.m_staticText_f5, self.org)
        if keycode == 345:
            self.ch_color(self.m_staticText_f6, self.org)
        if keycode == 346:
            self.ch_color(self.m_staticText_f7, self.org)
        if keycode == 347:
            self.ch_color(self.m_staticText_f8, self.org)
        if keycode == 348:
            self.ch_color(self.m_staticText_f9, self.org)
        if keycode == 349:
            self.ch_color(self.m_staticText_f10, self.org)
        if keycode == 351:
            self.ch_color(self.m_staticText_f12, self.org)
        if keycode == 96:
            self.ch_color(self.m_staticText_tilde, self.blu)
        if keycode == 49:
            self.ch_color(self.m_staticText_1, self.blu)
        if keycode == 50:
            self.ch_color(self.m_staticText_2, self.blu)
        if keycode == 51:
            self.ch_color(self.m_staticText_3, self.blu)
        if keycode == 52:
            self.ch_color(self.m_staticText_4, self.blu)
        if keycode == 53:
            self.ch_color(self.m_staticText_5, self.blu)
        if keycode == 54:
            self.ch_color(self.m_staticText_6, self.blu)
        if keycode == 55:
            self.ch_color(self.m_staticText_7, self.blu)
        if keycode == 56:
            self.ch_color(self.m_staticText_8, self.blu)
        if keycode == 57:
            self.ch_color(self.m_staticText_9, self.blu)
        if keycode == 48:
            self.ch_color(self.m_staticText_0, self.blu)
        if keycode == 45:
            self.ch_color(self.m_staticText_minus, self.blu)
        if keycode == 61:
            self.ch_color(self.m_staticText_plus, self.blu)
        if keycode == 8:
            self.ch_color(self.m_staticText_delete, self.blu)
        if keycode == 87:
            self.ch_color(self.m_staticText_w, self.blu)
        if keycode == 69:
            self.ch_color(self.m_staticText_e, self.blu)
        if keycode == 82:
            self.ch_color(self.m_staticText_r, self.blu)
        if keycode == 84:
            self.ch_color(self.m_staticText_t, self.blu)
        if keycode == 89:
            self.ch_color(self.m_staticText_y, self.blu)
        if keycode == 85:
            self.ch_color(self.m_staticText_u, self.blu)
        if keycode == 73:
            self.ch_color(self.m_staticText_i, self.blu)
        if keycode == 79:
            self.ch_color(self.m_staticText_o, self.blu)
        if keycode == 80:
            self.ch_color(self.m_staticText_p, self.blu)
        if keycode == 91:
            self.ch_color(self.m_staticText_curly_left, self.blu)
        if keycode == 93:
            self.ch_color(self.m_staticText_curly_right, self.blu)
        if keycode == 92:
            self.ch_color(self.m_staticText_pipe, self.grn)
        if keycode == 65:
            self.ch_color(self.m_staticText_a, self.blu)
        if keycode == 83:
            self.ch_color(self.m_staticText_s, self.blu)
        if keycode == 68:
            self.ch_color(self.m_staticText_d, self.blu)
        if keycode == 70:
            self.ch_color(self.m_staticText_f, self.blu)
        if keycode == 71:
            self.ch_color(self.m_staticText_g, self.blu)
        if keycode == 72:
            self.ch_color(self.m_staticText_h, self.blu)
        if keycode == 74:
            self.ch_color(self.m_staticText_j, self.blu)
        if keycode == 75:
            self.ch_color(self.m_staticText_k, self.blu)
        if keycode == 76:
            self.ch_color(self.m_staticText_l, self.blu)
        if keycode == 59:
            self.ch_color(self.m_staticText_colon, self.blu)
        if keycode == 39:
            self.ch_color(self.m_staticText_quote, self.blu)
        if keycode == 90:
            self.ch_color(self.m_staticText_z, self.blu)
        if keycode == 88:
            self.ch_color(self.m_staticText_x, self.blu)
        if keycode == 67:
            self.ch_color(self.m_staticText_c, self.blu)
        if keycode == 86:
            self.ch_color(self.m_staticText_v, self.blu)
        if keycode == 66:
            self.ch_color(self.m_staticText_b, self.blu)
        if keycode == 78:
            self.ch_color(self.m_staticText_n, self.blu)
        if keycode == 77:
            self.ch_color(self.m_staticText_m, self.blu)
        if keycode == 44:
            self.ch_color(self.m_staticText_less, self.blu)
        if keycode == 46:
            self.ch_color(self.m_staticText_more, self.blu)
        if keycode == 47:
            self.ch_color(self.m_staticText_question, self.blu)
        if keycode == 315:
            self.ch_color(self.m_staticText_top_arrow, self.grn)
        if keycode == 317:
            self.ch_color(self.m_staticText_down_arrow, self.grn)
        if keycode == 316:
            self.ch_color(self.m_staticText_right_arrow, self.grn)
        if keycode == 0:
            self.ch_color(self.m_staticText_fn, self.blu)
        if keycode == 9:
            self.ch_color(self.m_staticText_tab, self.grn)
        if keycode == 32:
            self.ch_color(self.m_staticText_spacebar, self.grn)
        if keycode == 81:
            self.ch_color(self.m_staticText_q, self.blu)
        event.Skip()


# Run the program
if __name__ == "__main__":
    app = wx.App()
    frame = kb_test(None)
    app.MainLoop()