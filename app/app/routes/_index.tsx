import type { ActionFunctionArgs } from '@remix-run/node';
import { useActionData } from '@remix-run/react';

import { loginAction } from '../actions/auth.server';
import { LoginFormData } from '../types/login';
import LoginForm from '../components/login-form';

import { BadgeDollarSign } from 'lucide-react';

export const action = async ({ request }: ActionFunctionArgs) => {
  const formData = await request.formData();

  const data: LoginFormData = {
    username: formData.get('username')?.toString() ?? '',
    password: formData.get('password')?.toString() ?? '',
    scope: '',
  };

  return await loginAction(data);
};

export default function Index() {
  const actionData = useActionData<typeof action>();

  return (
    <div className='flex flex-col items-center gap-5 justify-center h-screen'>
      <div className='flex flex-col items-center gap-2 hover:text-yellow-700 transition-colors'>
        <BadgeDollarSign className='size-10' />
        <h1 className='text-xl font-bold'>Where is my money?</h1>
      </div>

      <LoginForm />

      {actionData?.errors && (
        <div className='mb-4'>
          <p className='text-red-500'>{actionData.errors.form}</p>
        </div>
      )}
    </div>
  );
}
