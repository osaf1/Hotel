# Jarir Hotel - Hotelboekingswebsite

## 1. Projectbeschrijving

Jarir Hotel is een website waarmee gebruikers een hotelkamer kunnen bekijken en reserveren.

Het doel van dit project is om een eenvoudige en gebruiksvriendelijke hotelboekingswebsite te maken met Python en Flask.

Gebruikers kunnen:
- De homepage van het hotel bekijken
- Beschikbare kamers bekijken
- Informatie over kamers bekijken
- Een check-in- en check-outdatum kiezen
- Het aantal gasten en kamers kiezen
- Een hotelkamer reserveren
- Een account registreren en inloggen
- Een boekingsbevestiging bekijken

Het project wordt ontwikkeld op basis van het ontwerp dat ik in Figma heb gemaakt.

---

## 2. Doel van het project

Het belangrijkste doel van dit project is om een werkende hotelboekingswebsite te ontwikkelen.

De website moet een overzichtelijk en professioneel ontwerp hebben. Gebruikers moeten eenvoudig een kamer kunnen zoeken en reserveren.

Met dit project wil ik mijn vaardigheden verbeteren in:
- Python
- Flask
- HTML
- CSS
- JavaScript
- Databases
- Git en GitHub

---

## 3. Doelgroep

De website is bedoeld voor mensen die online een hotelkamer willen boeken.

Voorbeelden van gebruikers:
- Mensen die een hotelkamer zoeken
- Toeristen
- Gezinnen
- Zakelijke reizigers
- Mensen die een korte verblijfplaats zoeken

---

## 4. Gebruikte technologieën

Voor dit project gebruik ik de volgende technologieën:

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite

### Ontwerp
- Figma

### Versiebeheer
- Git
- GitHub

---

## 5. Pagina's van de website

### Homepage

De homepage bevat:
- Jarir Hotel-logo
- Navigatiemenu
- Join / Sign in
- Informatie over het hotel
- Check-in datum
- Check-out datum
- Aantal gasten
- Aantal kamers
- Zoekknop

### Kamerspagina

Op de kamerspagina worden de beschikbare kamers weergegeven.

De pagina bevat:
- Foto's van de kamers
- Naam van de kamer
- Beschrijving van de kamer
- Maximum aantal gasten
- Prijs per nacht
- Book Now-knop

### Boekingspagina

Op de boekingspagina kan de gebruiker een reservering maken.

De pagina bevat:
- Geselecteerde kamer
- Check-in datum
- Check-out datum
- Aantal gasten
- Naam van de gast
- E-mailadres
- Telefoonnummer
- Totale prijs
- Confirm Booking-knop

### Loginpagina

Gebruikers kunnen hier inloggen met:
- E-mailadres of gebruikersnaam
- Wachtwoord

### Registratiepagina

Nieuwe gebruikers kunnen hier een account maken.

De gebruiker vult in:
- Naam
- E-mailadres
- Wachtwoord

### Bevestigingspagina

Na een succesvolle reservering krijgt de gebruiker een bevestiging met:
- Bevestiging van de reservering
- Boekingsnummer
- Kamerinformatie
- Check-in datum
- Check-out datum
- Aantal gasten
- Totale prijs

---

## 6. Databaseplan

De website gebruikt een SQLite-database.

### Users-tabel

De users-tabel bevat:

- id
- name
- email
- password

### Rooms-tabel

De rooms-tabel bevat:

- id
- room_name
- description
- price
- guests
- image

### Bookings-tabel

De bookings-tabel bevat:

- id
- user_id
- room_id
- check_in
- check_out
- guests
- total_price
- booking_date

---

## 7. Projectstructuur

Het project heeft de volgende structuur:

hotel/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── rooms.html
│   ├── booking.html
│   ├── login.html
│   ├── register.html
│   └── confirmation.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       ├── logo.png
│       ├── hotel.jpg
│       ├── room-deluxe.jpg
│       ├── room-family.jpg
│       └── room-suite.jpg
│
└── database/
    └── hotel.db

