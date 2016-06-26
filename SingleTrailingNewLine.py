
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
# Settings Fields:    "syntax_list": a list of Sublime Text syntaxes which
#                     enable the plugin.
#
#                     "enable_for_all_files": boolean to control whether the
#                     plugin should be run for all files or not. If set to
#                     true then the "syntax_list" setting is ignored.
#
# Optional Command:   single_trailing_new_line (ignores settings file).
#
# This Sublime Text plugin makes sure that there is exactly one trailing newline
# at the end of a file. It works by deleting all the whitespace and newlines at
# the end of the file and then inserting a single newline.
#
# The plugin can be run in one of 2 ways (or both):
#
# 1) The plugin can be run automatically every time a file is saved. For this
#    various settings in the settings file can be set. To enable it for all
#    files, set the "enable_for_all_files" setting to true. To enable it only
#    for files of specific syntaxes, add the syntax names to the "syntax_list"
#    setting. The console command - view.settings().get("syntax") - can be used
#    to get the full syntax name of the current file.
#
# 2) The command "single_trailing_new_line" can be used by assigning it to a key
#    binding or by creating a command palette entry for it. When this is done
#    the settings file is ignored and the command will work with all files.
#


import sublime, sublime_plugin


class SingleTrailingNewLineListener(sublime_plugin.EventListener):
    """
    Calls the "single_trailing_new_line" command when a pre-save event occurs
    but only if the plugin has been enabled in the settings file for all files
    or for the syntax of the current file.

    Note: The EventListener class does not implement the is_enabled() method,
    unlike the TextCommand, ApplicationCommand, and WindowCommand classes.
    """

    def on_pre_save(self, view):
        """ Called immediately before the file in the view is saved. """

        if self.is_plugin_enabled(view):
            view.run_command("single_trailing_new_line")

    def is_plugin_enabled(self, view):
        """
        Controls whether or not the plugin should run. True is returned if the
        "enable_for_all_files" setting is true and for files whose syntax name
        has a match in the "syntax_list" setting, otherwise false.

        This method does not result in a disk file read every time a file is
        saved; the settings are loaded into memory at start-up and when the
        settings file is modified, thus this is not time expensive.
        """

        settings_file  = "SingleTrailingNewLine.sublime-settings"
        settings       = sublime.load_settings(settings_file)
        enable_for_all = settings.get("enable_for_all_files", False)
        syntaxes       = settings.get("syntax_list", [])

        if enable_for_all:
            return True

        if not isinstance(syntaxes, list) or len(syntaxes) == 0:
            return False

        syntax_current_file = view.settings().get("syntax")

        for syntax in syntaxes:
            if syntax in syntax_current_file:
                return True

        return False


class SingleTrailingNewLineCommand(sublime_plugin.TextCommand):
    """
    Deletes all trailing newlines and whitespace at the end of the file and
    then inserts a single trailing newline at the end of the file.
    """

    def run(self, edit):
        """ Called when the plugin is run. """

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
