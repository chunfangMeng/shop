import { ManagerUser } from "@/interface/staff";
import { AreaChartOutlined, DesktopOutlined, DownOutlined, FileOutlined, GiftOutlined, LogoutOutlined, OrderedListOutlined, TeamOutlined, UserOutlined } from "@ant-design/icons";
import { Avatar, Button, Card, Dropdown, Layout, Menu, MenuProps, Space } from "antd";
import React, { useState } from "react";
import { Link, Outlet, useNavigate, useRouteLoaderData } from "react-router-dom";


type MenuItem = Required<MenuProps>['items'][number];

function getItem(
  label: React.ReactNode,
  key: React.Key,
  icon?: React.ReactNode,
  children?: MenuItem[],
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
  } as MenuItem;
}
  
const items: MenuItem[] = [
  getItem('商城管理', 'order-manage', <OrderedListOutlined />, [
    getItem('商城订单', 'order-list'),
  ]),
  getItem('商城配置', 'config', <DesktopOutlined />, [
    getItem('商品列表', 'goods'),
    getItem('商品分类', 'classify'),
    getItem('品牌管理', 'brand'),
    getItem('商品属性', 'attr'),
    getItem(<Link to={'/product/tags/'}>商品标签</Link>, 'tags'),
    getItem('商品价格组', 'priceLevel'),
  ]),
  getItem('用户列表', 'member', <UserOutlined />),
  getItem(<Link to={'/staff/'}>员工列表</Link>, 'staff', <TeamOutlined />),
  getItem('商城营销', 'marking', <AreaChartOutlined />),
  getItem('内容管理', 'cms', <GiftOutlined />),
];

export function BaseLayout() {
  const loaderData = useRouteLoaderData('root') as ManagerUser.UserInfo
  const [collapsed, setCollapsed] = useState(false);
  const navigate = useNavigate()
  const siderMenuConfig: MenuProps = {
    items: items,
    mode: 'inline',
    theme: 'dark',
    className: 'h-full',
    onSelect: ({ key, keyPath, selectedKeys, domEvent }) => {
      switch(key) {
        case 'goods':
          navigate('/goods')
          break
      }
    }
  }

  const dropItems: MenuProps['items'] = [
    {
      key: 'logout',
      label: <Button danger type="link" icon={<LogoutOutlined />}>登出</Button>,
    },
  ];

  return (
    <Layout
      style={{ minHeight: '100vh' }}>
      <Layout.Sider theme="dark" collapsible collapsed={collapsed} onCollapse={value => setCollapsed(value)}>
        <div className="logo" />
        <Menu {...siderMenuConfig}/>
      </Layout.Sider>
      <Layout>
        <Layout.Header>
          <Card>
            <div className="text-right">
              <Avatar className="!mr-2" icon={<UserOutlined />} />
              <Dropdown menu={{items: dropItems}}>
                <a onClick={e => e.preventDefault()}>
                  <Space>
                    {loaderData?.nickname}
                    <DownOutlined />
                  </Space>
                </a>
              </Dropdown>
            </div>
          </Card>
        </Layout.Header>
        <Layout.Content
          className="site-layout-background">
          <div className="bg-[#F0F2F5]">
            <Outlet />
          </div>
        </Layout.Content>
        <Layout.Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Layout.Footer>
      </Layout>
    </Layout>
  )
}