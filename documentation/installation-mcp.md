# Installer les MCP OpenAlex et Operalta (Claude Code, Windows)

## OpenAlex (serveur distant, HTTP)
Il est déjà déclaré dans le `.mcp.json` du dépôt. Ouvrir Claude Code dans le dossier du dépôt, accepter le serveur proposé, puis taper `/mcp` pour se connecter.

Si besoin, l'ajouter à la main :
```powershell
claude mcp add --transport http openalex https://mcp.openalex.org/mcp
```

## Operalta (serveur local, STDIO)
Le MCP Operalta n'a **pas d'URL** : Claude Code lance lui-même le programme sur le poste, qui échange les messages par l'entrée et la sortie standard. Il faut donc d'abord installer le CLI Operalta, sur chaque poste.

1. Installer le CLI en suivant la doc officielle. Sous Windows, ne pas utiliser `install.sh` (prévu pour Mac et Linux) ni `npm install @operalta/...` (paquets non officiels).
2. Se connecter :
   ```powershell
   operalta login --mcp
   operalta status
   ```
3. Brancher Claude Code. Sous Windows, lancer Node directement, avec le chemin complet :
   ```powershell
   claude mcp add operalta -- node "$env:USERPROFILE\.operalta\dist\cli.js"
   claude mcp list
   ```
   L'entrée est propre à chaque poste, parce que le chemin change d'un utilisateur à l'autre. C'est pour ça qu'elle n'est pas dans `.mcp.json`. Ne l'ajouter qu'une seule fois.

## À savoir
- Au départ, Operalta ne montre que quelques outils. Demander à Claude Code d'utiliser `load_tools` pour trouver les autres.
- Chaque écriture dans Operalta demande une confirmation : c'est voulu.
- Les outils de recherche locale (`grep`) ne marchent pas sous Windows.
- Une erreur 404 sur `https://www.operalta.ai/api/cli/download` vient du serveur d'Operalta, pas du poste. Ce lien était en panne les 3 et 4 novembre 2026.

## Exemples de demandes à Claude Code
- « Pour chaque étape de la matrice Operalta "Chagas – DNDi", lance la requête OpenAlex correspondante et propose la nouvelle couleur. Montre-moi les changements avant d'écrire. »
- « Ajoute à chaque entrée les 3 articles les plus cités depuis 2020, avec leur lien. »
- « Qu'est-ce qui a changé dans les études depuis le 1er janvier 2025 ? »
