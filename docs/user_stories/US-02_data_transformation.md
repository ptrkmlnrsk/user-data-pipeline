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
