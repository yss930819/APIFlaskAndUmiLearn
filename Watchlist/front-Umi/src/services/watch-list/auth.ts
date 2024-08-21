// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 登录 用户名 test, 密码：87f77988ccb5aa917c93201ba314fcd4 POST /api/v0/auth/login */
export async function postAuthLogin(body: API.AuthRequest, options?: { [key: string]: any }) {
  return request<{ code?: number; data?: API.AuthResponse; message?: string }>(
    '/api/v0/auth/login',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      data: body,
      ...(options || {}),
    },
  );
}
