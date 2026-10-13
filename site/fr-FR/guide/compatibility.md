# Compatibilité

## Versions et loaders

Le code cible **Minecraft 1.21.1**, **Cobblemon 1.8.0+**, **Fabric** et **NeoForge**. Vérifiez toujours la version exacte du fichier à installer.

**Fabric :** Fabric Loader 0.17.2+, Fabric API, Fabric Language Kotlin 1.13.6+, Cloth Config 15.0.140+ et Cobblemon compatible.

**NeoForge :** NeoForge 21.1.182+, Cobblemon compatible, Cloth Config 15.0.140+ pour les clients utilisant l'interface de configuration. La compilation utilise Kotlin for Forge.

Ces exigences sont issues des métadonnées du mod et ne garantissent pas que toutes les versions ultérieures ont été testées.

## Intégrations facultatives

| Mod | Fonctionnement |
| --- | --- |
| **Accessories** | Slot de fiole `xp_flask`, avec repli vers l'inventaire |
| **Mod Menu** | Accès facultatif au menu de configuration Fabric |
| **Radical Cobblemon Trainers (RCT)** | Compatibilité conditionnelle des limites de niveau si son API attendue est disponible |

Le module RCT est recherché sans dépendance obligatoire. Si l'API attendue n'est pas accessible, son intégration ne s'active pas.

## Multijoueur et limites

Les récompenses et l'API de fiole sont gérées **côté serveur**. Serveur et clients doivent utiliser les versions compatibles. L'équilibrage se règle sur le serveur.

La fiole ne collecte que les récompenses d'XP du joueur générées par XP Overhaul. Son utilisation est limitée au prochain niveau Pokémon avant les événements Cobblemon. L'Exp All est **désactivé par défaut**.

Voir la [FAQ](/fr-FR/guide/faq) et l'[installation](/fr-FR/guide/getting-started).
