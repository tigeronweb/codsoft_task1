import re
import tkinter as tk
from tkinter import scrolledtext

def start_response():
    return "Hello! I'm your friendly chatbot. Ask me anything or tell me how I can assist you today."
def simple_chatbot(user_input):
    # The chatbot logic remains the same as provided earlier
    pass
def get_leader_info(country):
    
    leaders = {
        "United States": {"President": "Joe Biden", "Prime Minister": None},
        "United Kingdom": {"President": None, "Prime Minister": "Boris Johnson"},
        "France": {"President": "Emmanuel Macron", "Prime Minister": None},
        "Germany": {"President": "Frank-Walter Steinmeier", "Prime Minister": "Angela Merkel"},
        "India": {"President": "Droupadi Murmu", "Prime Minister": "Narendra Modi"},
        "Canada": {"President": None, "Prime Minister": "Justin Trudeau"},
        "Australia": {"President": None, "Prime Minister": "Scott Morrison"},
        "Brazil": {"President": "Jair Bolsonaro","Prime Minister": None},
        "South Africa": {"President": "Cyril Ramaphosa","Prime Minister": None},
        "Mexico": {"President": "Andrés Manuel López Obrador","Prime Minister": None},
        "Italy": {"President": None,"Prime Minister": "Mario Draghi"},
        "South Korea": {"President": "Moon Jae-in","Prime Minister": None},
        "Turkey": {"President": "Recep Tayyip Erdoğan","Prime Minister": None},
        "Saudi Arabia": {"King Salman bin Abdulaziz Al Saud"},
        "Israel": {"President": "Isaac Herzog","Prime Minister": "Naftali Bennett"},
        "Argentina": {"President": "Alberto Fernández","Prime Minister": None},
        "Nigeria": {"President": "Muhammadu Buhari","Prime Minister": None},
        "Denmark": {"President": None,"Prime Minister": "Mette Frederiksen"},
        "Portugal": {"President": None,"Prime Minister": "António Costa"},
        "Switzerland": {"President": "Guy Parmelin","Prime Minister": None},
        "Singapore": {"Prime Minister": "Lee Hsien Loong"},
        "Chile": {"President": "Sebastián Piñera","Prime Minister": None},
        "Colombia": {"President": "Iván Duque Márquez","Prime Minister": None},
        "Peru": {"President Pedro": "Castillo","Prime Minister": None},
        "Venezuela": {"President": "Nicolás Maduro","Prime Minister": None},
        "Iraq": {"President": None,"Prime Minister": "Mustafa Al-Kadhimi"},
        "Kenya": {"President": "Uhuru Kenyatta","Prime Minister": None},
        "Ethiopia": {"President": None,"Prime Minister": "Abiy Ahmed"},
        "Uganda": {"President": "Yoweri Museveni","Prime Minister": None},
        "Sudan": {"President": None,"Prime Minister": "Abdalla Hamdok"},
        "Algeria": {"President": "Abdelmadjid Tebboune","Prime Minister": None},
        "Angola": {"President": "João Lourenço","Prime Minister": None},
        "Azerbaijan": {"President": "Ilham Aliyev","Prime Minister": None},
        "Ireland": {"President": None,"Taoiseach (Prime Minister)": "Micheál Martin"},
        "New Zealand": {"President": None,"Prime Minister": "Jacinda Ardern"},
        "Romania": {"President": "Klaus Iohannis","Prime Minister": None},
        "Czech Republic": {"Prime Minister": "Andrej Babiš"},
        "Austria": {"Chancellor": "Karl Nehammer","Prime Minister": None},
        "Finland": {"President": None,"Prime Minister": "Sanna Marin"},
        "Croatia": {"President": None,"Prime Minister": "Andrej Plenković"},
    }

    return leaders.get(country, {"President": "Unknown", "Prime Minister": "Unknown"})
