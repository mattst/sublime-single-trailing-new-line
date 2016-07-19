
#
# Name:          Single Trailing Newline
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


SETTINGS_FILE = "SingleTrailingNewLine.sublime-settings"
ENABLE_FOR_ALL_SYNTAXES_SETTING  = "enable_for_all_syntaxes"
ENABLE_FOR_SYNTAXES_LIST_SETTING = "enable_for_syntaxes_list"


class SingleTrailingNewLineListener(sublime_plugin.EventListener):
    """
    Calls the "single_trailing_new_line" command when a pre-save event occurs but only if the plugin
    has been enabled in the settings file for all files or for the syntax of the current file.

    Note: The EventListener class does not implement the is_enabled() method, unlike all the rest of
    the sublime_plugin classes, so the is_plugin_enabled() method serves as a replacement.
    """

    def on_pre_save(self, view):
        """ Called immediately before the file in the view is saved. """

        if self.is_plugin_enabled(view):
            # A TextCommand derived class is needed to get an edit object.
            view.run_command("single_trailing_new_line")


    def is_plugin_enabled(self, view):
        """ Determines whether the plugin should be run automatically for the file in the view. """

        # This method does not result in a disk file read every time a file is
        # saved; the settings are loaded into memory at start-up and whenever
        # the settings file is modified, so this method is not time expensive.

        try:
            settings = sublime.load_settings(SETTINGS_FILE)

            if settings.get(ENABLE_FOR_ALL_SYNTAXES_SETTING, False):
                return True

            syntax_current_file = view.settings().get("syntax")

            for syntax in settings.get(ENABLE_FOR_SYNTAXES_LIST_SETTING, []):
                if len(syntax) > 0 and syntax in syntax_current_file:
                    return True

            return False

        except Exception:
            return False


class SingleTrailingNewLineCommand(sublime_plugin.TextCommand):
    """ Deletes all trailing whitespace at the end of the file and inserts a single newline. """

    def run(self, edit):

        # Ignore empty files.
        if self.view.size() < 1:
            return

        # Work backwards from the end of the file to find
        # the last significant (non-whitespace) character.

        last_sig_char = self.view.size() - 1

        while last_sig_char >= 0 and self.view.substr(last_sig_char).isspace():
            last_sig_char -= 1

        erase_region = sublime.Region(last_sig_char + 1, self.view.size())
        self.view.erase(edit, erase_region)
        self.view.insert(edit, self.view.size(), "\n")


class SingleTrailingNewLineAddSyntaxCommand(sublime_plugin.TextCommand):
    """ Adds the current file's syntax to the syntaxes list setting. """

    def run(self, edit):

        try:
            settings = sublime.load_settings(SETTINGS_FILE)

            syntax_current_file = self.view.settings().get("syntax")
            enable_for_syntaxes = settings.get(ENABLE_FOR_SYNTAXES_LIST_SETTING, [])

            if syntax_current_file not in enable_for_syntaxes:
                enable_for_syntaxes.append(syntax_current_file)
                enable_for_syntaxes.sort()
                settings.set(ENABLE_FOR_SYNTAXES_LIST_SETTING, enable_for_syntaxes)
                sublime.save_settings(SETTINGS_FILE)
                msg = "Syntax added to the syntax list"
                sublime.status_message(msg)
            else:
                msg = "Syntax already in the syntax list"
                sublime.status_message(msg)

        except Exception:
            msg = "The SingleTrailingNewLine.sublime-settings file is invalid"
            sublime.status_message(msg)


class SingleTrailingNewLineRemoveSyntaxCommand(sublime_plugin.TextCommand):
    """ Removes the current file's syntax from the syntaxes list setting. """

    def run(self, edit):

        try:
            settings = sublime.load_settings(SETTINGS_FILE)

            syntax_current_file = self.view.settings().get("syntax")
            enable_for_syntaxes = settings.get(ENABLE_FOR_SYNTAXES_LIST_SETTING, [])

            if syntax_current_file in enable_for_syntaxes:
                enable_for_syntaxes.remove(syntax_current_file)
                enable_for_syntaxes.sort()
                settings.set(ENABLE_FOR_SYNTAXES_LIST_SETTING, enable_for_syntaxes)
                sublime.save_settings(SETTINGS_FILE)
                msg = "Syntax removed from the syntax list"
                sublime.status_message(msg)
            else:
                msg = "Syntax was not in the syntax list"
                sublime.status_message(msg)

        except Exception:
            msg = "The SingleTrailingNewLine.sublime-settings file is invalid"
            sublime.status_message(msg)


class SingleTrailingNewLineEnableForAllSyntaxesSettingCommand(sublime_plugin.TextCommand):
    """ Sets the enable for all syntaxes setting to a boolean value. """

    def run(self, edit, **kwargs):

        try:
            arg_value = kwargs.get("value", None)

            if not isinstance(arg_value, bool):
                msg = "Invalid args"
                sublime.status_message(msg)
                return

            settings = sublime.load_settings(SETTINGS_FILE)

            if arg_value:
                settings.set(ENABLE_FOR_ALL_SYNTAXES_SETTING, True)
                msg = "Enable For All Syntaxes - True"

            else:
                settings.set(ENABLE_FOR_ALL_SYNTAXES_SETTING, False)
                msg = "Enable For All Syntaxes - False"

            sublime.save_settings(SETTINGS_FILE)
            sublime.status_message(msg)

        except Exception:
            msg = "The SingleTrailingNewLine.sublime-settings file is invalid"
            sublime.status_message(msg)


class SingleTrailingNewLineCopySyntaxCommand(sublime_plugin.TextCommand):
    """ Copies the current file's syntax into the clipboard. """

    def run(self, edit):

        syntax_current_file = self.view.settings().get("syntax")
        sublime.set_clipboard(syntax_current_file)

        msg = "Syntax copied to the clipboard"
        sublime.status_message(msg)
