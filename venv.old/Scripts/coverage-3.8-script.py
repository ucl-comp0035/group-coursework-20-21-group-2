#!"C:\Users\Paul\Documents\UCL\Year 3\COMP0035 Applied Software Engineering\Group Coursework\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'coverage==5.3.1','console_scripts','coverage-3.8'
__requires__ = 'coverage==5.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('coverage==5.3.1', 'console_scripts', 'coverage-3.8')()
    )
