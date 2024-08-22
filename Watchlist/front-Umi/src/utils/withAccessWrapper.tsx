import React from 'react';
import { useAccess } from '@@/exports';
import lodash from 'lodash';
import NoPermission from '@/pages/NoPermission';

export const withAccessWrapper = (Component: React.FC, access_key: string): React.FC => () => {
  const access = useAccess();
  const access_value = lodash.get(access, access_key, false);
  const has_permission = lodash.isFunction(access_value) ? access_value() : access_value;

  if (has_permission) {
    return <Component />;
  } else {
    return <NoPermission />;
  }
};