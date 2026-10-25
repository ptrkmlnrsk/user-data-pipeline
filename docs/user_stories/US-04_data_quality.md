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