import os, platform

try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from RDX64 import intro
    intro()
elif bit == '32bit':
    print(f"     {purple}╓═════{purple}════{yellow}─────────────────{purple}════{purple}════════╖{white}")
    print(f"     {yellow}│{white}【{green}✘{white}】{yellow} DEVICE DOESNT SUPPORT THIS TOOL {yellow}│")
    print(f"     {purple}╙{purple}═════════{yellow}─────────────────{purple}════════════{purple}╜{white}")