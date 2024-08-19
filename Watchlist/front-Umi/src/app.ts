// 运行时配置

// 全局初始化数据配置，用于 Layout 用户信息和权限初始化
// 更多信息见文档：https://umijs.org/docs/api/runtime-config#getinitialstate

import { RequestConfig } from '@@/plugin-request/request';

export const request:RequestConfig = {
  baseURL: 'http://127.0.0.1:5000',
}