def get_country_capital(country):
    
    capitals = {
        "United States": "Washington, D.C.",
        "United Kingdom": "London",
        "India": "Delhi",
        "France": "Paris",
        "Philippines": "Manila",
        "Morocco": "Rabat",
        "Venezuela": "Caracas",
        "Algeria": "Algiers",
        "Iraq": "Baghdad",
        "Afghanistan": "Kabul",
        "Saudi Arabia": "Riyadh",
        "Jordan": "Amman",
        "Lebanon": "Beirut",
        "Cuba": "Havana",
        "Ecuador": "Quito",
        "Ghana": "Accra",
        "Sudan": "Khartoum",
        "Angola": "Luanda",
        "Sri Lanka": "Colombo",
        "Tunisia": "Tunis",
        "Bolivia": "Sucre (constitutional), La Paz (seat of government)",
        "Uzbekistan": "Tashkent",
        "Cameroon": "Yaoundé",
        "Mozambique": "Maputo",
        "Uruguay": "Montevideo",
        "Nepal": "Kathmandu",
        "Paraguay": "Asunción",
        "Zambia": "Lusaka",
        "Somalia": "Mogadishu",
        "Luxembourg": "Luxembourg City",
        "Belarus": "Minsk",
        "Gabon": "Libreville",
        "Malta": "Valletta",
        "Brunei": "Bandar Seri Begawan",
        "Maldives": "Malé",
        "Suriname": "Paramaribo",
        "Eswatini": "Mbabane (administrative), Lobamba (royal and legislative)",
        "Belize": "Belmopan",
        "Lesotho": "Maseru",
        "Equatorial Guinea": "Malabo",
        "Guinea-Bissau": "Bissau",
        "Tajikistan": "Dushanbe",
        "Cyprus": "Nicosia",
        "Trinidad  Tobago": "Port of Spain",
        "Guyana": "Georgetown",
        "Benin": "Porto-Novo (official), Cotonou (economic)",
        "Andorra": "Andorra la Vella",
        "Solomon Islands": "Honiara",
        "Comoros": "Moroni",
        "Micronesia": "Palikir",
        "São Tomé  Príncipe": "São Tomé",
        "Vanuatu": "Port Vila",
        "Sierra Leone": "Freetown",
        "Togo": "Lome",
        "Central African Republic": "Bangui",
        "Burundi": "Bujumbura",
        "Timor Leste": "Dili",
        "Chad": "NDjamena",
        "Seychelles": "Victoria",
        "Mauritius": "Port Louis",
        "Malawi": "Lilongwe",
        
    }
    return capitals.get(country, "Unknown")

def get_country_currency(country):
    
    currencies = {
        "United States": "US Dollar (USD)",
        "United Kingdom": "British Pound (GBP)",
        "France": "Euro",
        "Japan": "Japanese Yen (JPY)",
        "China": "Chinese Yuan Renminbi (CNY)",
        "Russia": "Russian Ruble (RUB)",
        "India": "Indian Rupee (INR)",
        "Brazil": "Brazilian Real (BRL)",
        "South Africa": "South African Rand (ZAR)",
        "Mexico": "Mexican Peso (MXN)",
        "Switzerland": "Swiss Franc (CHF)",
        "New Zealand": "New Zealand Dollar (NZD)",
        "Sweden": "Swedish Krona (SEK)",
        "Norway": "Norwegian Krone (NOK)",
        "Denmark": "Danish Krone (DKK)",
        "Singapore": "Singapore Dollar (SGD)",
        "Hong Kong": "Hong Kong Dollar (HKD)",
        "South Korea": "South Korean Won (KRW)",
        "Turkey": "Turkish Lira (TRY)",
        "Saudi Arabia": "Saudi Riyal (SAR)",
        "Israel": "Israeli New Shekel (ILS)",
        "Argentina": "Argentine Peso (ARS)",
        "Nigeria": "Nigerian Naira (NGN)",
        "United Arab Emirates": "UAE Dirham (AED)",
        "Indonesia": "Indonesian Rupiah (IDR)",
        "Malaysia": "Malaysian Ringgit (MYR)",
        "Thailand": "Thai Baht (THB)",
        "Egypt": "Egyptian Pound (EGP)",
        "Philippines": "Philippine Peso (PHP)",
        "Vietnam": "Vietnamese Dong (VND)",
        "Pakistan": "Pakistani Rupee (PKR)",
        "Iran": "Iranian Rial (IRR)",
        "Iraq": "Iraqi Dinar (IQD)",
        "Bangladesh": " Taka (BDT)",
        "Afghanistan": "Afghan Afghani (AFN)",
        "South Sudan": "South Sudanese Pound (SSP)",
        "Kenya": "Kenyan Shilling (KES)",
        "Tanzania": "Tanzanian Shilling (TZS)",
        "Ethiopia": "Ethiopian Birr (ETB)",
        "Uganda": "Ugandan Shilling (UGX)",
        "Ghana": "Ghanaian Cedi (GHS)",
        "Nigeria": "Nigerian Naira (NGN)",
        "South Sudan": "South Sudanese Pound (SSP)",
        "Angola": "Angolan Kwanza (AOA)",
        "Mozambique": "Mozambican Metical (MZN)",
        "Zimbabwe": "Zimbabwean Dollar (ZWL)",
        "Sudan": "Sudanese Pound (SDG)",
        "Morocco": "Moroccan Dirham (MAD)",
    }
    return currencies.get(country, "Unknown")

