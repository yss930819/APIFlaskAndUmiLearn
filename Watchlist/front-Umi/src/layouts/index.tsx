import { history, Outlet } from '@umijs/max';
import { App, Button, Flex } from 'antd';
import React from 'react';
import LOGO from '@/assets/black-cat.jpg';
import { Access, useAccess, useModel } from '@@/exports';


export default function() {
  const access = useAccess();
  const { userInfo, setToken } = useModel('global');

  return (
    <App>
      <Flex justify={'center'}>
        <Flex gap={0} className={'tw-w-580px'} vertical>
          <div className={'tw-flex tw-items-end tw-my-4'}>
            <img src={LOGO} className={'tw-size-12 tw-mr-4'} />
            <div className={'tw-text-2xl tw-font-bold'}>电影清单</div>
          </div>

          <Flex className={'tw-bg-black'} justify={'space-between'}>
            <Flex justify={'flex-start'}>
              <Button type={'link'} className={'tw-nav-link-button'}
                      onClick={() => {
                        history.push('/home');
                      }}
              >首页</Button>
              <Access accessible={access.hasLogin()}>
                <Button type={'link'} className={'tw-nav-link-button'}>管理</Button>
              </Access>
            </Flex>
            <Flex justify={'flex-end'}>
              <Access accessible={access.hasLogin()}>
                <Button type={'link'} className={'tw-nav-link-button'}>{userInfo.name}</Button>
              </Access>
              <Access accessible={!access.hasLogin()}>
                <Button type={'link'} className={'tw-nav-link-button'}
                        onClick={() => {
                          history.push('/login');
                        }}
                >登录</Button>
              </Access>

              <Access accessible={access.hasLogin()}>
                <Button type={'link'} className={'tw-nav-link-button'}
                        onClick={() => {
                          setToken();
                        }}
                >登出</Button>
              </Access>
            </Flex>
          </Flex>

          <Outlet />

          <Flex
            vertical
          >
            <Flex gap={'small'}
                  justify={'center'}
                  align={'center'}>
              <div className={'tw-footer-link-button'}>©2024</div>
              <Button type={'link'} href={'https://github.com/yss930819'}
                      className={'tw-footer-link-button'}>yss930819</Button>
              <Button type={'link'} href={'https://github.com/yss930819/APIFlaskAndUmiLearn'}
                      className={'tw-footer-link-button'}>APIFlaskAndUmiLearn </Button>
              <Button type={'link'} href={'https://umijs.org/docs/introduce/introduce'}
                      className={'tw-footer-link-button'}>Umi.js</Button>
              <Button type={'link'} href={'https://ant-design.antgroup.com/index-cn'}
                      className={'tw-footer-link-button'}>Antd</Button>
              <Button type={'link'} href={'https://pro-components.antdigital.dev/'}
                      className={'tw-footer-link-button'}>Pro Components</Button>
              <Button type={'link'} href={'https://apiflask.com/'}
                      className={'tw-footer-link-button'}>APIFlask</Button>
              <Button type={'link'} href={'http://watchlist.helloflask.com/'}
                      className={'tw-footer-link-button'}>Watchlist</Button>

            </Flex>

          </Flex>
        </Flex>
      </Flex>
    </App>
  );
}