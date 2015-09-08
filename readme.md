# PHPUnit Create Specifications

<img src="http://d.pr/i/eYSZ+" alt="Screencast" width="400" />

When testing via PHPUnit or PHPSpec, some of us actually prefer snake case since it's a tad bit more readable. Then just annotate the method with `@test`.

    function testItDoesSomethingSomewhere()
    {
    }

    /** @test **/
    function it_does_something_somewhere()
    {
    }

## Nutshell

You type the spec with spaces (since it's hard to type a spec when using underscores versus spaces) and it generates the method for you.
