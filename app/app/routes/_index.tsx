import type { MetaFunction } from '@remix-run/node';

import { loginAction } from '~/actions/auth.server';
import LoginForm from '~/components/login-form';




export const meta: MetaFunction = () => {
  return [
    { title: 'Where is my Money???' },
    { name: 'description', content: 'where is my money?' },
  ];
};

export const action = loginAction

export default function Index() {

  return (
    <div>
      <LoginForm />
    </div>
  );
}
