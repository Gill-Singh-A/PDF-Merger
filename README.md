# PDF Merger
Merges multiple PDF Files into a single PDF File

## Requirements
Language Used = Python3
Modules/Packges used:
* os
* sys
* datetime
* pypdf
* time
* colorama

## Input
It takes input through the command by which we run the python file.<br />
If we specify '*' then it will merge all the PDF Files present in the folder into a single PDF File. <br />
For example:
```bash
python pdf_merger.py *
```
Otherwise we have to specify the PDF File names present in the folder to merge into a single PDF File. <br />
For example:
```bash
python pdf_merger.py pdf_file_1 pdf_file_2 ...
```