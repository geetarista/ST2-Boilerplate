# These two are required for plugin development
import sublime
import sublime_plugin

# Usually necessary for commands
import os
import subprocess

# Helper method
def helper_method(something):
    return something

class ApplicationCommand(sublime_plugin.ApplicationCommand):
    """ This is an application command """
    def run(self):
        something = helper_method("application")

class WindowCommand(sublime_plugin.WindowCommand):
    """ This is a window command """
    def run(self):
        something = helper_method("window")

class LocalHelpCommand(sublime_plugin.TextCommand):
    """ This is a text command """
    def run(self, edit):
        something = helper_method("text")
