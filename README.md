# War and Peace
+ Downloaded from [Project Gutenberg](https://www.gutenberg.org/ebooks/2600)

## Workflow
+ Manual cleaning; TOC, etc at the beginning of the book were deleted
by hand, copyright and other materials appended by Project
Gutenberg were deleted by hand

+ first run the scripts in src/textprocessing in the following order
: get_embeddings.py, cluster_sentences.py, network.py, backbone.py
, final_processing.py, vizdata.py

+ to generate the viz, run src/turtle/poc.py

## Notes
### Backbone filtering
Although it is not strictly necessary for this project, we employed backbone
filtering on the semantic similarity graph of the sentences. src
/textprocessing/disparity.py is based on [this repo](https://github.com/DerwenAI/disparity_filter) (with minor modifications).
### Dependecies
```bash
sudo apt install texlive-font-utils
sudo apt install pdf2svg
```
### Converting the saved eps to svg
```bash
epstopdf lines.eps lines.pdf
pdf2svg lines.pdf lines.svg
```

### Dotplot to svg
+ cut & enhance img in Shotwell
+ ```convert -negate dotplot.jpg dotplot_inverted.jpg``` if 
you need to reverse the colors
+ ```convert dotplot_inverted.jpg dotplot.svg```