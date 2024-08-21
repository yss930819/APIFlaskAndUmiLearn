import React from 'react';
import { Button, Result } from 'antd';
import { history } from '@@/core/history';

export default function Page() {
  return (
    <Result
      status="404"
      title="不存在（404）"
      subTitle="对不起，你访问的页面不存在！"
      extra={
        <Button type="primary" onClick={() => history.replace('/home')}>
          返回首页
        </Button>
      }
    />
  );
}
