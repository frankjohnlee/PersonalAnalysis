#!D:/Projects/PersonalAnalysis/venv\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'nose==1.3.7','console_scripts','nosetests-3.5'
__requires__ = 'nose==1.3.7'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('nose==1.3.7', 'console_scripts', 'nosetests-3.5')()
    )
