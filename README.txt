Wywołanie programu z consoli:
    py -m p1.py source_file target_file

    gdzie: p1.py - plik zawierający kod programu
           source_file - plik zawierający żródłowy tekst do przetworzenia
           target_file - plik wynikowy (tu artykul.html)

Plik .env zawiera klucz do API OpenAI

Program wymaga doinstalowania:
    python-dotenv do odczytywania pliku .env

    openai do komunikacji z OpenAI

Działanie programu:
    importuje i ładuje potrzebne moduły

    odczytuje klucz API z pliku .env

    sprawdza formalną poprawność polecenia wysłąnego z konsoli, w przypadku zaistnienia nieprawidłowoći, to wysyła komunikat na konsolę i przerywa działanie programu

    sprawdza istnienie pliku z żródłowym tekstem, w przypadku gdy plik nie istnieje,to wysyła komunikat na konsolę i przerywa działanie programu

    definiuje pomocnicze zmienne source_file i target_file identyfikujące odpowiednio plik z tekstem źródłowym i plik wynikowy

    buduje treść promptu na bazie tekstu źrółowego pobranego z pliku source_file i wyyła go do API OpenAI

    otrzymaną odpowiedź zapisuje w pliku target_file
    
    