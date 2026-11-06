# Script de l’oral — Chagas – DNDi (7 minutes)

Menna Mahmoud · Randrianasolo Rabehaja Néaria Yohan · Marwan Ben Mansour

Oral de 6 min 35 sur 11 slides, puis 3 minutes de questions. Les slides 12 et 13 sont des annexes.

## Slide 1 · Titre — MENNA · ~15 s.

Bonjour à toutes et à tous. Je suis Menna, avec Yohan et Marwan. Notre question est simple : comment la science ouverte peut-elle aider une organisation à prendre une décision difficile ? Pour y répondre, nous avons choisi un cas réel, ici, à Genève.

## Slide 2 · L’escalier qui s’effondre — MENNA · ~35 s.

Ce cas, c’est DNDi, qui cherche comment mieux soigner la maladie de Chagas. Pour choisir une piste de traitement, il faut franchir six marches, du besoin médical jusqu’à l’accès des patients. Chaque barre, c’est le nombre d’études publiées sur une marche. Les deux premières sont solides : 185 et 300 études. Puis l’escalier s’effondre : 27, 3, 35… et zéro étude sur l’accès au traitement. Autrement dit : plus on s’approche de la décision, moins la science a de choses à dire.

Transition : « Avant d’aller plus loin, trois noms. »

## Slide 3 · Trois noms à connaître — MENNA · ~30 s.

DNDi, la Drugs for Neglected Diseases initiative, est une organisation à but non lucratif fondée en 2003 à Genève. Elle développe des médicaments pour les maladies que l’industrie délaisse, parce qu’elles touchent surtout des populations pauvres. OpenAlex est un catalogue ouvert et gratuit de 250 millions de publications scientifiques : tout le monde peut l’interroger. Et Operalta, qui nous a lancé ce défi, est un outil qui découpe une décision en étapes, dans une matrice que l’équipe partage.

Transition : « Revenons à Chagas. »

## Slide 4 · La question et les six étapes — MENNA · ~35 s.

La maladie de Chagas est causée par un parasite, transmis par une punaise. Elle touche six à sept millions de personnes, surtout en Amérique latine, et peut abîmer le cœur des années plus tard. Les deux seuls médicaments, le benznidazole et le nifurtimox, ont plus de cinquante ans et provoquent souvent des effets secondaires. DNDi doit donc choisir où investir. Nous avons découpé ce choix en six questions, de « le besoin est-il établi ? » à « les patients y auront-ils accès ? ». Précision honnête : c’est un scénario réaliste, que nous n’avons pas validé avec DNDi.

Transition : « Marwan va vous montrer comment on a mesuré chaque marche. »

## Slide 5 · La méthode — MARWAN · ~35 s.

Notre méthode tient en trois gestes. Un : chercher. Pour chaque étape, on interroge OpenAlex en exigeant que tous les mots de la requête figurent dans le titre. C’est strict, mais ça écarte les articles hors sujet. Deux : ranger. Les résultats vont dans la matrice Operalta, et chaque étape prend une couleur par rapport à la mieux documentée : vert, jaune ou rouge. Trois : décider. L’outil montre ; c’est l’équipe qui vérifie et tranche.

Transition : « Voici ce que ça donne. »

## Slide 6 · La couverture par étape — MARWAN · ~45 s.

Seuls les traitements actuels sont en vert : 300 études, dont 128 depuis 2020. Le besoin médical est en jaune. Tout le reste est en rouge. Les essais cliniques et les nouvelles molécules : une trentaine d’études chacun. La toxicité : trois études, aucune depuis 2020. L’accès : zéro. On connaît bien ce qui existe déjà. On connaît mal ce qui permettrait de choisir. Et précisons-le : on compte des études, on ne juge pas leur qualité.

Transition : « Si on additionne… »

## Slide 7 · 12 % des preuves — MARWAN · ~30 s.

485 études sur les deux étapes établies. 65 seulement sur les quatre qui départagent les pistes. 12 % de la base de preuves. Et ces trous portent justement sur la tolérance et l’accès : ce qui fait qu’un traitement sert vraiment aux patients.

