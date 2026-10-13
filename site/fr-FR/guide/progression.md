# Progression et expérience

Les récompenses **XP du joueur** (barre d'expérience Minecraft) et **XP des Pokémon** sont gérées indépendamment.

## Captures et XP du joueur

Capturer un Pokémon peut rapporter de l'XP selon une valeur de base, son niveau, un multiplicateur global et des bonus. Valeurs initiales : `baseXp=4` et `levelMultiplier=0.2`.

Les modificateurs de capture couvrent :
- Première capture d'une espèce ou captures répétées
- Pokémon Shiny, Alpha et formes spéciales
- Pokémon légendaires, fabuleux et Ultra-Chimères
- Œuf Chance lorsque ce bonus est actif

L'historique des espèces est conservé par joueur. Les multiplicateurs Shiny et Alpha valent **1.0 par défaut** : aucune augmentation sans personnalisation.

## Combats et XP du joueur

Les victoires contre les Pokémon **sauvages**, **dresseurs PNJ** et en **PvP** disposent chacune d'un profil : activation, XP de base, coefficient de niveau et multiplicateur global. Un niveau minimum des Pokémon vaincus peut filtrer les récompenses.

Par défaut, les victoires causées par une capture sauvage sont exclues du calcul de récompense de combat afin d'éviter un double gain.

## Captures et XP des Pokémon

Les Pokémon éligibles de l'équipe peuvent obtenir de l'XP suivant leur rôle :

- **Participants** : `participantMultiplier` (défaut **1.0**).
- Porteurs d'un **Multi Exp** avec Exp All désactivé : `expShareMultiplier` (défaut **0.5**).
- Bénéficiaires de l'**Exp All** : `expAllMultiplier` (défaut **0.35**).

`pokemon.capture.expAllEnabled` est `false` par défaut. Un porteur du Multi Exp peut bénéficier d'un **bonus optionnel de 10 %** lorsque l'Exp All est actif. Le Pokémon capturé peut aussi être éligible si `allowCapturedPokemonWithExpAll` est activé.

## Combats contre des dresseurs

L'XP des Pokémon éligibles est distribuée après chaque **K.O.** en combat de dresseur, sans attendre une victoire finale. Les récompenses déjà gagnées peuvent donc être conservées même en cas de défaite ultérieure.

## Œuf Chance

Pour l'XP du joueur, la détection dépend des réglages d'inventaire et d'objets tenus par l'équipe. Pour l'XP de capture des Pokémon, l'Œuf Chance tenu par chaque bénéficiaire est examiné individuellement. Multiplicateur par défaut : **1.5**.

## Examiner un calcul d'XP du joueur (v2.1)

Les opérateurs peuvent utiliser `/cxpo xp explain` ou `/cxpo xp explain <player>` pour afficher le dernier calcul d'**XP du joueur**, les bonus appliqués et la répartition entre joueur et fiole. Les traces ne sont conservées que pendant la session serveur. Voir les [commandes](/fr-FR/guide/commands).

Consultez la [référence de configuration](/fr-FR/guide/configuration-reference).
