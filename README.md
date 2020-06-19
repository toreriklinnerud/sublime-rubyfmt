# sublime-rubyfmt
[Sublime text](https://www.sublimetext.com) plugin to autoformat [Ruby](https://www.ruby-lang.org/en/) code with [Rubyfmt](https://github.com/samphippen/rubyfmt). If the file contains syntax errors it won't be formatted and the error is displayed in the Sublime status bar at the bottom of the editor window.

## Dependencies
The correct `ruby` and `rubyfmt` executables are assumed to be in path but this can be overriden with absolute paths in the package settings (`"ruby_executable"` and `"rubyfmt_executable"` respectively).

## Plugin installation

Through [Sublime Package Control](https://packagecontrol.io):
```
Tools ->
   Command Palette ->
     type: Install Package (enter)
     type: rubyfmt (enter)
```

or manually:

Download [Rubyfmt.sublime-package](https://github.com/toreriklinnerud/sublime-rubyfmt/releases/download/v0.1.0/Rubyfmt.sublime-package) and place in `Installed Packages` (not `Packages`). See [Sublime Packages docs](https://www.sublimetext.com/docs/3/packages.html).

## Formatting code

On Windows/Linux: `Alt + ;`
On MacOS: `Cmd + ;`

With a file open and syntax set to Ruby or Ruby on Rails, hit the above combination to apply auto format.

If your file contains syntax errors it won't be formatted. The syntax error will briefly flash in the Sublime Text status bar at the bottom of the editor window.

## Format on Save / Other settings

Format on save is disabled by default but can be enabled from `Sublime Text -> Preferences -> Package Settings -> Rubyfmt -> Settings - User` and adding `{"format_on_save: true"}`.

See other settings available under `Settings - Default`.

## Troubleshooting

If execution of Ruby/Rubyfmt fails, debug information will be printed to the Sublime Text console: View -> Show Console
