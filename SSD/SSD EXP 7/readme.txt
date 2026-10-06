
**Experiment 7: Secure Error Handling and Logging**

We made a small Python program that:

1. **Takes user input**
   - Number
   - Divisor

2. **Handles errors using `try-except`**
   - Prevents the program from crashing.

3. **Handles division by zero**
   - Instead of exposing a Python error, it shows:
   ```text
   Error: Invalid input or operation.
   ```

4. **Handles invalid input**
   - For example:
   ```text
   abc
   ```
   - Again, it gives a safe error message.

5. **Logs the actual error**
   - Errors are written to:
   ```text
   error.log
   ```

### Why is this "secure"?

We are preventing **information leakage**.

Instead of showing the user something technical like:

```text
ZeroDivisionError: float division by zero
```

we show:

```text
Error: Invalid input or operation.
```

But the technical error is still recorded in the log for the developer.

### Where CERT/MISRA comes in

This is the part I want you to explain carefully:

> **CERT and MISRA are secure/safety-oriented coding guidelines. They encourage practices such as proper error handling, avoiding unsafe behavior, and writing predictable, reliable code.**

We are **not implementing a special "CERT algorithm" or "MISRA algorithm."** We're applying secure coding principles consistent with those guidelines.

### So tomorrow:

**Normal input:**

```text
10
2
```

→ `Result: 5.0`

**Error input:**

```text
10
0
```

→ `Error: Invalid input or operation.`

**Then show `error.log`:**

```text
ERROR - Invalid operation: Division by zero
```

### One-line explanation for ma'am

> **"I implemented exception handling to prevent crashes, used generic error messages to avoid information leakage, and logged the actual errors for debugging and security monitoring, following secure coding principles from CERT/MISRA."**

That's **exactly what we did**.