"""Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used."""

import sys

if len(sys.argv) == 1:
    print(f"You are using: {sys.platform}")
else:
    print("No arguments needed. Just run the script without any.")
