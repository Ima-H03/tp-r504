# TP9 - Sockets UDP et TCP en Java

## Réponses aux questions

### Q2.1 - Que se passe-t-il si on lance le client sans que le serveur ne soit actif ?

Le client UDP s'exécute sans erreur et se termine normalement.

En UDP, il n'y a pas d'établissement de connexion préalable avec le serveur. Le client envoie simplement le datagramme vers l'adresse et le port indiqués. Il ne vérifie donc pas que le serveur est actif avant l'envoi.

---

### Q2.2 - Quel est le numéro de port utilisé ?

Le port utilisé est le port **1234**.

Ce choix est pertinent car, d'après le cours, les ports **0 à 1023 sont réservés**. Les ports **1024 à 49151 sont utilisables pour les applications**. Le port 1234 appartient donc à cette plage et convient pour une application comme celle du TP.

---

### Q2.3 - Modifier les deux programmes pour que le serveur renvoie la chaîne reçue au client, et que celui-ci attende cette chaîne et l'affiche avant de quitter.

Le client envoie la chaîne au serveur. Le serveur reçoit cette chaîne puis la renvoie au client. Enfin, le client attend la réponse et l'affiche avant de se terminer.

Lors du test, la chaîne envoyée par le client est bien reçue puis renvoyée par le serveur.

---

## 3.1 - Communication unidirectionnelle

Le client TCP établit une connexion avec le serveur sur le port **2016** et lui envoie une chaîne avec `DataOutputStream` et `writeUTF()`.

Le serveur accepte la connexion, lit la chaîne avec `DataInputStream` et `readUTF()`, affiche le message, puis ferme la connexion et s'arrête.

Test effectué :

```text
Message: message test
```

Le fonctionnement est correct.

---

## 3.2 - Serveur statique

Le serveur est placé dans une boucle infinie `while(true)`, ce qui lui permet de rester actif et d'accepter plusieurs clients successivement.

Le socket serveur reste ouvert tandis que le socket correspondant à chaque client est fermé après le traitement de sa demande.

Tests effectués :

```text
Message: coucou
Message: bonjour
Message: Hello World
```

Le serveur reste actif après chaque client et peut donc recevoir plusieurs messages successivement.

---

## 3.3 - Communication bidirectionnelle

Le client envoie une chaîne au serveur.

Le serveur reçoit la chaîne, l'inverse avec :

```java
String rev = new StringBuilder(msg).reverse().toString();
```

Puis il renvoie la chaîne inversée au client.

Le client reçoit la réponse et l'affiche.

Tests effectués :

```text
bonjour -> ruojnob
coucou -> uocouc
```

Le fonctionnement est correct.

---

# 4. Client HTTP via socket TCP

## Q4.1 - Vérifiez le fonctionnement avec `java Clienthttp www.univ-rouen.fr`

Le client HTTP fonctionne correctement et reçoit une réponse du serveur.

Une sortie redirigée vers le fichier `ur.html` a également été réalisée avec :

```bash
java Clienthttp www.univ-rouen.fr > ur.html
```

Le fichier contient bien la réponse HTTP reçue par le programme.

---

## Q4.2 - Le contenu du fichier est-il conforme à ce qui est attendu ?

Le fichier contient une réponse HTTP composée d'une ligne de statut, d'en-têtes HTTP, d'une ligne vide puis du contenu HTML.

Dans notre cas, le serveur de `www.univ-rouen.fr` renvoie :

```text
HTTP/1.1 302 Found
```

avec l'en-tête :

```text
Location: https://www.univ-rouen.fr/
```

Le serveur indique donc que la ressource demandée est redirigée vers une adresse HTTPS.

Le fonctionnement du client est donc correct, mais il ne récupère pas directement la page finale du site.

---

## Q4.3 - La sortie est-elle constituée uniquement d'un fichier HTML conforme ? Pourquoi ?

Non.

La sortie ne contient pas uniquement du HTML. Elle contient d'abord la réponse HTTP avec la ligne de statut et les en-têtes HTTP, puis une ligne vide et enfin le contenu HTML.

Le programme affiche toutes les lignes reçues du serveur. Il affiche donc à la fois les informations HTTP et le contenu HTML.

---

## Q4.4 - Essayer ensuite avec le site `www.javaworld.com`. Cela fonctionne-t-il correctement ? Essayer ensuite avec d'autres URLs.

Avec `www.javaworld.com`, le serveur renvoie :

```text
HTTP/1.1 403 Forbidden
```

La requête est donc refusée par le serveur.

La réponse indique également :

```text
Server: cloudflare
```

et :

```text
error code: 1003
```

Avec `www.univ-rouen.fr`, le serveur renvoie :

```text
HTTP/1.1 302 Found
```

avec une redirection vers :

```text
https://www.univ-rouen.fr/
```

Avec `www.exemple.com`, le serveur renvoie :

```text
HTTP/1.1 200 OK
```

et le contenu HTML est bien récupéré.

Les résultats sont donc différents selon le serveur contacté.

---

## Q4.5 - Pourquoi obtient-on des résultats différents d'un navigateur ?

Notre programme envoie une requête HTTP très simple :

```text
GET / HTTP/1.0
```

Un navigateur envoie une requête plus complète contenant notamment plusieurs en-têtes HTTP et il sait gérer automatiquement différents mécanismes du protocole HTTP, comme les redirections et les connexions HTTPS.

Notre programme ne reproduit donc pas tout le comportement d'un navigateur. C'est pourquoi les résultats peuvent être différents.

---

## Q4.6 - Analyser la réponse de `www.univ-rouen.fr` et observer les en-têtes

La réponse reçue est :

```text
HTTP/1.1 302 Found
Date: Mon, 21 Sep 2026 11:59:18 GMT
Server: Apache
Strict-Transport-Security: max-age=63072000
Location: https://www.univ-rouen.fr/
Content-Length: 250
Connection: close
Content-Type: text/html; charset=iso-8859-1
```

### Date

```text
Date: Mon, 21 Sep 2026 11:59:18 GMT
```

Indique la date et l'heure auxquelles la réponse a été générée par le serveur.

### Server

```text
Server: Apache
```

Indique le logiciel utilisé par le serveur. Ici, il s'agit d'Apache.

### Strict-Transport-Security

```text
Strict-Transport-Security: max-age=63072000
```

Indique une politique de sécurité HSTS. La valeur `max-age=63072000` indique une durée de validité de cette politique.

### Location

```text
Location: https://www.univ-rouen.fr/
```

Indique l'adresse vers laquelle le client doit être redirigé. Ici, la redirection est effectuée vers `https://www.univ-rouen.fr/`.

### Content-Length

```text
Content-Length: 250
```

Indique la taille du contenu envoyé dans le corps de la réponse. Ici, elle est de 250 octets.

### Connection

```text
Connection: close
```

Indique que la connexion sera fermée après l'envoi de la réponse.

### Content-Type

```text
Content-Type: text/html; charset=iso-8859-1
```

Indique le type du contenu retourné par le serveur. Ici, il s'agit de HTML avec le jeu de caractères `iso-8859-1`.

### Ligne de statut

```text
HTTP/1.1 302 Found
```

Il s'agit de la ligne de statut HTTP et non d'un en-tête. Le code `302` indique une redirection temporaire de la ressource demandée.
