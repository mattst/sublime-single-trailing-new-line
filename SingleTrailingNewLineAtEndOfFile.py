#
# A Sublime Text plugin to ensure that exactly one trailing
# newline is at the end of all files when files are saved.
#
# License: MIT License
#

import sublime, sublime_plugin


def is_newline_or_whitespace(char):

    return char == '\n' or char == '\t' or char == ' '


class SingleTrailingNewLineAtEndOfFileListener(sublime_plugin.EventListener):

    def on_pre_save(self, view):

        # A sublime_plugin.TextCommand class is needed for an edit object.
        view.run_command("single_trailing_new_line_at_end_of_file")
        return None


class SingleTrailingNewLineAtEndOfFileCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # Ignore empty files.
        if self.view.size() == 0:
            return

        # Work backwards from the end of the file to find the position of the
        # last significant char, one that is neither whitespace nor a newline.

        pos = self.view.size() - 1
        char = self.view.substr(pos)

        while pos >= 0 and is_newline_or_whitespace(char):
            pos -= 1
            char = self.view.substr(pos)

        # Delete from the last significant char (not inc.) to the end of the
        # file and then add a single trailing newline at the end of the file.

        del_region = sublime.Region(pos + 1, self.view.size())
        self.view.erase(edit, del_region)
        self.view.insert(edit, self.view.size(), "\n")
