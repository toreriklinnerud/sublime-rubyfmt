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

Ruby and rubyfmt must already be installed and in your path:

```shell
$ which {ruby,rubyfmt}
/Users/tel/.rbenv/shims/ruby
/Users/tel/bin//rubyfmt
```

## Formatting code

On MacOS: `cmd+;`

With a file open, hit ```cmd + ;``` and your code will be formatted.

If your file contains syntax errors it won't be formatted. The syntax error will breiefly flash in the Sublime Text status bar at the bottom of the editor window.

## Troubleshooting

If execution of Ruby/Rubyfmt fails, debug information will be printed to the Sublime Text console: View -> Show Console
