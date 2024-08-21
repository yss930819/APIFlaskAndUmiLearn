import React from 'react';
import { Button, Result } from 'antd';
import { history } from '@umijs/max';

export default function Page() {
  return (
    <Result
      status="403"
      title="无权限（403）"
      subTitle="对不起，你无权限访问该页面！"
      extra={
        <Button type="primary" onClick={() => history.replace('/home')}>
          返回首页
        </Button>
      }
    />
  );
}
