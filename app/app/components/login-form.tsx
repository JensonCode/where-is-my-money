import { Form, useNavigation } from '@remix-run/react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Loader2 } from 'lucide-react';

export default function LoginForm() {
  const navigation = useNavigation();

  return (
    <Form method='post'>
      <div className='rounded-md -space-y-px border border-gray-300 p-5 gap-6 grid grid-cols-1'>
        <div>
          <label
            htmlFor='username'
            className='block text-sm font-medium text-gray-700'
          >
            Username
          </label>
          <Input
            id='username'
            name='username'
            type='text'
            autoComplete='username'
            required
            placeholder='Username'
          />
        </div>

        <div>
          <label
            htmlFor='password'
            className='block text-sm font-medium text-gray-700'
          >
            Password
          </label>
          <Input
            id='password'
            name='password'
            type='password'
            autoComplete='current-password'
            required
            placeholder='Password'
          />
        </div>

        <Button
          type='submit'
          disabled={navigation.state === 'submitting'}
        >
          {navigation.state === 'submitting' ? (
            <Loader2 className='size-4 animate-spin' />
          ) : (
            'Login'
          )}
        </Button>
      </div>
    </Form>
  );
}
