import sublime
import sublime_plugin

def swap_slashes(str):
    split_on_bs = str.split("\\")

    rejoin_w_fs = []
    for _ in split_on_bs:
        rejoin_w_fs.append(_.replace("/", "\\"))

    return("/".join(rejoin_w_fs))

class ToggleSlashesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Go through all the regions that might be selected
        for selection in self.view.sel():
            if (selection.empty()):
                # An empty selection region means we have a single cursor on a line.
                line = self.view.line(selection)

                # Line contents
                contents = self.view.substr(line)

                # Replace with slash-swapped contents
                self.view.replace(edit, line, swap_slashes(contents))
            else:
                # Region contents
                contents = self.view.substr(selection)

                # Replace with slash-swapped contents
                self.view.replace(edit, selection, swap_slashes(contents))
