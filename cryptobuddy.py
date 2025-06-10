# cryptobuddy.py (with CoinGecko API)
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("COINGECKO_API_KEY")

def fetch_crypto_data():
    """Fetch live crypto data from CoinGecko API"""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,cardano",
        "price_change_percentage": "24h",
        "x_cg_demo_api_key": API_KEY  # Free-tier key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ API Error: {e}")
        return None

def get_crypto_db():
    """Convert API data into our expected format"""
    api_data = fetch_crypto_data()
    if not api_data:
        print("Using fallback data (API failed).")
        return {
            "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3/10, "current_price": 50000},
            "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6/10, "current_price": 3000},
            "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8/10, "current_price": 1.5}
        }
    
    crypto_db = {}
    for coin in api_data:
        name = coin["name"]
        price_change = coin["price_change_percentage_24h"]
        
        # Determine price trend
        if price_change > 2:
            trend = "rising"
        elif price_change < -2:
            trend = "falling"
        else:
            trend = "stable"
        
        # (Note: Sustainability data isn't in the API, so we keep our manual scores)
        sustainability_scores = {
            "Bitcoin": 3/10,
            "Ethereum": 6/10,
            "Cardano": 8/10
        }
        
        energy_use = {
            "Bitcoin": "high",
            "Ethereum": "medium",
            "Cardano": "low"
        }
        
        crypto_db[name] = {
            "price_trend": trend,
            "market_cap": "high" if coin["market_cap"] > 10e10 else "medium",
            "energy_use": energy_use.get(name, "medium"),
            "sustainability_score": sustainability_scores.get(name, 5/10),
            "current_price": coin["current_price"]
        }
    
    return crypto_db

# The rest of your chatbot code remains the same!
# Just replace `crypto_db` with `get_crypto_db()` where needed.

def chatbot():
    crypto_db = get_crypto_db()  # Now fetches LIVE data!
    print(f"📡 Fetched real-time data for: {', '.join(crypto_db.keys())}")
    
    # ... (Rest of your existing chatbot function)

if __name__ == "__main__":
    chatbot()