# Operating System Security Implementation

## Caesar Cipher Encryption System with User Authentication

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Use](#how-to-use)
5. [Security Features](#security-features)
6. [Complexity Analysis](#complexity-analysis)
7. [Algorithm Flowcharts](#algorithm-flowcharts)
8. [File Structure](#file-structure)
9. [Code Explanation](#code-explanation)
10. [Authors](#authors)

---

## 📖 Project Overview

This project implements a complete security system for an Operating System environment. It demonstrates fundamental OS security concepts including:

- **User Authentication** - Secure login with password hashing
- **Cryptography** - Caesar cipher encryption/decryption
- **File Protection** - Encrypted file storage and retrieval
- **Security Auditing** - Event logging for all security-related actions

This project was developed as a group assignment for the Operating Systems course, focusing on **Security Implementation** (Option 6) based on Chapter 8: Security and Protection.

### Course Topics Covered:
- Cryptography (Slide 12-13)
- Authentication (Slide 14)
- Access Control (Slide 10)
- Security Auditing
- File Protection

---

## ✅ Features

| # | Feature | Status | Description |
|---|---------|--------|-------------|
| 1 | Account creation with hashed passwords | ✅ Working | Users can create secure accounts with SHA-256 hashed passwords |
| 2 | Login with hidden password input | ✅ Working | Passwords are hidden during typing using getpass module |
| 3 | Caesar cipher encryption | ✅ Working | Encrypt text using customizable shift (1-25) |
| 4 | Caesar cipher decryption | ✅ Working | Decrypt text when shift key is known |
| 5 | Brute force decryption | ✅ Working | Try all 25 possible shifts automatically |
| 6 | Save encrypted messages to file | ✅ Working | Save with random shift keys and direction |
| 7 | Load and decrypt files | ✅ Working | Load previously saved encrypted files |
| 8 | Security audit log with timestamps | ✅ Working | Track all security events with datetime stamps |
| 9 | Change password functionality | ✅ Working | Users can update their passwords securely |
| 10 | User logout | ✅ Working | End session and return to login screen |

---

## 🛠️ Installation

### Prerequisites
- Python 3.x installed on your system
- No external libraries required (uses only built-in modules: os, random, datetime, hashlib, getpass)

### Setup Instructions

1. **Download the project files**

2. **Run the program**:
```bash
python security_system.py
```
3. **No additional setup required - The program creates necessary folders automatically**


## ▶ How to Use

Follow these steps after launching the program:

1. Create an account (first-time users) by choosing the "Create Account" option. Enter a username and a password. Passwords are hashed with SHA-256 before storage.
2. Log in with your username and password. Password input is hidden during typing.
3. After login you'll see a menu with options similar to:
	 - Encrypt message — enter plaintext and a shift key (1–25) to encrypt. The program returns ciphertext.
	 - Decrypt message — enter ciphertext and the shift key used to decrypt back to plaintext.
	 - Brute-force decrypt — automatically try all 25 shifts and show candidate plaintexts.
	 - Save encrypted message — save ciphertext to an encrypted file (randomized shift/direction metadata stored securely).
	 - Load & decrypt file — open a previously saved file and attempt to decrypt using stored metadata or manual key.
	 - Change password — update your account password (new password will be hashed).
	 - Logout — securely end your session.

4. All security-related actions (login, logout, file save/load, password change, failed login attempts) are recorded in the audit log with timestamps.

Tips:
- Keep your shift key secret when you want confidentiality. If you forget the exact key, use the brute-force option.
- When saving files, note the filename and any optional password prompts the program may request.

## 🔒 Security Features

- Password hashing: user passwords are never stored in plain text — SHA-256 hashing is used with a per-user salt if implemented in code.
- Hidden password input: the program uses secure hidden input for passwords (getpass) to avoid shoulder-surfing.
- Audit logging: every authentication attempt and file operation is logged with a timestamp for later review.
- Limited keyspace awareness: the Caesar cipher uses shifts of 1–25; brute-force is feasible but logged so attempts are auditable.
- File protection: encrypted messages are stored in the `Files/` directory; the program can optionally set restrictive file permissions when creating files (OS permitting).
- Least-privilege menu model: user actions are limited to the functions implemented, reducing accidental exposure.

## ⏱️ Complexity Analysis

- Encryption / decryption (single pass Caesar cipher): O(n) time where n is the length of the input string — the algorithm performs a constant-time character shift for each character. Space complexity is O(n) for the output string.
- Brute-force decryption: O(k * n) time where k = 25 (number of shifts) and n is message length. Since k is constant (25), this is effectively O(n) in practice.
- File I/O: reading or writing a file is O(m) where m is file size. Combined operations (encrypt + save) remain linear in input size.

## 🧭 Algorithm Flowcharts

This repository uses simple, linear algorithms; below are compact flow descriptions you can translate to flowcharts:

- Authentication flow:
	1. Prompt for username and password
	2. Lookup user record
	3. Hash entered password and compare with stored hash
	4. If match → grant access; else → log failure and retry/exit

- Encrypt flow:
	1. Receive plaintext and shift
	2. For each character, shift within alphabet preserving case; non-letter characters are left unchanged
	3. Output ciphertext and (optionally) save to file with metadata

- Brute-force flow:
	1. Receive ciphertext
	2. For shift = 1..25, apply reverse shift and collect candidate plaintext
	3. Present candidates to user for selection

If you want visual PNG/SVG flowcharts, add images to a `docs/` folder and reference them here (e.g., `docs/auth-flow.png`).

## 📁 File Structure

Project layout (top-level):

```
HelperCeasar.py      # helper functions for Caesar cipher (encrypt/decrypt/bruteforce)
Mock.py              # sample data or mock routines used during development
ReadMe.md            # this file
Security.py          # main security and authentication routines (user creation, login, audit logging)
Files/               # saved ciphertext files and sample inputs
		pa.txt
		vmHate.txt
```

Add any additional configuration or example files here. The program will create the `Files/` folder if it does not exist.

## 🧩 Code Explanation

High-level responsibilities by file/module:

- `Security.py` — handles user accounts, password hashing, login/logout flows, audit logging, and password changes. Functions include: create_account(), login(), change_password(), log_event().
- `HelperCeasar.py` — contains the Caesar cipher logic: encrypt(text, shift), decrypt(text, shift), brute_force(text). It handles letter wrapping and preserves case and non-letter characters.
- `Mock.py` — small utility or sample data used for demonstration or testing.
- `Files/` — directory used to store saved encrypted messages. File metadata includes the shift/direction (if stored) and a timestamp.

Code contract (simple):
- Inputs: user text (string), numeric shift (int 1–25), username/password strings, filenames for save/load.
- Outputs: ciphertext/plaintext strings, saved files on disk, audit log entries.
- Error modes: invalid username/password, invalid shift values, missing files — all are logged and produce a user-facing error message.

Edge cases handled:
- Empty input strings (returns empty output)
- Non-letter characters are preserved
- Shift values outside 1–25 are rejected with an instruction to provide a valid key

## ✍️ Authors

- kidus1001 — primary author (GitHub: `kidus1001`)

If this was a group assignment, add the other team members below in the same format (Name — role / contact). You can also include institution and course details.

---

If you'd like, I can also:
- Add small example screenshots showing the program menu
- Generate simple flowchart PNGs and add them under `docs/`
- Expand the `Code Explanation` with function-level docs pulled from the source files

