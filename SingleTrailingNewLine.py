
#
# Name:          Single Trailing New Line
#
# Requirements:  Sublime Text v2 and v3
#
# Written by:    mattst - https://github.com/mattst
# 
# Homepage:      https://github.com/mattst/sublime-single-trailing-new-line
#
# License:       MIT License
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
        "enable_for_all" setting is true and for files whose syntax name has a
        match in the "syntax_list" setting, otherwise false.

        This method does not result in a disk file read every time a file is
        saved; the settings are loaded into memory at start-up and when the
        settings file is modified, thus this is not time expensive.
        """

        settings_file  = "SingleTrailingNewLine.sublime-settings"
        settings       = sublime.load_settings(settings_file)
        enable_for_all = settings.get("enable_for_all", False)
        syntax_list    = settings.get("syntax_list", [])

        if enable_for_all:
            return True

        if not isinstance(syntax_list, list) or len(syntax_list) == 0:
            return False

        syntax_current_file = view.settings().get("syntax")

        for syntax in syntax_list:
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


class CopySyntaxNameCommand(sublime_plugin.TextCommand):
    """ Copies the current file's syntax name into the clipboard. """

    def run(self, edit):
        """ Called when the plugin is run. """

        syntax_current_file = self.view.settings().get("syntax") 
        sublime.set_clipboard(syntax_current_file)
