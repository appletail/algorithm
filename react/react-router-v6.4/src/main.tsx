import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

// import Contact from './routes/Contact';
// import RootLayout from '@/routes/RootLayer';
// import NotFound from './pages/NotFound';
import routers from './routes/routers';

import '@/styles/global.css';
import App from '@/app/App';

const router = createBrowserRouter(routers)

const container = document.getElementById('root') as HTMLElement;

createRoot(container).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
