import React from 'react';
import { ProCard, ProForm, ProFormText } from '@ant-design/pro-components';
import { withAccessWrapper } from '@/utils/withAccessWrapper';
import { App, Button, Flex, Space, Typography } from 'antd';
import { useModel } from '@@/exports';
import api from '@/services/watch-list';
import md5 from 'md5';
import { useResponseError } from '@/utils/useResponseError';

function User() {

  const { userInfo, setUserInfo } = useModel('global');

  const { message } = App.useApp();
  const { showError } = useResponseError();

  return (
    <Flex className={'tw-my-4'} vertical={true} gap={'middle'}>
      <ProCard
        title={
          <Typography.Title level={4}> 基本信息 </Typography.Title>
        }
        bordered
      >
        <ProForm
          initialValues={userInfo}
          submitter={{
            render: (props) => {
              return (
                <Space>
                  <Button type={'primary'} onClick={props.submit}>
                    更新
                  </Button>
                  <Button onClick={props.reset}>
                    重置
                  </Button>
                </Space>
              );
            },

          }}
          onFinish={async (formData) => {
            await api.user.putUserId(
              {
                _id: userInfo.id!,
              },
              {
                name: formData.name,
                username: formData.username,
              },
            ).then(
              (res) => {
                setUserInfo(res.data!);
                message.success('更新信息成功！');
              },
            ).catch((err) => {
              showError(err);
            });
          }}
        >
          <ProForm.Group>
            <ProFormText
              width={'xs'}
              label={'姓名'}
              name={'name'}
              rules={[
                {
                  required: true,
                  message: '请输入姓名',
                },
              ]}
            />

            <ProFormText
              label={'用户名'}
              name={'username'}
              readonly
            />
          </ProForm.Group>


        </ProForm>
      </ProCard>
      <ProCard
        title={
          <Typography.Title level={4}> 更改密码 </Typography.Title>
        }
        bordered
      >
        <ProForm
          initialValues={userInfo}
          submitter={{
            render: (props) => {
              return (
                <Space>
                  <Button type={'primary'} onClick={props.submit}>
                    更新
                  </Button>
                  <Button onClick={props.reset}>
                    重置
                  </Button>
                </Space>
              );
            },

          }}
          onFinish={async (formData) => {
            await api.user.putUserIdPassword({ _id: userInfo.id! }, { password: formData.password }).then(
              () => {
                message.success('更新密码成功！');
              },
            ).catch((err) => {
              showError(err);
            });
          }}
        >
          <ProFormText.Password
            hasFeedback
            label={'新密码'}
            name={'password'}
            rules={[
              {
                required: true,
                message: '请输入密码',
              },
            ]}
            transform={(value) => {
              return {
                password: md5(value + userInfo.username),
              };
            }}
          />

          <ProFormText.Password
            hasFeedback
            validateTrigger={'onBlur'}
            label={'重复密码'}
            name={'repassword'}
            rules={[
              {
                required: true,
                message: '请输重复输入密码',
              },
              ({ getFieldValue }) => {
                return {
                  validator(_, value) {
                    console.log('value', value, getFieldValue('password'));
                    if (!value || getFieldValue('password') === value) {
                      return Promise.resolve();
                    }
                    return Promise.reject(new Error('两次输入的密码不一致'));
                  },
                };
              },
            ]}
          />


        </ProForm>
      </ProCard>
    </Flex>
  )
    ;
}

export default withAccessWrapper(User, 'hasLogin');
