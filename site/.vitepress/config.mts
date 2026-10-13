import { defineConfig } from 'vitepress'
const EN='/guide/', FR='/fr-FR/guide/'
export default defineConfig({
  title:'Cobblemon XP Overhaul',
  description:'Player and server guide for Cobblemon XP Overhaul v2.1',
  lang:'en-US',
  base:'/CobblemonXPOverhaul-Multi-1.21.1-Wiki/',
  cleanUrls:true,
  lastUpdated:false,
  head:[['meta',{name:'theme-color',content:'#10b981'}],['meta',{property:'og:title',content:'Cobblemon XP Overhaul Wiki'}]],
  locales:{
    root:{
      label:'English',lang:'en-US',
      themeConfig:{
        nav:[{text:'Guide',link:EN+'getting-started'},{text:'Configuration',link:EN+'configuration'},{text:'CurseForge',link:'https://www.curseforge.com/minecraft/mc-mods/cobblemon-xp-overhaul'},{text:'Discord',link:'https://discord.gg/kb8NSTF45n'}],
        sidebar:[
          {text:'Getting started',items:[{text:'Install & requirements',link:EN+'getting-started'},{text:'XP progression',link:EN+'progression'},{text:'XP Flask',link:EN+'xp-flask'}]},
          {text:'Administration',items:[{text:'Configuration',link:EN+'configuration'},{text:'Settings reference',link:EN+'configuration-reference'},{text:'Commands',link:EN+'commands'},{text:'Compatibility',link:EN+'compatibility'}]},
          {text:'Help & integration',items:[{text:'FAQ & troubleshooting',link:EN+'faq'},{text:'Developer API',link:EN+'api'}]}
        ]
      }
    },
    'fr-FR':{
      label:'Français',lang:'fr-FR',link:'/fr-FR/',
      themeConfig:{
        nav:[{text:'Guide',link:FR+'getting-started'},{text:'Configuration',link:FR+'configuration'},{text:'CurseForge',link:'https://www.curseforge.com/minecraft/mc-mods/cobblemon-xp-overhaul'},{text:'Discord',link:'https://discord.gg/kb8NSTF45n'}],
        sidebar:[
          {text:'Bien démarrer',items:[{text:'Installation',link:FR+'getting-started'},{text:'Progression XP',link:FR+'progression'},{text:'Fiole d’XP',link:FR+'xp-flask'}]},
          {text:'Administration',items:[{text:'Configuration',link:FR+'configuration'},{text:'Référence des paramètres',link:FR+'configuration-reference'},{text:'Commandes',link:FR+'commands'},{text:'Compatibilité',link:FR+'compatibility'}]},
          {text:'Aide et intégration',items:[{text:'FAQ et dépannage',link:FR+'faq'},{text:'API développeur',link:FR+'api'}]}
        ]
      }
    }
  },
  themeConfig:{
    logo:'/mark.svg',
    socialLinks:[{icon:'discord',link:'https://discord.gg/kb8NSTF45n'}],
    search:{provider:'local'},
    docFooter:{prev:'Previous',next:'Next'},
    footer:{message:'Cobblemon XP Overhaul · Documentation v2.1'}
  }
})
