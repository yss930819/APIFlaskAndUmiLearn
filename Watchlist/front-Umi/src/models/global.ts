// 全局共享数据示例
import { useLocalStorageState } from 'ahooks';
import { useEffect, useState } from 'react';
import api from '@/services/watch-list';
import { useResponseError } from '@/utils/useResponseError';
import { TOKEN_KEY } from '@/constants';
import lodash from 'lodash';
import { jwtDecode, JwtPayload } from 'jwt-decode';
import { useModel } from '@@/exports';

const useAuth = () => {
  const { refresh, setInitialState } = useModel('@@initialState');

  const [token, setToken] = useLocalStorageState(TOKEN_KEY, {
    defaultValue: '',
  });
  const [userInfo, setUserInfo] = useState<API.UserResponse>({ id: -1, name: '', username: '' });
  const { showError } = useResponseError();

  useEffect(
    () => {
      if (!lodash.isEmpty(token)) {
        const payload = jwtDecode<JwtPayload>(token!);
        // 通过 Token 的 id 获取用户信息
        api.user.getUserId({ _id: Number(payload.sub) }).then(res => {
          setUserInfo(res.data!);
          setInitialState({
            id: Number(res.data!.id),
          });
        }).catch((err) => {
          showError(err, true);
        });
      } else {
        refresh();
      }
    }, [token],
  );

  return {
    token,
    setToken,
    userInfo,
    setUserInfo,
  };
};

export default useAuth;


export const getTokenFromLocalStorage = () => {
  const token = localStorage.getItem(TOKEN_KEY);
  if (!lodash.isEmpty(token)) {
    return JSON.parse(token!);
  }
  return null;
};