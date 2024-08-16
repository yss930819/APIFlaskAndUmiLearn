import { defineConfig } from '@umijs/max';

export default defineConfig({
  plugins: [
    '@umijs/max-plugin-openapi/dist',
  ],
  antd: {},
  access: {},
  model: {},
  initialState: {},
  request: {},
  routes: [
    {
      path: '/',
      redirect: '/home',
    },
    {
      name: '首页',
      path: '/home',
      component: './Home',
    },
  ],

  npmClient: 'pnpm',
  tailwindcss: {},
  openAPI: {
    schemaPath: 'http://127.0.0.1:5000/openapi.json',
    requestLibPath: 'import { request } from \'@umijs/max\';',
    mock: false,
  },
});
