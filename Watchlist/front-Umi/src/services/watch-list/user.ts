// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Get Users GET /api/v0/user */
export async function getUser(options?: { [key: string]: any }) {
  return request<{ code?: number; data?: API.UserResponse[]; message?: string }>('/api/v0/user', {
    method: 'GET',
    ...(options || {}),
  });
}

/** Create User POST /api/v0/user */
export async function postUser(body: API.UserRequest, options?: { [key: string]: any }) {
  return request<{ code?: number; data?: API.UserResponse; message?: string }>('/api/v0/user', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}

/** Get User GET /api/v0/user/${param0} */
export async function getUserId(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.getUserIdParams,
  options?: { [key: string]: any },
) {
  const { _id: param0, ...queryParams } = params;
  return request<{ code?: number; data?: API.UserResponse; message?: string }>(
    `/api/v0/user/${param0}`,
    {
      method: 'GET',
      params: { ...queryParams },
      ...(options || {}),
    },
  );
}

/** Update User PUT /api/v0/user/${param0} */
export async function putUserId(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.putUserIdParams,
  body: API.UserUpdateRequest,
  options?: { [key: string]: any },
) {
  const { _id: param0, ...queryParams } = params;
  return request<{ code?: number; data?: API.UserResponse; message?: string }>(
    `/api/v0/user/${param0}`,
    {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      params: { ...queryParams },
      data: body,
      ...(options || {}),
    },
  );
}

/** Delete User DELETE /api/v0/user/${param0} */
export async function deleteUserId(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.deleteUserIdParams,
  options?: { [key: string]: any },
) {
  const { _id: param0, ...queryParams } = params;
  return request<{ code?: number; data?: API.Empty; message?: string }>(`/api/v0/user/${param0}`, {
    method: 'DELETE',
    params: { ...queryParams },
    ...(options || {}),
  });
}

/** Update User Password PUT /api/v0/user/${param0}/password */
export async function putUserIdPassword(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.putUserIdPasswordParams,
  body: API.UserUpdatePasswordRequest,
  options?: { [key: string]: any },
) {
  const { _id: param0, ...queryParams } = params;
  return request<{ code?: number; data?: API.Empty; message?: string }>(
    `/api/v0/user/${param0}/password`,
    {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      params: { ...queryParams },
      data: body,
      ...(options || {}),
    },
  );
}
