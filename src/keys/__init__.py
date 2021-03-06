# -*- coding: utf-8 -*-
import platform
import exceptions
from ctypes import c_char_p
from libloader import load_library
import paths
if platform.architecture()[0][:2] == "32":
	lib = load_library("api_keys32", x86_path=paths.app_path("keys/lib"))
else:
	lib = load_library("api_keys64", x64_path=paths.app_path("keys/lib"))

keyring = None

def setup():
	global keyring
	if keyring == None:
		keyring = Keyring()

class Keyring(object):
	def __init__(self):
		super(Keyring, self).__init__()

	def _call_method(self, function):
		result = getattr(lib, function)
		result = c_char_p(result.__call__())
		return result.value

	def get(self, func):
		return getattr(self, "_call_method")("get_"+func)