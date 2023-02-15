# sublime-rubyfmt
[Sublime text](https://www.sublimetext.com) plugin to autoformat [Ruby](https://www.ruby-lang.org/en/) code with [Rubyfmt](https://github.com/samphippen/rubyfmt). If the file contains syntax errors it won't be formatted and the error is displayed in the Sublime status bar at the bottom of the editor window.

## Dependencies
A `ruby` and `rubyfmt` executable is assumed to be in path but this can be overriden with absolute paths in the package settings (`"ruby_executable"` and `"rubyfmt_executable"` respectively).

## Plugin installation

Through [Sublime Package Control](https://packagecontrol.io): Install Package -> Rubyfmt

## Formatting code

On Windows/Linux: `Alt + ;`
On MacOS: `Cmd + ;`

With a file open and syntax set to Ruby or Ruby on Rails, hit the above combination to apply auto format.

If your file contains syntax errors it won't be formatted. The syntax error will briefly flash in the Sublime Text status bar at the bottom of the editor window.

## Format on Save / Other settings

  * Format on save is enabled by default but can be disabled from `Sublime Text -> Preferences -> Package Settings -> Rubyfmt -> Settings - User` and adding `{"format_on_save: false"}`.
  * `rubyfmt_flags` can be added to use `--header-opt-in` or `--header-opt-out` behaviors.

All settings with default values:

```json
{
  "ruby_executable": "ruby",
  "rubyfmt_executable": "rubyfmt",
  "rubyfmt_flags": "",
  "format_on_save": true,
}
```

## Troubleshooting

If execution of Ruby/Rubyfmt fails, debug information will be printed to the Sublime Text console: View -> Show Console
