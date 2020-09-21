#!/usr/bin/env python3

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk,Gdk
from time import strftime
import alsaaudio
import subprocess
import Xlib
from libraries import wifi
from Xlib.display import Display
from Xlib import X

class TimeWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self,type=Gtk.WindowType.TOPLEVEL)
		self.set_type_hint(Gdk.WindowTypeHint.POPUP_MENU)
		self.label = Gtk.Label()
		self.label2 = Gtk.Label()
		s = Gdk.Screen.get_default()
		self.resize(220,s.get_height()-80)
		self.move(s.get_width()-220,40)
		self.vbox = Gtk.VBox()
		self.vbox2 = Gtk.VBox()
		self.vbox.set_spacing(10)
		self.vbox2.set_spacing(10)
		
		self.back_button = Gtk.Button(label="Çık")
		self.activity_box = Gtk.VBox(spacing=5)
		self.activity_label = Gtk.Label(label="Etkinlikler:")
		self.activity_box.pack_start(self.activity_label,False,False,0)
		self.add_activity = Gtk.Button(label="Etkinlik Ekle")

		self.calendar = Gtk.Calendar()
		
		self.save_button = Gtk.Button(label="Kaydet")
		self.close_button = Gtk.Button(label="İptal")
		self.hbox1 = Gtk.HBox()
		self.hbox1.pack_start(self.save_button,False,False,0)
		self.hbox1.pack_end(self.close_button,False,False,0)
		self.calendar2 = Gtk.Calendar()
		
		self.entry1 = Gtk.Entry()
		self.entry1.set_text(strftime("%H"))
		self.entry1.set_editable(False)
		self.entry2 = Gtk.Entry()
		self.entry2.set_text(strftime("%M"))
		self.entry2.set_editable(False)
		self.entry3 = Gtk.Entry()
		self.entry3.set_text(strftime("%S"))
		self.entry3.set_editable(False)
		self.up_button_1 = Gtk.Button(label="+")
		self.up_button_2 = Gtk.Button(label="+")
		self.up_button_3 = Gtk.Button(label="+")
		self.up_button_1.connect("clicked",self.up1)
		self.up_button_2.connect("clicked",self.up2)
		self.up_button_3.connect("clicked",self.up3)
		self.down_button_1 = Gtk.Button(label="-")
		self.down_button_2 = Gtk.Button(label="-")
		self.down_button_3 = Gtk.Button(label="-")
		self.down_button_1.connect("clicked",self.down1)
		self.down_button_2.connect("clicked",self.down2)
		self.down_button_3.connect("clicked",self.down3)
		self.label3 = Gtk.Label(label="Saat:  ")
		self.label4 = Gtk.Label(label="Dakika:")
		self.label5 = Gtk.Label(label="Saniye:")
		self.hbox2 = Gtk.HBox()
		self.hbox3 = Gtk.HBox()
		self.hbox4 = Gtk.HBox()
		self.hbox2.pack_start(self.label3,False,False,0)
		self.hbox2.pack_end(self.up_button_1,False,False,0)
		self.hbox2.pack_end(self.down_button_1,False,False,0)
		self.hbox2.pack_end(self.entry1,False,True,0)
		self.hbox3.pack_start(self.label4,False,False,0)
		self.hbox3.pack_end(self.up_button_2,False,False,0)
		self.hbox3.pack_end(self.down_button_2,False,False,0)
		self.hbox3.pack_end(self.entry2,False,True,0)
		self.hbox4.pack_start(self.label5,False,False,0)
		self.hbox4.pack_end(self.up_button_3,False,False,0)
		self.hbox4.pack_end(self.down_button_3,False,False,0)		
		self.hbox4.pack_end(self.entry3,False,True,0)

		self.name_of_activity_label = Gtk.Label("Etkinliğin adı")
		self.name_of_activity_entry = Gtk.Entry()
		self.info_about_activity_label = Gtk.Label("Etkinlik hakkında kısa bilgi")
		self.info_about_activity_entry = Gtk.Entry()


		self.vbox2.pack_start(self.calendar2,False,False,0)
		self.vbox2.pack_start(self.hbox2,False,False,0)
		self.vbox2.pack_start(self.hbox3,False,False,0)
		self.vbox2.pack_start(self.hbox4,False,False,0)
		self.vbox2.pack_start(self.name_of_activity_label,False,False,0)
		self.vbox2.pack_start(self.name_of_activity_entry,False,False,0)
		self.vbox2.pack_start(self.info_about_activity_label,False,False,0)
		self.vbox2.pack_start(self.info_about_activity_entry,False,False,0)
		self.vbox2.pack_start(self.hbox1,False,False,0)
		self.vbox2.show_all()

		self.vbox.pack_start(self.back_button,False,True,0)
		self.vbox.pack_start(self.label,False,False,0)
		self.vbox.pack_start(self.label2,False,False,0)
		self.vbox.pack_start(self.calendar,False,False,0)
		self.vbox.pack_start(self.add_activity,False,False,0)
		self.vbox.pack_start(self.activity_box,False,False,0)
		self.add(self.vbox)
		self.show_all()
		
	def up1(self,widget):
		a = int(self.entry1.get_text())
		if a == 23:
			pass
		else:
			self.entry1.set_text(str(a+1))

	def up2(self,widget):
		a = int(self.entry2.get_text())
		if a == 59:
			pass
		else:
			self.entry2.set_text(str(a+1))
			
	def up3(self,widget):
		a = int(self.entry3.get_text())
		if a == 59:
			pass
		else:
			self.entry3.set_text(str(a+1))
			
	def down1(self,widget):
		a = int(self.entry1.get_text())
		if a == 0:
			pass
		else:
			self.entry1.set_text(str(a-1))	

	def down2(self,widget):
		a = int(self.entry2.get_text())
		if a == 0:
			pass
		else:
			self.entry2.set_text(str(a-1))	
			
	def down3(self,widget):
		a = int(self.entry3.get_text())
		if a == 0:
			pass
		else:
			self.entry3.set_text(str(a-1))	

class WifiWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self,type=Gtk.WindowType.TOPLEVEL)
		self.set_type_hint(Gdk.WindowTypeHint.POPUP_MENU)
		s = Gdk.Screen.get_default()
		self.resize(220,s.get_height()-80)
		self.move(s.get_width()-220,40)
		self.vbox = Gtk.VBox()
		self.vbox.set_spacing(10)
		self.hbox1 = Gtk.HBox()
		self.hbox1.set_spacing(10)
		self.back_button = Gtk.Button(label="Çık")
		self.wifi_box = Gtk.VBox(spacing=10)
		self.switch = Gtk.Switch()
		self.switch.set_active(False)
		self.label = Gtk.Label(label="Wifi Durumu")
		self.hbox1.pack_start(self.label,False,False,0)
		self.hbox1.pack_start(self.switch,False,True,0)
		self.vbox.pack_start(self.back_button,False,True,0)
		self.vbox.pack_start(self.hbox1,False,False,0)
		
		self.vbox2 = Gtk.VBox(spacing=10)
		self.current_wifi = None
		self.password_entry = Gtk.Entry()
		self.back_button2 = Gtk.Button(label="Çık")
		self.back_button2.connect("clicked",self.out)
		self.save_button = Gtk.Button(label="Kaydet")
		self.save_button.connect("clicked",self.get_pass)
		self.vbox2.pack_start(self.back_button2,False,False,0)
		self.vbox2.pack_start(self.password_entry,False,False,0)
		self.vbox2.pack_start(self.save_button,False,False,0)
		self.vbox2.show_all()
		
		self.add(self.vbox)
		self.show_all()
		a = wifi.Search()
		for x in a:
			if not r'\x00' in x.ssid:
				print(x.ssid)
				a = Gtk.HBox(spacing=10)
				b = Gtk.Button(label=x.ssid)
				b.connect("clicked",self.wifi_clicked)
				a.add(b)
				self.vbox.pack_start(a,False,False,0)
	def wifi_clicked(self,widget):
		if wifi.Connect(widget.get_label()) == False:
			self.remove(self.vbox)
			self.add(self.vbox2)
			self.current_wifi = widget.get_label()
	def out(self,widget):
		self.remove(self.vbox2)
		self.add(self.vbox)
		
	def get_pass(self,widget):
		password = self.password_entry.get_text()
		print(self.current_wifi)
		wifi.Connect(self.current_wifi,password)

		
class AppsWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self,type=Gtk.WindowType.TOPLEVEL)
		self.set_type_hint(Gdk.WindowTypeHint.POPUP_MENU)
		self.resize(400,300)
		self.move(0,40)
		self.vbox = Gtk.VBox()
		self.vbox.set_spacing(10)
		self.back_button = Gtk.Button(label="Çık")
		self.entry = Gtk.Entry()
		self.label2 = Gtk.Label(label="label2")
		self.label4 = Gtk.Label(label="label4")
		self.notebook = Gtk.Notebook()
		self.notebook.set_tab_pos(Gtk.PositionType.LEFT)
		self.web_label = Gtk.Label(label="İnternet")
		self.web_box = Gtk.VBox()
		self.chat_label = Gtk.Label(label="Mesajlaşma")
		self.chat_box = Gtk.VBox()
		self.music_label = Gtk.Label(label="Müzik")
		self.music_box = Gtk.VBox()
		self.video_label = Gtk.Label(label="Video")
		self.video_box = Gtk.VBox()
		self.graphic_label = Gtk.Label(label="Grafik")
		self.graphic_box = Gtk.VBox()
		self.game_label = Gtk.Label(label="Oyun")
		self.game_box = Gtk.VBox()
		self.office_label = Gtk.Label(label="Ofis")
		self.office_box = Gtk.VBox()
		self.reading_label = Gtk.Label(label="Okuma")
		self.reading_box = Gtk.VBox()
		self.development_label = Gtk.Label(label="Geliştirme")
		self.development_box = Gtk.VBox()
		self.system_label = Gtk.Label(label="Sistem")
		self.system_box = Gtk.VBox()
		self.notebook.append_page(self.web_box,self.web_label)
		self.notebook.append_page(self.chat_box,self.chat_label)
		self.notebook.append_page(self.music_box,self.music_label)
		self.notebook.append_page(self.video_box,self.video_label)
		self.notebook.append_page(self.graphic_box,self.graphic_label)
		self.notebook.append_page(self.game_box,self.game_label)
		self.notebook.append_page(self.office_box,self.office_label)
		self.notebook.append_page(self.reading_box,self.reading_label)
		self.notebook.append_page(self.development_box,self.development_label)
		self.notebook.append_page(self.system_box,self.system_label)
		self.vbox.pack_start(self.back_button,False,False,0)
		self.vbox.pack_start(self.entry,False,False,0)
		self.vbox.pack_start(self.notebook,False,False,0)
		self.add(self.vbox)
		self.show_all()
		
class SoundWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self,type=Gtk.WindowType.TOPLEVEL)
		self.set_type_hint(Gdk.WindowTypeHint.POPUP_MENU)
		s = Gdk.Screen.get_default()
		self.resize(220,s.get_height()-80)
		self.move(s.get_width()-220,40)
		self.vbox = Gtk.VBox()
		self.vbox.set_spacing(10)
		self.hbox1 = Gtk.HBox()
		self.hbox1.set_spacing(10)
		self.back_button = Gtk.Button(label="Çık")
		self.adjustment = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		self.scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=self.adjustment)
		self.scale.connect("value-changed",self.set_sound)
		self.label = Gtk.Label(label="Ses Çıkışı")
		self.hbox1.pack_start(self.label,False,False,0)
		self.hbox1.add(self.scale)
		self.vbox.pack_start(self.back_button,False,True,0)
		self.vbox.pack_start(self.hbox1,False,False,0)
		self.add(self.vbox)
		self.show_all()

	def set_sound(self,widget):
		value = self.scale.get_value()
		alsaaudio.Mixer().setvolume(int(value))

