// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Get Hello World GET /api/v0/hello/ */
export async function getHello(options?: { [key: string]: any }) {
  return request<{ code?: number; data?: any; message?: string }>('/api/v0/hello/', {
    method: 'GET',
    ...(options || {}),
  });
}

/** Post Hello World POST /api/v0/hello/ */
export async function postHello(body: API.HelloRequest, options?: { [key: string]: any }) {
  return request<{ code?: number; data?: any; message?: string }>('/api/v0/hello/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}

/** Get Hello World GET /api/v0/hello/${param0} */
export async function getHelloName(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.getHelloNameParams,
  options?: { [key: string]: any },
) {
  const { name: param0, ...queryParams } = params;
  return request<{ code?: number; data?: any; message?: string }>(`/api/v0/hello/${param0}`, {
    method: 'GET',
    params: { ...queryParams },
    ...(options || {}),
  });
}
