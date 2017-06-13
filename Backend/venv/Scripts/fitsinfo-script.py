#!D:/Projects/PersonalAnalysis/venv\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'astropy==1.2.1','console_scripts','fitsinfo'
__requires__ = 'astropy==1.2.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('astropy==1.2.1', 'console_scripts', 'fitsinfo')()
    )
