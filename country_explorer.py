import requests
from urllib.parse import quote
def get_languages(country_data):
    languages = []
    if country_data.get('languages'):
        for language in country_data['languages']:
            languages.append(language.get('name', 'Unknown'))  
        return languages


def extract_country_info(country_data):
    country_info = {
        'name': country_data.get('names', {}).get('common', 'Unknown'),
        'region': country_data.get('region', 'Unknown'),
        'population': country_data.get('population', 'Unknown') 
    }
    capitals = country_data.get('capitals')
    if capitals:
        country_info['capital'] = capitals[0].get('name', 'Unknown')
    else:
        country_info['capital']= " No capital information available"
    currencies = country_data.get('currencies')
    if currencies:
        country_info['currency'] = currencies[0].get('name', 'Unknown')
    else:
        country_info['currency'] = "No currency information available"
    languages = []
    if country_data.get('languages'):
        for language in country_data['languages']:
            languages.append(language.get('name', 'Unknown')) 
    country_info["languages"] = languages
    
    return country_info



def display_country(country_info):
        title = "\nCOUNTRY INFORMATION\n\n"
        title += f"Country: {country_info['name']}\n"
        title += f"Region: {country_info['region']}\n"
        if country_data.get('languages'):
            title += f"First Language: {country_data['languages'][0]['name']}\n"
        else:
            title += "First Language: No language information available\n"
        title += f"Capital: {country_info['capital']}\n"
        title += f'Population: {country_info["population"]}\n'
        title += f"Currency: {country_info['currency']}\n"
        languages = get_languages(country_data)
        if country_info['languages']:
            title += f"Languages: {', '.join(country_info['languages'])}\n"
        else:
            title += "Languages: No language information available\n"
        return title
def get_country(country):
    
    try:
        country_encoded = quote(country)
        response = requests.get(
        f"https://api.restcountries.com/countries/v5/names.common/{country_encoded}",
        headers={"Authorization": "Bearer rc_live_demo"},
        timeout=10
        )
        response.raise_for_status()
    except requests.RequestException as error:
        print("Request failed:", error)
        return None
    data = response.json()
    countries = data['data']['objects']
    for country_data in countries:
        if country_data.get('names', {}).get('common', '').lower() == country:
            return country_data
        
    return None
result = {'name': 'canada'}
if result is not None:
    print("We have data")
else:
    print("We dont have data")


country_data = get_country("canada")
country_info = extract_country_info(country_data)
print(country_info)
print(display_country(country_info))



while True:
    country = input("Enter country: ").strip().lower()
    if country == 'exit':
        break
    if not country:
        print("Please enter a country.")
        continue
    country_data = get_country(country)
    if country_data:
        country_info = extract_country_info(country_data)
        print(display_country(country_info))
    else:
        print("Country not found")
    
    