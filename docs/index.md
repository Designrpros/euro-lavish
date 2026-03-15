---
title: 🪙 Cost of Living in Europe
description: Compare cost of living across 50 European countries
---

# 🪙 Cost of Living in Europe

*Your complete guide to cost of living in Europe*

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
    #map { 
        height: 600px; 
        width: 100%; 
        border-radius: 12px; 
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        z-index: 1;
        cursor: crosshair;
    }
    .leaflet-tooltip {
        background: rgba(0,0,0,0.8);
        color: white;
        border: none;
        border-radius: 4px;
        padding: 5px 10px;
        font-size: 14px;
    }
</style>

<div id="map"></div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
    var map = L.map('map').setView([48.0, 15.0], 4);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    function addCountry(name, lat, lon, price, link) {
        var color = "#e74c3c"; // Red (>1500)
        if (price === "N/A") color = "#888";
        else {
            var val = parseInt(price.replace(/[^0-9]/g, ""));
            if (val < 800) color = "#2ecc71"; // Green
            else if (val < 1500) color = "#f1c40f"; // Yellow
        }

        L.circleMarker([lat, lon], {
            radius: 9,
            fillColor: color,
            color: "#fff",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.8
        }).addTo(map)
        .bindTooltip("<b>" + name + "</b><br>Rent: " + price, { sticky: true })
        .on('click', function() { window.location.href = link; });
    }

    addCountry("Norway", 60.47, 8.46, "1,603€", "norway/");
    addCountry("Sweden", 60.12, 18.64, "1,404€", "sweden/");
    addCountry("Denmark", 56.26, 9.50, "1,775€", "denmark/");
    addCountry("Finland", 61.92, 25.74, "1,300€", "finland/");
    addCountry("Estonia", 58.59, 25.01, "698€", "estonia/");
    addCountry("Iceland", 64.96, -19.02, "1,800€", "iceland/");
    addCountry("Latvia", 56.87, 24.60, "550€", "latvia/");
    addCountry("Lithuania", 55.17, 23.88, "650€", "lithuania/");
    addCountry("Poland", 51.91, 19.14, "1,000€", "poland/");
    addCountry("Czechia", 49.81, 15.47, "1,000€", "czech/");
    addCountry("Hungary", 47.16, 19.50, "650€", "hungary/");
    addCountry("Romania", 45.94, 24.96, "600€", "romania/");
    addCountry("Serbia", 44.01, 21.00, "700€", "serbia/");
    addCountry("Bulgaria", 42.73, 25.48, "669€", "bulgaria/");
    addCountry("Belarus", 53.71, 27.95, "350€", "belarus/");
    addCountry("Moldova", 47.41, 28.36, "400€", "moldova/");
    addCountry("Ukraine", 48.37, 31.16, "400€", "ukraine/");
    addCountry("Russia", 55.75, 37.61, "600€", "russia/");
    addCountry("Kazakhstan", 48.01, 66.92, "300€", "kazakhstan/");
    addCountry("Spain", 40.46, -3.74, "1,350€", "spain/");
    addCountry("Portugal", 39.39, -8.22, "1,100€", "portugal/");
    addCountry("Italy", 41.87, 12.56, "1,000€", "italy/");
    addCountry("Greece", 39.07, 21.82, "550€", "greece/");
    addCountry("Croatia", 45.10, 15.20, "700€", "croatia/");
    addCountry("Malta", 35.93, 14.37, "1,100€", "malta/");
    addCountry("Albania", 41.15, 20.17, "400€", "albania/");
    addCountry("Andorra", 42.50, 1.52, "1,200€", "andorra/");
    addCountry("Bosnia", 43.91, 17.67, "300€", "bosnia/");
    addCountry("Cyprus", 35.12, 33.42, "900€", "cyprus/");
    addCountry("Montenegro", 42.70, 19.37, "500€", "montenegro/");
    addCountry("North Macedonia", 41.60, 21.74, "300€", "north-macedonia/");
    addCountry("San Marino", 43.94, 12.45, "800€", "san-marino/");
    addCountry("Turkey", 41.00, 28.97, "500€", "turkey/");
    addCountry("Vatican", 41.90, 12.45, "N/A", "vatican/");
    addCountry("Germany", 51.16, 10.45, "1,270€", "germany/");
    addCountry("Austria", 47.52, 14.55, "1,077€", "austria/");
    addCountry("Switzerland", 46.81, 8.22, "2,580€", "switzerland/");
    addCountry("Slovakia", 48.66, 19.69, "600€", "slovakia/");
    addCountry("Slovenia", 46.15, 14.99, "750€", "slovenia/");
    addCountry("Liechtenstein", 47.14, 9.52, "2,200€", "liechtenstein/");
    addCountry("UK", 55.37, -3.43, "2,530€", "uk/");
    addCountry("Ireland", 53.41, -8.24, "2,118€", "ireland/");
    addCountry("Netherlands", 52.13, 5.29, "2,260€", "netherlands/");
    addCountry("Belgium", 50.50, 4.47, "1,125€", "belgium/");
    addCountry("France", 46.22, 2.21, "2,000€", "france/");
    addCountry("Luxembourg", 49.81, 6.12, "1,800€", "luxembourg/");
    addCountry("Monaco", 43.73, 7.42, "6,000€", "monaco/");
    addCountry("Georgia", 42.31, 43.35, "600€", "georgia/");
    addCountry("Armenia", 40.07, 45.04, "500€", "armenia/");
    addCountry("Azerbaijan", 40.14, 47.57, "450€", "azerbaijan/");
</script>

