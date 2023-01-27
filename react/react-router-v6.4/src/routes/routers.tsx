import Contact from './Contact';
import RootLayout, {
  loader as rootLoader,
  action as rootAction,
} from './RootLayer';
import NotFound from '@/pages/NotFound';



export default [
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <NotFound />,
    loader: rootLoader,
    action: rootAction,
    children: [
      {
        path: '/contacts/:contactId',
        element: <Contact />
      },
    ]
  },

]