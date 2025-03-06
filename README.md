**Conception et réalisation de la partie commande d’une maison intelligente basée sur l’IoT**

 
 📌 Description du projet:
Ce projet IoT vise à concevoir un système de commande pour une maison intelligente en utilisant une carte **ESP32**, un capteur **DHT22** et un **relais** pour contrôler un ventilateur.  
- Le capteur **DHT22** mesure la température et l'humidité ambiantes.  
- L’ESP32 est un  Microcontrôleur Wi-Fi utilisé pour collecter et transmettre les données à la plateforme **Arduino IoT Cloud** .  
- Un **relais** est utilisé pour **activer/désactiver un ventilateur** à distance.  
- Deux modes sont disponibles :  
  - **Mode automatique** : Le ventilateur s'active/désactive en fonction de la température.  
  - **Mode manuel** : L’utilisateur peut allumer/éteindre le ventilateur depuis l’application **Arduino IoT Cloud Remote**.
  - Arduino IoT Cloud : Plateforme cloud pour stocker et afficher les données  
    Arduino IoT Cloud Remote : Application mobile pour surveiller et contrôler le système

L’intégration avec l’application **Arduino IoT Cloud Remote** est automatisée par la plateforme, simplifiant la gestion du système.  
![image](https://github.com/user-attachments/assets/7b9df3a6-7f3f-4769-be74-99328f19b778)


📌 **Variables créées dans Arduino IoT Cloud**  
Lors de la configuration sur **Arduino IoT Cloud**, les variables suivantes ont été créées dans **Cloud Variables**. Elles seront automatiquement générées dans le **Sketch** et donc ne nécessitent pas d’être déclarées manuellement dans le code :  

- **temperature** → Température mesurée (°C)  
- **humidity** → Humidité mesurée (%)  
- **Relay_switch** → Activation/désactivation manuelle du relais (ventilateur)  
- **automatic_mode** → Activation/désactivation du mode automatique  
⚠️ **Pour assurer le bon fonctionnement du code, ces variables doivent conserver exactement ces noms, sans modification.**  


## 📊 Résultats et affichage  
Une fois configuré, les valeurs de température et d'humidité seront envoyées à **Arduino IoT Cloud** et affichées sur l’application **Arduino IoT Cloud Remote**.  


📸 **Exemples d'affichage** :  
![image](https://github.com/user-attachments/assets/374a836d-271b-4727-87fd-6e8b434294cd)




