# Flask Stack Simulator startup template

This is the unfinished repository for a pre-demo reading activity. Read `Flask_PreDemo_Reading_Activity.pdf` first. 

## Student Information

- **Name:** Panoringan, Mike Edrian M.
- **Section:** BSIT-WMT 4-2
- **Original starter repository:** https://github.com/Jackson-Soriano/f1-elec4-stack-simulator-starter.git

## Activity Description

This repository contains my copy of the Flask Stack Simulator for the ELEC 4 Week 11: Pre-Demo Reading Activity. It demonstrates how a stack works using the Last In, First Out (LIFO) principle, where the last item added is the first to be removed. The simulator allows users to add items using Push, remove the top item using Pop, view the top item using Peek, and remove all items using Clear.

The repository also contains a Flask Queue Simulator that follows the First In, First Out (FIFO) principle. Users add items at the rear using Enqueue, remove the front item using Dequeue, view the front item using Peek, and remove all items using Clear.

## Projects

- **Stack Simulator (LIFO):** the Flask app in the root folder. Run `python app.py` and open http://127.0.0.1:5000
- **Queue Simulator (FIFO):** the Flask app in the `queue-simulator` folder. Run `python app.py` inside that folder and open http://127.0.0.1:5001

## Before the demonstration

1. Clone the repository URL supplied by your instructor.
2. Open the cloned folder in VS Code.
3. Open `templates/index.html` directly in a browser. This is a static preview.
4. Click through the navigation to the contact placeholder.
5. Read the HTML comments, app.py TODOs, and stack_model.py TODOs.
6. Answer the reading worksheet. Do not complete the TODOs before the demonstration.

## Files

- app.py: Flask setup and route TODOs P1-P9.
- stack_model.py: Stack method.
- templates/index.html: standalone static simulator preview.
- templates/contact.html: standalone placeholder page.
- templates/base.html: standalone layout reference; inheritance is not active yet.
- static/css/style.css: supplied appearance adapted for this preview.
- static/js/ui.js: optional focus enhancement and a later effect TODO.
- requirements.txt: Flask dependency only.

During the demo, the instructor will convert static paths into url_for calls, connect form submission, introduce Jinja variables and loops, and connect Python stack operations. The three HTML files are intentionally independent before that conversion.