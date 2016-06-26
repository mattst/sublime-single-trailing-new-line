
## Single Trailing New Line - Plugin for Sublime Text

This Sublime Text plugin makes sure that there is exactly one trailing newline at the end of a file. It works by deleting all the whitespace and newlines at the end of the file and then inserting a single newline.

The plugin can be run in various ways:

- The plugin can be set to run automatically every time a file is saved. This is disabled by default but by changing the settings it can be enabled either for all files or for only files of specific syntaxes.

- The plugin can be used by assigning it to a key binding or by using its command palette entry. In both these cases the settings file is ignored and the plugin will work with all files.

### Requirements

- Sublime Text v2 or v3
- Tested with: v2 build 2221 and v3 build 3114

### Installation Instructions

#### Package Control

This package has been submitted to [Package Control](http://packagecontrol.io) and installation instructions will be added when the submission process has been completed.

#### Manual Installation

Download the [ZIP file](https://github.com/mattst/sublime-single-trailing-new-line/archive/master.zip) and extract it or use `git clone` to get the files from its [GitHub page](https://github.com/mattst/sublime-single-trailing-new-line). Then move the package's folder to your Sublime Text config `Packages` directory renaming it to `SingleTrailingNewLine` or to something else if you prefer.

### Setup and Usage

#### Key Binding

When run from a key binding the plugin will work with all files, the settings file will be ignored.

Add the key binding of your choice to your user key bindings file (`Menu --> Preferences --> Key Bindings - User`):

    { "keys": ["ctrl+whatever"], "command": "single_trailing_new_line" }

There are now so many Sublime Text packages available that key conflicts are commonplace, it is therefore best for users to decide their own keys for small plugins like this one.

Not sure? You could try: `"ctrl+k", "ctrl+n"` (which is not in use on my system).

#### Command Palette

When run from the command palette the plugin will work with all files, the settings file will be ignored.

The `Single Trailing New Line` command palette entry will be available if either of the installation instructions have been followed. 

#### Running Automatically

This plugin has always been intended to be run automatically when a file is saved, rather than by manually launching it with a key binding or from the command palette.

It can be enabled for either all files or for only files of specific syntaxes.

To enable it the settings in the settings file `SingleTrailingNewLine.sublime-settings` must be changed since running automatically is disabled by default.

If this package has been installed using *Package Control* then you will need to create a `SingleTrailingNewLine.sublime-settings` file typically in the `Packages/User/` folder. The easiest way to do this is to download the package's [default settings file](https://raw.githubusercontent.com/mattst/sublime-single-trailing-new-line/master/SingleTrailingNewLine.sublime-settings) from its [GitHub page](https://github.com/mattst/sublime-single-trailing-new-line).

There are 2 settings available:

- `enable_for_all` - *true/false*. If this is set to true the plugin will be active for all files, every time any file is saved the plugin will be run. If this is set to false the plugin will examine the `syntax_list` setting.

- `syntax_list` - *a list*. If syntax names are added to this list, the plugin will only be run when the syntax of the current file matches one of the syntaxes in the `syntax_list`.

Here is an example Sublime Text v3 `SingleTrailingNewLine.sublime-settings` file:

*Note: Sublime Text v3 can use ".sublime-syntax" and ".tmLanguage" syntax files; the latter will only be available if a syntax package that includes them has been installed. e.g. `PythonImproved` below.*

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

Here is an example Sublime Text v2 `SingleTrailingNewLine.sublime-settings` file:

*Note: Sublime Text v2 can only use ".tmLanguage" syntax files.*

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

To get the full syntax name of the current file's syntax simply enter the following command in the Sublime Text console:

     view.settings().get("syntax")

For reference use only, this package also includes a full list of the syntaxes available by default in Sublime Text [version 2](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/Sublime_Text_2221_Syntax_List) and [version 3](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/Sublime_Text_3114_Syntax_List).

The `syntax_list` entries are case sensitive and wildcards can not be used.

It is generally advisable to use the full syntax name in the `syntax_list` entries (as shown in the examples above) but partial syntax names are also acceptable, e.g. `"XML.sublime-syntax"`. 

The following should be noted:

- Be careful: `"C.sublime-syntax"` would match both `"Packages/C++/C.sublime-syntax"` and `"Packages/Objective-C/Objective-C.sublime-syntax"`.

- All of the syntaxes in a package can be matched by using just the path. e.g. `"Packages/Rails/"` would match all 5 syntaxes from the `Rails` package, i.e. `"Packages/Rails/Ruby on Rails.sublime-syntax"` as well as the other 4.

- Using just `"Java"` would match all 7 syntaxes from the `Java` and `JavaScript` packages, as would `"Packages/Java"` but not `"Packages/Java/"` because the trailing forward slash would not match `"Packages/JavaScript/"`.

### License

This plugin is licensed under The MIT License (MIT), see the [LICENSE file](https://github.com/mattst/sublime-single-trailing-new-line/blob/master/LICENSE).
