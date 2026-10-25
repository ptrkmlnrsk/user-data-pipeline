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
