// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** Get Movies GET /api/v0/movie */
export async function getMovie(options?: { [key: string]: any }) {
  return request<{ code?: number; data?: API.MovieResponse[]; message?: string }>('/api/v0/movie', {
    method: 'GET',
    ...(options || {}),
  });
}

/** Create Movie POST /api/v0/movie */
export async function postMovie(body: API.MovieRequest, options?: { [key: string]: any }) {
  return request<{ code?: number; data?: API.MovieResponse; message?: string }>('/api/v0/movie', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}

/** Get Movie GET /api/v0/movie/${param0} */
export async function getMovieId(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.getMovieIdParams,
  options?: { [key: string]: any },
) {
  const { _id: param0, ...queryParams } = params;
  return request<{ code?: number; data?: API.MovieResponse; message?: string }>(
    `/api/v0/movie/${param0}`,
    {
      method: 'GET',
      params: { ...queryParams },
      ...(options || {}),
    },
  );
}

/** Update Movie PUT /api/v0/movie/${param0} */
export async function putMovieId(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.putMovieIdParams,
  body: API.MovieRequest,
  options?: { [key: string]: any },
) {
  const { _id: param0, ...queryParams } = params;
  return request<{ code?: number; data?: API.MovieResponse; message?: string }>(
    `/api/v0/movie/${param0}`,
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

/** Delete Movie DELETE /api/v0/movie/${param0} */
export async function deleteMovieId(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.deleteMovieIdParams,
  options?: { [key: string]: any },
) {
  const { _id: param0, ...queryParams } = params;
  return request<{ code?: number; data?: API.Empty; message?: string }>(`/api/v0/movie/${param0}`, {
    method: 'DELETE',
    params: { ...queryParams },
    ...(options || {}),
  });
}
