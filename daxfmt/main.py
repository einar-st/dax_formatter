import sys
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.daxformatter.com/?embed=1"

    if sys.stdin.isatty():
        print("No content given", file=sys.stderr)
        return

    dax_code = sys.stdin.read().strip()

    if not dax_code:
        print("No content given", file=sys.stderr)
        return

    data = {
        'r': 'US',
        'fx': dax_code
    }

    try:
        response = requests.post(url, data=data, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}", file=sys.stderr)
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        formatted_div = soup.find('div', {'class': 'formatted'})
        if formatted_div:
            for br in formatted_div.find_all('br'):
                br.replace_with('\n')
            text = formatted_div.get_text().replace('\xa0', ' ')
            print(text)
        else:
            print("Could not find formatted DAX.", file=sys.stderr)
    else:
        print("Error:", response.status_code, response.text, file=sys.stderr)


if __name__ == "__main__":
    main()
