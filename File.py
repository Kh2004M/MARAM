# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))