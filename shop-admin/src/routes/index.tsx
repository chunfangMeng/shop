import LazyImport from '@/components/Lazy/ImportComponent';
import { BaseLayout } from '@/layout/Base';
import { lazy } from 'react';
import { RouteObject } from 'react-router-dom';

const routesConfig: RouteObject[] = [{
  path: '/',
  element: <BaseLayout />,
  children: [{
    path: '/',
    element: <LazyImport code="home" lazyChildren={lazy(() => import('../pages/Home'))}/>
  }, {
    path: '/staff/',
    element: <LazyImport code="staffList" lazyChildren={lazy(() => import('@/pages/staff'))}/>
  }, {
    path: '/product/tags/',
    element: <LazyImport code="productTags" lazyChildren={lazy(() => import('@/pages/product/tags'))}/>
  }]
}, {
  path: '/login',
  element: <LazyImport lazyChildren={lazy(() => import('@/pages/Login'))} code="login" />
}, {
  path: '*',
  element: <BaseLayout />,
  children: [{
    path: '*',
    element: <LazyImport lazyChildren={lazy(() => import('../pages/404'))} code='404' />
  }]
}]



export default routesConfig;