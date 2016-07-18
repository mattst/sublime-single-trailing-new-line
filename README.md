
## Single Trailing New Line - Package for Sublime Text

This Sublime Text package makes sure that there is exactly one trailing newline at the end of a file. All the whitespace and trailing newlines at the end of the file (if any) are removed and a single newline is inserted. Note that empty files (a file size of zero) are deliberately ignored and will not have a newline inserted into them.

Note: This is different from the `ensure_newline_at_eof_on_save` setting which makes sure that there is *at least one trailing newline* at the end of the file, rather than making sure that there is *exactly one trailing newline* at the end of the file.

### Features

- It can be set to run automatically every time a file is saved. This is disabled by default but by changing the settings it can be enabled either for all files or for only files of specific syntaxes.

- It can be run by using its command palette entry or by assigning it to a key binding. In both these cases the settings file is ignored and it will work with all files.

- Command palette entries to add and remove the syntax of the current file to the syntaxes list setting are also included.

### Requirements

- Sublime Text v2 or v3
- Tested with: v2 build 2221 and v3 builds 3114 and 3083

### Installation Instructions

#### Package Control

- Open the command palette and select: `Package Control: Install Package`
- Wait for the package list to be updated and then select: `SingleTrailingNewLine`

#### Manual Installation

- Download the package's [zip file](https://github.com/mattst/sublime-single-trailing-new-line/archive/master.zip) and extract it, or use `git clone` to get the package from its [GitHub page](https://github.com/mattst/sublime-single-trailing-new-line).
- Move the package's folder to your Sublime Text *config* `Packages` folder. [*Where is that?*](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)
- Rename it from `sublime-single-trailing-new-line-master` to `SingleTrailingNewLine`.
- You should end up with this folder: `Packages/SingleTrailingNewLine/`

### Setup and Usage

The plugin was designed to be run automatically when a file is saved, rather than by manually running it from the command palette or with a key binding. However some users may prefer to run it manually on an as-needed basis, or to have that option available for syntaxes they have not added to the syntaxes list setting.

#### Command Palette

The package includes several command palette commands:

- `Single Trailing New Line`: ensure there is exactly one trailing newline at the end of the file. When run from the command palette the plugin will work with all files, the settings file will be ignored.

- `Single Trailing New Line: Add Current Syntax`: adds the full syntax name of the current file to the syntax list setting.

- `Single Trailing New Line: Remove Current Syntax`: removes the full syntax name of the current file from the syntax list setting.

- `Single Trailing New Line: Copy Current Syntax`: copies the full syntax name of the current file into the clipboard.

#### Key Bindings

When run from a key binding the plugin will work with all files, the settings file will be ignored.

Add the key binding of your choice to your user key bindings file (`Menu --> Preferences --> Key Bindings - User`):

    { "keys": ["ctrl+whatever"], "command": "single_trailing_new_line" }

There are now so many Sublime Text packages available that key conflicts are commonplace, it is therefore best for users to decide their own keys for small packages like this one.

Not sure? You could try: `"ctrl+k", "ctrl+n"` (which is not in use on my system).

For users who would like to use keys for all the features here are the available commands:

- `single_trailing_new_line`: ensures there is exactly one trailing newline at the end of the file.
- `single_trailing_new_line_add_syntax`: adds the current syntax to the syntaxes list setting.
- `single_trailing_new_line_remove_syntax`: removes the current syntax from the syntaxes list setting.
- `single_trailing_new_line_copy_syntax`: copies the current syntax into the clipboard.

#### Running Automatically

The plugin can be run automatically every time a file is saved to ensure that the file is saved with exactly one trailing newline but this is disabled by default. It can be enabled for either all files or for only files of specific syntaxes by changing the default settings in the package's user settings file.

The path of the package's user settings file, in your Sublime Text config folders ([*where is that?*](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)), must be:

    Packages/User/SingleTrailingNewLine.sublime-settings

