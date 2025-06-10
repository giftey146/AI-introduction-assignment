CryptoBuddy is a rule-based chatbot that provides cryptocurrency investment advice based on:
-Profitability (real-time price trends & market cap)
-Sustainability (energy efficiency & project viability)

It fetches live crypto data from the CoinGecko API and gives personalized recommendations.

Features
Real-time price analysis (Bitcoin, Ethereum, Cardano & more)

Investment advice based on trends & sustainability

Simple CLI interface (easy to use)

Fallback data (works offline if API fails)

Setup & Installation
1. Clone the Repository
bash
git clone https://github.com/yourusername/cryptobuddy.git
cd cryptobuddy
2. Install Dependencies
bash
pip install requests python-dotenv
3. Get a Free CoinGecko API Key
Sign up at CoinGecko API

Create a .env file in the project folder:

plaintext
COINGECKO_API_KEY=your_api_key_here
(Never share this key publicly!)

4. Run the Chatbot
bash
python cryptobuddy.py
How It Works
Fetches live crypto prices from CoinGecko

Analyzes trends (rising/falling prices)

Recommends investments based on:

-Profitability (market cap & price trends)

-Sustainability (energy efficiency scores)

Example Queries You Can Try:
"Which crypto is trending up?"

"What’s the most sustainable coin?"

"Should I buy Bitcoin?"

Project Structure
text
cryptobuddy/
├── cryptobuddy.py   # Main chatbot script
├── .env             # Stores API key (SECRET!)
├── README.md        # This file
└── requirements.txt # Python dependencies
Future Improvements
Add more cryptocurrencies (Solana, Polkadot, etc.)

Graphical price charts (using matplotlib)

Telegram/Discord bot integration

Disclaimer
This is not financial advice. Always DYOR (Do Your Own Research) before investing.

License
This project is licensed under MIT License.

Contribute
Found a bug? Want a new feature? Open an Issue or PR!

Star this repo if you found it useful!



