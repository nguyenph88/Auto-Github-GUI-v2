# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Auto Github 1.0", pos = wx.DefaultPosition, size = wx.Size( 286,252 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Link To Profile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.fieldProfile = wx.TextCtrl( self, wx.ID_ANY, u"http://www.github.com/nguyenph88/", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer1.Add( self.fieldProfile, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"List of Repo(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.fieldRepos = wx.TextCtrl( self, wx.ID_ANY, u"Autogithub, AutoDropbox", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer1.Add( self.fieldRepos, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.fieldQuantity = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer1.Add( self.fieldQuantity, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.boxFollow = wx.CheckBox( self, wx.ID_ANY, u"Follow", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.boxFollow, 0, wx.ALL, 5 )
		
		self.boxStar = wx.CheckBox( self, wx.ID_ANY, u"Star", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.boxStar, 0, wx.ALL, 5 )
		
		self.boxFork = wx.CheckBox( self, wx.ID_ANY, u"Fork", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.boxFork, 0, wx.ALL, 5 )
		
		self.buttonStart = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.buttonStart, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"* Features:\n- Multiple Repos Support\n- Multithread supported", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonStart.Bind( wx.EVT_BUTTON, self.buttonStartEvent )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonStartEvent( self, event ):
		event.Skip()
	