The default and user settings files can be accessed from the Sublime Text menu:

    Menu --> Preferences --> Package Settings --> SingleTrailingNewLine --> Settings - Default
    Menu --> Preferences --> Package Settings --> SingleTrailingNewLine --> Settings - User

When changing the settings make sure you use the user settings file.

There are 2 settings:

- `enable_for_all_syntaxes`: *true/false*. If this is set to *true* the plugin will be active for all files, regardless of their syntax, every time any file is saved the plugin will be run. Default: *false*.

- `enable_for_syntaxes_list`: *a list of strings*. If one or more syntax names are added to this list, the plugin will be run every time a file, whose syntax matches one of the syntax names, is saved. Default: `[]` - *an empty list*. This setting will be ignored if the `enable_for_all_syntaxes` setting is set to *true*.

The `.sublime-syntax` syntax file format was introduced by Sublime Text v3 build 3084, from that version onwards all built-in syntax files use that format, with the exception of `Packages/Text/Plain text.tmLanguage`. Other `.tmLanguage` syntax files may be on your system if a syntax package that includes them has been installed, e.g. `PythonImproved`. Sublime Text v2 and v3 builds earlier than 3084 use only `.tmLanguage` syntax files.

Here is an example `Packages/User/SingleTrailingNewLine.sublime-settings` file:

    {
        "enable_for_all_syntaxes": false,

        "enable_for_syntaxes_list":
        [
            "Packages/C++/C.sublime-syntax",
            "Packages/C++/C++.sublime-syntax",
            "Packages/Java/Java.sublime-syntax",
            "Packages/JavaScript/JSON.sublime-syntax",
            "Packages/Python/Python.sublime-syntax",
            "Packages/Python Improved/PythonImproved.tmLanguage",
            "Packages/Rails/",
            "Packages/XML/XML.sublime-syntax"
        ]
    }

The full syntax name of the current file's syntax can be added to or removed from the `enable_for_syntaxes_list` by entering `Single Trailing New Line: Add Current Syntax` or `Single Trailing New Line: Remove Current Syntax` into the command palette or it can be copied into the clipboard by entering `Single Trailing New Line: Copy Current Syntax`. It can also be displayed by using the `view.settings().get("syntax")` command in the console.

The following information about the `enable_for_syntaxes_list` entries should be noted:

- They are case sensitive and neither regular expressions nor wildcards are accepted.

- It is generally advisable to use full syntax names, as shown in the example file above. Partial syntax names will work, e.g. `"XML.sublime-syntax"`, but only full syntax names will be added and removed when using the palette commands.

- In fact any case sensitive substring match will work. e.g. the list `["C++", "Java", "Python", "Rails", "XML"]` would match all of the syntaxes shown in the example file above, but it would also match a whole lot more (17 of the ST v3 default syntaxes).

- `"C.sublime-syntax"` would match both `"Packages/C++/C.sublime-syntax"` and `"Packages/Objective-C/Objective-C.sublime-syntax"`. Using just `"C"` on its own would be inadvisable because it would match any syntax containing an upper-case letter C (16 of the ST v3 default syntaxes).

- All of the syntaxes in a (multi-syntax) package can be matched by using the syntax's path component on its own. e.g. `"Packages/Rails/"` would match all 5 syntaxes from the `Rails` package, i.e. `"Packages/Rails/Ruby on Rails.sublime-syntax"` as well as the other 4.

- Using just `"Java"` would match all 7 syntaxes from the `Java` and `JavaScript` packages, as would `"Packages/Java"` but not `"Packages/Java/"` because the trailing slash would not match `"Packages/JavaScript/"`.

For reference use only, 2 lists of Sublime Text built-in syntaxes are provided:

- [Sublime Text v2 build 2221 syntax list](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/Sublime_Text_2221_Syntax_List)
- [Sublime Text v3 build 3114 syntax list](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/Sublime_Text_3114_Syntax_List)

Those using Sublime Text v3 builds earlier than 3084 should use the v2 list.

### License

This package is licensed under The MIT License (MIT). See the [LICENSE file](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/LICENSE).