class TPanel:
	def __init__(self):
		
		#gerekli değişkenler oluşturuluyor
		self.panel = None
		self.time_button = None
		self.time_window = None
		self.time_window_showing = False
		self.calendar = None
		self.volume_button = None
		self.sound_window = None
		self.sound_window_showing = False
		self.wifi_button = None
		self.wifi_image = None
		self.wifi_window = None
		self.wifi_window_showing = False
		self.apps_image = None
		self.apps_button = None
		self.apps_window = None
		self.apps_window_showing = False
		self.sound_system = alsaaudio.Mixer()
		self.g_c_year,self.g_c_month,self.g_c_day = None,None,None
		self.activities = []
		
		#pencere düzenleniyor
		self.window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
		self.window.set_type_hint(Gdk.WindowTypeHint.DOCK)
		self.window.set_wmclass("panel","tpanel")
		self.window.move(0,0)
		self.window.set_decorated(False)
		
		#panel oluşturulup düzenleniyor
		self.create_panel_box()
		self.add_plugins_to_panel()
		self.window.add(self.panel)
		self.xstuff()
		
		
	def xstuff(self):
		screen = self.window.get_screen()
		s = Gdk.Screen.get_default()
		disp = screen.get_display()
		width = s.get_width()
		height = s.get_height()
		bar_size = 40
		x,y = 0,0
		self.window.move(x,y)
		self.window.resize(width,bar_size)
		self.window.show_all()

		display = Display()
		topw = display.create_resource_object('window',
                                       self.window.get_toplevel().get_window().get_xid())
		topw.change_property(display.intern_atom('_NET_WM_STRUT'),
                       display.intern_atom('CARDINAL'), 32,
                       [0, 0, bar_size, 0 ],
                       X.PropModeReplace)

		topw.change_property(display.intern_atom('_NET_WM_STRUT_PARTIAL'),
		display.intern_atom('CARDINAL'), 32,
		[0, 0, bar_size, 0, 0, 0, 0, 0, x, x+width-1, 0, 0],
		X.PropModeReplace)
		
	def shutdown_panel(self,widget):
		Gtk.main_quit()
		exit()
		
	def create_panel_box(self):
		self.panel = Gtk.HBox()
		self.panel.set_spacing(0)

	def add_activity_setting(self,widget):
		self.time_window.remove(self.time_window.vbox)
		self.time_window.add(self.time_window.vbox2)

	def close_activity_setting(self,widget):
		self.time_window.remove(self.time_window.vbox2)
		self.time_window.add(self.time_window.vbox)	

	def add_activity_to_box(self,activity):
		b = activity[1]+" "+activity[0]+"\n"+activity[2]
		c = Gtk.Label(label=b)
		self.time_window.activity_box.add(c)
		self.time_window.activity_box.show_all()

	def add_activity(self,widget):
		a,b,c = self.time_window.calendar2.get_date()
		d = str(a)+":"+str(b)+":"+str(c)
		e = self.time_window.name_of_activity_entry.get_text()
		f = self.time_window.info_about_activity_entry.get_text()
		self.activities.append([d,e,f])
		self.add_activity_to_box(self.activities[-1])
		self.close_activity_setting(widget)

	def control_time_button(self):
		if self.time_window_showing == True:
			self.time_window.hide()
			self.time_window_showing = False
		else:
			self.time_window_showing = True
			self.time_window.show_all()
			self.time_window.label.set_label(strftime('%d %B %Y %A %X'))
			self.time_window.calendar.select_day(self.g_c_day)
			self.time_window.calendar.select_month(self.g_c_month,self.g_c_year)

	def time_clicked(self,widget):
		if self.time_window == None:
			self.time_window = TimeWindow()
			self.time_window.back_button.connect("clicked",self.time_clicked)
			self.time_window.add_activity.connect("clicked",self.add_activity_setting)
			self.time_window.close_button.connect("clicked",self.close_activity_setting)
			self.time_window.save_button.connect("clicked",self.add_activity)
			self.g_c_year,self.g_c_month,self.g_c_day = self.time_window.calendar.get_date()
		if self.wifi_window_showing == True:
			self.wifi_window_showing = False
			self.wifi_window.hide()
		if self.sound_window_showing == True:
			self.sound_window_showing = False
			self.sound_window.hide()
		if self.apps_window_showing == True:
			self.apps_window_showing = False
			self.apps_window.hide()
		self.control_time_button()

	def create_time_plugin(self):
		self.time_button = Gtk.Button(strftime('%X'))
		self.time_button.connect("clicked", self.time_clicked)
        
	def volume_changed(self,button,value):
		pass
        
	def control_sound_button(self):
		if self.sound_window_showing == True:
			self.sound_window.hide()
			self.sound_window_showing = False
		else:
			self.sound_window_showing = True
			self.sound_window.show_all()    
        
	def sound_clicked(self,widget):
		if self.sound_window == None:
			self.sound_window = SoundWindow()
			self.sound_window.back_button.connect("clicked",self.sound_clicked)
			self.sound_window.scale.set_value(int(self.sound_system.getvolume()[0]))
		if self.wifi_window_showing == True:
			self.wifi_window_showing = False
			self.wifi_window.hide()
		if self.time_window_showing == True:
			self.time_window_showing = False
			self.time_window.hide()
		if self.apps_window_showing == True:
			self.apps_window_showing = False
			self.apps_window.hide()
		self.control_sound_button()
        
	def create_sound_button(self):
		self.sound_image = Gtk.Image()
		self.sound_image.set_from_file("sound.png")
		self.volume_button = Gtk.Button()
		self.volume_button.connect("clicked",self.sound_clicked)
		self.volume_button.set_image(self.sound_image)
		

	def control_wifi_button(self):
		if self.wifi_window_showing == True:
			self.wifi_window.hide()
			self.wifi_window_showing = False
		else:
			self.wifi_window_showing = True
			self.wifi_window.show_all()
		
	def wifi_clicked(self,widget):
		if self.wifi_window == None:
			self.wifi_window = WifiWindow()
			self.wifi_window.back_button.connect("clicked",self.wifi_clicked)
		if self.sound_window_showing == True:
			self.sound_window_showing = False
			self.sound_window.hide()
		if self.apps_window_showing == True:
			self.apps_window_showing = False
			self.apps_window.hide()
		if self.time_window_showing == True:
			self.time_window_showing = False
			self.time_window.hide()
		self.control_wifi_button()
		
	def create_wifi_button(self):
		self.wifi_image = Gtk.Image()
		self.wifi_image.set_from_file("wifi.png")
		self.wifi_button = Gtk.Button()
		self.wifi_button.set_image(self.wifi_image)
		self.wifi_button.connect("clicked",self.wifi_clicked)

	def control_apps_button(self):
		if self.apps_window_showing == True:
			self.apps_window.hide()
			self.apps_window_showing = False
		else:
			self.apps_window_showing = True
			self.apps_window.show_all()

	def apps_clicked(self,widget):
		if self.apps_window == None:
			self.apps_window = AppsWindow()
			self.apps_window.back_button.connect("clicked",self.apps_clicked)
		if self.wifi_window_showing == True:
			self.wifi_window_showing = False
			self.wifi_window.hide()
		if self.sound_window_showing == True:
			self.sound_window_showing = False
			self.sound_window.hide()
		if self.time_window_showing == True:
			self.time_window_showing = False
			self.time_window.hide()
		self.control_apps_button()

	def create_apps_button(self):
		self.apps_image = Gtk.Image()
		self.apps_image.set_from_file("gezgin.png")
		self.apps_button = Gtk.Button()
		self.apps_button.set_image(self.apps_image)
		self.apps_button.connect("clicked",self.apps_clicked)

	def add_plugins_to_panel(self):
		self.create_time_plugin()
		self.create_sound_button()
		self.create_wifi_button()
		self.create_apps_button()
		shutdown = Gtk.Button(label="Kapat")
		shutdown.connect("clicked",self.shutdown_panel)
		self.panel.pack_start(self.apps_button,False,False,0)
		self.panel.pack_end(self.volume_button,False,False,0)
		self.panel.pack_end(self.time_button,False,False,0)
		self.panel.pack_end(self.wifi_button,False,False,0)
		self.panel.pack_start(shutdown,False,False,0)

app = TPanel()
Gtk.main()
