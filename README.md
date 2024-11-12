# SecureAuth


A secure authentication system implementing industry-standard encryption and security practices for user authentication and data protection.

![Security Badge](https://img.shields.io/badge/security-enhanced-blue)
![Python Version](https://img.shields.io/badge/python-3.x-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## Features

- **Secure Password Storage**: Implements salted password hashing using PBKDF2
- **Symmetric Encryption**: Secures sensitive user data using AES-256
- **Data Integrity**: Uses HMAC for verifying data authenticity
- **Database Security**: Prepared statements to prevent SQL injection
- **Session Management**: Secure token-based authentication

## Quick Start

1. **Prerequisites**
   ```bash
   # Python 3.x required
   python --version
   ```

2. **Installation**
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/SecureAuth.git
   cd SecureAuth

   # Create and activate virtual environment
   python -m venv SecureAuth
   source SecureAuth/bin/activate  # On Windows: SecureAuth\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Database Setup**
   - Configure MySQL (via XAMPP or standalone)
   - Update database credentials in `main.py`
   - Run the provided SQL scripts to create necessary tables

4. **Run the Application**
   ```bash
   python main.py
   ```

## Documentation

For detailed setup instructions and configuration options, see:
- [Setup Guide](setup/setup.md)
- [flowchart](setup/flowchart.md)
- [pseudocode](setup/pseudocode.md)

## Security Features

- **Password Protection**
  - PBKDF2 with SHA-256
  - Unique salt per user
  - High iteration count for enhanced security

- **Data Encryption**
  - AES-256 in CBC mode
  - Secure key generation
  - Protected key storage

- **Integrity Verification**
  - HMAC-SHA256 for data authentication
  - Protected against tampering

## Project Structure

```
SecureAuth/
├── main.py              
├── config/
│   └── settings.py      
├── Models/
│   ├── user.py    
|
|___Utils/
|    |___encryption.py
|    |
|
|    
├── database/
│   └── models.py       
└── Setup
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
mail : thompsonrejen@yahoo.com

Project Link: [https://github.com/thompson005/SecureAuth](https://github.com/thompson005/SecureAuth)

## Acknowledgments

- [Python Cryptography](https://cryptography.io/)
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [PBKDF2 Documentation](https://en.wikipedia.org/wiki/PBKDF2)
- [Youtube Video](https://www.youtube.com/watch?v=NuyzuNBFWxQ)




