# sublime-rubyfmt
[Sublime text](https://www.sublimetext.com) plugin to autoformat [Ruby](https://www.ruby-lang.org/en/) code with [Rubyfmt](https://github.com/samphippen/rubyfmt)

## Installation
By Sublime package control (recommended):
```
Tools ->
   Command Palette ->
     type: Install Package (enter)
     type: rubyfmt (enter)
```

`ruby` and `rubyfmt` must already be installed and in your path:

```shell
$ which {ruby,rubyfmt}
/Users/tel/.rbenv/shims/ruby
/Users/tel/bin/rubyfmt
```

## Formatting code

On Windows/Linux: `Ctrl + ;`
On MacOS: `Cmd + ;`

With a file open and syntax set to Ruby or Ruby on Rails, hit the above combination to apply auto format.

If your file contains syntax errors it won't be formatted. The syntax error will briefly flash in the Sublime Text status bar at the bottom of the editor window.

## Format on Save / Other settings

Format on save is disabled by default but can be enabled from `Sublime Text -> Preferences -> Package Settings -> Rubyfmt -> Settings - User` and adding `{"format_on_save: true"}`.

See other settings available under `Settings - Default`.

## Troubleshooting

If execution of Ruby/Rubyfmt fails, debug information will be printed to the Sublime Text console: View -> Show Console