## 🏆 Top 10 Cheapest

| # | Country | Rent | Meal | Beer |
|---|---------|------|------|------|
| 1 | 🇬🇷 Greece | 550€ | 15€ | 5€ |
| 2 | 🇷🇴 Romania | 600€ | 12€ | 3€ |
| 3 | 🇭🇺 Hungary | 650€ | 10€ | 2.80€ |
| 4 | 🇧🇬 Bulgaria | 669€ | 10€ | 2.69€ |
| 5 | 🇪🇪 Estonia | 698€ | 15€ | 6€ |
| 6 | 🇷🇸 Serbia | 700€ | 12€ | 3.20€ |
| 7 | 🇭🇷 Croatia | 700€ | 12€ | 4€ |
| 8 | 🇵🇱 Poland | 1,000€ | 10€ | 4.30€ |
| 9 | 🇨🇿 Czechia | 1,000€ | 9.50€ | 2.40€ |
| 10 | 🇮🇹 Italy | 1,000€ | 15€ | 5€ |

## 🏔️ Northern Europe (6)

| Country | Rent | → |
|---------|------|---|
| 🇳🇴 [Norway](norway/) | 1,603€ | → |
| 🇸🇪 [Sweden](sweden/) | 1,404€ | → |
| 🇩🇰 [Denmark](denmark/) | 1,775€ | → |
| 🇫🇮 [Finland](finland/) | 1,300€ | → |
| 🇪🇪 [Estonia](estonia/) | 698€ | → |
| 🇮🇸 [Iceland](iceland/) | 1,800€ | → |
| 🇱🇻 [Latvia](latvia/) | 550€ | → |
| 🇱🇹 [Lithuania](lithuania/) | 650€ | → |

## 🏗️ Eastern Europe (6)

| Country | Rent | → |
|---------|------|---|
| 🇵🇱 [Poland](poland/) | 1,000€ | → |
| 🇨🇿 [Czechia](czech/) | 1,000€ | → |
| 🇭🇺 [Hungary](hungary/) | 650€ | → |
| 🇷🇴 [Romania](romania/) | 600€ | → |
| 🇷🇸 [Serbia](serbia/) | 700€ | → |
| 🇧🇬 [Bulgaria](bulgaria/) | 669€ | → |
| 🇧🇾 [Belarus](belarus/) | 350€ | → |
| 🇲🇩 [Moldova](moldova/) | 400€ | → |
| 🇺🇦 [Ukraine](ukraine/) | 400€ | → |
| 🇷🇺 [Russia](russia/) | 600€ | → |
| 🇰🇿 [Kazakhstan](kazakhstan/) | 300€ | → |

## ☀️ Southern Europe (6)

| Country | Rent | → |
|---------|------|---|
| 🇪🇸 [Spain](spain/) | 1,350€ | → |
| 🇵🇹 [Portugal](portugal/) | 1,100€ | → |
| 🇮🇹 [Italy](italy/) | 1,000€ | → |
| 🇬🇷 [Greece](greece/) | 550€ | → |
| 🇭🇷 [Croatia](croatia/) | 700€ | → |
| 🇲🇹 [Malta](malta/) | 1,100€ | → |
| 🇦🇱 [Albania](albania/) | 400€ | → |
| 🇦🇩 [Andorra](andorra/) | 1,200€ | → |
| 🇧🇦 [Bosnia](bosnia/) | 300€ | → |
| 🇨🇾 [Cyprus](cyprus/) | 900€ | → |
| 🇲🇪 [Montenegro](montenegro/) | 500€ | → |
| 🇲🇰 [Macedonia](north-macedonia/) | 300€ | → |
| 🇸🇲 [San Marino](san-marino/) | 800€ | → |
| 🇹🇷 [Turkey](turkey/) | 500€ | → |
| 🇻🇦 [Vatican](vatican/) | N/A | → |

## 🔵 Central Europe (3)

| Country | Rent | → |
|---------|------|---|
| 🇩🇪 [Germany](germany/) | 1,270€ | → |
| 🇦🇹 [Austria](austria/) | 1,077€ | → |
| 🇨🇭 [Switzerland](switzerland/) | 2,580€ | → |
| 🇸🇰 [Slovakia](slovakia/) | 600€ | → |
| 🇸🇮 [Slovenia](slovenia/) | 750€ | → |
| 🇱🇮 [Liechtenstein](liechtenstein/) | 2,200€ | → |

## 🌊 Western Europe (5)

| Country | Rent | → |
|---------|------|---|
| 🇬🇧 [UK](uk/) | 2,530€ | → |
| 🇮🇪 [Ireland](ireland/) | 2,118€ | → |
| 🇳🇱 [Netherlands](netherlands/) | 2,260€ | → |
| 🇧🇪 [Belgium](belgium/) | 1,125€ | → |
| 🇫🇷 [France](france/) | 2,000€ | → |
| 🇱🇺 [Luxembourg](luxembourg/) | 1,800€ | → |
| 🇲🇨 [Monaco](monaco/) | 6,000€ | → |

## ⛰️ Caucasus (3)

| Country | Rent | → |
|---------|------|---|
| 🇬🇪 [Georgia](georgia/) | 600€ | → |
| 🇦🇲 [Armenia](armenia/) | 500€ | → |
| 🇦🇿 [Azerbaijan](azerbaijan/) | 450€ | → |

## 📊 Statistics

- 50 Countries
- 300+ Cities
- Cheapest: 550€ (Greece)
- Most Expensive: 2,580€ (Switzerland)

*Data: Numbeo.com, March 2026*
