# -*- coding: utf-8 -*-
# Python GUI code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/

import wx

class kb_test(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Keyboard Test Utility", pos=wx.DefaultPosition,
                          size=wx.Size(710, 370), style=wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

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

        self.m_staticText_empty1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"                                                                   ", wx.DefaultPosition, wx.DefaultSize,
                                                )
        self.m_staticText = wx.StaticText(self.m_panel1, wx.ID_ANY, u"MacBook Pro / Air", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.m_staticText.SetFont(
            wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))
        self.m_staticText_empty2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize,
                                                )
        bSizer3.Add(self.m_staticText_empty1, 0, wx.ALL, 5)
        bSizer3.Add(self.m_staticText, 0, wx.ALL, 5)
        # bSizer3.Add(self.m_staticText_empty2, 0, wx.ALL, 5)

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

        self.m_staticText_esc.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_esc.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_esc, 0, wx.ALL, 5)

        self.m_staticText_f1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f1.Wrap(-1)

        self.m_staticText_f1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f1.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f1, 0, wx.ALL, 5)

        self.m_staticText_f2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F2", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f2.Wrap(-1)

        self.m_staticText_f2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f2.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f2, 0, wx.ALL, 5)

        self.m_staticText_f3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F3", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f3.Wrap(-1)

        self.m_staticText_f3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f3.SetBackgroundColour(wx.Colour(76, 75, 77))

        bSizer5.Add(self.m_staticText_f3, 0, wx.ALL, 5)

        self.m_staticText_f4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F4", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f4.Wrap(-1)

        self.m_staticText_f4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f4.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f4, 0, wx.ALL, 5)

        self.m_staticText_f5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F5", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f5.Wrap(-1)

        self.m_staticText_f5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f5.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f5, 0, wx.ALL, 5)

        self.m_staticText_f6 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F6", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f6.Wrap(-1)

        self.m_staticText_f6.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f6.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f6, 0, wx.ALL, 5)

        self.m_staticText_f7 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F7", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f7.Wrap(-1)

        self.m_staticText_f7.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f7.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f7, 0, wx.ALL, 5)

        self.m_staticText_f8 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F8", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f8.Wrap(-1)

        self.m_staticText_f8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f8.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f8, 0, wx.ALL, 5)

        self.m_staticText_f9 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F9", wx.DefaultPosition, wx.Size(40, 20),
                                             wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f9.Wrap(-1)

        self.m_staticText_f9.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f9.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f9, 0, wx.ALL, 5)

        self.m_staticText_f10 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F10", wx.DefaultPosition, wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f10.Wrap(-1)

        self.m_staticText_f10.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f10.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f10, 0, wx.ALL, 5)

        self.m_staticText_f11 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F11", wx.DefaultPosition, wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f11.Wrap(-1)

        self.m_staticText_f11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f11.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f11, 0, wx.ALL, 5)

        self.m_staticText_f12 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F12", wx.DefaultPosition, wx.Size(40, 20),
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f12.Wrap(-1)

        self.m_staticText_f12.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f12.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_f12, 0, wx.ALL, 5)

        self.m_staticText_eject = wx.StaticText(self.m_panel1, wx.ID_ANY, u'\u23CF', wx.DefaultPosition, wx.Size(40, 20),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_eject.Wrap(-1)

        self.m_staticText_eject.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_eject.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer5.Add(self.m_staticText_eject, 0, wx.ALL, 5)

        bSizer4.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_tilde = wx.StaticText(self.m_panel1, wx.ID_ANY, u"~\n`", wx.DefaultPosition, wx.Size(38, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_tilde.Wrap(-1)

        self.m_staticText_tilde.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_tilde.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_tilde, 0, wx.ALL, 5)

        self.m_staticText_1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"!\n1", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_1.Wrap(-1)

        self.m_staticText_1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_1.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_1, 0, wx.ALL, 5)

        self.m_staticText_2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"@\n2", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_2.Wrap(-1)

        self.m_staticText_2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_2.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_2, 0, wx.ALL, 5)

        self.m_staticText_3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"#\n3", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_3.Wrap(-1)

        self.m_staticText_3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_3.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_3, 0, wx.ALL, 5)

        self.m_staticText_4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"$\n4", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_4.Wrap(-1)

        self.m_staticText_4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_4.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_4, 0, wx.ALL, 5)

        self.m_staticText_5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"%\n5", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_5.Wrap(-1)

        self.m_staticText_5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_5.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_5, 0, wx.ALL, 5)

        self.m_staticText_6 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"^\n6", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_6.Wrap(-1)

        self.m_staticText_6.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_6.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_6, 0, wx.ALL, 5)

        self.m_staticText_7 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"&&\n7", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_7.Wrap(-1)

        self.m_staticText_7.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_7.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_7, 0, wx.ALL, 5)

        self.m_staticText_8 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"*\n8", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_8.Wrap(-1)

        self.m_staticText_8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_8.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_8, 0, wx.ALL, 5)

        self.m_staticText_9 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"(\n9", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_9.Wrap(-1)

        self.m_staticText_9.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_9.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_9, 0, wx.ALL, 5)

        self.m_staticText_0 = wx.StaticText(self.m_panel1, wx.ID_ANY, u")\n0", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_0.Wrap(-1)

        self.m_staticText_0.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_0.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_0, 0, wx.ALL, 5)

        self.m_staticText_minus = wx.StaticText(self.m_panel1, wx.ID_ANY, u"_\n-", wx.DefaultPosition, wx.Size(38, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_minus.Wrap(-1)

        self.m_staticText_minus.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_minus.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_minus, 0, wx.ALL, 5)

        self.m_staticText_plus = wx.StaticText(self.m_panel1, wx.ID_ANY, u"+\n=", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_plus.Wrap(-1)

        self.m_staticText_plus.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_plus.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_plus, 0, wx.ALL, 5)

        self.m_staticText_delete = wx.StaticText(self.m_panel1, wx.ID_ANY, u"delete", wx.DefaultPosition,
                                                 wx.Size(67, 38),
                                                 wx.ALIGN_RIGHT)
        self.m_staticText_delete.Wrap(-1)

        self.m_staticText_delete.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_delete.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer6.Add(self.m_staticText_delete, 0, wx.ALL, 5)

        bSizer4.Add(bSizer6, 0, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_tab = wx.StaticText(self.m_panel1, wx.ID_ANY, u"tab", wx.DefaultPosition, wx.Size(67, 38), 0)
        self.m_staticText_tab.Wrap(-1)

        self.m_staticText_tab.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_tab.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_tab, 0, wx.ALL, 5)

        self.m_staticText_q = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Q", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_q.Wrap(-1)

        self.m_staticText_q.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_q.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_q, 0, wx.ALL, 5)

        self.m_staticText_w = wx.StaticText(self.m_panel1, wx.ID_ANY, u"W", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_w.Wrap(-1)

        self.m_staticText_w.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_w.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_w, 0, wx.ALL, 5)

        self.m_staticText_e = wx.StaticText(self.m_panel1, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_e.Wrap(-1)

        self.m_staticText_e.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_e.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_e, 0, wx.ALL, 5)

        self.m_staticText_r = wx.StaticText(self.m_panel1, wx.ID_ANY, u"R", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_r.Wrap(-1)

        self.m_staticText_r.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_r.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_r, 0, wx.ALL, 5)

        self.m_staticText_t = wx.StaticText(self.m_panel1, wx.ID_ANY, u"T", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_t.Wrap(-1)

        self.m_staticText_t.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_t.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_t, 0, wx.ALL, 5)

        self.m_staticText_y = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_y.Wrap(-1)

        self.m_staticText_y.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_y.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_y, 0, wx.ALL, 5)

        self.m_staticText_u = wx.StaticText(self.m_panel1, wx.ID_ANY, u"U", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_u.Wrap(-1)

        self.m_staticText_u.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_u.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_u, 0, wx.ALL, 5)

        self.m_staticText_i = wx.StaticText(self.m_panel1, wx.ID_ANY, u"I", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_i.Wrap(-1)

        self.m_staticText_i.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_i.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_i, 0, wx.ALL, 5)

        self.m_staticText_o = wx.StaticText(self.m_panel1, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_o.Wrap(-1)

        self.m_staticText_o.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_o.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_o, 0, wx.ALL, 5)

        self.m_staticText_p = wx.StaticText(self.m_panel1, wx.ID_ANY, u"P", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_p.Wrap(-1)

        self.m_staticText_p.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_p.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_p, 0, wx.ALL, 5)

        self.m_staticText_curly_left = wx.StaticText(self.m_panel1, wx.ID_ANY, u"{\n[", wx.DefaultPosition,
                                                     wx.Size(38, 38),
                                                     wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_curly_left.Wrap(-1)

        self.m_staticText_curly_left.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_curly_left.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_curly_left, 0, wx.ALL, 5)

        self.m_staticText_curly_right = wx.StaticText(self.m_panel1, wx.ID_ANY, u"}\n]", wx.DefaultPosition,
                                                      wx.Size(38, 38),
                                                      wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_curly_right.Wrap(-1)

        self.m_staticText_curly_right.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_curly_right.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_curly_right, 0, wx.ALL, 5)

        self.m_staticText_pipe = wx.StaticText(self.m_panel1, wx.ID_ANY, u"|\n\\", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_pipe.Wrap(-1)

        self.m_staticText_pipe.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_pipe.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer7.Add(self.m_staticText_pipe, 0, wx.ALL, 5)

        bSizer4.Add(bSizer7, 0, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_caps = wx.StaticText(self.m_panel1, wx.ID_ANY, u"caps lock", wx.DefaultPosition,
                                               wx.Size(77, 38), wx.ALIGN_LEFT)
        self.m_staticText_caps.Wrap(-1)

        self.m_staticText_caps.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_caps.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_caps, 0, wx.ALL, 5)

        self.m_staticText_a = wx.StaticText(self.m_panel1, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_a.Wrap(-1)

        self.m_staticText_a.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_a.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_a, 0, wx.ALL, 5)

        self.m_staticText_s = wx.StaticText(self.m_panel1, wx.ID_ANY, u"S", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_s.Wrap(-1)

        self.m_staticText_s.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_s.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_s, 0, wx.ALL, 5)

        self.m_staticText_d = wx.StaticText(self.m_panel1, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_d.Wrap(-1)

        self.m_staticText_d.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_d.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_d, 0, wx.ALL, 5)

        self.m_staticText_f = wx.StaticText(self.m_panel1, wx.ID_ANY, u"F", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_f.Wrap(-1)

        self.m_staticText_f.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_f.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_f, 0, wx.ALL, 5)

        self.m_staticText_g = wx.StaticText(self.m_panel1, wx.ID_ANY, u"G", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_g.Wrap(-1)

        self.m_staticText_g.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_g.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_g, 0, wx.ALL, 5)

        self.m_staticText_h = wx.StaticText(self.m_panel1, wx.ID_ANY, u"H", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_h.Wrap(-1)

        self.m_staticText_h.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_h.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_h, 0, wx.ALL, 5)

        self.m_staticText_j = wx.StaticText(self.m_panel1, wx.ID_ANY, u"J", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_j.Wrap(-1)

        self.m_staticText_j.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_j.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_j, 0, wx.ALL, 5)

        self.m_staticText_k = wx.StaticText(self.m_panel1, wx.ID_ANY, u"K", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_k.Wrap(-1)

        self.m_staticText_k.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_k.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_k, 0, wx.ALL, 5)

        self.m_staticText_l = wx.StaticText(self.m_panel1, wx.ID_ANY, u"L", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_l.Wrap(-1)

        self.m_staticText_l.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_l.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_l, 0, wx.ALL, 5)

        self.m_staticText_colon = wx.StaticText(self.m_panel1, wx.ID_ANY, u":\n;", wx.DefaultPosition, wx.Size(38, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_colon.Wrap(-1)

        self.m_staticText_colon.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_colon.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_colon, 0, wx.ALL, 5)

        self.m_staticText_quote = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\"\n'", wx.DefaultPosition, wx.Size(38, 38),
                                                wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_quote.Wrap(-1)

        self.m_staticText_quote.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_quote.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_quote, 0, wx.ALL, 5)

        self.m_staticText_enter = wx.StaticText(self.m_panel1, wx.ID_ANY, u"enter\nreturn", wx.DefaultPosition,
                                                wx.Size(77, 38), wx.ALIGN_RIGHT)
        self.m_staticText_enter.Wrap(-1)

        self.m_staticText_enter.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_enter.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer8.Add(self.m_staticText_enter, 0, wx.ALL, 5)

        bSizer4.Add(bSizer8, 0, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_left_shift = wx.StaticText(self.m_panel1, wx.ID_ANY, u"shift", wx.DefaultPosition,
                                                     wx.Size(101, 38),
                                                     0)
        self.m_staticText_left_shift.Wrap(-1)

        self.m_staticText_left_shift.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_left_shift.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_left_shift, 0, wx.ALL, 5)

        self.m_staticText_z = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Z", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_z.Wrap(-1)

        self.m_staticText_z.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_z.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_z, 0, wx.ALL, 5)

        self.m_staticText_x = wx.StaticText(self.m_panel1, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_x.Wrap(-1)

        self.m_staticText_x.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_x.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_x, 0, wx.ALL, 5)

        self.m_staticText_c = wx.StaticText(self.m_panel1, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_c.Wrap(-1)

        self.m_staticText_c.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_c.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_c, 0, wx.ALL, 5)

        self.m_staticText_v = wx.StaticText(self.m_panel1, wx.ID_ANY, u"V", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_v.Wrap(-1)

        self.m_staticText_v.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_v.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_v, 0, wx.ALL, 5)

        self.m_staticText_b = wx.StaticText(self.m_panel1, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_b.Wrap(-1)

        self.m_staticText_b.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_b.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_b, 0, wx.ALL, 5)

        self.m_staticText_n = wx.StaticText(self.m_panel1, wx.ID_ANY, u"N", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_n.Wrap(-1)

        self.m_staticText_n.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_n.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_n, 0, wx.ALL, 5)

        self.m_staticText_m = wx.StaticText(self.m_panel1, wx.ID_ANY, u"M", wx.DefaultPosition, wx.Size(38, 38),
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_m.Wrap(-1)

        self.m_staticText_m.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_m.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_m, 0, wx.ALL, 5)

        self.m_staticText_less = wx.StaticText(self.m_panel1, wx.ID_ANY, u"<\n,", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_less.Wrap(-1)

        self.m_staticText_less.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_less.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_less, 0, wx.ALL, 5)

        self.m_staticText_more = wx.StaticText(self.m_panel1, wx.ID_ANY, u">\n.", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_more.Wrap(-1)

        self.m_staticText_more.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_more.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_more, 0, wx.ALL, 5)

        self.m_staticText_question = wx.StaticText(self.m_panel1, wx.ID_ANY, u"?\n/", wx.DefaultPosition,
                                                   wx.Size(38, 38),
                                                   wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_question.Wrap(-1)

        self.m_staticText_question.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_question.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_question, 0, wx.ALL, 5)

        self.m_staticText_right_shift = wx.StaticText(self.m_panel1, wx.ID_ANY, u"shift", wx.DefaultPosition,
                                                      wx.Size(101, 38),
                                                      wx.ALIGN_RIGHT)
        self.m_staticText_right_shift.Wrap(-1)

        self.m_staticText_right_shift.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_right_shift.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer9.Add(self.m_staticText_right_shift, 0, wx.ALL, 5)

        bSizer4.Add(bSizer9, 0, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_fn = wx.StaticText(self.m_panel1, wx.ID_ANY, u"fn", wx.DefaultPosition, wx.Size(38, 38),
                                             wx.ALIGN_LEFT)
        self.m_staticText_fn.Wrap(-1)

        self.m_staticText_fn.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_fn.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_fn, 0, wx.ALL, 5)

        self.m_staticText_ctrl = wx.StaticText(self.m_panel1, wx.ID_ANY, u"ctrl", wx.DefaultPosition, wx.Size(38, 38),
                                               wx.ALIGN_LEFT)
        self.m_staticText_ctrl.Wrap(-1)

        self.m_staticText_ctrl.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_ctrl.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_ctrl, 0, wx.ALL, 5)

        self.m_staticText_left_option = wx.StaticText(self.m_panel1, wx.ID_ANY, u"opt", wx.DefaultPosition,
                                                      wx.Size(38, 38), 0)
        self.m_staticText_left_option.Wrap(-1)

        self.m_staticText_left_option.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_left_option.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_left_option, 0, wx.ALL, 5)

        self.m_staticText_left_command = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2318", wx.DefaultPosition,
                                                       wx.Size(38, 38), 0)
        self.m_staticText_left_command.Wrap(-1)

        self.m_staticText_left_command.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_left_command.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_left_command, 0, wx.ALL, 5)

        self.m_staticText_spacebar = wx.StaticText(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                   wx.Size(268, 38), 0)
        self.m_staticText_spacebar.Wrap(-1)

        self.m_staticText_spacebar.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_spacebar, 0, wx.ALL, 5)

        self.m_staticText_right_command = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2318", wx.DefaultPosition,
                                                        wx.Size(38, 38), 0)
        self.m_staticText_right_command.Wrap(-1)

        self.m_staticText_right_command.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_right_command.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_right_command, 0, wx.ALL, 5)

        self.m_staticText_right_option = wx.StaticText(self.m_panel1, wx.ID_ANY, u"opt", wx.DefaultPosition,
                                                       wx.Size(38, 38), 0)
        self.m_staticText_right_option.Wrap(-1)

        self.m_staticText_right_option.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_right_option.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_right_option, 0, wx.ALL, 5)

        self.m_staticText_let_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2190", wx.DefaultPosition, wx.Size(38, 20),
                                                    wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_let_arrow.Wrap(-1)

        self.m_staticText_let_arrow.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_let_arrow.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_let_arrow, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText_top_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2191", wx.DefaultPosition, wx.Size(38, 20),
                                                    wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_top_arrow.Wrap(-1)

        self.m_staticText_top_arrow.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_top_arrow.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer11.Add(self.m_staticText_top_arrow, 0, wx.ALL, 1)

        self.m_staticText_down_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2193", wx.DefaultPosition,
                                                     wx.Size(38, 20),
                                                     wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_down_arrow.Wrap(-1)

        self.m_staticText_down_arrow.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_down_arrow.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer11.Add(self.m_staticText_down_arrow, 0, wx.ALL, 1)

        bSizer10.Add(bSizer11, 0, wx.EXPAND, 5)

        self.m_staticText_right_arrow = wx.StaticText(self.m_panel1, wx.ID_ANY, u"\u2192", wx.DefaultPosition,
                                                      wx.Size(38, 20),
                                                      wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_right_arrow.Wrap(-1)

        self.m_staticText_right_arrow.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_staticText_right_arrow.SetBackgroundColour(wx.Colour(76, 76, 76))

        bSizer10.Add(self.m_staticText_right_arrow, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        bSizer4.Add(bSizer10, 0, wx.EXPAND, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 10)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_panel1.Bind(wx.EVT_KEY_DOWN, self.onTextKeyEvent)
        self.Show()

    def __del__(self):
        pass

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
            wgt.SetForegroundColour(wx.Colour(76, 76, 76))

    def onTextKeyEvent(self, event):
        print(event.GetKeyCode())
        keycode = event.GetKeyCode()
        self.m_panel1.SetFocus()
        if keycode == 396:
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
            self.ch_color(self.m_staticText_fn, self.grn)
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
