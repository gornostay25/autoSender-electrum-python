# Bitcoin Wallet Automation Script

> Electrum is a popular Bitcoin wallet that provides a command-line interface, API, and libraries for interacting with Bitcoin wallets. This project aims to develop an automated Python script for managing an Electrum Bitcoin wallet, specifically for sending bitcoins and retrieving the current wallet balance.

## Requirements

- Python programming language
- Interaction with the Electrum wallet using command-line interface, API, or libraries
- Ability to send bitcoins with a specified recipient address and amount
- Ability to retrieve the wallet balance
- Error handling for scenarios such as insufficient balance or incorrect data
- Well-documented code with comments for easy understanding and usage of the script
- Thorough testing on various usage scenarios to ensure correct functionality and stability
- Ensuring script security and secure storage of sensitive data, such as private keys

## 📋 Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/gornostay25/wbl-1209958-electrum-python.git
   ```

2. Create and activate a virtual environment:

   ```shell
   python -m venv .venv
   ```

   #### For Unix/Linux
   ```shell
   source .venv/bin/activate  
   ```

   #### For Windows
   ```shell
   .venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Run the installation script to install Electrum:

   ```shell
   python installElectrum.py
   ```

## 🚀 Usage

1. Set up the MySQL database and configure the connection details in the script.

2. Customize the script to match your specific use case, including the database schema and table structure.

3. Create a configuration file `config.ini` with the following contents:

   ```ini
   [mysql]
   host=<DB HOST>
   user=<DB USER>
   password=<DB PASS>
   database=<DB NAME>

   [settings]
   delay=600 # 10MIN = 600 SEC

   [electrum]
   password=<WALLET PASS>
   testnetwork=true
   ```

4. Run the script:

   ```shell
   python main.py
   ```

5. The script will periodically check the database for transactions with the desired status. It will retrieve the wallet address and amount from the MySQL database and perform the corresponding transactions using the Electrum wallet.

## ✍️ Author

Volodymyr Palamar - gornostay25

GitHub: [gornostay25](https://github.com/gornostay25)

## 📄 License

All rights reserved. This project is proprietary and the source code is confidential. Unauthorized use, distribution, or reproduction of this code or any portion of it is strictly prohibited.
