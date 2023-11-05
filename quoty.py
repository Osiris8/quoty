import os
from datetime import datetime

# Générez la citation motivante du jour
today = datetime.today().strftime('%Y-%m-%d')
quote = f"La persévérance est la clé du succès - {today}"

# Écrivez la citation dans un fichier
with open('motivational_quote.txt', 'w') as file:
    file.write(quote)

# Effectuez un commit et poussez vers GitHub
os.system("git add motivational_quote.txt")
os.system(f'git commit -m "Ajout de la citation motivante du jour - {today}"')
os.system("git push")
