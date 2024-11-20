import re

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

person_name_pattern = r'\b[A-Z][a-zāčēģīļņšž]+ [A-Z][a-zāčēģīļņšž]+\b'
organization_pattern = r'\b[A-Z][a-zāčēģīļņšž]+(?: [A-Z][a-zāčēģīļņšž]+)+\b'

person_names = re.findall(person_name_pattern, text)
organizations = re.findall(organization_pattern, text)

organization_filter = [org for org in organizations if "Universitāte" in org or "Akadēmija" in org or "Sabiedrība" in org or "Universitāte" in org]
organization_names = [org for org in organizations if org not in organization_filter]

person_names = [name for name in person_names if name != "Latvijas Universitāte"]

print("Personvārdi:")
for name in person_names:
    print(f'Frāze: "{name}", Tips: Personvārds')

print("\nOrganizācijas:")
for org in organization_filter:
    print(f'Frāze: "{org}", Tips: Organizācija')
