# TO DO
- Projektreferenz, Personalnummer in der Anzeige umwandeln in Name und Titel
- /delete Seite benötigt es nicht dringend
- services Verzeichnis wird nicht benötigt
- Aktivität, Projektphase, Meilensteine ausprogrammieren
- Benutzerfreundlichkeit erhöhen

## base.html
```
<li><a href="{{ url_for('projektphase.list_projektphasen') }}">Projektphasen</a></li>
<li><a href="{{ url_for('aktivitaet.list_aktivitaeten') }}">Aktivitäten</a></li>
<li><a href="{{ url_for('meilenstein.list_meilensteine') }}">Meilensteine</a></li>
```