US-01 — Pobieranie danych z REST API
Jako Data Engineer
Chcę pobierać dane użytkowników i postów z API JSONPlaceholder
Aby przygotować surowe dane do dalszego przetwarzania.
Kryteria akceptacji
- [ ] System pobiera dane z endpointów /users i /posts.
- [ ] Żądania mają skonfigurowany timeout.
- [ ] Błędy HTTP i transportowe są obsługiwane jawnie.
- [ ] Odpowiedź jest sprawdzana pod kątem oczekiwanego formatu JSON.
- [ ] Surowe odpowiedzi są zapisywane w plikach JSON z identyfikatorem uruchomienia.
- [ ] Nieudane pobranie nie jest raportowane jako udany ekstrakt.
- [ ] Testy jednostkowe nie wymagają połączenia z Internetem.
Zadania techniczne:
1. Implementacja klienta HTTP.
2. Modele Pydantic dla użytkownika i postu.
3. Zapis odpowiedzi w raw layer.
4. Testy timeoutów, błędów HTTP i niepoprawnego JSON-a.
US-02 — Walidacja i transformacja danych
Jako Data Engineer
Chcę walidować, normalizować i deduplikować pobrane rekordy
Aby zapewnić spójność danych przekazywanych do bazy.
Kryteria akceptacji
- [ ] Rekordy są walidowane zgodnie z kontraktem danych.
- [ ] Brak wymaganych pól powoduje odrzucenie rekordu z podaniem przyczyny.
- [ ] Pola tekstowe są normalizowane według ustalonych reguł.
- [ ] Duplikaty są wykrywane i raportowane.
- [ ] Posty wskazujące nieistniejących użytkowników są identyfikowane.
- [ ] Rekordy odrzucone są raportowane i nie znikają bez śladu.
- [ ] Transformacja nie modyfikuje surowych danych wejściowych.
Zadania techniczne:
1. Implementacja funkcji transformujących.
2. Określenie polityki duplikatów i błędnych rekordów.
3. Przygotowanie raportu jakości.
4. Testy parametryzowane w pytest.
US-03 — Ładowanie danych do PostgreSQL
Jako Data Engineer
Chcę ładować zwalidowanych użytkowników i posty do PostgreSQL
Aby udostępnić je w formie umożliwiającej wykonywanie zapytań analitycznych.
Kryteria akceptacji
- [ ] Istnieją tabele users i posts.
- [ ] Klucze główne i klucz obcy zapewniają integralność referencyjną.
- [ ] Ładowanie obsługuje wiele rekordów w jednym batchu.
- [ ] Ponowne załadowanie tych samych danych nie tworzy duplikatów.
- [ ] Zmiana danych dla istniejącego ID jest obsługiwana przez uzgodnioną strategię UPSERT.
- [ ] Błąd zapisu nie pozostawia częściowo zatwierdzonego batcha.
- [ ] Warstwa dostępu do bazy jest oddzielona od transformacji.
Zadania techniczne:
1. Przygotowanie schematu SQL.
2. Konfiguracja SQLAlchemy 2.
3. Implementacja repozytoriów.
4. Transakcje, batch insert i UPSERT.
5. Testy integracyjne z PostgreSQL.
US-04 — Testy i jakość danych
Jako Data Engineer
Chcę automatycznie sprawdzać jakość danych i poprawność działania pipeline'u
Aby wykrywać błędy zarówno w kodzie, jak i w samych danych.
Kryteria akceptacji
- [ ] Testy sprawdzają duplikaty kluczy.
- [ ] Testy sprawdzają nieoczekiwane wartości NULL.
- [ ] Testy sprawdzają integralność referencyjną postów i użytkowników.
- [ ] Liczby rekordów na poszczególnych etapach są raportowane.
- [ ] Zmiana schematu wejściowego jest wykrywana i testowana.
- [ ] Testy sprawdzają puste odpowiedzi oraz błędne rekordy.
- [ ] Testy integracyjne potwierdzają rzeczywisty zapis i odczyt danych z PostgreSQL.
Zadania techniczne:
1. Testy jednostkowe i integracyjne.
2. Fixture'y i mockowanie HTTP.
3. Reguły jakości danych.
4. Test regresyjny z wcześniej przygotowanym zestawem danych.
5. Raportowanie odrzuceń i anomalii.
Ważne: nie każdy NULL musi być błędem. Reguły powinny wynikać z kontraktu konkretnej kolumny, a nie z ogólnego założenia, że wszystkie pola muszą być niepuste.
US-05 — Uruchamianie i monitoring pipeline'u
Jako Data Engineer
Chcę uruchamiać pipeline jako jeden proces, z czytelnymi logami i raportem końcowym
Aby móc go powtarzalnie wykonywać i diagnozować problemy.
Kryteria akceptacji
- [ ] Cały proces można uruchomić jedną komendą CLI.
- [ ] Konfiguracja jest przekazywana przez zmienne środowiskowe.
- [ ] Pipeline raportuje czas wykonania oraz liczbę pobranych, załadowanych i odrzuconych rekordów.
- [ ] Błąd krytyczny powoduje niezerowy kod wyjścia.
- [ ] Testy i lintowanie uruchamiają się w GitHub Actions.
- [ ] Środowisko lokalne można uruchomić przez Docker Compose.
- [ ] README opisuje konfigurację, uruchomienie i sposób diagnozowania błędów.
Zadania techniczne:
1. Orkiestracja kroków w pipeline.py.
2. CLI w cli.py.
3. Logowanie i statystyki wykonania.
4. Docker Compose dla aplikacji i PostgreSQL.
5. CI oraz dokumentacja.
