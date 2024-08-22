import React from 'react';
import { useAccess } from '@@/exports';
import lodash from 'lodash';
import NoPermission from '@/pages/NoPermission';
import accessFactory from '@/access';


type AccessKey = keyof ReturnType<typeof accessFactory> // 获取函数返回值，并提取键名作为一个类型
export const withAccessWrapper = (Component: React.FC, accessKey: AccessKey): React.FC => () => {
  const access = useAccess();
  const access_value = lodash.get(access, accessKey, false);
  const has_permission = lodash.isFunction(access_value) ? access_value() : access_value;

  if (has_permission) {
    return <Component />;
  } else {
    return <NoPermission />;
  }
};