ble File  8 lines (8 sloc)  260 Bytes

#!/Users/manuelramos/Desktop/intro/scripts/store_backend/venv/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from autopep8 import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main()