def get_country_population(country):
    
    populations = {
        "United States": 331002651,
        "United Kingdom": 67886011,
        "France": 65273511,
        "Brazil": 214000000,
        "Nigeria": 211000000,
        "Bangladesh": 166000000,
        "Russia": 145000000,
        "Mexico": 126000000,
        "Japan": 126000000,
        "Ethiopia": 120000000,
        "Philippines": 113000000,
        "Egypt": 104000000,
        "Vietnam": 98000000,
        "Congo": 92000000,
        "Turkey": 85000000,
        "Iran": 85000000,
        "Germany": 83000000,
        "Thailand": 69000000,
        "France": 67000000,
        "United Kingdom": 67000000,
        "Italy": 60000000,
        "South Africa": 61000000,
        "Tanzania": 61000000,
        "Myanmar (Burma)": 54000000,
        "South Korea": 51000000,
        "Colombia": 51000000,
        "Kenya": 54000000,
        "Spain": 47000000,
        "Argentina": 45000000,
        "Ukraine": 41000000,
        "Algeria": 44000000,
        "Sudan": 44000000,
        "Uganda": 45000000,
        "Iraq": 42000000,
        "Poland": 38000000,
        "Canada": 38000000,
        "Morocco": 38000000,
        "Saudi Arabia": 35000000,
        "Uzbekistan": 34000000,
        "Malaysia": 32000000,
        "Peru": 33000000,
        "Venezuela": 28000000,
        "Afghanistan": 38000000,
        "Ghana": 32000000,
        "Mozambique": 31000000,
        "Yemen": 30000000,
        "North Korea": 25000000,
        "Madagascar": 27000000,
    }
    return populations.get(country, "Unknown")

