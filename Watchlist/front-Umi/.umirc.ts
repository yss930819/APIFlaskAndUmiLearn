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
    {
      name: '登录',
      path: '/login',
      component: './Login',
    },
    {
      name: '用户信息',
      path: '/user',
      component: './User',
    },
    {
      name: '不存在',
      path: '*',
      component: './NotFound',
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
