import openai
import os
from sys import argv
from dotenv import load_dotenv

# Wczytaj zmienne środowiskowe z pliku .env
load_dotenv()

# Ustaw klucz API dla OpenAI
openai.api_key = os.getenv('API_KEY')

def main():
    """
    Program do poprawy ortografii i gramatyki tekstu zawartego w pliku źródłowym,
    oraz generowania poprawionej wersji w formacie HTML. 

    Używa modelu OpenAI do przetworzenia tekstu i zwraca sformatowany kod HTML 
    w pliku wynikowym.

    Argumenty:
    1. source_file (str): Ścieżka do pliku źródłowego zawierającego tekst do poprawy.
    2. target_file (str): Ścieżka do pliku, w którym zostanie zapisany poprawiony tekst w HTML.

    Zasady działania:
    - Sprawdza, czy podano dwa argumenty (ścieżki do plików).
    - Weryfikuje istnienie pliku źródłowego.
    - Wczytuje tekst z pliku źródłowego, używa modelu OpenAI do poprawy tego tekstu.
    - Zapisuje poprawiony tekst w formatowaniu HTML do pliku wynikowego.
    """

    if len(argv) != 3:
        print('\n---> Nie podałeś: pliku źródłowego lub wynikowego lub obu')
        quit()

    if not os.path.exists(argv[1]):
        print('\n---> Plik źródłowy nie istnieje')
        quit()

    _, source_file, target_file = argv

    # Wczytaj tekst z pliku źródłowego
    with open(source_file, encoding='utf8') as file:
        command = 'Popraw ortografię i gramatykę następującego tekstu: "'
        command += ''.join(file.readlines())
        command += '".\n\nPoprawiony tekst podaj jako kod html strony www. Użyj odowiednich tagów HTML do strukturyzacji treści. Określ miejsca gdzie warto wstawić grafiki. Oznacz je z użyciem tagu <img> z atrybutem scr="image_placeholder.jpg". Dodaj atrybut alt do każdego obrazka z dokładnym promtem, który będzie można użyć do wygenerowania grafiki. Umieść podpisy od grafikami używając odowiedniego tagu HTML. Grafikę i jej podpis umieść w <div> z atrybutem class. Podaj tylko wnętrze tagu <body> bez <body> i </body>.'
        print(command)

        # Wysłanie zapytania do API OpenAI
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=command,
            temperature=0.5,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

    # Zapisz poprawiony tekst do pliku wynikowego
    with open(target_file, 'w') as file:
        file.write(response.choices[0].text)

if __name__ == "__main__":
    main()