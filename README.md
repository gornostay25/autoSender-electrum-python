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

## Usage

📋 Clone the repository:

   ```shell
   git clone https://github.com/gornostay25/wbl-1209958-electrum-python.git
   ```

💻 Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

🔧 Set up the MySQL database and configure the connection details in the `config.ini` file. Here's an example of the `config.ini` file contents:

   ```ini
   [mysql]
   host=<DB HOST>
   user=<DB USER>
   password=<DB PASS>
   database=<DB DATABASE>

   [settings]
   delay=600 # 10 min = 600 sec
   ```

🔩 Customize the script to match your specific use case, including the database schema and table structure.

▶️ Run the script:

   ```shell
   python main.py
   ```

⏰ The script will periodically check the database for transactions with the desired status. It will retrieve the wallet address and amount from the MySQL database and perform the corresponding transactions using the Electrum wallet.

## ✍️ Author

Volodymyr Palamar - gornostay25

GitHub: [gornostay25](https://github.com/gornostay25)

## License

📝 All rights reserved. This project is proprietary and the source code is confidential. Unauthorized use, distribution, or reproduction of this code or any portion of it is strictly prohibited.