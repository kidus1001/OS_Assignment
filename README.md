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
7. [File Structure](#file-structure)
8. [Authors](#authors)

---

## 📖 Project Overview

This project implements a complete security system for an Operating System environment. It demonstrates fundamental OS security concepts including:

- **User Authentication** - Secure login with password hashing
- **Cryptography** - Caesar cipher encryption/decryption
- **File Protection** - Encrypted file storage and retrieval
- **Security Auditing** - Event logging for all security-related actions

This project was developed as a group assignment for the Operating Systems course, focusing on **Security Implementation**.

---

## ✅ Features

| # | Feature | Status |
|---|---------|--------|
| 1 | Account creation with hashed passwords | ✅ Working |
| 2 | Login with hidden password input | ✅ Working |
| 3 | Caesar cipher encryption | ✅ Working |
| 4 | Caesar cipher decryption | ✅ Working |
| 5 | Brute force decryption (all 25 shifts) | ✅ Working |
| 6 | Save encrypted messages to file with random keys | ✅ Working |
| 7 | Load and decrypt files from storage | ✅ Working |
| 8 | Security audit log with timestamps | ✅ Working |
| 9 | Change password functionality | ✅ Working |
| 10 | User logout | ✅ Working |

---

## 🛠️ Installation

### Prerequisites
- Python 3.x installed on your system
- No external libraries required (uses only built-in modules)

### Setup Instructions

1. **Clone or download** the project files

2. **Run the program**:
```bash
python security_system.py