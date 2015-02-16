# -*- coding: utf-8 -*-
import application
import update
import platform
#if platform.system() == "Windows":
from wxUpdater import *

def do_update():
	try:
		update.perform_update(endpoint=application.update_url, current_version=application.version, app_name=application.name, update_available_callback=available_update_dialog, progress_callback=progress_callback, update_complete_callback=update_finished)
	except:
		pass