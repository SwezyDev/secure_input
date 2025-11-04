## 🧪 Examples

A short interactive example:

```py
from secure_input import secure_input

api_key = secure_input("API Key: ", show="*")
if len(api_key) == 0:
    print("No key provided")
else:
    print("Key received (length):", len(api_key))
```