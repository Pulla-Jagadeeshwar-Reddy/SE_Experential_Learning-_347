# Issues found

| Issue | Type | Line(s) in original file | Description | Fix Approach |
|---|---|---:|---|---|
| Shell execution in backup | Security, high | 61 | A folder value was concatenated into a command run with `shell=True`. | Replaced shell execution with `pathlib.Path` and `shutil.copy2`. |
| Weak MD5 digest | Security, high | 39 | MD5 was used to generate job card IDs. | Replaced it with SHA-256. |
| Mutable default argument | Bug, medium | 12 | Calls that omitted `history` shared the same list. | Defaulted to `None` and created a new list inside the function. |
| Broad exception handling | Reliability, medium | 23 | `except Exception` could hide unrelated errors. | Used `.get()` and handled a missing vehicle record directly. |
| Hard-coded password | Security, low | 8 | An unused credential-like value was stored in source code. | Removed the unused constant. |
| Naming and documentation issues | Style, low | Throughout | CamelCase names and missing docstrings reduced readability. | Renamed functions and added docstrings. |
| Formatting issues | Style, low | 7, 43, 49, 77 | Flake8 reported spacing, blank-line, and line-length problems. | Corrected whitespace and wrapped the long print call. |