def simple_chatbot(user_input):
    
    user_input_lower = user_input.lower()

    
    if 'hello' in user_input_lower or 'hi' in user_input_lower or 'hey' in user_input_lower:
        return 'Hello! How can I help you?'
    elif 'how are you' in user_input_lower:
        return 'I am a chatbot, but thanks for asking!'
    elif 'your name' in user_input_lower:
        return 'I am a chatbot and I don\'t have a name.'
    elif 'favorite color' in user_input_lower:
        return 'I do not have a favorite color. I am just a computer program.'
    elif 'how old are you' in user_input_lower:
        return 'I do not have an age. I am a piece of software.'
    elif 'bye' in user_input_lower or 'goodbye' in user_input_lower:
        return 'Goodbye! Have a great day!'
    elif 'help' in user_input_lower:
        return 'I can assist you with basic information. Just ask!'
    elif 'current leaders' in user_input_lower:
        return "Sure! I can provide information about the current leaders of various countries. " \
               "Please ask about a specific country, for example, 'Tell me about the leaders of the United States.'"
    elif 'leaders of'in user_input_lower or 'leader of' in user_input_lower or 'prime minister of' in user_input_lower or 'president of' in user_input_lower:
        
        country_start_index = user_input_lower.find('leaders of') + len('leaders of')
        country = user_input[country_start_index:].strip()
        leaders_info = get_leader_info(country)
        president = leaders_info["President"]
        prime_minister = leaders_info["Prime Minister"]
        return f"The current leaders of {country} are: President - {president}, Prime Minister - {prime_minister}"
    elif 'weather' in user_input_lower:
        return 'I do not have real-time weather information. Please check a weather website for the current forecast.'
    elif 'meaning of life' in user_input_lower:
        return 'The meaning of life is a philosophical question. Different people have different perspectives on it.'
    elif 'joke' in user_input_lower:
        return 'Why did the computer go to therapy? It had too many bytes of emotional baggage!'
    elif 'song recommendation' in user_input_lower:
        return 'I recommend listening to "Imagine" by John Lennon.'
    elif 'book recommendation' in user_input_lower:
        return 'I recommend reading "To Kill a Mockingbird" by Harper Lee.'
    elif 'programming language' in user_input_lower:
        return 'There are many programming languages. Some popular ones include Python, JavaScript, and Java.'
    elif 'movie recommendation' in user_input_lower:
        return 'I recommend watching "The Shawshank Redemption."'
    elif 'your favorite food' in user_input_lower:
        return 'I do not have preferences as I am just a computer program.'
    elif 'capital of' in user_input_lower:
        
        country_start_index = user_input_lower.find('capital of') + len('capital of')
        country = user_input[country_start_index:].strip()
        capital = get_country_capital(country)
        return f"The capital of {country} is {capital}."
    elif 'currency of' in user_input_lower:
        
        country_start_index = user_input_lower.find('currency of') + len('currency of')
        country = user_input[country_start_index:].strip()
        currency = get_country_currency(country)
        return f"The currency of {country} is {currency}."
    elif 'population of' in user_input_lower:
        
        country_start_index = user_input_lower.find('population of') + len('population of')
        country = user_input[country_start_index:].strip()
        population = get_country_population(country)
        return f"The population of {country} is {population}."
    elif re.match(r'^\s*\d+(\.\d+)?\s*[\+\-\*/]\s*\d+(\.\d+)?\s*$', user_input):
        try:
            result = eval(user_input)
            return f"The result of the expression is: {result}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
print(start_response())
# Function to handle user input and display chatbot responses
def process_user_input():
    user_input = user_entry.get()
    if user_input.lower() == 'exit':
        chatbot_display.insert(tk.END, "Chatbot: Goodbye!\n")
        root.destroy()
    else:
        response = simple_chatbot(user_input)
        chatbot_display.config(state=tk.NORMAL)  # Allow modifications to the chat display
        chatbot_display.insert(tk.END, f"You: {user_input}\n")
        chatbot_display.insert(tk.END, f"Chatbot: {response}\n")
        chatbot_display.config(state=tk.DISABLED)  # Make the chat display read-only
        user_entry.delete(0, tk.END)

# Create the main GUI window
root = tk.Tk()
root.title("Simple Chatbot")
# Create custom fonts
message_font = ("Roboto", 12)
response_font = ("Lato", 12, "bold")

# Create custom colors
user_message_color = "black"
chatbot_response_color = "red"

# Create and configure the chat display area
chatbot_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chatbot_display.insert(tk.END, start_response())
chatbot_display.config(state=tk.DISABLED)  # Make the chat display read-only
chatbot_display.pack(padx=10, pady=10)

# Create and configure the user input field
user_entry = tk.Entry(root, width=50)
user_entry.pack(padx=10, pady=(0, 10))

# Create and configure the send button
send_button = tk.Button(root, text="Send", command=process_user_input)
send_button.pack(pady=(0, 10))

# Function to bind the "Enter" key to the send button
def on_enter_key(event):
    process_user_input()

# Bind the "Enter" key to the send button
root.bind('<Return>', on_enter_key)

# Run the Tkinter event loop
root.mainloop()
