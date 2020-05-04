Artefakty do utworzenia:

- wykresy od JMeter
    - wykres czasu odpowiedzi
    - wykres error rate'u
    - wykres throughputu
    - wykres bandwidth
    - wykres Concurrent users
- wykresy od Glances
    - wykres zuzycia CPU
    - wykres zuzycia pamieci
    - wykres zuzycia sieci
    - wykres zuzycia dysku

TODO:

- JMETER
    - podzielenie danych na 120 chunkow
    - obliczenie sredniej, mediany, odchylenia standardowego, max i min dla kazdego z chunkow
    - wyplucie pliku, ktory zawiera tylko wymagane dane + labelke chunka + labelke systemu konteneryzacji
    - zlaczenie wyjsciowych plikow 3 systemow
    - uruchomienie tego skryptu na dla kazdej z metryk
- GLANCES
    - obczaić wykresy
    - zaznaczyc na wykresie poczatek testu
    - wypluc plik, ktory zawiera tylko wymagane dane + labelke systemu konteneryzacji
    - zlaczenie dla 3 systemow
    - uruchomienie dla kazdej z badanych metryk
