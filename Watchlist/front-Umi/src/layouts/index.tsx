import { Outlet } from '@umijs/max';
import { Button, Flex } from 'antd';
import React from 'react';
import LOGO from '@/assets/black-cat.jpg';


export default function() {
  return (
    <Flex justify={'center'}>
      <Flex gap={0} className={'tw-w-580px'} vertical>
        <div className={'tw-flex tw-items-end tw-my-4'}>
          <img src={LOGO} className={'tw-size-12 tw-mr-4'} />
          <div className={'tw-text-2xl tw-font-bold'}>电影清单</div>
        </div>

        <Flex className={'tw-bg-black'} justify={'space-between'}>
          <Flex justify={'flex-start'}>
            <Button type={'link'} className={'tw-nav-link-button'}>首页</Button>
            <Button type={'link'} className={'tw-nav-link-button'}>管理</Button>
          </Flex>
          <Flex justify={'flex-end'}>
            <Button type={'link'} className={'tw-nav-link-button'}>xxxx</Button>
            <Button type={'link'} className={'tw-nav-link-button'}>登录</Button>
            <Button type={'link'} className={'tw-nav-link-button'}>登出</Button>
          </Flex>
        </Flex>

        <Outlet />

        <Flex
          gap={'small'}
          justify={'center'}
          align={'center'}>
          <div className={'tw-footer-link-button'}>©2024</div>
          <Button type={'link'} href={'https://github.com/yss930819'}
                  className={'tw-footer-link-button'}>yss930819</Button>
          <Button type={'link'} href={'https://github.com/yss930819/APIFlaskAndUmiLearn'}
                  className={'tw-footer-link-button'}>APIFlaskAndUmiLearn </Button>
        </Flex>
      </Flex>
    </Flex>
  );
}