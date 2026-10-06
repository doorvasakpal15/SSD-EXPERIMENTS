EXP 6

TEST 1 - LOGIN SUCCESSFULL
Username:
admin

Password:
admin123

OUTPUT:

Login successful.

TEST 2 — WRONG PASSWORD
Username:
admin

Password:
wrong

OUTPUT:

Invalid username or password.

TEST 3 — SQL INJECTION ATTEMPT

Username:
' OR '1'='1

Password:
anything

OUTPUT:

 SQL INJECTION ATTEMPT DETECTED!

 Malicious input detected and blocked.

B) BUFFER OVERFLOW PROTECTION
====================================================

1. Open terminal in SSD EXP 6.

2. Compile:

   gcc safe_buffer.c -o safe_buffer.exe

3. Run:

   .\safe_buffer.exe

TEST 1 — NORMAL INPUT

Input:

Doorva

OUTPUT:

Safe input: Doorva


TEST 2 — EXCESSIVELY LONG INPUT

Run again:

.\safe_buffer.exe

Input:

ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789

OUTPUT:

BUFFER OVERFLOW ATTEMPT DETECTED!
Input exceeded the maximum buffer size.
Excess input was safely limited.

