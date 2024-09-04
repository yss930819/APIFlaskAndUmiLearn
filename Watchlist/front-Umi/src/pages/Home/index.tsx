import { Button, Typography } from 'antd';
import React, { useRef } from 'react';
import { Access, useAccess } from '@@/exports';
import api from '@/services/watch-list';
import { useResponseError } from '@/utils/useResponseError';
import { ActionType, ProCard, ProList } from '@ant-design/pro-components';

const HomePage: React.FC = () => {

  // Hooks 要在函数顶部
  const { showError } = useResponseError();
  const access = useAccess();

  const ref = useRef<ActionType>();

  return (
    <ProCard bordered className={'tw-my-4'}>
      <ProList<API.MovieResponse>
        actionRef={ref}
        toolBarRender={() => {
          return [
            <Access key={'new'} accessible={access.hasLogin()}>
              <Button type={'primary'} size={'small'}>
                新建
              </Button>
            </Access>,

          ];
        }}
        rowKey="id"
        headerTitle={<Typography.Title level={5}>清单列表</Typography.Title>}

        request={async () => {
          let data: API.MovieResponse[] = [];
          let hasError = false;
          // 读取数据
          await api.movie.getMovie().then((res) => {
            data = res.data!;
          }).catch((error) => {
            showError(error);
            hasError = true;
          });

          return {
            data,
            success: !hasError,
          };
        }}

        metas={
          {
            title: {
              dataIndex: 'title',
              render: (_, record) => {
                return <Typography.Text>{record.title}</Typography.Text>;
              },
            },
            subTitle: {
              dataIndex: 'year',
            },
            actions: {
              render: (_, record) => [
                <Access key={'edit'} accessible={access.hasLogin()}>
                  <Button size={'small'}>编辑</Button>
                </Access>,
                <Access key={'delete'} accessible={access.hasLogin()}>
                  <Button
                    size={'small'}
                    onClick={async () => {
                      await api.movie.deleteMovieId({ _id: record.id! }).then(
                        () => {
                          ref.current?.reload();
                        },
                      ).catch(
                        (error) => {
                          showError(error);
                        });
                    }}
                  >
                    删除
                  </Button>
                </Access>,
                <Button
                  key={'imdb'} className={'tw-item-imdb-button'}
                  href={'https://www.imdb.com/find/?q=' + record.title}
                  size={'small'}

                >
                  <Typography.Text strong> IMDb </Typography.Text>
                </Button>,
              ],
            },
          }
        }
      >

      </ProList>
    </ProCard>

  );


};

export default HomePage;
