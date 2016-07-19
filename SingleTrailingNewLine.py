
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


settings_file = "SingleTrailingNewLine.sublime-settings"
setting_enable_for_all_syntaxes  = "enable_for_all_syntaxes"
setting_enable_for_syntaxes_list = "enable_for_syntaxes_list"


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
        """ Determines whether the plugin should be run for the file in the current view. """

        # This method does not result in a disk file read every time a file is
        # saved; the settings are loaded into memory at start-up and whenever
        # the settings file is modified, so this method is not time expensive.

        try:
            settings = sublime.load_settings(settings_file)

            if settings.get(setting_enable_for_all_syntaxes, False):
                return True

            current_syntax = view.settings().get("syntax")

            for syntax in settings.get(setting_enable_for_syntaxes_list, []):
                if len(syntax) > 0 and syntax in current_syntax:
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

        last_significant_char = self.view.size() - 1

        while last_significant_char >= 0 and self.view.substr(last_significant_char).isspace():
            last_significant_char -= 1

        erase_region = sublime.Region(last_significant_char + 1, self.view.size())
        self.view.erase(edit, erase_region)
        self.view.insert(edit, self.view.size(), "\n")


class SingleTrailingNewLineAddSyntaxCommand(sublime_plugin.TextCommand):
    """ Adds the current file's syntax to the syntaxes list setting. """

    def run(self, edit):

        try:
            settings = sublime.load_settings(settings_file)

            current_syntax = self.view.settings().get("syntax")
            enable_for_syntaxes = settings.get(setting_enable_for_syntaxes_list, [])

            if current_syntax not in enable_for_syntaxes:
                enable_for_syntaxes.append(current_syntax)
                enable_for_syntaxes.sort()
                settings.set(setting_enable_for_syntaxes_list, enable_for_syntaxes)
                sublime.save_settings(settings_file)
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
            settings = sublime.load_settings(settings_file)

            current_syntax = self.view.settings().get("syntax")
            enable_for_syntaxes = settings.get(setting_enable_for_syntaxes_list, [])

            if current_syntax in enable_for_syntaxes:
                enable_for_syntaxes.remove(current_syntax)
                enable_for_syntaxes.sort()
                settings.set(setting_enable_for_syntaxes_list, enable_for_syntaxes)
                sublime.save_settings(settings_file)
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

            settings = sublime.load_settings(settings_file)

            if arg_value:
                settings.set(setting_enable_for_all_syntaxes, True)
                msg = "Enable For All Setting - True"

            else:
                settings.set(setting_enable_for_all_syntaxes, False)
                msg = "Enable For All Setting - False"

            sublime.save_settings(settings_file)
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
