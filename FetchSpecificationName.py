import sublime, sublime_plugin

class FetchSpecificationNameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel("Test Name:", 'it ', self.on_finish, None, None)

    def on_finish(self, specification):
        method_name = specification.replace(' ', '_')

        self.view.window().run_command("write_specification", { "specification": method_name })
