import Contact from './Contact';
import RootLayout from './RootLayer';
import NotFound from '@/pages/NotFound';

export default [
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <NotFound />,
    children: [
      {
        path: '/contacts/:contactId',
        element: <Contact />
      },
    ]
  },

]