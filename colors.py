# Styles
RESET = '\033[0m'
BOLD = '\033[1m'

# Foreground colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'

def cprint(*args, color=RESET):
    
    # Reset color to default, then add current color settings
    print(RESET, color, sep='', end='')
    
    # Print each argument to be printed in desired color
    for arg in args:
        print(arg)
    
    # Reset color to default when finished
    print(RESET, end='')