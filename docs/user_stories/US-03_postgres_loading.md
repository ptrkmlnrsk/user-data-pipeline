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