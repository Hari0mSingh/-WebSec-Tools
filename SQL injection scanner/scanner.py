import requests
from bs4 import BeautifulSoup

bad_char = ["'", "<", ">", "(", ")", ";"]

def spider_inputs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find("form")
    if not form:
        print("No form was found")
        return []
    return form.findAll('input')

def test_inputs(url, inputs):
    result = {}
    for input_field in inputs:
        name = input_field.get('name')
        if name:
            for i in bad_char:
                payload = {name: i}
                response = requests.post(url, data=payload)
                key = f"{url} input field: {name} payload {i}"
                result[key] = response.status_code
    return result  

def main():
    url = input("What URL do you want to scan for SQL injection: ")
    inputs = spider_inputs(url)

    if not inputs:
        return

    results = test_inputs(url, inputs)
    for key, value in results.items():
        print(f"{key} and status code {value}")

if __name__ == "__main__":
    main()
