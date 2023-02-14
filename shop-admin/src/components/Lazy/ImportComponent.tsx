import React, { LazyExoticComponent } from 'react';

type LazyProps = {
  lazyChildren: LazyExoticComponent<() => JSX.Element> | LazyExoticComponent<React.FC<{}>>;
  code?: string
}

const LazyImport: React.FC<LazyProps> = (props) => {
  return (
    <React.Suspense>
      <props.lazyChildren />
    </React.Suspense>
  )
}

export default LazyImport;