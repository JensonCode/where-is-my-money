import { Form, useNavigation } from '@remix-run/react';
import { Loader2 } from 'lucide-react';
import { Input } from './ui/input';
import { Button } from './ui/button';

export default function CreateExpenseCategoryForm() {
  const navigation = useNavigation();

  return (
    <Form method='post'>
      <div>
        <label
          htmlFor='name'
          className='block text-sm font-medium text-gray-700'
        >
          Username
        </label>
        <Input
          id='name'
          name='name'
          type='text'
          required
          placeholder='Name'
        />
      </div>
      <Button
        type='submit'
        disabled={navigation.state === 'submitting'}
      >
        {navigation.state === 'submitting' ? (
          <Loader2 className='size-4 animate-spin' />
        ) : (
          'Create'
        )}
      </Button>
    </Form>
  );
}
