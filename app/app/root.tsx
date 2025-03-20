import {
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
  useLoaderData,
} from '@remix-run/react';
import type { LinksFunction, MetaFunction } from '@remix-run/node';

import './tailwind.css';
import Nav from './components/nav';
import AdminLayout from './components/layout/admin';
import { LoaderFunctionArgs, redirect } from '@remix-run/node';
import { getUserToken } from './utils/auth';

export const links: LinksFunction = () => [
  { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
  {
    rel: 'preconnect',
    href: 'https://fonts.gstatic.com',
    crossOrigin: 'anonymous',
  },
  {
    rel: 'stylesheet',
    href: 'https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap',
  },
];

export const meta: MetaFunction = () => {
  return [
    { title: 'Where is my Money???' },
    { name: 'description', content: 'where is my money?' },
  ];
};

export async function loader({ request }: LoaderFunctionArgs) {
 
  const token = await getUserToken(request);
  if (!token) {
    throw redirect('/');
  }

  const url = new URL(request.url);
  if (url.pathname === '/' && token) {
    throw redirect('/dashbroad');
  }

  const isAdmin = token ? true : false
  return { isAdmin };
}

export function Layout({ children }: { children: React.ReactNode }) {
  const { isAdmin } = useLoaderData<typeof loader>();

  return (
    <html lang='en'>
      <head>
        <meta charSet='utf-8' />
        <meta
          name='viewport'
          content='width=device-width, initial-scale=1'
        />
        <Meta />
        <Links />
      </head>
      <body>
        <AdminLayout isAdmin={isAdmin}>
          {children}
        </AdminLayout>
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export default function App() {
  return <Outlet />;
}