Transition : « Et ce n’est pas une image figée. »

## Slide 8 · Démo en direct — MARWAN (~25 s) puis YOHAN (~35 s). Avant l’oral : carte ouverte, clé saisie, méthode « titre seul », cache rempli ; Operalta ouvert sur la matrice ; Claude Code prêt. Plan B : l’export HTML figé du jour.

MARWAN : Voici la carte vivante, en ligne. Je clique sur Actualiser : elle interroge OpenAlex en direct. Je clique sur Toxicité : voici les articles trouvés, et un lien vers la requête exacte. N’importe qui peut vérifier nos chiffres. « Yohan, et dans Operalta ? »

YOHAN : Ces mêmes données vivent dans Operalta, dans la matrice Chagas–DNDi. Et grâce au protocole MCP, notre assistant Claude Code est connecté à la fois à OpenAlex et à Operalta. Je lui demande : quelle étape repose sur le moins de preuves ? Il répond en citant ses sources, mais il ne modifie rien sans notre accord.

Transition : « Maintenant, ce que nos chiffres ne disent pas. »

## Slide 9 · Limites et robustesse — YOHAN · ~40 s.

Soyons honnêtes sur nos limites. D’abord, les mots comptent : en exigeant « adverse effects » dans le titre, on rate les articles qui parlent d’« adverse events ». Zéro étude ne veut donc pas dire zéro recherche. Ensuite, un nombre d’études ne dit rien de leur qualité. Mais notre conclusion tient : avec une méthode plus large, titre et résumé, on trouve plusieurs fois plus d’études, et pourtant le classement des étapes reste le même.

Transition : « Alors, que peut en faire DNDi ? »

## Slide 10 · Ce que DNDi devrait faire — YOHAN · ~40 s.

Ce n’est pas un avis médical, mais la carte pointe trois actions. Un : avant de trancher, combler les preuves sur la tolérance et l’accès, les deux critères qui départagent les pistes. Deux : suivre les essais et les nouvelles molécules, où la moitié des études datent de 2020 ou après. Trois : refaire la carte avant chaque décision ; il suffit de cliquer sur Actualiser.

Transition : « Menna, pour conclure. »

## Slide 11 · Conclusion — MENNA · ~30 s.

Pour conclure : la science ouverte ne décide pas à la place de DNDi. Mais elle montre, en quelques minutes, où la décision est solide et où elle repose sur le vide. Nous vous laissons avec une question : si vous aviez un seul financement de recherche à attribuer demain, sur quelle marche de l’escalier le mettriez-vous ? Merci, place à vos questions.

## Questions du jury (3 minutes)

Une réponse = 20 secondes au maximum.

- **« Toxicité à 3 études, accès à 0 : un artefact de vos requêtes ? »** (Yohan) En partie : les mots exigés comptent. Mais avec la méthode plus large, ces deux étapes restent les plus faibles : 37 et 57 études depuis 2020, toujours en rouge.
- **« Un nombre d’études dit-il quelque chose de la qualité ? »** (Marwan) Non. On mesure le volume publié, pas le niveau de preuve.
- **« La recherche progresse-t-elle ? »** (Yohan, annexe A) Sur les essais (51 % depuis 2020) et les nouvelles molécules (48 %), oui, mais avec 0 à 6 publications par an.
- **« Qui fait cette recherche ? Pourquoi la Suisse ? »** (Menna, annexe B) Le Brésil signe près d’un tiers des 4 986 publications depuis 2020. La Suisse est 8e avec 154, et DNDi en co-signe 81, soit 53 %.
- **« Pourquoi ne pas laisser l’IA décider ? »** (Marwan) Elle ne voit que ce qui est publié, et nos requêtes peuvent se tromper. Toute écriture dans Operalta attend une validation humaine.
- **« Pourquoi la couverture sur les études depuis 2020 ? »** (Marwan) Pour mesurer l’état actuel de la recherche. Sur toutes les années, le besoin médical passerait en vert, mais toxicité et accès resteraient en rouge.
