#
# A Sublime Text plugin to ensure that exactly one trailing
# newline is at the end of all files when files are saved.
#
# License: MIT License
#

import sublime, sublime_plugin

class SingleTrailingNewLineAtEndOfFileListener(sublime_plugin.EventListener):

    def on_pre_save(self, view):

        current_syntax = view.settings().get('syntax')
    
        if self.should_plugin_run_with_syntax(current_syntax):
            # A sublime_plugin.TextCommand class is needed for an edit object.
            view.run_command("single_trailing_new_line_at_end_of_file")

        return None


    def should_plugin_run_with_syntax(self, current_syntax):

        settings_file = "SingleTrailingNewLineAtEndOfFile.sublime-settings"
        settings = sublime.load_settings(settings_file)
        valid_sytaxes = settings.get("syntax_list", [])
        
        if not isinstance(valid_sytaxes, list):
            return True

        if len(valid_sytaxes) == 0:
            return True

        for valid_sytax in valid_sytaxes:
            if valid_sytax.lower() in current_syntax.lower():
                return True
        
        return False


class SingleTrailingNewLineAtEndOfFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # Ignore empty files.
        if self.view.size() == 0:
            return

        # Work backwards from the end of the file to find the position of the
        # last significant char, one that is neither whitespace nor a newline.

        pos = self.view.size() - 1
        char = self.view.substr(pos)

        while pos >= 0 and char.isspace():
            pos -= 1
            char = self.view.substr(pos)

        # Delete from the last significant char (not inc.) to the end of the
        # file and then add a single trailing newline at the end of the file.

        del_region = sublime.Region(pos + 1, self.view.size())
        self.view.erase(edit, del_region)
        self.view.insert(edit, self.view.size(), "\n")
