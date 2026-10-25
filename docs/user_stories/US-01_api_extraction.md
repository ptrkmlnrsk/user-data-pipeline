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