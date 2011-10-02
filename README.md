# markdown2deckjs

Author: Ulf Bögeholz

Version: 0.1 | 2011/09/21

## What is this?

After I saw deck.js recently, I immediatelly liked the look and feel of it. What I did not like was to generate HTML slides by hand. I surfed around a bit and quickly found out that there was a nice markdown library for python. Playing around (and not sleeping instead) quickly showed results. Voila.

## Dependencies

* markdown
* jinja2
* elementtree

Install by using Pip: `pip install markdown jinja2`

## How to use

* Get a local copy of deck.js
* Write a markdown file with your presentation in it
* Compile the markdown file to a deck.js HTML file
* Enjoy the slides

### Play-by-play

    $ mkdir m2d
    $ cd m2d
    $ git clone https://github.com/imakewebthings/deck.js.git
    # Now setup your local webserver to serve the deck.js/introduction directory
    $ git clone https://github.com/ulf/markdown2deckjs.git
    $ cd markdown2deckjs
    $ ./m2d README.md templates/plain.html "Readme" > ../deck.js/introduction/readme.html
    # Look at the readme.html file in your browser. Done

## How do I create my slides?

Every time the markdown contains a H1 or H2 (#, ##), a new slide will be created in your presentation. Basically just write your text and mix in a heading if you need a new slide.

    # Title Slide
	
	## First Content Slide
	This is nice
	
	## Second Content Slide
	This too

will result in a three-slide presentation. Try it:
  
    $ m2d example1.md templates/plain.html "My Test" > ../deck.js/example1.html

	

## Seems like magic. How does it work?

The python markdown module offers a broad scope for writing extensions. I found a possibility to hook in an extension after the HTML element tree has already been generated from the markdown file. All I do is traverse the tree and make some minor adjustments in the element configuration. The altered HTML is then pasted into a plain deck.js template to generate the presentation.

## Differences to markdown

I added a little feature to make slides more interactive. If your text elements end with a tilde, the char is stripped and the element is instead given the `slide` class, which has the effect that the element will not be shown initially. Instead, you need to advance the slide to show the element. This seemed to be te easiest way to construct incremental slides.

## I want to extend this

Feel free! Just fork or get in touch if you like, there might be a lot of ways to make this better.

