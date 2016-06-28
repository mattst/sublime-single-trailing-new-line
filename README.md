
## Single Trailing New Line - Package for Sublime Text

This Sublime Text package makes sure that there is exactly one trailing newline at the end of a file. It works by deleting all the whitespace and newlines at the end of the file (if there are any) and then inserting a single newline.

Note: This is different from the `ensure_newline_at_eof_on_save` setting which makes sure that there is *at least one trailing newline* at the end of the file, rather than making sure that there is *exactly one trailing newline* at the end of the file.

### Features

- It can be set to run automatically every time a file is saved. This is disabled by default but by changing the settings it can be enabled either for all files or for only files of specific syntaxes.

- It can be run by using its command palette entry or by assigning it to a key binding. In both these cases the settings file is ignored and it will work with all files.

- A command palette entry that copies the full syntax name of the current file into the clipboard. This is to help users to get full syntax names quickly (for use in the settings file).

### Requirements

- Sublime Text v2 or v3
- Tested with: v2 build 2221 and v3 build 3114

### Installation Instructions

#### Package Control

This package has been submitted to [Package Control](http://packagecontrol.io) and installation instructions will be added when the submission process has been completed.

#### Manual Installation

Download the [ZIP file](https://github.com/mattst/sublime-single-trailing-new-line/archive/master.zip) and extract it or use `git clone` to get the files from its [GitHub page](https://github.com/mattst/sublime-single-trailing-new-line). Then move the package's folder to your Sublime Text config `Packages` directory renaming it (for neatness) from `sublime-single-trailing-new-line-master` to `SingleTrailingNewLine` or to something else if you prefer. e.g. `Packages/SingleTrailingNewLine/`.

### Setup and Usage

This plugin has always been intended to be run automatically when a file is saved, rather than by manually running it from the command palette or with a key binding. However some users may prefer to run it manually on an as-needed basis, or to have that option available for syntaxes they have not added in the settings.

#### Command Palette

The package includes 2 command palette commands:

- `Single Trailing New Line` - ensure there is exactly one trailing newline at the end of the file. When run from the command palette the plugin will work with all files, the settings file will be ignored.

- `Copy Syntax Name` - copies the full syntax name of the current file into the clipboard. This is to help users to get full syntax names quickly (for use in the settings file).

#### Key Binding

When run from a key binding the plugin will work with all files, the settings file will be ignored.

Add the key binding of your choice to your user key bindings file (`Menu --> Preferences --> Key Bindings - User`):

    { "keys": ["ctrl+whatever"], "command": "single_trailing_new_line" }

There are now so many Sublime Text packages available that key conflicts are commonplace, it is therefore best for users to decide their own keys for small plugins like this one.

Not sure? You could try: `"ctrl+k", "ctrl+n"` (which is not in use on my system).

#### Running Automatically

The plugin will be run automatically every time a file is saved to ensure that the file is saved with exactly one trailing newline. This is disabled by default.

It can be enabled for either all files or for only files of specific syntaxes. To enable it the settings in the settings file `SingleTrailingNewLine.sublime-settings` must be changed.

If this package has been installed using *Package Control* then you will need to create a `SingleTrailingNewLine.sublime-settings` file typically in the `Packages/User/` folder. The easiest way to do this is to download the package's [default settings file](https://raw.githubusercontent.com/mattst/sublime-single-trailing-new-line/master/SingleTrailingNewLine.sublime-settings) from its [GitHub page](https://github.com/mattst/sublime-single-trailing-new-line).

There are 2 settings available:

- `enable_for_all` - *true/false*. If this is set to true the plugin will be active for all files, every time any file is saved the plugin will be run. If this is set to false the plugin will examine the `syntax_list` setting.

- `syntax_list` - *a list*. If syntax names are added to this list, the plugin will only be run when the syntax of the current file matches one of the syntaxes in `syntax_list`.

Note: The `.sublime-syntax` syntax file format was introduced by Sublime Text v3 build 3084, from that version onwards all built-in syntax files use that format; however `.tmLanguage` syntax files are still compatible and will be present if a syntax package that includes them has been installed, e.g. `PythonImproved`. Sublime Text v2 and v3 builds earlier than 3084 use `.tmLanguage` syntax files.

Here is an example `SingleTrailingNewLine.sublime-settings` file for Sublime Text v3 builds from 3084 onwards:

    {
        "enable_for_all": false,

        "syntax_list":
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

Here is an example `SingleTrailingNewLine.sublime-settings` file for Sublime Text v2 and v3 builds earlier than 3084:

    {
        "enable_for_all": false,

        "syntax_list":
        [
            "Packages/C++/C.tmLanguage",
            "Packages/C++/C++.tmLanguage",
            "Packages/Java/Java.tmLanguage",
            "Packages/JavaScript/JavaScript.tmLanguage",
            "Packages/Python/Python.tmLanguage",
            "Packages/Python Improved/PythonImproved.tmLanguage",
            "Packages/Rails/",
            "Packages/XML/XML.tmLanguage"
        ]
    }

The full syntax name of the current file's syntax can be copied into the clipboard by entering `Copy Syntax Name` in the command palette. It can also be retrieved by using the `view.settings().get("syntax")` command in the Sublime Text console.

The `syntax_list` entries are case sensitive and wildcards can not be used.

It is generally advisable to use the full syntax name in the `syntax_list` entries (as shown in the examples above) but partial syntax names are also acceptable, e.g. `"XML.sublime-syntax"`.

The following tips should be noted:

- Be careful: `"C.sublime-syntax"` would match both `"Packages/C++/C.sublime-syntax"` and `"Packages/Objective-C/Objective-C.sublime-syntax"`.

- All of the syntaxes in a package can be matched by using just the path. e.g. `"Packages/Rails/"` would match all 5 syntaxes from the `Rails` package, i.e. `"Packages/Rails/Ruby on Rails.sublime-syntax"` as well as the other 4.

- Using just `"Java"` would match all 7 syntaxes from the `Java` and `JavaScript` packages, as would `"Packages/Java"` but not `"Packages/Java/"` because the trailing forward slash would not match `"Packages/JavaScript/"`.

For reference use only, this package also includes 2 lists of Sublime Text built-in syntaxes:

- [Sublime Text v2 build 2221 syntax list](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/Sublime_Text_2221_Syntax_List)
- [Sublime Text v3 build 3114 syntax list](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/Sublime_Text_3114_Syntax_List)
- Those using Sublime Text v3 builds earlier than 3084 should use the v2 list.

### License

This plugin is licensed under The MIT License (MIT), see the [LICENSE file](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/LICENSE).
