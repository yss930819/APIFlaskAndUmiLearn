import { App, Button, Flex, List, Spin, Typography } from 'antd';
import React from 'react';
import { useRequest } from '@@/exports';
import api from '@/services/watch-list';

const HomePage: React.FC = () => {

  const { data, error, loading } = useRequest(
    () => {
      return api.movie.getMovie();
    },
  );




  if (loading) {
    return (
      <Flex className={'tw-my-4 '} gap="middle" justify={'center'} vertical>
        <Spin tip="正在加载中...">
          <div className={'tw-h-64 tw-bg-gray-100'}></div>
        </Spin>
      </Flex>

    );
  }

  const { message } = App.useApp();
  if (error) {
    message.error(`数据加载失败！${error.message}`);
  }

  return (
    <>
      <Flex vertical>
        <Typography.Text className={'tw-my-4 tw-text-sm'}>{data ? data.length : 0} Titles</Typography.Text>
        <List
          bordered
          dataSource={data}
          renderItem={
            (item) => (
              <List.Item>
                <Flex className={'tw-w-full'} justify={'space-between'}>
                  <Typography.Text>{item.title}-{item.year}</Typography.Text>
                  <Button className={'tw-item-imdb-button'} href={'https://www.imdb.com/find/?q=' + item.title}
                          size={'small'}><Typography.Text strong> IMDb </Typography.Text></Button>
                </Flex>

              </List.Item>
            )}
        >
        </List>
      </Flex>

    </>
  );


};

export default HomePage;
