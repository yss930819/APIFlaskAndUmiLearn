import React, { useRef } from 'react';
import { LoginForm, ProFormInstance, ProFormText } from '@ant-design/pro-components';
import { LockOutlined, UserOutlined } from '@ant-design/icons';
import md5 from 'md5';
import api from '@/services/watch-list';
import { useResponseError } from '@/utils/useResponseError';
import { App } from 'antd';
import { useModel } from '@@/plugin-model';
import { history } from '@umijs/max';

interface FormData {
  username: string;
  password: string;
}

export default function Page() {
  const { showError } = useResponseError();
  const { setToken } = useModel('global', (model) => ({
    setToken: model.setToken,
  }));

  const { message } = App.useApp();

  const formRef = useRef<ProFormInstance<FormData>>();

  return (
    <div>
      <LoginForm
        formRef={formRef}
        title="登录"
        subTitle="欢迎登录"
        onFinish={async (formData) => {

          await api.auth.postAuthLogin(formData).then((res) => {
            message.success('登陆成功！');
            setToken(res.data!.access_token!);
            // 返回登录前的页面
            history.replace('/home');
          }).catch((err) => {
            showError(err);
          });

          return true;

        }}

      >
        <ProFormText
          name="username"
          fieldProps={{
            size: 'large',
            prefix: <UserOutlined className={'prefixIcon'} />,
          }}
          placeholder={'用户名: admin or user'}
          rules={[
            {
              required: true,
              message: '请输入用户名!',
            },
          ]}
        />

        <ProFormText.Password
          name="password"
          transform={(value, namePath, allValues: FormData) => {
            return {
              password: md5(value + allValues.username),
            };
          }}
          fieldProps={{
            size: 'large',
            prefix: <LockOutlined className={'prefixIcon'} />,
          }}
          placeholder={'密码: ant.design'}
          rules={[
            {
              required: true,
              message: '请输入密码！',
            },
          ]}
        />

      </LoginForm>
    </div>
  )
    ;
}
