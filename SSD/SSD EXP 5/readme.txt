# Experiment 5 — Inputs & Outputs

### 1. ✅ Valid Input
```text
Name: Doorva
Email: doorva@gmail.com
Address: Panvel, Maharashtra
```
**Output:** `✅ All inputs are valid.`

### 2. ❌ Invalid Name
```text
Name: Doorva123
Email: doorva@gmail.com
Address: Panvel, Maharashtra
```
**Output:** `❌ Invalid Name: Name should contain only letters.`

### 3. ❌ Invalid Email
```text
Name: Doorva
Email: doorva
Address: Panvel, Maharashtra
```
**Output:** `❌ Invalid Email Address.`

### 4. ❌ Empty Address
```text
Name: Doorva
Email: doorva@gmail.com
Address:
```
**Output:** `❌ Invalid Address: Address cannot be empty.`

### 5. ❌ Short Address
```text
Name: Doorva
Email: doorva@gmail.com
Address: abc
```
**Output:** `❌ Invalid Address: Address is too short.`

### 6. 🔐 HTML Encoding
```text
Name: ssssss
Email: test@example.com
Address: <b>Panvel</b>
```
**Output:**
```text
Name: ssssss | Address: <b>Panvel</b>
```
➡️ Displayed as **text**, not bold.

### 7. 🔐 XSS Test
```text
Name: ssssss
Email: test@example.com
Address: <script>alert("XSS Test")</script>
```
**Output:** Script is displayed safely / **no alert executes**.