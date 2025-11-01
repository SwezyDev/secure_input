![standard (3)](https://github.com/SwezyDev/secure_input/assets/109398018/72249ff7-eb81-4dbf-b9d9-accf1b359e65)

<p align="center">
  <a href="https://pypi.org/project/secure-input/"><img src="https://img.shields.io/badge/PyPI-secure--input-orange?style=for-the-badge&logo=pypi" alt="PyPI"></a>
  <a href="https://www.python.org" target="_blank"><img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python" alt="Python"></a>
  <a href="https://t.me/swezy" target="_blank"><img src="https://img.shields.io/badge/Telegram-@Swezy-blue?style=for-the-badge&logo=telegram" alt="Telegram"/></a>
  <br>
  <a href="https://pypi.org/project/secure-input/"><img src="https://img.shields.io/badge/Version-1.0.3-green?style=for-the-badge&logo=pypi" alt="PyPI"></a>
  <br>
  <code>Leave a ⭐ if you like this repository</code>
</p>

---

## 🚩 What is `secure_input`?

`secure_input` is a tiny, dependency-free Python package that provides a secure, user-friendly way to prompt for sensitive input (like passwords) in terminal applications. It supports masking (e.g. `*`) and aims to be simple to use and easy to drop into any script.

---

## 🚀 Installation

Install from PyPI:

```bash
pip install secure-input
```

PyPI: [https://pypi.org/project/secure-input/](https://pypi.org/project/secure-input/)

---

## 🧩 Quick usage

```py
from secure_input import secure_input

password = secure_input("Enter your Password: ", show="*")
print("You entered:", password)
```

`secure_input(prompt: str, show: str) -> str`

* `prompt`: text shown to the user
* `show`: masking character (e.g. `"*"`)

---

## 📚 Features

* Easy Usage
* Optional masking character for input
* Cross-platform terminals supported

---

## ⚠️ Notes & Limitations

* Non-ASCII characters (e.g. `Ö Ä Ü ß`) may **not** be handled correctly — use plain ASCII letters, numbers and symbols for best results.
* Always validate and handle the secret data securely in your application (do not print or log real passwords in production).

---

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

---

## 📦 Where to get help

* Project on PyPI: [pypi.org/project/secure-input/](https://pypi.org/project/secure-input/)
* Telegram: [@Swezy](https://t.me/Swezy)

---

## 📝 License

Distributed under the **MIT License** — see `LICENSE` for details.

---

## 👤 Maintainer & Contact

* Maintainer: [@SwezyDev](https://github.com/SwezyDev)
* Telegram: [@Swezy](https://t.me/Swezy)

---

<p align="center">
  <sub>Made with ❤️ — If you find this useful, please leave a ⭐ on the repo</sub>
</p>

<a href="https://star-history.com/#SwezyDev/secure_input&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=SwezyDev/secure_input&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=SwezyDev/secure_input&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=SwezyDev/secure_input&type=Date" />
  </picture>
</a>

