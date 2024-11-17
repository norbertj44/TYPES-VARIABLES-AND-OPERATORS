###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
feet = cm//30
inches = (cm%30)//2 # (%)to zamienia pozostale centymetry na inche (poniewaz 1 inch to ok. 2.5 cm, to % usuwa reszte i dzielimy przez 2) a to (//) potem jeszcze zaokragla

print(f'I am {cm}cm tall, {feet} feet and {inches} inches')