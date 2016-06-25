
#
# Name:               Single Trailing New Line
#
# Requirements:       Plugin for Sublime Text v2 and v3
#
# Written by:         mattst - https://github.com/mattst
#
# License:            MIT License
#
# Plugin File:        SingleTrailingNewLine.py
#
# Settings File:      SingleTrailingNewLine.sublime-settings
#
# Settings Fields:    syntax_list: a list of Sublime Text syntaxes which
#                     enable the plugin.
# 
#                     enable_for_all_files: boolean to control whether the
#                     plugin should be run for all files or not. If set to
#                     true then the "syntax_list" setting is ignored.
# 
# This Sublime Text plugin makes sure that when files are saved there is always
# exactly one trailing newline at the end the files. It works by deleting all
# the newlines and whitespace at the end of the file and then inserting a single
# newline at the end of the file.
#
# By default the plugin is active for all files and it will be run every time,
# and immediately before, any file is saved by Sublime Text. Users can control
# which syntaxes the plugin will be active for by adding the full or partial
# names of the required syntaxes to the syntax_list in the settings file, there
# is an example list commented out in the file. A lower case partial match is
# used so, for example, "python" would match both the "Python.sublime-syntax"
# and the (Text Mate compatible) "PythonImproved.tmLanguage" syntax. Users can
# run the "view.settings().get('syntax')" command in the console to retrieve 
# the full syntax name of the current file.
#

import sublime, sublime_plugin

#
# This Sublime Text package uses both an EventListener and a TextCommand derived
# class. This is because an edit object is needed to delete and insert text in a
# buffer and edit objects are not available in EventListener classes while they
# are in TextCommand classes. Accordingly this plugin is designed so that the
# EventListener class calls the TextCommand class. This design also allows the
# TextCommand class to override the is_enabled() method, which controls whether
# the plugin will be run, and which is not implemented by the EventListener API.
#

class SingleTrailingNewLineListener(sublime_plugin.EventListener):
    """ Calls the corresponding TextCommand when a pre-save event occurs. """

    def on_pre_save(self, view):
        """ Called immediately before the file in the view is saved. """
        
        view.run_command("single_trailing_new_line")
        return None


class SingleTrailingNewLineCommand(sublime_plugin.TextCommand):
    """
    Deletes all trailing newlines and whitespace at the end of the file and then
    inserts a single trailing newline at the end of the file. The is_enabled()
    method controls whether the plugin will be run or not.
    """

    def run(self, edit):
        """ Called when the TextCommand plugin is run. """

        # Do nothing if the file is empty.
        if self.view.size() < 1:
            return

        # Find the last character that is neither whitespace nor a newline.

        pos = self.view.size() - 1

        while pos >= 0 and self.view.substr(pos).isspace():
            pos -= 1

        # Delete trailing whitespace and add a single trailing newline.

        erase_region = sublime.Region(pos + 1, self.view.size())
        self.view.erase(edit, erase_region)
        self.view.insert(edit, self.view.size(), "\n")


    def is_enabled(self):
        """
        Controls whether or not the plugin should be run. True is returned if
        the "enable_for_all_files" setting is true or for files whose syntax
        name has a match in the "syntax_list" setting, otherwise false.
        """

        settings_file = "SingleTrailingNewLine.sublime-settings"
        settings = sublime.load_settings(settings_file)

        enable_for_all_files = settings.get("enable_for_all_files", False)

        if enable_for_all_files:
            return True

        syntax_list = settings.get("syntax_list", [])

        if not isinstance(syntax_list, list) or len(syntax_list) == 0:
            return False

        current_syntax = self.view.settings().get('syntax')

        for syntax in syntax_list:
            # Partial matches are allowed. For example:
            # "Java" will match "JavaScript.sublime-syntax"
            if syntax in current_syntax:
                return True

        return False