---

## 8. Belangrijkste functies

### Kamer zoeken

Gebruikers kunnen een kamer zoeken door te kiezen voor:
- Check-in datum
- Check-out datum
- Aantal gasten
- Aantal kamers

De website laat vervolgens de beschikbare kamers zien.

### Registreren

Gebruikers kunnen een account maken met hun naam, e-mailadres en wachtwoord.

### Inloggen

Geregistreerde gebruikers kunnen inloggen op hun account.

### Hotelkamer boeken

Gebruikers kunnen een kamer selecteren en een reservering maken.

### Boekingsbevestiging

Na het boeken krijgt de gebruiker een bevestigingspagina met alle informatie over de reservering.

### Beschikbaarheid van kamers

Het systeem controleert of een kamer al is gereserveerd voor de gekozen datums.

---

## 9. Ontwerpplan

Het ontwerp van de website wordt eerst gemaakt in Figma.

Het ontwerp richt zich op:
- Eenvoudige navigatie
- Professionele uitstraling
- Een eenvoudig boekingsproces
- Duidelijke knoppen
- Goed leesbare tekst
- Responsive design

De kleuren van de website worden gebaseerd op het Jarir Hotel-logo.

---

## 10. Ontwikkelplan

### Fase 1 - Planning

- Het idee voor de website bepalen
- De doelgroep bepalen
- Het projectplan maken
- Het ontwerp in Figma maken
- De gebruikte technologieën bepalen

### Fase 2 - Project opzetten

- Het Flask-project maken
- De mappen en bestanden maken
- Een Python virtual environment maken
- Flask installeren
- De GitHub repository maken

### Fase 3 - Frontend

- De homepage maken
- De kamerspagina maken
- De boekingspagina maken
- De login- en registratiepagina maken
- CSS-styling toevoegen
- JavaScript-functionaliteit toevoegen

### Fase 4 - Backend

- Flask-routes maken
- Flask verbinden met SQLite
- De database maken
- Gebruikers toevoegen
- Kamers toevoegen
- Boekingen toevoegen

### Fase 5 - Boekingssysteem

- De zoekfunctie voor kamers maken
- De beschikbaarheid van kamers controleren
- De totale prijs berekenen
- Boekingen opslaan in de database
- De boekingsbevestiging maken

### Fase 6 - Testen

Ik test:
- Homepage
- Kamer zoeken
- Registreren
- Inloggen
- Boeken
- Beschikbaarheid van kamers
- Prijsberekening
- Bevestigingspagina
- Formulieren en knoppen
- Responsive design

### Fase 7 - Afronden

- Bugs oplossen
- Het ontwerp verbeteren
- De code opruimen
- De volledige website testen
- De README bijwerken
- Het project naar GitHub pushen

---

## 11. Testplan

De website wordt getest om te controleren of alle belangrijke functies goed werken.

| Test | Verwacht resultaat |
|---|---|
| Homepage openen | De homepage wordt weergegeven |
| Een kamer zoeken | Beschikbare kamers worden weergegeven |
| Registreren | Een nieuw account wordt aangemaakt |
| Inloggen | De gebruiker kan inloggen |
| Kamer selecteren | De gekozen kamer wordt geselecteerd |
| Reservering maken | De reservering wordt opgeslagen |
| Niet-beschikbare kamer boeken | De gebruiker krijgt een melding |
| Reservering bevestigen | De bevestiging wordt weergegeven |
| Uitloggen | De gebruiker wordt uitgelogd |

---

## 12. GitHub-plan

Git wordt gebruikt om de ontwikkeling van het project bij te houden.

Voorbeelden van commits:

```text
Initial project setup
Add Flask application
Add homepage
Add rooms page
Add booking page
Add database
Add user registration
Add login system
Add booking system
Add room availability
Add booking confirmation
Improve styling
Fix bugs
Final version