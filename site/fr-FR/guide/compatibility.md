# Compatibilité

## Versions et loaders

Le code cible **Minecraft 1.21.1**, **Cobblemon 1.8.2 minimum et strictement inférieur à 1.9.0**, **Fabric** et **NeoForge**. Vérifiez toujours la version exacte du fichier à installer.

**Fabric :** Fabric Loader 0.17.2+, Fabric API, Fabric Language Kotlin 1.13.6+, Cloth Config 15.0.140+, **OS Cobblemon Library 1.3.0+** et Cobblemon 1.8.2 à 1.8.x.

**NeoForge :** NeoForge 21.1.182+, Cobblemon 1.8.2 à 1.8.x, **OS Cobblemon Library 1.3.0+**, Cloth Config 15.0.140+ pour les clients utilisant l'interface de configuration. La compilation utilise Kotlin for Forge.

**OS Cobblemon Library est obligatoire** sur les deux loaders : le mod utilise son accès au stockage d'équipe Pokémon.

Ces exigences sont issues des métadonnées du mod et ne garantissent pas que toutes les versions ultérieures ont été testées.

## Langues disponibles en jeu

La version **2.1** enrichit les **traductions intégrées au mod**. Le site de documentation est disponible en anglais et en français.

## Intégrations facultatives

| Mod | Fonctionnement |
| --- | --- |
| **Accessories** | Slot de fiole `xp_flask`, avec repli vers l'inventaire |
| **Mod Menu** | Accès facultatif au menu de configuration Fabric |
| **Radical Cobblemon Trainers (RCT)** | Compatibilité conditionnelle des limites de niveau si son API attendue est disponible |

Le module RCT est recherché sans dépendance obligatoire. Si l'API attendue n'est pas accessible, son intégration ne s'active pas.

## Multijoueur et limites

Les récompenses et l'API de fiole sont gérées **côté serveur**. Serveur et clients doivent utiliser les versions compatibles. L'équilibrage se règle sur le serveur.

La fiole ne collecte que les récompenses d'XP du joueur générées par XP Overhaul. Son utilisation normale est limitée au prochain niveau Pokémon avant les événements Cobblemon. Shift + clic droit prévisualise le transfert sans retirer d'XP. L'Exp All est **désactivé par défaut**.

Voir la [FAQ](/fr-FR/guide/faq) et l'[installation](/fr-FR/guide/getting-started).
