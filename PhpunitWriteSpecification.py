import sublime, sublime_plugin

class PhpunitWriteSpecificationCommand(sublime_plugin.TextCommand):
    def run(self, edit, specification):
        method_name = specification.replace(' ', '_')

        method = """/** @test **/
    function %s()
    {
    }
""" % method_name

        self.view.insert(edit, self.view.sel()[0].begin(), method)
