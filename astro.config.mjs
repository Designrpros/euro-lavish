import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [
    starlight({
      title: '🪙 Euro Lavish',
      logo: {
        src: './src/assets/logo.svg',
      },
      customCss: ['./src/styles/custom.css'],
      social: {
        github: 'https://github.com/Designrpros/euro-lavish',
      },
      sidebar: [
        {
          label: '🏔️ Nord-Europa',
          items: [
            { label: 'Norge', link: '/norway/' },
            { label: 'Sverige', link: '/sweden/' },
            { label: 'Danmark', link: '/denmark/' },
            { label: 'Finland', link: '/finland/' },
            { label: 'Estland', link: '/estonia/' },
            { label: 'Island', link: '/iceland/' },
          ],
        },
        {
          label: '🏗️ Øst-Europa',
          items: [
            { label: 'Polen', link: '/poland/' },
            { label: 'Tsjekkia', link: '/czech/' },
            { label: 'Ungarn', link: '/hungary/' },
            { label: 'Romania', link: '/romania/' },
            { label: 'Serbia', link: '/serbia/' },
            { label: 'Bulgaria', link: '/bulgaria/' },
          ],
        },
        {
          label: '☀️ Sør-Europa',
          items: [
            { label: 'Spania', link: '/spain/' },
            { label: 'Portugal', link: '/portugal/' },
            { label: 'Italia', link: '/italy/' },
            { label: 'Hellas', link: '/greece/' },
            { label: 'Kroatia', link: '/croatia/' },
            { label: 'Malta', link: '/malta/' },
          ],
        },
        {
          label: '🔵 Sentral-Europa',
          items: [
            { label: 'Tyskland', link: '/germany/' },
            { label: 'Østerrike', link: '/austria/' },
            { label: 'Sveits', link: '/switzerland/' },
          ],
        },
        {
          label: '🌊 Vest-Europa',
          items: [
            { label: 'Storbritannia', link: '/uk/' },
            { label: 'Irland', link: '/ireland/' },
            { label: 'Nederland', link: '/netherlands/' },
            { label: 'Belgia', link: '/belgium/' },
            { label: 'Frankrike', link: '/france/' },
          ],
        },
      ],
    }),
  ],
});
