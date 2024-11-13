import cv2
from datetime import datetime
import os

now = datetime.now()

today_date = now.date()
current_time = str(now.time())


folder_path = f"{today_date}/{current_time[:8]}"
print(folder_path)

os.makedirs(folder_path, exist_ok=True)
# Ouvre la caméra (0 pour la caméra par défaut)
cap = cv2.VideoCapture(0)

# Vérifie si la caméra s'est ouverte correctement
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

# Définit le codec et crée un objet VideoWriter

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Essaye XVID
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(f'{folder_path}/output.mp4', fourcc, 20.0, (width, height))

print("Enregistrement de la vidéo. Appuyez sur 'q' pour arrêter.")

while True:
    ret, frame = cap.read()  # Capture un frame de la caméra
    if not ret:
        print("Erreur : Impossible de lire le frame.")
        break

    out.write(frame)  # Écrit le frame dans le fichier

    # Affiche le frame dans une fenêtre
    cv2.imshow('Frame', frame)

    # Quitte si 'q' est pressé
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère la caméra et ferme les fenêtres
cap.release()
out.release()
cv2.destroyAllWindows()

