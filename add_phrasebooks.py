import os

BASE_DOCS = "/home/vegar/.openclaw/workspace/costofliving/europa/docs"

# Phrasebook data for 26 countries
PHRASEBOOKS = {
    "norway": {"Hello": "Hallo", "Thank you": "Takk", "Yes/No": "Ja / Nei", "How are you?": "Hvordan har du det?", "Excuse me": "Unnskyld", "Check, please!": "Regningen, takk!", "Do you speak English?": "Snakker du engelsk?"},
    "sweden": {"Hello": "Hej", "Thank you": "Tack", "Yes/No": "Ja / Nej", "How are you?": "Hur mår du?", "Excuse me": "Ursäkta", "Check, please!": "Notan, tack!", "Do you speak English?": "Pratar du engelska?"},
    "denmark": {"Hello": "Hej", "Thank you": "Tak", "Yes/No": "Ja / Nej", "How are you?": "Hvordan har du det?", "Excuse me": "Undskyld", "Check, please!": "Regningen, tak!", "Do you speak English?": "Taler du engelsk?"},
    "finnland": {"Hello": "Hei", "Thank you": "Kiitos", "Yes/No": "Kyllä / Ei", "How are you?": "Mitä kuuluu?", "Excuse me": "Anteeksi", "Check, please!": "Lasku, kiitos!", "Do you speak English?": "Puhutteko englantia?"},
    "estonia": {"Hello": "Tere", "Thank you": "Aitäh", "Yes/No": "Jah / Ei", "How are you?": "Kuidas läheb?", "Excuse me": "Vabandust", "Check, please!": "Arve, palun!", "Do you speak English?": "Kas te räägite inglise keelt?"},
    "iceland": {"Hello": "Halló", "Thank you": "Takk", "Yes/No": "Já / Nei", "How are you?": "Hvernig hefurðu það?", "Excuse me": "Afsakið", "Check, please!": "Reikninginn, takk!", "Do you speak English?": "Talarðu ensku?"},
    "germany": {"Hello": "Hallo", "Thank you": "Danke", "Yes/No": "Ja / Nein", "How are you?": "Wie geht es dir?", "Excuse me": "Entschuldigung", "Check, please!": "Die Rechnung, bitte!", "Do you speak English?": "Sprechen Sie Englisch?"},
    "austria": {"Hello": "Servus / Hallo", "Thank you": "Danke", "Yes/No": "Ja / Nein", "How are you?": "Wie geht's?", "Excuse me": "Entschuldigen Sie", "Check, please!": "Zahlen bitte!", "Do you speak English?": "Sprechen Sie Englisch?"},
    "switzerland": {"Hello": "Grüezi / Hallo", "Thank you": "Danke", "Yes/No": "Ja / Nein", "How are you?": "Wie geht's?", "Excuse me": "Exgüsi", "Check, please!": "Zahlen bitte!", "Do you speak English?": "Sprechen Sie Englisch?"},
    "france": {"Hello": "Bonjour", "Thank you": "Merci", "Yes/No": "Oui / Non", "How are you?": "Comment ça va ?", "Excuse me": "Excusez-moi", "Check, please!": "L'addition, s'il vous plaît !", "Do you speak English?": "Parlez-vous anglais ?"},
    "belgium": {"Hello": "Hallo / Bonjour", "Thank you": "Dank u / Merci", "Yes/No": "Ja / Oui", "How are you?": "Hoe gaat het? / Ça va?", "Excuse me": "Excuseer / Pardon", "Check, please!": "De rekening, aub / L'addition, svp", "Do you speak English?": "Spreekt u Engels? / Anglais?"},
    "netherlands": {"Hello": "Hoi / Hallo", "Thank you": "Bedankt", "Yes/No": "Ja / Nee", "How are you?": "Hoe gaat het?", "Excuse me": "Pardon", "Check, please!": "De rekening, alstublieft!", "Do you speak English?": "Spreekt u Engels?"},
    "spain": {"Hello": "Hola", "Thank you": "Gracias", "Yes/No": "Sí / No", "How are you?": "¿Cómo estás?", "Excuse me": "Perdone", "Check, please!": "¡La cuenta, por favor!", "Do you speak English?": "¿Habla inglés?"},
    "portugal": {"Hello": "Olá", "Thank you": "Obrigado", "Yes/No": "Sim / Não", "How are you?": "Como está?", "Excuse me": "Com licença", "Check, please!": "A conta, por favor!", "Do you speak English?": "Fala inglês?"},
    "italy": {"Hello": "Ciao / Buongiorno", "Thank you": "Grazie", "Yes/No": "Sì / No", "How are you?": "Come stai?", "Excuse me": "Scusi", "Check, please!": "Il conto, per favore!", "Do you speak English?": "Parla inglese?"},
    "greece": {"Hello": "Yassas", "Thank you": "Efcharisto", "Yes/No": "Nai / Ochi", "How are you?": "Ti kanis?", "Excuse me": "Signomi", "Check, please!": "Ton logariasmo, parakalo!", "Do you speak English?": "Milate Anglika?"},
    "croatia": {"Hello": "Bok / Zdravo", "Thank you": "Hvala", "Yes/No": "Da / Ne", "How are you?": "Kako ste?", "Excuse me": "Oprostite", "Check, please!": "Račun, molim!", "Do you speak English?": "Govorite li engleski?"},
    "poland": {"Hello": "Cześć", "Thank you": "Dziękuję", "Yes/No": "Tak / Nie", "How are you?": "Jak się masz?", "Excuse me": "Przepraszam", "Check, please!": "Poproszę rachunek!", "Do you speak English?": "Czy mówisz po angielsku?"},
    "czech": {"Hello": "Ahoj", "Thank you": "Děkuji", "Yes/No": "Ano / Ne", "How are you?": "Jak se máš?", "Excuse me": "Promiňte", "Check, please!": "Účet, prosím!", "Do you speak English?": "Mluvíte anglicky?"},
    "hungary": {"Hello": "Szia", "Thank you": "Köszönöm", "Yes/No": "Igen / Nem", "How are you?": "Hogy vagy?", "Excuse me": "Elnézést", "Check, please!": "A számlát, kérem!", "Do you speak English?": "Beszél angolul?"},
    "romania": {"Hello": "Salut", "Thank you": "Mulțumesc", "Yes/No": "Da / Nu", "How are you?": "Ce faci?", "Excuse me": "Scuzați-må", "Check, please!": "Nota, vă rog!", "Do you speak English?": "Vorbiți engleză?"},
    "bulgaria": {"Hello": "Zdravei", "Thank you": "Blagodarya", "Yes/No": "Da / Ne", "How are you?": "Kak si?", "Excuse me": "Izvinete", "Check, please!": "Smetkata, molya!", "Do you speak English?": "Govorite li angliiski?"},
    "serbia": {"Hello": "Zdravo", "Thank you": "Hvala", "Yes/No": "Da / Ne", "How are you?": "Kako si?", "Excuse me": "Izvinite", "Check, please!": "Račun, molim!", "Do you speak English?": "Govorite li engleski?"},
    "malta": {"Hello": "Bonġu", "Thank you": "Grazzi", "Yes/No": "Iva / Le", "How are you?": "Kif anti?", "Excuse me": "Skużani", "Check, please!": "Il-kont, jekk jogħġbok!", "Do you speak English?": "Titkellem bl-Ingliż?"},
    "uk": {"Hello": "Hello", "Thank you": "Thank you", "Yes/No": "Yes / No", "How are you?": "How are you?", "Excuse me": "Excuse me", "Check, please!": "The check, please!", "Do you speak English?": "Do you speak English?"},
    "ireland": {"Hello": "Dia dhuit", "Thank you": "Go raibh maith agat", "Yes/No": "Tá / Níl", "How are you?": "Conas atá tú?", "Excuse me": "Gabh mo leithscéal", "Check, please!": "An bille, le do thoil!", "Do you speak English?": "An labhraíonn tú Béarla?"},
}

def inject_phrasebooks():
    print("--- Injecting Phrasebooks into index.md files ---")
    for country, phrases in PHRASEBOOKS.items():
        index_path = os.path.join(BASE_DOCS, country, "index.md")
        if not os.path.exists(index_path):
            print(f"Skipping {country} (index.md not found)")
            continue
            
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "🗣️ Essential Phrases" in content:
            print(f"Skipping {country} (Already has phrasebook)")
            continue
            
        # Build table
        table = "\n\n## 🗣️ Essential Phrases\n\n| English | Local Language |\n|---------|----------------|\n"
        for eng, local in phrases.items():
            table += f"| **{eng}** | {local} |\n"
            
        # Place before Useful Links if it exists, otherwise at the end
        if "## 🔗 Useful Links" in content:
            new_content = content.replace("## 🔗 Useful Links", table + "\n## 🔗 Useful Links")
        else:
            new_content = content.rstrip() + table
            
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added phrasebook to: {index_path}")

if __name__ == "__main__":
    inject_phrasebooks()
