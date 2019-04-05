import sublime
import sublime_plugin

import os.path
import subprocess

class FormatCodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        syntax = self.view.settings().get('syntax').lower()
        if 'ruby' in syntax:
            self.format_view(edit)

    def format_view(self, edit):
        region = sublime.Region(0, self.view.size())
        unformatted_bytes = self.view.substr(region)

        formatted_bytes = FormatCodeCommand.format_bytes(unformatted_bytes)

        if formatted_bytes:
            if unformatted_bytes != formatted_bytes:
                self.view.replace(edit, region, formatted_bytes)
        else:
            syntax_error = FormatCodeCommand.check_syntax(unformatted_bytes)
            if(syntax_error):
                window = self.view.window()
                window.set_status_bar_visible(True)
                window.status_message(syntax_error)

    @staticmethod
    def check_syntax(bytes):
        command = ["ruby", "-c"]

        formatter = subprocess.Popen(command,
          stdin=subprocess.PIPE,
          stderr=subprocess.PIPE)

        _, stderr = formatter.communicate(bytes.encode())

        if formatter.returncode != 0:
            return stderr.decode()

    @staticmethod
    def format_bytes(bytes):
        command = ["rubyfmt"]

        formatter = subprocess.Popen(command,
          stdout=subprocess.PIPE,
          stdin=subprocess.PIPE,
          stderr=subprocess.PIPE)

        formatted, stderr = formatter.communicate(bytes.encode())

        if formatter.returncode == 0:
            return formatted.decode()
        else:
            syntax_error = FormatCodeCommand.check_syntax(bytes)
            if not syntax_error:
                print("Rubyfmt failed:")
                print(stderr.decode())


