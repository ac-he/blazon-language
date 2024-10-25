<h1>Blazon Language</h1>
<h6>10/19/2024, 4:40 PM ~ Experimental Parser</h6>
I am currently building out the language in EBNF.
<h6>Dependencies</h6>
<ul>
<li>Pycairo</li>
<li>PIL (pillow)</li>
<li>TatSu</li>
</ul>
I'm also in Python 3.12. I started out in a lower version but 
something broke so keep that in mind if you try to set it up for 
yourself.
<h6>Generate Parser</h6>
    
    tatsu --outfile language/_parser.py --generate-parser language/blazon.ebnf