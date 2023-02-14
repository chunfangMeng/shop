import React, { Suspense } from 'react';
import { ConfigProvider } from 'antd';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import routesConfig from '@/routes';


function App() {
  const routes = createBrowserRouter(routesConfig)
  return (
    <ConfigProvider>
      <RouterProvider router={routes} />
    </ConfigProvider>
  )
}

export default React.memo(App);
