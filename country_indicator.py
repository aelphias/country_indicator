import gi
import requests

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator

class TrayIndicator:
    def __init__(self):
        
        self.app = 'Country indicator'
        self.indicator = appindicator.Indicator.new(
            self.app, 'indicator-messages', appindicator.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        self.indicator.set_label('Loading COUNTRY', self.app)

    def create_menu(self):
        menu = Gtk.Menu()
        item = Gtk.MenuItem('Quit')
        item.connect('activate', self.quit)
        menu.append(item)
        menu.show_all()
        return menu

    def quit(self, source):
        Gtk.main_quit()

    def update_label(self):
        response = requests.get('http://ipinfo.io/country')
        self.indicator.set_label(response.text.strip(), self.app)
        return True

app = TrayIndicator()

GLib.timeout_add_seconds(2, app.update_label)

Gtk.main()
