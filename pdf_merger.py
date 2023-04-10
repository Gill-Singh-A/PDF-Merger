from os import listdir
from sys import argv
from datetime import date
from pypdf import PdfMerger
from time import strftime, localtime
from colorama import Fore, Back, Style

status_color = {
    '+': Fore.GREEN,
    '-': Fore.RED,
    '*': Fore.YELLOW,
    ':': Fore.CYAN,
    ' ': Fore.WHITE
}

def display(status, data):
    print(f"{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {strftime('%H:%M:%S', localtime())}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")

if __name__ == "__main__":
    if argv[2] == '*':
        pdf_files = listdir()
        pdf_files = [pdf_file for pdf_file in pdf_files if pdf_file.endswith(".pdf")]
    else:
        pdf_files = argv[2:]
    final_pdf = PdfMerger()
    for pdf_file in pdf_files:
        try:
            final_pdf.append(pdf_file)
            display('+', f"{Back.MAGENTA}{pdf_file}{Back.RESET} Merged")
        except:
            display('-', f"{Back.MAGENTA}{pdf_file}{Back.RESET} not found")
    final_pdf.write(argv[1])
    display('+', f"Saving final PDF File to {Back.MAGENTA}{argv[1]}{Back.RESET}")
    final_pdf.close()