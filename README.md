<h1>Blazon Language</h1>

<h2>Dependencies</h2>
<ul>
<li>Python 3.12</li>
<li>Pycairo</li>
<li>PIL (pillow)</li>
<li>TatSu</li>
<li>Click</li>
</ul>

<h2>Documentation</h2>
<a href="https://ac-he.github.io/blazon-docs">Found here</a>

<h2>Run your programs</h2>
<h3>Run</h3>
To run file.blzn as a program and generate images in this directory. The default settings will be used.

    blazon run <file.blzn>
<h4>Options</h4>
Change output directory (for images and pseudocode)
    
    --output-destination <directory>
    -o <directory>

Change output configuration file (controls graphics settings, etc.)
    
    --output-config <file.json>
    -c <file.json>

Generate pseudocode

    --pseudocode

DO NOT generate images
    
    --no-images

DO NOT generate program

    --no-program
<h3>Debug</h3>
To debug file.blzn:

    blazon run <file.blzn>
This will show the pseudocode before every instruction is carried out and 
display the states of all variables after each instruction is carried out.
<h4>Options</h4>
Step-through mode (prompts for import before moving to the next step)
    
    --step-thru
    -s

<h2>Other Notes</h2>
<h6>Make the lock file (you might need to do this)</h6>

    poetry install

<h6>Make package (you probably won't need to do this)</h6>

    poetry build

<h6>Regenerate Parser (you shouldn't need to do this)</h6>

    tatsu --outfile blazon_language/language/_parser.py --generate-parser blazon_language/language/blazon.ebnf
